"""Tests de l'application : AppTest exécute app.py sans navigateur."""
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).parent.parent / "app.py")


def remplir(at, **valeurs):
    for cle, v in valeurs.items():
        widget = at.selectbox(key=cle) if cle in ("type_contrat", "historique_credit") else at.number_input(key=cle)
        widget.set_value(v)
    return at


def evaluer(at):
    next(b for b in at.button if b.label == "Évaluer la demande").click()
    return at.run()


def test_l_application_demarre():
    at = AppTest.from_file(APP, default_timeout=60).run()
    assert not at.exception
    assert at.title[0].value == "Pré-évaluation d'une demande de crédit"
    assert [t.label for t in at.tabs] == ["📝 Nouvelle demande", "📂 Lot de demandes",
                                          "🗂️ Journal des décisions", "📋 Fiche du modèle"]


def test_dossier_solide_avis_favorable():
    at = AppTest.from_file(APP, default_timeout=60).run()
    remplir(at, age=42, revenu_mensuel=359_000, anciennete_emploi=16, montant_demande=5_870_000,
            duree_pret_mois=60, nb_credits_actuels=1, apport_personnel=1_010_000, type_contrat="CDI",
            historique_credit="Bon")
    evaluer(at)
    assert not at.exception
    assert any("Avis favorable" in s.value for s in at.success)


def test_dossier_fragile_avis_defavorable():
    at = AppTest.from_file(APP, default_timeout=60).run()
    remplir(at, revenu_mensuel=120_000, anciennete_emploi=1, montant_demande=15_000_000, nb_credits_actuels=4,
            apport_personnel=0, type_contrat="Indépendant", historique_credit="Mauvais")
    evaluer(at)
    assert any("Avis défavorable" in e.value for e in at.error)


def test_ne_pas_suivre_l_avis_exige_un_commentaire():
    at = AppTest.from_file(APP, default_timeout=60).run()
    remplir(at, age=42, revenu_mensuel=359_000, anciennete_emploi=16, montant_demande=5_870_000,
            duree_pret_mois=60, nb_credits_actuels=1, apport_personnel=1_010_000, type_contrat="CDI",
            historique_credit="Bon")
    evaluer(at)
    at.radio[0].set_value("Refuser")
    next(b for b in at.button if b.label == "Enregistrer la décision").click()
    at.run()
    assert any("expliquez pourquoi" in e.value for e in at.error)
    assert at.session_state.journal == []

    at.text_area[0].set_value("Garant insuffisant constaté en entretien.")
    next(b for b in at.button if b.label == "Enregistrer la décision").click()
    at.run()
    assert len(at.session_state.journal) == 1
    assert at.session_state.journal[0]["avis_suivi"] is False


def test_le_commentaire_ne_passe_pas_au_dossier_suivant():
    """Régression : le commentaire d'un dossier ne doit jamais réapparaître sur le suivant."""
    at = AppTest.from_file(APP, default_timeout=60).run()
    evaluer(at)
    at.text_area[0].set_value("Commentaire du premier client")
    next(b for b in at.button if b.label == "Enregistrer la décision").click()
    at.run()
    assert len(at.session_state.journal) == 1
    assert any("enregistrée dans le journal" in s.value for s in at.success)

    remplir(at, revenu_mensuel=120_000, montant_demande=15_000_000, historique_credit="Mauvais")
    evaluer(at)
    assert at.text_area[0].value == ""


def test_un_commentaire_non_enregistre_ne_passe_pas_au_dossier_suivant():
    """Régression : même NON enregistré, un commentaire ne doit pas suivre l'agent sur le dossier suivant.
    (Ce test échoue si les widgets de décision gardent une clé fixe.)"""
    at = AppTest.from_file(APP, default_timeout=60).run()
    evaluer(at)
    at.text_area[0].set_value("Commentaire du premier client")      # saisi, mais pas enregistré
    remplir(at, revenu_mensuel=120_000, montant_demande=15_000_000, historique_credit="Mauvais")
    evaluer(at)
    assert at.text_area[0].value == ""
