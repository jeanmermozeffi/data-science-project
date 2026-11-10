"""Application de pré-évaluation des demandes de crédit — microfinance.

Lancer (depuis ce dossier) :
    streamlit run app.py
"""
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

import scoring

ICI = Path(__file__).parent

st.set_page_config(page_title="Pré-évaluation crédit", page_icon="💳", layout="wide")


# --------------------------------------------------------------------------- chargement (une seule fois)
@st.cache_resource
def charger_modele():
    return scoring.charger()


@st.cache_data
def fichier_exemple():
    return (ICI / "donnees" / "demandes_exemple.csv").read_bytes()


modele, fiche = charger_modele()
SEUILS = fiche["seuils"]
DECISION_ATTENDUE = {"Favorable": "Accorder", "Défavorable": "Refuser", "À étudier": "Transmettre au comité"}
AFFICHER_AVIS = {"Favorable": st.success, "À étudier": st.warning, "Défavorable": st.error}

if "journal" not in st.session_state:
    st.session_state.journal = []          # décisions enregistrées pendant la session
    st.session_state.n_evaluation = 0      # numéro du dossier évalué (sert à réinitialiser le formulaire de décision)


def ordonner(valeurs, ordre):
    return [v for v in ordre if v in valeurs] + [v for v in valeurs if v not in ordre]


# --------------------------------------------------------------------------- barre latérale
with st.sidebar:
    st.header("💳 Pré-évaluation crédit")
    st.caption(f"Modèle v{fiche['version']} · entraîné le {fiche['date_entrainement']}")
    st.info("Outil d'**aide à la décision**. L'avis du modèle ne remplace ni l'analyse de l'agent "
            "ni la décision du comité de crédit.")
    st.markdown(f"""**Comment lire l'avis**
- ✅ **Favorable** : probabilité ≥ {SEUILS['haut']:.0%}
- 🟠 **À étudier** : entre {SEUILS['bas']:.0%} et {SEUILS['haut']:.0%}
- ⛔ **Défavorable** : probabilité ≤ {SEUILS['bas']:.0%}""")

st.title("Pré-évaluation d'une demande de crédit")
onglet_demande, onglet_lot, onglet_journal, onglet_fiche = st.tabs(
    ["📝 Nouvelle demande", "📂 Lot de demandes", "🗂️ Journal des décisions", "📋 Fiche du modèle"])

# --------------------------------------------------------------------------- 1. une demande
with onglet_demande:
    with st.form("demande"):
        st.subheader("Le demandeur")
        c1, c2, c3 = st.columns(3)
        age = c1.number_input("Âge", min_value=18, max_value=80, value=35, key="age")
        type_contrat = c2.selectbox("Type de contrat",
                                    ordonner(fiche["categories"]["type_contrat"],
                                             ["CDI", "Fonctionnaire", "CDD", "Indépendant"]), key="type_contrat")
        anciennete = c3.number_input("Ancienneté dans l'emploi (ans)", 0, 50, 5, key="anciennete_emploi")
        c1, c2, c3 = st.columns(3)
        revenu = c1.number_input("Revenu mensuel (FCFA)", 0, 10_000_000, 300_000, step=10_000, key="revenu_mensuel")
        personnes = c2.number_input("Personnes à charge", 0, 15, 1, key="nb_personnes_charge")
        historique = c3.selectbox("Historique de crédit",
                                  ordonner(fiche["categories"]["historique_credit"], ["Bon", "Moyen", "Mauvais"]),
                                  key="historique_credit")

        st.subheader("Le crédit demandé")
        c1, c2, c3, c4 = st.columns(4)
        montant = c1.number_input("Montant demandé (FCFA)", 0, 100_000_000, 3_000_000, step=100_000,
                                  key="montant_demande")
        duree = c2.number_input("Durée (mois)", 1, 240, 36, key="duree_pret_mois")
        apport = c3.number_input("Apport personnel (FCFA)", 0, 100_000_000, 500_000, step=50_000,
                                 key="apport_personnel")
        credits = c4.number_input("Crédits en cours", 0, 20, 0, key="nb_credits_actuels")
        envoyer = st.form_submit_button("Évaluer la demande", type="primary")

    if envoyer:
        demande = {"age": age, "revenu_mensuel": revenu, "anciennete_emploi": anciennete,
                   "montant_demande": montant, "duree_pret_mois": duree, "nb_credits_actuels": credits,
                   "apport_personnel": apport, "nb_personnes_charge": personnes,
                   "type_contrat": type_contrat, "historique_credit": historique}
        erreurs, avertissements = scoring.valider(demande, fiche)
        evaluation = {"demande": demande, "erreurs": erreurs, "avertissements": avertissements}
        if not erreurs:
            p = scoring.probabilite(modele, demande, fiche)
            evaluation.update(p=p, avis=scoring.decision(p, fiche),
                              indicateurs=scoring.indicateurs(demande),
                              explication=scoring.expliquer(modele, demande, fiche))
        st.session_state.n_evaluation += 1
        evaluation["numero"] = st.session_state.n_evaluation
        st.session_state.evaluation = evaluation        # survit aux réexécutions du script

    ev = st.session_state.get("evaluation")
    if ev:
        for e in ev["erreurs"]:
            st.error(e)
        for a in ev["avertissements"]:
            st.warning(a)
        if not ev["erreurs"]:
            st.divider()
            AFFICHER_AVIS[ev["avis"]](scoring.AVIS[ev["avis"]])
            c1, c2, c3 = st.columns(3)
            c1.metric("Probabilité d'accord", f"{ev['p']:.0%}")
            c2.metric("Capital à rembourser par mois", f"{scoring.nombre(ev['indicateurs']['capital_mensuel'])} FCFA",
                      help="Montant ÷ durée, hors intérêts et frais.")
            c3.metric("Part du revenu mensuel", f"{ev['indicateurs']['part_du_revenu']:.0%}",
                      help="Capital mensuel ÷ revenu mensuel, hors intérêts.")

            objectif, etapes = ev["explication"]
            if objectif == "atouts":
                st.subheader("Les atouts du dossier")
                st.caption("On dégrade les critères un par un, en commençant par celui qui pèse le plus, en les "
                           "remplaçant par la valeur d'un dossier refusé typique, jusqu'à un avis défavorable. "
                           "Les critères qui font le plus baisser la probabilité sont les vrais atouts du dossier.")
            else:
                st.subheader("Que faudrait-il pour un avis favorable ?")
                st.caption("On corrige les critères un par un, en commençant par celui qui fait le plus monter la "
                           "probabilité, en les remplaçant par la valeur d'un dossier accordé typique, jusqu'à un "
                           "avis favorable. Tant que d'autres critères bloquent, les premières corrections "
                           "peuvent peser peu.")
            if etapes.empty:
                st.write("Aucun critère ne diffère du profil de référence : pas d'explication possible.")
            else:
                en_texte = lambda v: v if isinstance(v, str) else scoring.nombre(v)   # colonnes mixtes -> texte
                affichage = etapes.assign(**{c: etapes[c].map(en_texte)
                                             for c in ["valeur du dossier", "remplacée par"]})
                st.dataframe(affichage, hide_index=True, use_container_width=True,
                             column_config={"probabilité après": st.column_config.ProgressColumn(
                                 "probabilité après", min_value=0.0, max_value=1.0, format="%.2f")})
                st.caption("⚠️ Explication approximative : elle dépend des profils de référence et de l'ordre "
                           "des étapes. Elle aide à comprendre l'avis, elle ne constitue pas un motif de décision.")

            st.subheader("Décision de l'agent")
            if ev.get("enregistree"):
                st.success(f"Décision « {ev['enregistree']} » enregistrée dans le journal. "
                           "Saisissez une nouvelle demande pour continuer.")
            else:
                n = ev["numero"]                    # clés propres à CE dossier : rien ne passe au dossier suivant
                with st.form(f"decision_{n}"):
                    attendue = DECISION_ATTENDUE[ev["avis"]]
                    options = ["Accorder", "Refuser", "Transmettre au comité"]
                    choix = st.radio("Votre décision", options, index=options.index(attendue), horizontal=True,
                                     key=f"choix_{n}")
                    commentaire = st.text_area("Commentaire (obligatoire si vous ne suivez pas l'avis du modèle)",
                                               key=f"commentaire_{n}")
                    enregistrer = st.form_submit_button("Enregistrer la décision")
                if enregistrer:
                    if choix != attendue and not commentaire.strip():
                        st.error("Vous ne suivez pas l'avis du modèle : expliquez pourquoi dans le commentaire.")
                    else:
                        st.session_state.journal.append({
                            "horodatage": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            **ev["demande"], "probabilite": round(ev["p"], 3), "avis_modele": ev["avis"],
                            "decision_agent": choix, "avis_suivi": choix == attendue,
                            "commentaire": commentaire.strip(), "version_modele": fiche["version"]})
                        ev["enregistree"] = choix
                        st.rerun()                  # réaffiche la page : le formulaire laisse place à la confirmation

# --------------------------------------------------------------------------- 2. un lot
with onglet_lot:
    st.write("Évaluez en une fois toutes les demandes de la journée à partir d'un fichier CSV "
             "(une ligne par demande, mêmes colonnes que le fichier modèle).")
    st.download_button("📄 Télécharger le fichier modèle", fichier_exemple(), "demandes_exemple.csv",
                       mime="text/csv")
    fichier = st.file_uploader("Fichier des demandes (CSV)", type="csv")
    if fichier is not None:
        try:
            resultats = scoring.scorer_lot(modele, pd.read_csv(fichier), fiche)
        except ValueError as e:
            st.error(str(e))
        else:
            comptes = resultats["avis"].value_counts()
            c1, c2, c3 = st.columns(3)
            c1.metric("✅ Favorables", int(comptes.get("Favorable", 0)))
            c2.metric("🟠 À étudier", int(comptes.get("À étudier", 0)))
            c3.metric("⛔ Défavorables", int(comptes.get("Défavorable", 0)))
            en_tete = [c for c in ["id_dossier", "avis", "probabilite_accord"] if c in resultats.columns]
            st.dataframe(resultats, hide_index=True, use_container_width=True,
                         column_order=en_tete + [c for c in resultats.columns if c not in en_tete])
            st.download_button("⬇️ Télécharger les résultats", resultats.to_csv(index=False).encode("utf-8-sig"),
                               "demandes_evaluees.csv", mime="text/csv")

# --------------------------------------------------------------------------- 3. journal
with onglet_journal:
    journal = st.session_state.journal
    if not journal:
        st.info("Aucune décision enregistrée pendant cette session.")
    else:
        df_journal = pd.DataFrame(journal)
        c1, c2 = st.columns(2)
        c1.metric("Décisions enregistrées", len(df_journal))
        c2.metric("Avis du modèle suivi", f"{df_journal['avis_suivi'].mean():.0%}")
        st.dataframe(df_journal, hide_index=True, use_container_width=True)
        st.download_button("⬇️ Exporter le journal", df_journal.to_csv(index=False).encode("utf-8-sig"),
                           "journal_decisions.csv", mime="text/csv")
    st.caption("⚠️ Le journal est conservé le temps de la session du navigateur. En production, "
               "il serait enregistré dans une base de données.")

# --------------------------------------------------------------------------- 4. fiche du modèle
with onglet_fiche:
    m = fiche["metriques_test"]
    st.subheader("Performance mesurée sur des dossiers jamais vus (jeu de test)")
    c1, c2, c3 = st.columns(3)
    c1.metric("AUC", f"{m['auc']:.3f}")
    c2.metric("Accuracy (seuil 0,5)", f"{m['accuracy_seuil_0_5']:.1%}")
    c3.metric("Dossiers de test", fiche["donnees"]["test"])
    st.dataframe(pd.DataFrame([{"avis": nom, "part des dossiers": f"{z['part']:.1%}",
                                "dossiers réellement accordés": f"{z['taux_accordes_reels']:.1%}"}
                               for nom, z in m["zones"].items()]), hide_index=True)
    st.markdown(f"""**Ce que prédit le modèle.** {fiche['cible']}. Il reproduit donc les décisions passées
de l'institution — y compris leurs éventuels biais — et ne mesure pas directement le risque de non-remboursement.

**Variables utilisées.** {", ".join(scoring.LIBELLES[c] for c in scoring.colonnes(fiche))}.

**Variable exclue.** Situation familiale : ce n'est pas un critère de solvabilité légitime, et l'exclure ne
dégrade pas la performance.

**Seuils.** {SEUILS['regle']}.

**Limites.** Données d'entraînement : {fiche['donnees']['lignes']} demandes historiques
({fiche['donnees']['fichier']}). Les prédictions sont moins fiables hors des plages vues à l'entraînement
(un avertissement s'affiche alors). Le modèle doit être réévalué régulièrement sur les nouveaux dossiers.""")
