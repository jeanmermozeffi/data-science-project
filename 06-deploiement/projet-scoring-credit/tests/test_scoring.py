"""Tests unitaires de la logique métier (sans Streamlit)."""
import pandas as pd
import pytest

import scoring

MODELE, FICHE = scoring.charger()
BON = {"age": 42, "revenu_mensuel": 359_000, "anciennete_emploi": 16, "montant_demande": 5_870_000,
       "duree_pret_mois": 60, "nb_credits_actuels": 1, "apport_personnel": 1_010_000, "nb_personnes_charge": 1,
       "type_contrat": "CDI", "historique_credit": "Bon"}
MAUVAIS = {**BON, "historique_credit": "Mauvais", "revenu_mensuel": 120_000, "montant_demande": 15_000_000,
           "nb_credits_actuels": 4, "apport_personnel": 0, "type_contrat": "Indépendant", "anciennete_emploi": 1}


def test_probabilite_entre_0_et_1():
    for d in (BON, MAUVAIS):
        assert 0 <= scoring.probabilite(MODELE, d, FICHE) <= 1


def test_decision_respecte_les_seuils():
    bas, haut = FICHE["seuils"]["bas"], FICHE["seuils"]["haut"]
    assert scoring.decision(haut, FICHE) == "Favorable"
    assert scoring.decision(bas, FICHE) == "Défavorable"
    assert scoring.decision((bas + haut) / 2, FICHE) == "À étudier"


def test_profils_extremes():
    assert scoring.decision(scoring.probabilite(MODELE, BON, FICHE), FICHE) == "Favorable"
    assert scoring.decision(scoring.probabilite(MODELE, MAUVAIS, FICHE), FICHE) == "Défavorable"


def test_validation_bloque_un_mineur():
    erreurs, _ = scoring.valider({**BON, "age": 16}, FICHE)
    assert any("majeur" in e for e in erreurs)


def test_validation_bloque_un_champ_manquant():
    erreurs, _ = scoring.valider({**BON, "revenu_mensuel": None}, FICHE)
    assert erreurs and "Revenu mensuel" in erreurs[0]


def test_validation_avertit_hors_plage_et_incoherence():
    _, avertissements = scoring.valider({**BON, "age": 25, "anciennete_emploi": 15, "montant_demande": 90_000_000},
                                        FICHE)
    assert any("hors de la plage" in a for a in avertissements)
    assert any("incohérente" in a for a in avertissements)


def test_explication_dossier_defavorable_mene_a_un_avis_favorable():
    objectif, etapes = scoring.expliquer(MODELE, MAUVAIS, FICHE)
    assert objectif == "vers_favorable"
    assert scoring.decision(etapes["probabilité après"].iloc[-1], FICHE) == "Favorable"


def test_explication_dossier_favorable_donne_ses_atouts():
    objectif, etapes = scoring.expliquer(MODELE, BON, FICHE)
    assert objectif == "atouts" and (etapes["effet (points)"] < 0).all()


def test_lot_conserve_les_lignes_et_ajoute_l_avis():
    df = pd.read_csv(scoring.DOSSIER_MODELE.parent / "donnees" / "demandes_exemple.csv")
    res = scoring.scorer_lot(MODELE, df, FICHE)
    assert len(res) == len(df) and {"probabilite_accord", "avis"} <= set(res.columns)


def test_lot_refuse_un_fichier_incomplet():
    with pytest.raises(ValueError, match="Colonnes manquantes"):
        scoring.scorer_lot(MODELE, pd.DataFrame({"age": [30]}), FICHE)
