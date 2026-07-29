# 🏦 Projet SQL — FinBank CI

> Projet pédagogique **complet et pratique** couvrant les 5 familles de
> commandes SQL : **DDL · DML · DQL · DCL · TCL**, sur le cas d'une banque
> numérique ivoirienne fictive.
>
> Base : **PostgreSQL 16** · Interface : **pgAdmin 4** · Tout en **Docker**.

---

## 🎯 Ce que vous allez pratiquer

| Chapitre | Famille | Compétences |
|---|---|---|
| 1 | **DDL** | `CREATE`/`ALTER`/`DROP`/`TRUNCATE`, contraintes (PK, FK, UNIQUE, CHECK, DEFAULT) |
| 2 | **DML** | `INSERT`/`UPDATE`/`DELETE`, `WHERE`, `BETWEEN`, `IN`, `LIKE` |
| 3 | **DQL** | `SELECT`, agrégats, `GROUP BY`/`HAVING`, `JOIN`, sous-requêtes, `CASE`, fenêtrage |
| 4 | **DCL** | `GRANT`/`REVOKE`, rôles, privilèges colonne, moindre privilège |
| 5 | **TCL** | `BEGIN`/`COMMIT`/`ROLLBACK`/`SAVEPOINT`, atomicité, ACID |

---

## 🚀 Démarrage rapide

> **Pré-requis** : Docker Desktop installé et démarré.

```bash
# 1. Se placer dans le dossier du projet
cd projet-banque-sql

# 2. Créer le fichier d'environnement
cp .env.example .env

# 3. Lancer PostgreSQL + pgAdmin
docker compose up -d

# 4. (au 1er démarrage) la base se crée et se remplit toute seule :
#    schéma + ~10 700 lignes de données. Suivre les logs :
docker compose logs -f postgres
```

Quand vous voyez `database system is ready to accept connections`, c'est prêt.

### Accéder à la base

**Option A — pgAdmin (navigateur)** → http://localhost:8088
- Email : `admin@finbank.ci` · Mot de passe : `admin`
- Le serveur **« FinBank CI (local) »** est déjà pré-configuré dans la barre
  latérale. Cliquez dessus, mot de passe `admin`.

**Option B — psql (terminal)**
```bash
docker exec -it finbank_postgres psql -U admin -d finbank
# puis :   SET search_path TO banque;   puis vos requêtes.
```

**Option C — client externe** (DBeaver, DataGrip, Azure Data Studio…)
| Champ | Valeur |
|---|---|
| Hôte | `localhost` |
| Port | `5432` |
| Base | `finbank` |
| Utilisateur | `admin` |
| Mot de passe | `admin` |

---

## 📂 Organisation des fichiers

```
projet-banque-sql/
├── README.md                 ← vous êtes ici
├── docker-compose.yml        ← PostgreSQL 16 + pgAdmin 4
├── .env.example              ← variables (à copier en .env)
│
├── sql/                      ← exécuté AUTOMATIQUEMENT au 1er démarrage
│   ├── 01_ddl_schema.sql     ← création des 10 tables + contraintes
│   ├── 02_dml_donnees.sql    ← insertion des données (générées, reproductibles)
│   ├── 03_dcl_roles.sql      ← rôles & privilèges (analyste, guichetier…)
│   └── maintenance/reset.sql ← réinitialisation manuelle
│
├── docs/
│   └── 00-MODELE-DONNEES.md  ← schéma relationnel + dictionnaire de données
│
├── exercices/                ← énoncés, par chapitre, niveaux 🟢🟡🟠🔴
│   ├── 01-DDL.md
│   ├── 02-DML.md
│   ├── 03-DQL.md
│   ├── 04-DCL.md
│   └── 05-TCL.md
│
└── solutions/                ← corrigés détaillés + astuces 💡 + réponses ❓
    ├── 01-DDL-solutions.md
    ├── 02-DML-solutions.md
    ├── 03-DQL-solutions.md
    ├── 04-DCL-solutions.md
    └── 05-TCL-solutions.md
```

---

## 🧭 Parcours conseillé

1. Lisez d'abord **[`docs/00-MODELE-DONNEES.md`](docs/00-MODELE-DONNEES.md)**
   pour comprendre les tables et leurs liens.
2. Faites les chapitres **dans l'ordre** (1 → 5). Chaque énoncé monte en
   difficulté : 🟢 simple → 🟡 → 🟠 → 🔴 cas complet.
3. **Cherchez par vous-même** avant d'ouvrir le corrigé.
4. Répondez aux **❓ questions de compréhension** à la fin de chaque chapitre.

> 🛡️ **Conseil de sécurité** : pour tester un `UPDATE`/`DELETE` sans risque,
> encadrez-le par `BEGIN; ... ROLLBACK;`. Les données reviennent intactes.
> (C'est aussi un avant-goût du chapitre TCL !)

---

## 👥 Comptes de démonstration (chapitre DCL)

Le script `03_dcl_roles.sql` crée 4 profils métier déjà utilisables :

| Utilisateur | Rôle | Droits | Mot de passe |
|---|---|---|---|
| `aya_analyste` | analyste | lecture seule (toutes tables) | `analyste123` |
| `koffi_guichet` | guichetier | lit tout + écrit transactions + maj soldes | `guichet123` |
| `mariam_audit` | auditeur | lecture des flux & crédits | `audit123` |
| `konan_dir` | directeur | tous droits sur les données | `directeur123` |

Exemple :
```bash
docker exec -e PGPASSWORD=analyste123 -it finbank_postgres \
  psql -U aya_analyste -d finbank -c "SELECT count(*) FROM banque.clients;"
```

---

## 🔁 Commandes utiles

```bash
docker compose stop          # arrêter (les données restent)
docker compose start         # redémarrer
docker compose down          # supprimer les conteneurs (données conservées)
docker compose down -v       # ⚠️ TOUT réinitialiser (re-déclenche l'init complète)
```

> ℹ️ Les scripts `sql/*.sql` ne s'exécutent **qu'au premier** démarrage (quand
> le volume de données est vide). Pour tout rejouer depuis zéro :
> `docker compose down -v && docker compose up -d`.

---

## 🛠️ Dépannage

- **Le port 5432 est déjà pris** → changez `POSTGRES_PORT` dans `.env`
  (ex. `5433`) puis `docker compose up -d`.
- **pgAdmin ne se télécharge pas** (`authentication required`) → faites
  `docker logout` puis relancez, ou connectez-vous à la base via psql / DBeaver.
- **Les données semblent absentes** → vérifiez que vous avez bien fait
  `SET search_path TO banque;` (les tables sont dans le schéma `banque`).
- **Modifié un script SQL ?** → il faut `docker compose down -v` pour que l'init
  le rejoue (sinon le volume existant est réutilisé tel quel).

---

*Fait pour s'entraîner. Données 100 % fictives. Devise : FCFA (XOF).* 🇨🇮
