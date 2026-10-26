# Bootcamp Data Science — GOMYCODE 2026

Ressources pédagogiques du bootcamp Data Science (promotion mai 2026).  
Repo instructeur — le repo apprenant est [data-scientist-bootcamp-2026-05](https://github.com/jeanmermozeffi/data-scientist-bootcamp-2026-05).

## Structure des modules

```
01-sql/
├── notions/              # Cours théoriques SQL (DDL, DML, DQL, DCL, TCL)
└── projet-banque-sql/    # Projet pratique complet (exercices + solutions + Docker)

02-python/
├── cours/                # Chapitres Python (Introduction → OOP)
├── notebooks/            # Notebooks interactifs
└── TP/                   # 5 projets pratiques + TP final

03-data-science/
├── cours/                # NumPy, Pandas, Exploration, Visualisation, Web Scraping
├── notebooks/            # Notebooks interactifs
└── TP/                   # Data Cleaning (Employés) + web-scraping (exercice HTML/CSS)

04-machine-learning/
├── cours/                # 01 Algorithmes ML · 02 Checkpoint 5 Iris · 03 Train/Test & Validation croisée
│                         # 04 Métriques d'évaluation · 05 Nettoyage & Feature Scaling · 06 Checkpoint 8 Preprocessing
├── notebooks/            # Notebooks interactifs
└── TP/                   # TP1 Loyer, TP2 Crédit, TP3 Churn, TP4 Facture (énoncés + guides corrigés + notebooks)

05-deep-learning/
├── cours/                # 01 Fondamentaux IA/ML/DL · 02 Checkpoint 9 Réseau de neurones
│   │                     # 03 Forward & Backward Propagation · 04 Concevoir et entraîner des CNN
│   └── images/           # Illustrations des cours 03 et 04
└── notebooks/            # Notebooks interactifs (TensorFlow/Keras pour le 04 ; Colab + GPU conseillé)

data/                     # Jeux de données partagés (CSV)
checkpoint/               # Corrections des checkpoints
```

## Infrastructure SQL (Azure SQL Edge)

Stack Docker local pour les exercices SQL (compatible Apple Silicon ARM64).

```bash
cp .env.example .env   # configurer MSSQL_SA_PASSWORD
./scripts/start.sh     # démarrer
open http://localhost:8080  # Adminer
```

| Champ    | Valeur              |
|----------|---------------------|
| Driver   | MS SQL Server       |
| Serveur  | `sqledge`           |
| Login    | `sa`                |
| Base     | `DataScienceDB`     |

```bash
./scripts/connect.sh   # shell sqlcmd
./scripts/stop.sh      # arrêter
./scripts/backup.sh    # backup .bak
```

> **Note :** Azure SQL Edge est en fin de support Microsoft. Pour la partie SQL du bootcamp, le projet-banque-sql utilise **PostgreSQL** (plus adapté à la pédagogie).
