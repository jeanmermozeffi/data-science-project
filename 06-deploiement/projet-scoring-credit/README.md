# 💳 Pré-évaluation des demandes de crédit — application Streamlit

Projet fil rouge du cours **Model Serving with Streamlit** (`06-deploiement/cours/01-Deploiement_Model_Serving_Streamlit.md`).

Une institution de microfinance veut aider ses agents de crédit à **pré-évaluer** une demande pendant l'entretien :
avis du modèle (favorable / à étudier / défavorable), explication, décision de l'agent tracée dans un journal,
traitement par lot et fiche du modèle.

> ⚠️ Outil d'**aide à la décision** entraîné sur des données d'exemple (`04-machine-learning/TP/demandes_credit.csv`, données du TP2).
> Il ne doit pas être utilisé pour de vraies décisions de crédit.

## Démarrage rapide

```bash
pip install -r requirements.txt
python entrainer_modele.py      # (ré)entraîne le modèle -> modele/ et donnees/demandes_exemple.csv
streamlit run app.py            # ouvre l'application sur http://localhost:8501
python -m pytest tests          # 16 tests : logique métier + application (AppTest)
```

## Organisation

```
projet-scoring-credit/
├── app.py                 # interface Streamlit (4 onglets)
├── scoring.py             # logique métier pure : validation, probabilité, avis, explication, lot
├── entrainer_modele.py    # entraînement, choix des seuils, fiche du modèle
├── modele/
│   ├── modele_credit.joblib   # pipeline scikit-learn enregistré
│   └── fiche_modele.json      # version, métriques, seuils, bornes, profils de référence
├── donnees/
│   └── demandes_exemple.csv   # 20 demandes du jeu de test, pour l'onglet « Lot »
├── tests/
│   ├── test_scoring.py        # tests unitaires
│   └── test_app.py            # tests de l'interface avec streamlit.testing.AppTest
├── .streamlit/config.toml     # thème et options de l'application
└── requirements.txt           # dépendances aux versions figées
```
