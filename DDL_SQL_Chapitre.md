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

## 1\. Introduction à la définition de SQL

### 🔍 Qu'est-ce que SQL ?

**SQL** (Structured Query Language, prononcé « sequel ») est un **langage standardisé** utilisé pour interagir avec les bases de données relationnelles. Il permet de :

- **Créer** et **modifier** la structure d'une base de données  
- **Insérer**, **lire**, **mettre à jour** et **supprimer** des données  
- **Contrôler** les accès et les droits des utilisateurs

💡 **Analogie** : Imaginez une bibliothèque. SQL est le langage qui permet à la fois de **construire les étagères** (structure), **ajouter des livres** (données), **les retrouver** (requêtes) et **gérer qui peut accéder à quoi** (permissions).

### 🏛️ Un peu d'histoire

| Année | Événement |
| :---- | :---- |
| 1970 | Edgar F. Codd publie le modèle relationnel |
| 1974 | IBM développe SEQUEL (ancêtre de SQL) |
| 1986 | SQL devient un standard ISO/ANSI |
| Aujourd'hui | Utilisé dans presque tous les systèmes de bases de données |

---

## 2\. Catégories de commandes SQL

SQL est organisé en **5 grandes catégories** de commandes. Chacune a un rôle bien précis.

┌─────────────────────────────────────────────────────────────┐

│                      COMMANDES SQL                          │

├──────────┬──────────┬──────────┬──────────┬─────────────────┤

│   DDL    │   DML    │   DQL    │   DCL    │      TCL        │

│ Définir  │Manipuler │Interroger│Contrôler │  Transactions   │

└──────────┴──────────┴──────────┴──────────┴─────────────────┘

| Sigle | Nom complet | Rôle principal | Commandes clés |
| :---- | :---- | :---- | :---- |
| **DDL** | Data Definition Language | Définir la **structure** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Manipuler les **données** | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | **Interroger** les données | `SELECT` |
| **DCL** | Data Control Language | Gérer les **droits** | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Gérer les **transactions** | `COMMIT`, `ROLLBACK` |

🎯 **Dans ce chapitre, nous nous concentrons sur le DDL.**

---

## 3\. Qu'est-ce que le Langage de Définition de Données (DDL) ?

### 📖 Définition

Le **DDL (Data Definition Language)** est l'ensemble des commandes SQL qui permettent de **définir, créer, modifier et supprimer la structure** d'une base de données.

En d'autres termes, le DDL s'occupe du **squelette** de votre base de données, pas de son contenu.

💡 **Analogie** : Construire une maison. Le DDL, c'est l'architecte qui dessine les plans, construit les murs, crée les pièces. Les données (DML), c'est le mobilier qu'on met à l'intérieur.

### 🔑 Ce que le DDL permet de faire

- ✅ Créer une nouvelle base de données ou table  
- ✅ Modifier la structure d'une table existante (ajouter/supprimer une colonne)  
- ✅ Supprimer une table ou une base de données  
- ✅ Vider le contenu d'une table sans la supprimer  
- ✅ Renommer des objets de la base de données

### ⚠️ Caractéristique importante

Les commandes DDL sont **auto-validées (auto-commit)**. Cela signifie que les modifications sont **immédiatement permanentes** et ne peuvent généralement pas être annulées avec un `ROLLBACK`.

---

## 4\. Commandes DDL clés et leurs utilisations

Voici un aperçu des commandes DDL les plus importantes :

| Commande | Description | Exemple d'usage |
| :---- | :---- | :---- |
| `CREATE` | Crée un objet (base, table, index…) | Créer une table `clients` |
| `ALTER` | Modifie la structure d'un objet existant | Ajouter une colonne `email` |
| `DROP` | Supprime définitivement un objet | Supprimer une table obsolète |
| `TRUNCATE` | Vide toutes les données d'une table | Réinitialiser une table de logs |
| `RENAME` | Renomme un objet | Renommer `users` en `clients` |

Chacune de ces commandes sera détaillée avec des exemples dans les sections suivantes.

---

## 5\. Définition SQL — Récapitulatif

Avant de passer à la pratique, voici les concepts fondamentaux à retenir :

### 🗂️ Objets d'une base de données relationnelle

BASE DE DONNÉES

│

├── TABLES (stockent les données en lignes et colonnes)

│   ├── Colonnes (attributs / champs)

│   └── Lignes (enregistrements / tuples)

│

├── VUES (tables virtuelles basées sur des requêtes)

├── INDEX (accélèrent les recherches)

└── CONTRAINTES (règles d'intégrité des données)

### 📐 Types de données courants en SQL

| Type | Description | Exemple |
| :---- | :---- | :---- |
| `INT` / `INTEGER` | Nombre entier | `25`, `100`, `-3` |
| `VARCHAR(n)` | Chaîne de caractères variable (max n) | `'Alice'`, `'Paris'` |
| `CHAR(n)` | Chaîne de caractères fixe | `'FR'` (code pays) |
| `FLOAT` / `DECIMAL` | Nombre décimal | `19.99`, `3.14` |
| `DATE` | Date (AAAA-MM-JJ) | `2024-01-15` |
| `DATETIME` | Date et heure | `2024-01-15 10:30:00` |
| `BOOLEAN` | Vrai ou Faux | `TRUE`, `FALSE` |
| `TEXT` | Texte long | Description longue |

---

## 6\. Configuration de l'environnement pour SQL

### 🛠️ Outils recommandés

Pour pratiquer SQL, vous pouvez utiliser l'un de ces outils :

| Outil | Type | Recommandé pour |
| :---- | :---- | :---- |
| **MySQL Workbench** | Application desktop | MySQL |
| **pgAdmin** | Application desktop | PostgreSQL |
| **DBeaver** | Application desktop | Multi-bases (universel) |
| **SQLite Browser** | Application desktop | SQLite (léger, sans installation serveur) |
| **DB Fiddle** | En ligne | Tests rapides sans installation |
| **SQLiteOnline** | En ligne | Débutants, aucune configuration |

### 💻 Installation rapide de SQLite (recommandé pour démarrer)

SQLite est parfait pour apprendre car il ne nécessite **aucun serveur**.

**Sur Windows :**

\# Télécharger sqlite depuis https://sqlite.org/download.html

\# Puis lancer sqlite3 dans le terminal

sqlite3 ma\_base.db

**Sur Mac/Linux :**

\# Mac

brew install sqlite

\# Ubuntu/Debian

sudo apt-get install sqlite3

\# Lancer

sqlite3 ma\_base.db

### ✅ Vérifier que l'installation fonctionne

\-- Taper cette commande dans le terminal sqlite3

SELECT 'Bonjour SQL \!' AS message;

**Résultat attendu :**

message

\--------------

Bonjour SQL \!

---

## 7\. Créer une structure de données

### 7.1 Créer une base de données — `CREATE DATABASE`

\-- Syntaxe

CREATE DATABASE nom\_de\_la\_base;

\-- Exemple concret

CREATE DATABASE ecole\_bootcamp;

\-- Utiliser la base de données (MySQL/MariaDB)

USE ecole\_bootcamp;

---

### 7.2 Créer une table — `CREATE TABLE`

La commande `CREATE TABLE` est le cœur du DDL. Elle définit la structure d'une table.

**Syntaxe générale :**

CREATE TABLE nom\_table (

    nom\_colonne1  TYPE\_DONNEE  \[CONTRAINTE\],

    nom\_colonne2  TYPE\_DONNEE  \[CONTRAINTE\],

    ...

);

**Exemple — Table des étudiants :**

CREATE TABLE etudiants (

    id          INTEGER,

    prenom      VARCHAR(50),

    nom         VARCHAR(50),

    email       VARCHAR(100),

    date\_nais   DATE,

    note\_moy    DECIMAL(4, 2\)

);

**Résultat :** Une table vide avec 6 colonnes est créée.

┌────┬────────┬─────┬───────┬───────────┬──────────┐

│ id │ prenom │ nom │ email │ date\_nais │ note\_moy │

├────┼────────┼─────┼───────┼───────────┼──────────┤

│    │        │     │       │           │          │  ← vide pour l'instant

└────┴────────┴─────┴───────┴───────────┴──────────┘

---

### 7.3 Modifier une table — `ALTER TABLE`

Après la création d'une table, on peut modifier sa structure.

#### ➕ Ajouter une colonne

\-- Syntaxe

ALTER TABLE nom\_table ADD nom\_colonne TYPE\_DONNEE;

\-- Exemple : ajouter un numéro de téléphone

ALTER TABLE etudiants ADD telephone VARCHAR(15);

#### ✏️ Modifier une colonne existante

\-- MySQL / MariaDB

ALTER TABLE etudiants MODIFY telephone VARCHAR(20);

\-- PostgreSQL

ALTER TABLE etudiants ALTER COLUMN telephone TYPE VARCHAR(20);

#### ❌ Supprimer une colonne

\-- Syntaxe

ALTER TABLE nom\_table DROP COLUMN nom\_colonne;

\-- Exemple

ALTER TABLE etudiants DROP COLUMN telephone;

#### 🔄 Renommer une colonne

\-- MySQL 8+ / PostgreSQL

ALTER TABLE etudiants RENAME COLUMN note\_moy TO moyenne\_generale;

---

### 7.4 Supprimer une table — `DROP TABLE`

⚠️ **ATTENTION : Cette opération est irréversible \!** Toutes les données et la structure sont supprimées définitivement.

\-- Syntaxe

DROP TABLE nom\_table;

\-- Exemple

DROP TABLE etudiants;

\-- Bonne pratique : vérifier l'existence avant de supprimer

DROP TABLE IF EXISTS etudiants;

---

### 7.5 Vider une table — `TRUNCATE`

`TRUNCATE` supprime **toutes les données** d'une table mais **conserve sa structure**.

\-- Syntaxe

TRUNCATE TABLE nom\_table;

\-- Exemple

TRUNCATE TABLE etudiants;

#### 🆚 Différence entre `DROP`, `TRUNCATE` et `DELETE`

| Commande | Structure | Données | Annulable (ROLLBACK) | Catégorie |
| :---- | :---- | :---- | :---- | :---- |
| `DROP TABLE` | ❌ Supprimée | ❌ Supprimées | ❌ Non | DDL |
| `TRUNCATE TABLE` | ✅ Conservée | ❌ Supprimées | ❌ Non (en général) | DDL |
| `DELETE FROM` | ✅ Conservée | ❌ Supprimées | ✅ Oui | DML |

---

### 7.6 Exemple complet — Schéma d'une école

\-- 1\. Créer la base de données

CREATE DATABASE ecole\_bootcamp;

USE ecole\_bootcamp;

\-- 2\. Table des formateurs

CREATE TABLE formateurs (

    id\_formateur   INTEGER,

    prenom         VARCHAR(50),

    nom            VARCHAR(50),

    specialite     VARCHAR(100)

);

\-- 3\. Table des cours

CREATE TABLE cours (

    id\_cours       INTEGER,

    titre          VARCHAR(100),

    duree\_heures   INTEGER,

    id\_formateur   INTEGER

);

\-- 4\. Table des étudiants

CREATE TABLE etudiants (

    id\_etudiant    INTEGER,

    prenom         VARCHAR(50),

    nom            VARCHAR(50),

    email          VARCHAR(100),

    date\_inscription DATE

);

---

## 8\. Contraintes

Les **contraintes** (constraints) sont des règles appliquées aux colonnes pour **garantir l'intégrité et la cohérence** des données.

### 8.1 Vue d'ensemble des contraintes

| Contrainte | Description | Exemple d'usage |
| :---- | :---- | :---- |
| `PRIMARY KEY` | Identifiant unique d'une ligne | `id` d'un étudiant |
| `NOT NULL` | La valeur ne peut pas être vide | Le nom est obligatoire |
| `UNIQUE` | Toutes les valeurs doivent être différentes | Email unique |
| `DEFAULT` | Valeur par défaut si aucune n'est fournie | Statut \= 'actif' |
| `CHECK` | Vérifie qu'une condition est respectée | Note entre 0 et 20 |
| `FOREIGN KEY` | Lien vers une clé primaire d'une autre table | Lier étudiant à un cours |

---

### 8.2 PRIMARY KEY — Clé primaire

La clé primaire identifie **chaque ligne de manière unique**. Elle ne peut pas être `NULL` ni dupliquée.

CREATE TABLE etudiants (

    id\_etudiant   INTEGER     PRIMARY KEY,   \-- clé primaire

    prenom        VARCHAR(50),

    nom           VARCHAR(50)

);

**Avec auto-incrémentation (recommandé) :**

\-- MySQL

CREATE TABLE etudiants (

    id\_etudiant   INTEGER     AUTO\_INCREMENT PRIMARY KEY,

    prenom        VARCHAR(50),

    nom           VARCHAR(50)

);

\-- PostgreSQL

CREATE TABLE etudiants (

    id\_etudiant   SERIAL      PRIMARY KEY,

    prenom        VARCHAR(50),

    nom           VARCHAR(50)

);

💡 `AUTO_INCREMENT` / `SERIAL` génère automatiquement un nombre unique croissant : 1, 2, 3, ...

---

### 8.3 NOT NULL — Valeur obligatoire

Empêche qu'une colonne reste vide (sans valeur).

CREATE TABLE etudiants (

    id\_etudiant   INTEGER     PRIMARY KEY,

    prenom        VARCHAR(50) NOT NULL,    \-- obligatoire

    nom           VARCHAR(50) NOT NULL,    \-- obligatoire

    email         VARCHAR(100)             \-- optionnel

);

**Test :**

\-- ❌ Cette insertion échouera (prenom est NULL)

INSERT INTO etudiants (id\_etudiant, nom) VALUES (1, 'Dupont');

\-- Erreur : Column 'prenom' cannot be null

---

### 8.4 UNIQUE — Valeur unique

Garantit qu'aucune valeur ne se répète dans la colonne.

CREATE TABLE etudiants (

    id\_etudiant   INTEGER     PRIMARY KEY,

    prenom        VARCHAR(50) NOT NULL,

    email         VARCHAR(100) UNIQUE      \-- pas deux fois le même email

);

**Test :**

\-- ✅ Premier étudiant : OK

INSERT INTO etudiants VALUES (1, 'Alice', 'alice@email.com');

\-- ❌ Deuxième avec même email : ERREUR

INSERT INTO etudiants VALUES (2, 'Bob', 'alice@email.com');

\-- Erreur : Duplicate entry 'alice@email.com' for key 'email'

---

### 8.5 DEFAULT — Valeur par défaut

Définit une valeur utilisée automatiquement si aucune n'est fournie.

CREATE TABLE etudiants (

    id\_etudiant     INTEGER      PRIMARY KEY AUTO\_INCREMENT,

    prenom          VARCHAR(50)  NOT NULL,

    statut          VARCHAR(20)  DEFAULT 'actif',

    date\_inscription DATE        DEFAULT (CURRENT\_DATE)

);

**Test :**

\-- On n'indique pas de statut ni de date

INSERT INTO etudiants (prenom) VALUES ('Alice');

\-- Résultat automatique :

\-- statut \= 'actif'

\-- date\_inscription \= date d'aujourd'hui

---

### 8.6 CHECK — Vérification de condition

Valide qu'une valeur respecte une condition logique avant d'être insérée.

CREATE TABLE etudiants (

    id\_etudiant   INTEGER      PRIMARY KEY AUTO\_INCREMENT,

    prenom        VARCHAR(50)  NOT NULL,

    note          DECIMAL(4,2) CHECK (note \>= 0 AND note \<= 20),

    age           INTEGER      CHECK (age \>= 18\)

);

**Test :**

\-- ✅ Note valide

INSERT INTO etudiants (prenom, note, age) VALUES ('Alice', 15.5, 22);

\-- ❌ Note invalide

INSERT INTO etudiants (prenom, note, age) VALUES ('Bob', 25, 20);

\-- Erreur : Check constraint 'note' is violated

---

### 8.7 FOREIGN KEY — Clé étrangère

Crée un **lien entre deux tables** en s'assurant que la valeur référencée existe bien dans l'autre table.

\-- Table parente

CREATE TABLE cours (

    id\_cours   INTEGER      PRIMARY KEY AUTO\_INCREMENT,

    titre      VARCHAR(100) NOT NULL

);

\-- Table enfant avec clé étrangère

CREATE TABLE inscriptions (

    id\_inscription  INTEGER  PRIMARY KEY AUTO\_INCREMENT,

    id\_etudiant     INTEGER  NOT NULL,

    id\_cours        INTEGER  NOT NULL,

    date\_inscription DATE    DEFAULT (CURRENT\_DATE),

    FOREIGN KEY (id\_cours) REFERENCES cours(id\_cours)

);

**Visualisation :**

TABLE cours              TABLE inscriptions

┌──────────┬───────┐     ┌────────────────┬────────────┬──────────┐

│ id\_cours │ titre │     │ id\_inscription │ id\_etudiant│ id\_cours │

├──────────┼───────┤     ├────────────────┼────────────┼──────────┤

│    1     │  SQL  │◄────│       1        │     10     │    1     │

│    2     │Python │     │       2        │     11     │    1     │

└──────────┴───────┘     └────────────────┴────────────┴──────────┘

**Test :**

\-- ✅ id\_cours \= 1 existe dans la table cours : OK

INSERT INTO inscriptions (id\_etudiant, id\_cours) VALUES (10, 1);

\-- ❌ id\_cours \= 99 n'existe pas : ERREUR

INSERT INTO inscriptions (id\_etudiant, id\_cours) VALUES (11, 99);

\-- Erreur : Foreign key constraint fails

---

### 8.8 Exemple complet avec toutes les contraintes

CREATE DATABASE ecole\_bootcamp;

USE ecole\_bootcamp;

\-- Table formateurs

CREATE TABLE formateurs (

    id\_formateur   INTEGER       PRIMARY KEY AUTO\_INCREMENT,

    prenom         VARCHAR(50)   NOT NULL,

    nom            VARCHAR(50)   NOT NULL,

    email          VARCHAR(100)  UNIQUE NOT NULL,

    specialite     VARCHAR(100)  DEFAULT 'Non spécifiée'

);

\-- Table cours

CREATE TABLE cours (

    id\_cours       INTEGER       PRIMARY KEY AUTO\_INCREMENT,

    titre          VARCHAR(100)  NOT NULL,

    duree\_heures   INTEGER       CHECK (duree\_heures \> 0),

    id\_formateur   INTEGER,

    FOREIGN KEY (id\_formateur) REFERENCES formateurs(id\_formateur)

);

\-- Table étudiants

CREATE TABLE etudiants (

    id\_etudiant      INTEGER      PRIMARY KEY AUTO\_INCREMENT,

    prenom           VARCHAR(50)  NOT NULL,

    nom              VARCHAR(50)  NOT NULL,

    email            VARCHAR(100) UNIQUE NOT NULL,

    age              INTEGER      CHECK (age \>= 18),

    date\_inscription DATE         DEFAULT (CURRENT\_DATE),

    statut           VARCHAR(20)  DEFAULT 'actif'

);

\-- Table inscriptions (liaison étudiants ↔ cours)

CREATE TABLE inscriptions (

    id\_inscription  INTEGER  PRIMARY KEY AUTO\_INCREMENT,

    id\_etudiant     INTEGER  NOT NULL,

    id\_cours        INTEGER  NOT NULL,

    note\_finale     DECIMAL(4,2) CHECK (note\_finale \>= 0 AND note\_finale \<= 20),

    FOREIGN KEY (id\_etudiant) REFERENCES etudiants(id\_etudiant),

    FOREIGN KEY (id\_cours)    REFERENCES cours(id\_cours)

);

---

## 9\. Conclusion

### 📌 Récapitulatif des commandes DDL

DDL — Data Definition Language

│

├── CREATE    → Créer une base, une table, un index...

├── ALTER     → Modifier la structure (ajouter/supprimer/renommer une colonne)

├── DROP      → Supprimer définitivement un objet

└── TRUNCATE  → Vider les données d'une table (structure conservée)

### 🔑 Points clés à retenir

1. **DDL \= Structure** : le DDL définit le squelette de votre base de données, pas son contenu.  
2. **Auto-commit** : les commandes DDL sont permanentes dès leur exécution.  
3. **Les contraintes** garantissent la qualité et la cohérence des données.  
4. **La clé primaire** identifie chaque ligne de façon unique.  
5. **La clé étrangère** assure les liens et l'intégrité entre les tables.

### 🗺️ Ce qui vient ensuite

Maintenant que vous savez **construire** la structure d'une base de données avec le DDL, le prochain chapitre abordera le **DML (Data Manipulation Language)** pour **insérer, modifier et supprimer des données** dans vos tables.

---

## 10\. ✅ Point de contrôle — Data Definition Language

Testez vos connaissances avec ces exercices \!

---

### 📝 Questions théoriques

**Q1.** Que signifie l'acronyme DDL ?

**Réponse :** Data Definition Language — Langage de Définition de Données.

**Q2.** Quelle est la différence entre `DROP TABLE` et `TRUNCATE TABLE` ?

**Réponse :** `DROP TABLE` supprime la table **et** toutes ses données (la structure disparaît). `TRUNCATE TABLE` supprime uniquement les données mais **conserve la structure** de la table.

**Q3.** Quelle contrainte utilise-t-on pour s'assurer qu'une colonne ne peut pas contenir deux fois la même valeur ?

**Réponse :** La contrainte `UNIQUE`.

**Q4.** Peut-on annuler une commande DDL avec un `ROLLBACK` ?

**Réponse :** En général **non**, car les commandes DDL sont auto-commit (validées immédiatement). C'est pourquoi il faut être prudent avant d'exécuter un `DROP` ou un `TRUNCATE`.

---

### 💻 Exercices pratiques

**Exercice 1 — Créer une table**

Créez une table `produits` avec les colonnes suivantes :

- `id_produit` : entier, clé primaire, auto-incrémentée  
- `nom_produit` : texte (max 100 caractères), obligatoire  
- `prix` : décimal (6 chiffres, 2 après la virgule), vérification que le prix \> 0  
- `stock` : entier, valeur par défaut à 0  
- `categorie` : texte (max 50 caractères)

👀 Voir la solution CREATE TABLE produits (

    id\_produit   INTEGER       PRIMARY KEY AUTO\_INCREMENT,

    nom\_produit  VARCHAR(100)  NOT NULL,

    prix         DECIMAL(6,2)  CHECK (prix \> 0),

    stock        INTEGER       DEFAULT 0,

    categorie    VARCHAR(50)

);

---

**Exercice 2 — Modifier une table**

La table `produits` a été créée sans la colonne `description`. Ajoutez une colonne `description` de type `TEXT`.

👀 Voir la solution ALTER TABLE produits ADD description TEXT;

---

**Exercice 3 — Clé étrangère**

Créez une table `commandes` avec :

- `id_commande` : entier, clé primaire, auto-incrémentée  
- `id_produit` : entier, clé étrangère vers `produits(id_produit)`  
- `quantite` : entier, vérification que la quantité \>= 1  
- `date_commande` : date, valeur par défaut à la date courante

👀 Voir la solution CREATE TABLE commandes (

    id\_commande   INTEGER  PRIMARY KEY AUTO\_INCREMENT,

    id\_produit    INTEGER  NOT NULL,

    quantite      INTEGER  CHECK (quantite \>= 1),

    date\_commande DATE     DEFAULT (CURRENT\_DATE),

    FOREIGN KEY (id\_produit) REFERENCES produits(id\_produit)

);

---

**Exercice 4 — Tout ensemble**

Dessinez le schéma de la base `ecole_bootcamp` créée dans ce chapitre (tables, colonnes, types, contraintes et liens entre tables).

*Conseil : utilisez un outil comme dbdiagram.io pour visualiser votre schéma.*

---

### 🏆 Challenge bonus

Créez un schéma complet pour une **bibliothèque numérique** avec au minimum :

- Une table `auteurs`  
- Une table `livres` (liée aux auteurs)  
- Une table `membres`  
- Une table `emprunts` (liée aux livres et aux membres)

Appliquez toutes les contraintes appropriées.

---

*📘 Fin du chapitre — Data Definition Language | Bootcamp Data Science*  
