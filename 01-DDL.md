
# 🗄️ Data Definition Language (DDL) — Cours Bootcamp Data Science

---

## Table des matières

1. [Introduction à la définition de SQL](#1-introduction-à-la-définition-de-sql)
2. [Catégories de commandes SQL](#2-catégories-de-commandes-sql)
3. [Qu'est-ce que le DDL ?](#3-quest-ce-que-le-langage-de-définition-de-données-ddl)
4. [Commandes DDL clés et leurs utilisations](#4-commandes-ddl-clés-et-leurs-utilisations)
5. [Définition SQL — Récapitulatif](#5-définition-sql--récapitulatif)
6. [Configuration de l'environnement](#6-configuration-de-lenvironnement-pour-sql)
7. [Créer une structure de données](#7-créer-une-structure-de-données)
8. [Contraintes](#8-contraintes)
9. [Conclusion](#9-conclusion)
10. [✅ Point de contrôle — DDL](#10--point-de-contrôle--data-definition-language)

---

## 1. Introduction à la définition de SQL

### 🔍 Qu'est-ce que SQL ?

**SQL** (Structured Query Language, prononcé « sequel ») est un **langage standardisé** utilisé pour interagir avec les bases de données relationnelles. Il permet de :

- **Créer** et **modifier** la structure d'une base de données
- **Insérer**, **lire**, **mettre à jour** et **supprimer** des données
- **Contrôler** les accès et les droits des utilisateurs

> 💡 **Analogie** : Imaginez une bibliothèque. SQL est le langage qui permet à la fois de **construire les étagères** (structure), **ajouter des livres** (données), **les retrouver** (requêtes) et **gérer qui peut accéder à quoi** (permissions).

### 🏛️ Un peu d'histoire

| Année | Événement |
|-------|-----------|
| 1970 | Edgar F. Codd publie le modèle relationnel |
| 1974 | IBM développe SEQUEL (ancêtre de SQL) |
| 1986 | SQL devient un standard ISO/ANSI |
| Aujourd'hui | Utilisé dans presque tous les systèmes de bases de données |

---

## 2. Catégories de commandes SQL

SQL est organisé en **5 grandes catégories** de commandes. Chacune a un rôle bien précis.

```
┌─────────────────────────────────────────────────────────────┐
│                      COMMANDES SQL                          │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│   DDL    │   DML    │   DQL    │   DCL    │      TCL        │
│ Définir  │Manipuler │Interroger│Contrôler │  Transactions   │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

| Sigle | Nom complet | Rôle principal | Commandes clés |
|-------|-------------|----------------|----------------|
| **DDL** | Data Definition Language | Définir la **structure** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Manipuler les **données** | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | **Interroger** les données | `SELECT` |
| **DCL** | Data Control Language | Gérer les **droits** | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Gérer les **transactions** | `COMMIT`, `ROLLBACK` |

> 🎯 **Dans ce chapitre, nous nous concentrons sur le DDL.**

---

## 3. Qu'est-ce que le Langage de Définition de Données (DDL) ?

### 📖 Définition

Le **DDL (Data Definition Language)** est l'ensemble des commandes SQL qui permettent de **définir, créer, modifier et supprimer la structure** d'une base de données.

En d'autres termes, le DDL s'occupe du **squelette** de votre base de données, pas de son contenu.

> 💡 **Analogie** : Construire une maison. Le DDL, c'est l'architecte qui dessine les plans, construit les murs, crée les pièces. Les données (DML), c'est le mobilier qu'on met à l'intérieur.

### 🔑 Ce que le DDL permet de faire

- ✅ Créer une nouvelle base de données ou table
- ✅ Modifier la structure d'une table existante (ajouter/supprimer une colonne)
- ✅ Supprimer une table ou une base de données
- ✅ Vider le contenu d'une table sans la supprimer
- ✅ Renommer des objets de la base de données

### ⚠️ Caractéristique importante

> Les commandes DDL sont **auto-validées (auto-commit)**. Cela signifie que les modifications sont **immédiatement permanentes** et ne peuvent généralement pas être annulées avec un `ROLLBACK`.

---

## 4. Commandes DDL clés et leurs utilisations

| Commande | Description | Exemple d'usage |
|----------|-------------|-----------------|
| `CREATE` | Crée un objet (base, table, index…) | Créer une table `clients` |
| `ALTER` | Modifie la structure d'un objet existant | Ajouter une colonne `email` |
| `DROP` | Supprime définitivement un objet | Supprimer une table obsolète |
| `TRUNCATE` | Vide toutes les données d'une table | Réinitialiser une table de logs |
| `RENAME` | Renomme un objet | Renommer `users` en `clients` |

---

## 5. Définition SQL — Récapitulatif

### 🗂️ Objets d'une base de données relationnelle

```
BASE DE DONNÉES
│
├── TABLES (stockent les données en lignes et colonnes)
│   ├── Colonnes (attributs / champs)
│   └── Lignes (enregistrements / tuples)
│
├── VUES (tables virtuelles basées sur des requêtes)
├── INDEX (accélèrent les recherches)
└── CONTRAINTES (règles d'intégrité des données)
```

### 📐 Types de données courants en SQL

| Type | Description | Exemple |
|------|-------------|---------|
| `INT` / `INTEGER` | Nombre entier | `25`, `100`, `-3` |
| `VARCHAR(n)` | Chaîne de caractères variable (max n) | `'Alice'`, `'Paris'` |
| `CHAR(n)` | Chaîne de caractères fixe | `'FR'` (code pays) |
| `FLOAT` / `DECIMAL` | Nombre décimal | `19.99`, `3.14` |
| `DATE` | Date (AAAA-MM-JJ) | `2024-01-15` |
| `DATETIME` | Date et heure | `2024-01-15 10:30:00` |
| `BOOLEAN` | Vrai ou Faux | `TRUE`, `FALSE` |
| `TEXT` | Texte long | Description longue |

---

## 6. Configuration de l'environnement pour SQL

### 🛠️ Outils recommandés

| Outil | Type | Recommandé pour |
|-------|------|-----------------|
| **MySQL Workbench** | Application desktop | MySQL |
| **pgAdmin** | Application desktop | PostgreSQL |
| **DBeaver** | Application desktop | Multi-bases (universel) |
| **SQLite Browser** | Application desktop | SQLite (léger, sans installation serveur) |
| **DB Fiddle** | En ligne | Tests rapides sans installation |
| **SQLiteOnline** | En ligne | Débutants, aucune configuration |

### 💻 Installation rapide de SQLite

**Sur Windows :**
```bash
# Télécharger sqlite depuis https://sqlite.org/download.html
sqlite3 ma_base.db
```

**Sur Mac/Linux :**
```bash
# Mac
brew install sqlite

# Ubuntu/Debian
sudo apt-get install sqlite3

# Lancer
sqlite3 ma_base.db
```

### ✅ Vérifier que l'installation fonctionne

```sql
SELECT 'Bonjour SQL !' AS message;
```

**Résultat attendu :**
```
message
--------------
Bonjour SQL !
```

---

## 7. Créer une structure de données

### 7.1 Créer une base de données — `CREATE DATABASE`

```sql
CREATE DATABASE ecole_bootcamp;
USE ecole_bootcamp;
```

### 7.2 Créer une table — `CREATE TABLE`

**Syntaxe générale :**
```sql
CREATE TABLE nom_table (
    nom_colonne1  TYPE_DONNEE  [CONTRAINTE],
    nom_colonne2  TYPE_DONNEE  [CONTRAINTE],
    ...
);
```

**Exemple :**
```sql
CREATE TABLE etudiants (
    id          INTEGER,
    prenom      VARCHAR(50),
    nom         VARCHAR(50),
    email       VARCHAR(100),
    date_nais   DATE,
    note_moy    DECIMAL(4, 2)
);
```

### 7.3 Modifier une table — `ALTER TABLE`

```sql
-- Ajouter une colonne
ALTER TABLE etudiants ADD telephone VARCHAR(15);

-- Modifier une colonne (MySQL)
ALTER TABLE etudiants MODIFY telephone VARCHAR(20);

-- Supprimer une colonne
ALTER TABLE etudiants DROP COLUMN telephone;

-- Renommer une colonne
ALTER TABLE etudiants RENAME COLUMN note_moy TO moyenne_generale;
```

### 7.4 Supprimer une table — `DROP TABLE`

```sql
-- ⚠️ Irréversible !
DROP TABLE IF EXISTS etudiants;
```

### 7.5 Vider une table — `TRUNCATE`

```sql
TRUNCATE TABLE etudiants;
```

### 🆚 Comparaison DROP / TRUNCATE / DELETE

| Commande | Structure | Données | Annulable | Catégorie |
|----------|-----------|---------|-----------|-----------|
| `DROP TABLE` | ❌ Supprimée | ❌ Supprimées | ❌ Non | DDL |
| `TRUNCATE TABLE` | ✅ Conservée | ❌ Supprimées | ❌ Non | DDL |
| `DELETE FROM` | ✅ Conservée | ❌ Supprimées | ✅ Oui | DML |

---

## 8. Contraintes

### Vue d'ensemble

| Contrainte | Description | Exemple d'usage |
|------------|-------------|-----------------|
| `PRIMARY KEY` | Identifiant unique d'une ligne | `id` d'un étudiant |
| `NOT NULL` | La valeur ne peut pas être vide | Le nom est obligatoire |
| `UNIQUE` | Toutes les valeurs doivent être différentes | Email unique |
| `DEFAULT` | Valeur par défaut si aucune n'est fournie | Statut = 'actif' |
| `CHECK` | Vérifie qu'une condition est respectée | Note entre 0 et 20 |
| `FOREIGN KEY` | Lien vers une clé primaire d'une autre table | Lier étudiant à un cours |

### 8.1 PRIMARY KEY

```sql
CREATE TABLE etudiants (
    id_etudiant   INTEGER  PRIMARY KEY AUTO_INCREMENT,
    prenom        VARCHAR(50),
    nom           VARCHAR(50)
);
```

### 8.2 NOT NULL

```sql
CREATE TABLE etudiants (
    id_etudiant   INTEGER      PRIMARY KEY,
    prenom        VARCHAR(50)  NOT NULL,
    nom           VARCHAR(50)  NOT NULL,
    email         VARCHAR(100)
);
```

### 8.3 UNIQUE

```sql
CREATE TABLE etudiants (
    id_etudiant   INTEGER      PRIMARY KEY,
    prenom        VARCHAR(50)  NOT NULL,
    email         VARCHAR(100) UNIQUE
);
```

### 8.4 DEFAULT

```sql
CREATE TABLE etudiants (
    id_etudiant      INTEGER     PRIMARY KEY AUTO_INCREMENT,
    prenom           VARCHAR(50) NOT NULL,
    statut           VARCHAR(20) DEFAULT 'actif',
    date_inscription DATE        DEFAULT (CURRENT_DATE)
);
```

### 8.5 CHECK

```sql
CREATE TABLE etudiants (
    id_etudiant   INTEGER      PRIMARY KEY AUTO_INCREMENT,
    prenom        VARCHAR(50)  NOT NULL,
    note          DECIMAL(4,2) CHECK (note >= 0 AND note <= 20),
    age           INTEGER      CHECK (age >= 18)
);
```

### 8.6 FOREIGN KEY

```sql
CREATE TABLE cours (
    id_cours   INTEGER      PRIMARY KEY AUTO_INCREMENT,
    titre      VARCHAR(100) NOT NULL
);

CREATE TABLE inscriptions (
    id_inscription  INTEGER  PRIMARY KEY AUTO_INCREMENT,
    id_etudiant     INTEGER  NOT NULL,
    id_cours        INTEGER  NOT NULL,
    date_inscription DATE    DEFAULT (CURRENT_DATE),
    FOREIGN KEY (id_cours) REFERENCES cours(id_cours)
);
```

### 8.7 Exemple complet avec toutes les contraintes

```sql
CREATE DATABASE ecole_bootcamp;
USE ecole_bootcamp;

CREATE TABLE formateurs (
    id_formateur   INTEGER       PRIMARY KEY AUTO_INCREMENT,
    prenom         VARCHAR(50)   NOT NULL,
    nom            VARCHAR(50)   NOT NULL,
    email          VARCHAR(100)  UNIQUE NOT NULL,
    specialite     VARCHAR(100)  DEFAULT 'Non spécifiée'
);

CREATE TABLE cours (
    id_cours       INTEGER       PRIMARY KEY AUTO_INCREMENT,
    titre          VARCHAR(100)  NOT NULL,
    duree_heures   INTEGER       CHECK (duree_heures > 0),
    id_formateur   INTEGER,
    FOREIGN KEY (id_formateur) REFERENCES formateurs(id_formateur)
);

CREATE TABLE etudiants (
    id_etudiant      INTEGER      PRIMARY KEY AUTO_INCREMENT,
    prenom           VARCHAR(50)  NOT NULL,
    nom              VARCHAR(50)  NOT NULL,
    email            VARCHAR(100) UNIQUE NOT NULL,
    age              INTEGER      CHECK (age >= 18),
    date_inscription DATE         DEFAULT (CURRENT_DATE),
    statut           VARCHAR(20)  DEFAULT 'actif'
);

CREATE TABLE inscriptions (
    id_inscription  INTEGER      PRIMARY KEY AUTO_INCREMENT,
    id_etudiant     INTEGER      NOT NULL,
    id_cours        INTEGER      NOT NULL,
    note_finale     DECIMAL(4,2) CHECK (note_finale >= 0 AND note_finale <= 20),
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant),
    FOREIGN KEY (id_cours)    REFERENCES cours(id_cours)
);
```

---

## 9. Conclusion

### 📌 Récapitulatif des commandes DDL

```
DDL — Data Definition Language
│
├── CREATE    → Créer une base, une table, un index...
├── ALTER     → Modifier la structure
├── DROP      → Supprimer définitivement un objet
└── TRUNCATE  → Vider les données (structure conservée)
```

### 🔑 Points clés à retenir

1. **DDL = Structure** : le DDL définit le squelette, pas le contenu.
2. **Auto-commit** : les commandes DDL sont permanentes immédiatement.
3. **Les contraintes** garantissent la qualité des données.
4. **La clé primaire** identifie chaque ligne de façon unique.
5. **La clé étrangère** assure les liens entre les tables.

---

## 10. ✅ Point de contrôle — Data Definition Language

### 📝 Questions théoriques

**Q1.** Que signifie l'acronyme DDL ?
> **Réponse :** Data Definition Language — Langage de Définition de Données.

**Q2.** Quelle est la différence entre `DROP TABLE` et `TRUNCATE TABLE` ?
> **Réponse :** `DROP TABLE` supprime la table ET ses données. `TRUNCATE TABLE` supprime uniquement les données mais conserve la structure.

**Q3.** Quelle contrainte interdit les doublons dans une colonne ?
> **Réponse :** La contrainte `UNIQUE`.

**Q4.** Peut-on annuler une commande DDL avec un `ROLLBACK` ?
> **Réponse :** En général **non**, car les commandes DDL sont auto-commit.

---

### 💻 Exercices pratiques

**Exercice 1 — Créer une table**

Créez une table `produits` avec :
- `id_produit` : entier, clé primaire, auto-incrémentée
- `nom_produit` : texte (max 100 car.), obligatoire
- `prix` : décimal (6,2), vérification prix > 0
- `stock` : entier, défaut à 0
- `categorie` : texte (max 50 car.)

<details>
<summary>👀 Voir la solution</summary>

```sql
CREATE TABLE produits (
    id_produit   INTEGER       PRIMARY KEY AUTO_INCREMENT,
    nom_produit  VARCHAR(100)  NOT NULL,
    prix         DECIMAL(6,2)  CHECK (prix > 0),
    stock        INTEGER       DEFAULT 0,
    categorie    VARCHAR(50)
);
```
</details>

---

**Exercice 2 — Modifier une table**

Ajoutez une colonne `description` de type `TEXT` à la table `produits`.

<details>
<summary>👀 Voir la solution</summary>

```sql
ALTER TABLE produits ADD description TEXT;
```
</details>

---

**Exercice 3 — Clé étrangère**

Créez une table `commandes` liée à `produits` avec :
- `id_commande` : clé primaire auto-incrémentée
- `id_produit` : clé étrangère vers `produits`
- `quantite` : entier, vérification >= 1
- `date_commande` : date, défaut à la date courante

👀 Voir la solution

```sql
CREATE TABLE commandes (
    id_commande   INTEGER  PRIMARY KEY AUTO_INCREMENT,
    id_produit    INTEGER  NOT NULL,
    quantite      INTEGER  CHECK (quantite >= 1),
    date_commande DATE     DEFAULT (CURRENT_DATE),
    FOREIGN KEY (id_produit) REFERENCES produits(id_produit)
);
```

---

### 🏆 Challenge bonus

Créez un schéma complet pour une **bibliothèque numérique** avec :
- Une table `auteurs`
- Une table `livres` (liée aux auteurs)
- Une table `membres`
- Une table `emprunts` (liée aux livres et aux membres)

Appliquez toutes les contraintes appropriées.

---

*📘 Fin du chapitre — Data Definition Language | Bootcamp Data Science*
```