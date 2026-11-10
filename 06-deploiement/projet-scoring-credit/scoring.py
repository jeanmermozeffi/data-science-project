"""Logique métier de la pré-évaluation de crédit, indépendante de l'interface Streamlit.

Toutes les fonctions sont pures (pas d'appel à Streamlit) : elles se testent avec pytest
et pourraient être réutilisées telles quelles derrière une API.
"""
import json
from pathlib import Path

import joblib
import pandas as pd

DOSSIER_MODELE = Path(__file__).parent / "modele"

LIBELLES = {
    "age": "Âge",
    "revenu_mensuel": "Revenu mensuel (FCFA)",
    "anciennete_emploi": "Ancienneté dans l'emploi (ans)",
    "montant_demande": "Montant demandé (FCFA)",
    "duree_pret_mois": "Durée du prêt (mois)",
    "nb_credits_actuels": "Crédits en cours",
    "apport_personnel": "Apport personnel (FCFA)",
    "nb_personnes_charge": "Personnes à charge",
    "type_contrat": "Type de contrat",
    "historique_credit": "Historique de crédit",
}

AVIS = {
    "Favorable": "✅ Avis favorable",
    "À étudier": "🟠 Dossier à étudier par le comité",
    "Défavorable": "⛔ Avis défavorable",
}


def nombre(v):
    """1234567 -> '1 234 567' (séparateur de milliers à la française)."""
    return f"{v:,.0f}".replace(",", "\u202f")


def charger(dossier=DOSSIER_MODELE):
    """Charge le pipeline et sa fiche. Ne chargez JAMAIS un fichier .joblib d'origine inconnue :
    joblib (pickle) peut exécuter du code arbitraire au chargement."""
    modele = joblib.load(Path(dossier) / "modele_credit.joblib")
    fiche = json.loads((Path(dossier) / "fiche_modele.json").read_text(encoding="utf-8"))
    return modele, fiche


def colonnes(fiche):
    return fiche["variables"]["numeriques"] + fiche["variables"]["categorielles"]


def valider(demande, fiche):
    """Retourne (erreurs, avertissements). Une erreur bloque l'évaluation, un avertissement non."""
    erreurs, avertissements = [], []
    manquantes = [LIBELLES[c] for c in colonnes(fiche) if demande.get(c) is None or demande.get(c) == ""]
    if manquantes:
        erreurs.append("Champs manquants : " + ", ".join(manquantes))
        return erreurs, avertissements

    for c in fiche["variables"]["categorielles"]:
        if demande[c] not in fiche["categories"][c]:
            erreurs.append(f"{LIBELLES[c]} : valeur inconnue « {demande[c]} »")
    if demande["age"] < 18:
        erreurs.append("Le demandeur doit être majeur (18 ans au moins).")
    if demande["revenu_mensuel"] <= 0:
        erreurs.append("Le revenu mensuel doit être positif.")
    if demande["duree_pret_mois"] <= 0:
        erreurs.append("La durée du prêt doit être positive.")
    if erreurs:
        return erreurs, avertissements

    for c, (mini, maxi) in fiche["bornes"].items():
        if not mini <= demande[c] <= maxi:
            avertissements.append(f"{LIBELLES[c]} = {nombre(demande[c])} est hors de la plage vue à l'entraînement "
                                  f"({nombre(mini)} – {nombre(maxi)}) : la prédiction est moins fiable.")
    if demande["anciennete_emploi"] > demande["age"] - 16:
        avertissements.append("L'ancienneté dans l'emploi semble incohérente avec l'âge : vérifiez la saisie.")
    return erreurs, avertissements


def probabilite(modele, demande, fiche):
    X = pd.DataFrame([{c: demande[c] for c in colonnes(fiche)}])
    return float(modele.predict_proba(X)[0, 1])


def decision(p, fiche):
    s = fiche["seuils"]
    if p >= s["haut"]:
        return "Favorable"
    if p <= s["bas"]:
        return "Défavorable"
    return "À étudier"


def indicateurs(demande):
    """Indicateurs simples pour l'agent (capital seul, hors intérêts et frais)."""
    capital_mensuel = demande["montant_demande"] / demande["duree_pret_mois"]
    return {"capital_mensuel": capital_mensuel,
            "part_du_revenu": capital_mensuel / demande["revenu_mensuel"]}


def expliquer(modele, demande, fiche):
    """Explique un avis par un « chemin » pas à pas (méthode gloutonne, approximative).

    - Avis non favorable : quels critères corriger, et dans quel ordre, pour obtenir un avis favorable ?
      On remplace à chaque étape le critère qui fait le PLUS MONTER la probabilité par sa valeur
      dans un dossier accordé typique, jusqu'à l'avis favorable.
    - Avis favorable : quels sont les atouts du dossier ? On remplace à chaque étape le critère
      qui fait le PLUS BAISSER la probabilité par sa valeur dans un dossier refusé typique,
      jusqu'à l'avis défavorable.

    Retourne (objectif, tableau des étapes).
    """
    p = probabilite(modele, demande, fiche)
    favorable = decision(p, fiche) == "Favorable"
    objectif = "atouts" if favorable else "vers_favorable"
    cible = fiche["profil_refuse"] if favorable else fiche["profil_accorde"]
    sens = -1 if favorable else 1
    arrivee = "Défavorable" if favorable else "Favorable"

    courant, restants, etapes = dict(demande), [c for c in colonnes(fiche) if demande[c] != cible[c]], []
    while restants and decision(probabilite(modele, courant, fiche), fiche) != arrivee:
        essais = {c: probabilite(modele, {**courant, c: cible[c]}, fiche) for c in restants}
        meilleur = max(essais, key=lambda c: sens * essais[c])
        p_avant = probabilite(modele, courant, fiche)
        etapes.append({"étape": len(etapes) + 1, "critère": LIBELLES[meilleur],
                       "valeur du dossier": demande[meilleur], "remplacée par": cible[meilleur],
                       "probabilité après": round(essais[meilleur], 3),
                       "effet (points)": round(100 * (essais[meilleur] - p_avant), 1)})
        courant[meilleur] = cible[meilleur]
        restants.remove(meilleur)
    return objectif, pd.DataFrame(etapes, columns=["étape", "critère", "valeur du dossier", "remplacée par",
                                                   "probabilité après", "effet (points)"])


def scorer_lot(modele, df, fiche):
    """Évalue un fichier de demandes. Lève ValueError si des colonnes obligatoires manquent."""
    manquantes = [c for c in colonnes(fiche) if c not in df.columns]
    if manquantes:
        raise ValueError("Colonnes manquantes dans le fichier : " + ", ".join(manquantes))
    resultat = df.copy()
    resultat["probabilite_accord"] = modele.predict_proba(df[colonnes(fiche)])[:, 1].round(3)
    resultat["avis"] = [decision(p, fiche) for p in resultat["probabilite_accord"]]
    return resultat
