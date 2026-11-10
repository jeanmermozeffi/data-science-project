"""Entraîne le modèle de pré-évaluation des demandes de crédit et l'enregistre pour l'application.

Usage (depuis ce dossier) :
    python entrainer_modele.py

Produit :
    modele/modele_credit.joblib   le pipeline scikit-learn (prétraitement + modèle)
    modele/fiche_modele.json      la « fiche du modèle » : version, métriques, seuils, bornes, profil de référence
    donnees/demandes_exemple.csv  20 demandes du jeu de TEST (jamais vues à l'entraînement), sans la cible
"""
import json
from datetime import date
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.calibration import calibration_curve
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, brier_score_loss, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

ICI = Path(__file__).parent
DONNEES = ICI.parent.parent / "04-machine-learning" / "TP" / "demandes_credit.csv"   # données du TP2
SORTIE = ICI / "modele"
VERSION = "1.0.0"

CIBLE = "credit_accorde"
# Variable volontairement EXCLUE : la situation familiale n'est pas un critère de solvabilité
# légitime, et la retirer ne coûte rien en performance (AUC identique en validation croisée).
EXCLUES = ["situation_familiale"]
NUMERIQUES = ["age", "revenu_mensuel", "anciennete_emploi", "montant_demande", "duree_pret_mois",
              "nb_credits_actuels", "apport_personnel", "nb_personnes_charge"]
CATEGORIELLES = ["type_contrat", "historique_credit"]

# Règles métier des seuils, fixées AVEC le service risque
PRECISION_MIN_FAVORABLE = 0.97   # au moins 97 % des avis favorables doivent être des dossiers accordés
TAUX_MAX_BONS_DEFAVORABLE = 0.05  # au plus 5 % de dossiers accordés parmi les avis défavorables


def construire_pipeline():
    pretraitement = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), NUMERIQUES),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))]), CATEGORIELLES),
    ])
    return Pipeline([("prep", pretraitement),
                     ("modele", HistGradientBoostingClassifier(random_state=42))])


def choisir_seuils(p, y):
    """Seuil haut : le plus bas tel que la précision des favorables atteigne l'objectif.
    Seuil bas : le plus haut tel que la part de bons dossiers parmi les défavorables reste sous le plafond."""
    grille = np.round(np.arange(0.50, 1.00, 0.01), 2)
    haut = next(float(s) for s in grille if y[p >= s].mean() >= PRECISION_MIN_FAVORABLE)
    grille_bas = np.round(np.arange(0.50, 0.00, -0.01), 2)
    bas = next(float(s) for s in grille_bas if y[p <= s].mean() <= TAUX_MAX_BONS_DEFAVORABLE)
    return bas, haut


def zones(p, y, bas, haut):
    res = {}
    for nom, masque in [("Favorable", p >= haut), ("À étudier", (p > bas) & (p < haut)), ("Défavorable", p <= bas)]:
        res[nom] = {"part": round(float(masque.mean()), 4),
                    "taux_accordes_reels": round(float(y[masque].mean()), 4) if masque.any() else None}
    return res


def main():
    df = pd.read_csv(DONNEES)
    y = df[CIBLE].to_numpy()
    X = df[NUMERIQUES + CATEGORIELLES]

    # 60 % entraînement · 20 % validation (choix des seuils) · 20 % test (évaluation finale, une seule fois)
    X_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_tmp, y_tmp, test_size=0.25, random_state=42,
                                                      stratify=y_tmp)

    pipeline = construire_pipeline().fit(X_train, y_train)

    bas, haut = choisir_seuils(pipeline.predict_proba(X_val)[:, 1], y_val)
    p_test = pipeline.predict_proba(X_test)[:, 1]
    frac, moy = calibration_curve(y_test, p_test, n_bins=8)

    accordes, refuses = X_train[y_train == 1], X_train[y_train == 0]
    fiche = {
        "version": VERSION,
        "date_entrainement": date.today().isoformat(),
        "scikit_learn": sklearn.__version__,
        "donnees": {"fichier": DONNEES.name, "lignes": int(len(df)), "taux_accord": round(float(y.mean()), 4),
                    "entrainement": int(len(X_train)), "validation": int(len(X_val)), "test": int(len(X_test))},
        "cible": "credit_accorde : décision passée de l'institution (1 = accordé), PAS le remboursement",
        "variables": {"numeriques": NUMERIQUES, "categorielles": CATEGORIELLES, "exclues": EXCLUES},
        "categories": {c: sorted(X[c].dropna().unique().tolist()) for c in CATEGORIELLES},
        "bornes": {c: [float(X[c].min()), float(X[c].max())] for c in NUMERIQUES},
        "seuils": {"bas": bas, "haut": haut,
                   "regle": f"précision des favorables ≥ {PRECISION_MIN_FAVORABLE:.0%} ; "
                            f"bons dossiers parmi les défavorables ≤ {TAUX_MAX_BONS_DEFAVORABLE:.0%} (sur la validation)"},
        "metriques_test": {"auc": round(float(roc_auc_score(y_test, p_test)), 4),
                           "accuracy_seuil_0_5": round(float(accuracy_score(y_test, p_test >= 0.5)), 4),
                           "brier": round(float(brier_score_loss(y_test, p_test)), 4),
                           "ecart_calibration_max": round(float(np.max(np.abs(frac - moy))), 4),
                           "zones": zones(p_test, y_test, bas, haut)},
        # Profils « typiques » (médiane / modalité la plus fréquente) utilisés pour expliquer un avis
        "profil_accorde": {**{c: float(accordes[c].median()) for c in NUMERIQUES},
                           **{c: str(accordes[c].mode()[0]) for c in CATEGORIELLES}},
        "profil_refuse": {**{c: float(refuses[c].median()) for c in NUMERIQUES},
                          **{c: str(refuses[c].mode()[0]) for c in CATEGORIELLES}},
    }

    # Fichier d'exemple pour l'évaluation par lot : des dossiers du TEST, sans la cible
    exemple = X_test.sample(20, random_state=7).reset_index(drop=True)
    exemple.insert(0, "id_dossier", [f"D-{i:04d}" for i in range(1, len(exemple) + 1)])
    (ICI / "donnees").mkdir(exist_ok=True)
    exemple.to_csv(ICI / "donnees" / "demandes_exemple.csv", index=False)

    SORTIE.mkdir(exist_ok=True)
    joblib.dump(pipeline, SORTIE / "modele_credit.joblib")
    (SORTIE / "fiche_modele.json").write_text(json.dumps(fiche, ensure_ascii=False, indent=2), encoding="utf-8")

    m = fiche["metriques_test"]
    print(f"Modèle {VERSION} enregistré dans {SORTIE}/")
    print(f"Test : AUC {m['auc']:.3f} | accuracy (seuil 0,5) {m['accuracy_seuil_0_5']:.3f} | "
          f"Brier {m['brier']:.4f} | écart de calibration max {m['ecart_calibration_max']:.3f}")
    print(f"Seuils : défavorable si p ≤ {bas:.2f} · favorable si p ≥ {haut:.2f}")
    for nom, z in m["zones"].items():
        print(f"  {nom:12s} {z['part']:6.1%} des dossiers | dont accordés en réalité : {z['taux_accordes_reels']:.1%}")


if __name__ == "__main__":
    main()
