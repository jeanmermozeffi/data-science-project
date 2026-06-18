# Data Science Project — SQL Server sur Apple Silicon

Stack Docker local avec **Azure SQL Edge** (ARM64 natif) et **Adminer** pour le développement SQL sur Mac Apple Silicon.

## Prérequis

- Mac Apple Silicon (M1/M2/M3/M4/M5)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) ≥ 4.x avec support ARM64
- Au moins 2 Go de RAM alloués à Docker

## Démarrage rapide

```bash
# 1. Cloner et configurer les variables d'environnement
cp .env.example .env
# Éditez .env et définissez un mot de passe fort pour MSSQL_SA_PASSWORD

# 2. Lancer le stack
./scripts/start.sh

# 3. Accéder à Adminer
open http://localhost:8080
```

## Connexion à la base de données

### Via Adminer (interface web)

| Champ        | Valeur                                         |
|--------------|------------------------------------------------|
| Driver       | MS SQL Server                                  |
| Serveur      | `sqledge`                                      |
| Utilisateur  | `sa`                                           |
| Mot de passe | *(valeur de MSSQL_SA_PASSWORD dans .env)*      |
| Base         | `DataScienceDB`                                |

URL : [http://localhost:8080](http://localhost:8080)

### Via sqlcmd (shell interactif)

```bash
./scripts/connect.sh
```

### Via Azure Data Studio

1. Nouvelle connexion → SQL Server
2. Serveur : `localhost,1433`
3. Authentification : SQL Login
4. Utilisateur : `sa` / Mot de passe : voir `.env`

### Via Python (pyodbc / SQLAlchemy)

```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=DataScienceDB;"
    "UID=sa;"
    "PWD=<MSSQL_SA_PASSWORD>;"
    "TrustServerCertificate=yes;"
)
```

## Commandes utiles

```bash
# Démarrer le stack
./scripts/start.sh

# Arrêter proprement
./scripts/stop.sh

# Ouvrir un shell sqlcmd
./scripts/connect.sh

# Créer un backup .bak vers ./backups/
./scripts/backup.sh

# Voir les logs SQL Server en temps réel
docker logs -f sqledge

# Statut des containers
docker compose ps
```

## Structure du projet

```
.
├── docker-compose.yml      # Définition des services Docker
├── .env                    # Variables d'environnement (gitignored)
├── .env.example            # Template de configuration
├── init/
│   └── 01_init_db.sql      # Script d'initialisation (DataScienceDB + staging.raw_events)
├── backups/                # Fichiers .bak générés par backup.sh
└── scripts/
    ├── start.sh
    ├── stop.sh
    ├── connect.sh
    └── backup.sh
```

## Note sur Azure SQL Edge

Ce stack utilise **Azure SQL Edge** (`mcr.microsoft.com/azure-sql-edge`) car c'est la seule image SQL Server de Microsoft compilée nativement pour ARM64 — elle fonctionne sans émulation Rosetta sur Apple Silicon.

> **Important :** Microsoft a annoncé la **retraite d'Azure SQL Edge** (fin de support). Pour les projets de production ou à long terme, envisagez de migrer vers :
> - **SQL Server 2022 sur Linux** (via Rosetta/amd64 dans Docker Desktop, plus lent)
> - **Azure SQL Database** (cloud managé)
> - **PostgreSQL** ou **MySQL** si la compatibilité SQL Server n'est pas impérative

Pour le développement local sur Apple Silicon, Azure SQL Edge reste le choix pragmatique à ce jour.
