# ✅ Correction — Checkpoint SQL
## Système d'information sur la participation des employés

---

## 📋 Table des matières

1. [Analyse du schéma](#1-analyse-du-schéma)
2. [Schéma relationnel](#2-schéma-relationnel)
3. [Script SQL complet](#3-script-sql-complet)
4. [Explications pédagogiques](#4-explications-pédagogiques)
5. [Insertion de données de test](#5-insertion-de-données-de-test)
6. [Vérifications et requêtes de contrôle](#6-vérifications-et-requêtes-de-contrôle)
7. [Erreurs fréquentes à éviter](#7-erreurs-fréquentes-à-éviter)

---

## 1. Analyse du schéma

Avant d'écrire le moindre code SQL, il faut d'abord **comprendre les entités et leurs relations**.

### Les 4 entités identifiées

| Entité | Rôle | Clé primaire |
|--------|------|-------------|
| `Departement` | Informations sur les services | `Num_S` |
| `Employe` | Informations sur les employés | `Num_E` |
| `Projet` | Informations sur les projets | `Num_P` |
| `Employe_Projet` | Participation des employés aux projets | `(Num_E, Num_P)` |

### Les relations entre entités

```
Departement ──< Employe
     │          (Un département contient plusieurs employés)
     │
     └────────< Projet
               (Un département pilote plusieurs projets)

Employe >────< Projet
(via Employe_Projet : un employé peut participer à plusieurs projets,
 un projet peut avoir plusieurs employés → relation N:N)
```

### Ordre de création des tables

> ⚠️ **Règle fondamentale** : une table avec une clé étrangère doit être créée **APRÈS** la table qu'elle référence.

```
Ordre obligatoire :
1. Departement  (aucune dépendance)
2. Employe      (dépend de Departement)
3. Projet       (dépend de Departement)
4. Employe_Projet (dépend de Employe et Projet)
```

---

## 2. Schéma relationnel

```
┌───────────────────────┐         ┌───────────────────────────────┐
│      Departement      │         │            Employe            │
├───────────────────────┤         ├───────────────────────────────┤
│ Num_S (PK)        INT │◄────────│ Num_E (PK)              INT   │
│ Etiquette  VARCHAR(255│         │ Nom             VARCHAR(255)  │
│ Nom_responsable       │         │ Position        VARCHAR(255)  │
│            VARCHAR(255│         │ Salaire         DECIMAL(10,2) │
└───────────┬───────────┘         │ Num_S_Dept (FK)         INT   │
            │                     └───────────────┬───────────────┘
            │                                     │
            │                                     │
            ▼                                     ▼
┌───────────────────────┐         ┌───────────────────────────────┐
│        Projet         │         │        Employe_Projet         │
├───────────────────────┤         ├───────────────────────────────┤
│ Num_P (PK)        INT │◄────────│ Num_E_FK (FK)           INT   │
│ Titre  VARCHAR(255)   │         │ Num_P_FK (FK)           INT   │
│ Date_debut        DATE│         │ Role            VARCHAR(255)  │
│ Date_fin          DATE│         │ PK (Num_E_FK, Num_P_FK)       │
│ Num_S_FK (FK)     INT │         └───────────────────────────────┘
└───────────────────────┘
```

---

## 3. Script SQL complet

### Étape 1 — Créer la base de données

```sql
-- Création de la base de données
CREATE DATABASE IF NOT EXISTS systeme_employes;
USE systeme_employes;
```

---

### Étape 2 — Table `Departement`

```sql
-- Table Departement
-- Créée EN PREMIER car elle est référencée par Employe et Projet
CREATE TABLE Departement (
    Num_S            INT            NOT NULL,
    Etiquette        VARCHAR(255)   NOT NULL,
    Nom_responsable  VARCHAR(255)   NOT NULL,

    CONSTRAINT pk_departement PRIMARY KEY (Num_S)
);
```

**Explications :**
- `Num_S` est la **clé primaire** → identifie chaque département de façon unique
- `NOT NULL` sur tous les champs car un département sans nom ou sans responsable n'a pas de sens
- `CONSTRAINT pk_departement` : nommer les contraintes est une bonne pratique (facilite le débogage)

---

### Étape 3 — Table `Employe`

```sql
-- Table Employe
-- Dépend de Departement → créée APRÈS
CREATE TABLE Employe (
    Num_E            INT             NOT NULL,
    Nom              VARCHAR(255)    NOT NULL,
    Position         VARCHAR(255)    NOT NULL,
    Salaire          DECIMAL(10, 2)  NOT NULL,
    Num_S_Dept       INT,

    CONSTRAINT pk_employe   PRIMARY KEY (Num_E),
    CONSTRAINT fk_emp_dept  FOREIGN KEY (Num_S_Dept)
                            REFERENCES Departement(Num_S)
                            ON DELETE SET NULL
                            ON UPDATE CASCADE
);
```

**Explications :**
- `DECIMAL(10, 2)` : salaire avec 10 chiffres au total, dont 2 après la virgule (ex : `99999999.99`)
- `Num_S_Dept` peut être `NULL` : un employé peut exister temporairement sans département assigné
- `ON DELETE SET NULL` : si un département est supprimé, l'employé reste mais son département passe à NULL (plutôt que de supprimer l'employé)
- `ON UPDATE CASCADE` : si le numéro de département change, la mise à jour se propage automatiquement

---

### Étape 4 — Table `Projet`

```sql
-- Table Projet
-- Dépend de Departement → créée APRÈS Departement
CREATE TABLE Projet (
    Num_P      INT           NOT NULL,
    Titre      VARCHAR(255)  NOT NULL,
    Date_debut DATE          NOT NULL,
    Date_fin   DATE,
    Num_S_FK   INT,

    CONSTRAINT pk_projet        PRIMARY KEY (Num_P),
    CONSTRAINT fk_projet_dept   FOREIGN KEY (Num_S_FK)
                                REFERENCES Departement(Num_S)
                                ON DELETE SET NULL
                                ON UPDATE CASCADE,
    CONSTRAINT chk_dates        CHECK (Date_fin IS NULL OR Date_fin > Date_debut)
);
```

**Explications :**
- `Date_fin` est nullable : un projet en cours n'a pas encore de date de fin
- `CONSTRAINT chk_dates` : contrainte CHECK pour garantir que la date de fin est toujours après la date de début — bonne pratique de cohérence des données
- Même logique `ON DELETE SET NULL` / `ON UPDATE CASCADE` que pour Employe

---

### Étape 5 — Table `Employe_Projet`

```sql
-- Table Employe_Projet (table de liaison N:N)
-- Dépend de Employe ET de Projet → créée EN DERNIER
CREATE TABLE Employe_Projet (
    Num_E_FK   INT           NOT NULL,
    Num_P_FK   INT           NOT NULL,
    Role       VARCHAR(255)  NOT NULL,

    CONSTRAINT pk_employe_projet  PRIMARY KEY (Num_E_FK, Num_P_FK),
    CONSTRAINT fk_ep_employe      FOREIGN KEY (Num_E_FK)
                                  REFERENCES Employe(Num_E)
                                  ON DELETE CASCADE
                                  ON UPDATE CASCADE,
    CONSTRAINT fk_ep_projet       FOREIGN KEY (Num_P_FK)
                                  REFERENCES Projet(Num_P)
                                  ON DELETE CASCADE
                                  ON UPDATE CASCADE
);
```

**Explications :**
- **Clé primaire composite** `(Num_E_FK, Num_P_FK)` : un employé ne peut avoir qu'**un seul rôle par projet** (une même paire employé-projet est unique)
- `ON DELETE CASCADE` : si un employé ou un projet est supprimé, ses lignes dans `Employe_Projet` sont automatiquement supprimées (logique : la participation disparaît avec l'un ou l'autre)

---

### Script complet en un bloc

```sql
-- ================================================
-- SCRIPT COMPLET : Système de participation employés
-- ================================================

CREATE DATABASE IF NOT EXISTS systeme_employes;
USE systeme_employes;

-- 1. Table Departement
CREATE TABLE Departement (
    Num_S            INT            NOT NULL,
    Etiquette        VARCHAR(255)   NOT NULL,
    Nom_responsable  VARCHAR(255)   NOT NULL,
    CONSTRAINT pk_departement PRIMARY KEY (Num_S)
);

-- 2. Table Employe
CREATE TABLE Employe (
    Num_E        INT             NOT NULL,
    Nom          VARCHAR(255)    NOT NULL,
    Position     VARCHAR(255)    NOT NULL,
    Salaire      DECIMAL(10, 2)  NOT NULL,
    Num_S_Dept   INT,
    CONSTRAINT pk_employe  PRIMARY KEY (Num_E),
    CONSTRAINT fk_emp_dept FOREIGN KEY (Num_S_Dept)
                           REFERENCES Departement(Num_S)
                           ON DELETE SET NULL
                           ON UPDATE CASCADE
);

-- 3. Table Projet
CREATE TABLE Projet (
    Num_P      INT           NOT NULL,
    Titre      VARCHAR(255)  NOT NULL,
    Date_debut DATE          NOT NULL,
    Date_fin   DATE,
    Num_S_FK   INT,
    CONSTRAINT pk_projet      PRIMARY KEY (Num_P),
    CONSTRAINT fk_projet_dept FOREIGN KEY (Num_S_FK)
                              REFERENCES Departement(Num_S)
                              ON DELETE SET NULL
                              ON UPDATE CASCADE,
    CONSTRAINT chk_dates      CHECK (Date_fin IS NULL OR Date_fin > Date_debut)
);

-- 4. Table Employe_Projet
CREATE TABLE Employe_Projet (
    Num_E_FK  INT           NOT NULL,
    Num_P_FK  INT           NOT NULL,
    Role      VARCHAR(255)  NOT NULL,
    CONSTRAINT pk_employe_projet PRIMARY KEY (Num_E_FK, Num_P_FK),
    CONSTRAINT fk_ep_employe     FOREIGN KEY (Num_E_FK)
                                 REFERENCES Employe(Num_E)
                                 ON DELETE CASCADE
                                 ON UPDATE CASCADE,
    CONSTRAINT fk_ep_projet      FOREIGN KEY (Num_P_FK)
                                 REFERENCES Projet(Num_P)
                                 ON DELETE CASCADE
                                 ON UPDATE CASCADE
);
```

---

## 4. Explications pédagogiques

### 4.1 Pourquoi nommer les contraintes ?

```sql
-- ❌ Sans nom (difficile à déboguer)
FOREIGN KEY (Num_S_Dept) REFERENCES Departement(Num_S)

-- ✅ Avec nom (erreur claire, facile à modifier)
CONSTRAINT fk_emp_dept FOREIGN KEY (Num_S_Dept) REFERENCES Departement(Num_S)
```

Quand une contrainte est violée, MySQL affichera `fk_emp_dept` dans le message d'erreur — ce qui vous dit immédiatement d'où vient le problème.

---

### 4.2 Pourquoi une clé primaire composite dans `Employe_Projet` ?

```
Un employé peut travailler sur PLUSIEURS projets
Un projet peut avoir PLUSIEURS employés
→ Relation MANY-TO-MANY (N:N)

La paire (Num_E_FK, Num_P_FK) est unique :
✅ Employé 1 sur Projet 1 → autorisé
✅ Employé 1 sur Projet 2 → autorisé
✅ Employé 2 sur Projet 1 → autorisé
❌ Employé 1 sur Projet 1 (une 2ème fois) → interdit
```

---

### 4.3 Choix des actions ON DELETE / ON UPDATE

| Table | ON DELETE | ON UPDATE | Raison |
|-------|-----------|-----------|--------|
| `Employe` → `Departement` | `SET NULL` | `CASCADE` | Un employé peut exister sans département |
| `Projet` → `Departement` | `SET NULL` | `CASCADE` | Un projet peut exister sans département |
| `Employe_Projet` → `Employe` | `CASCADE` | `CASCADE` | La participation n'existe pas sans l'employé |
| `Employe_Projet` → `Projet` | `CASCADE` | `CASCADE` | La participation n'existe pas sans le projet |

---

### 4.4 Récapitulatif visuel des contraintes

```
Departement
  Num_S        → PK
  Etiquette    → NOT NULL
  Nom_resp.    → NOT NULL

Employe
  Num_E        → PK
  Nom          → NOT NULL
  Position     → NOT NULL
  Salaire      → NOT NULL, DECIMAL(10,2)
  Num_S_Dept   → FK → Departement(Num_S), nullable

Projet
  Num_P        → PK
  Titre        → NOT NULL
  Date_debut   → NOT NULL
  Date_fin     → nullable, CHECK > Date_debut
  Num_S_FK     → FK → Departement(Num_S), nullable

Employe_Projet
  Num_E_FK     → FK → Employe(Num_E), NOT NULL
  Num_P_FK     → FK → Projet(Num_P), NOT NULL
  Role         → NOT NULL
  (Num_E_FK, Num_P_FK) → PK composite
```

---

## 5. Insertion de données de test

Pour vérifier que le schéma fonctionne correctement, insérons quelques données.

```sql
-- 1. Insérer des départements EN PREMIER
INSERT INTO Departement (Num_S, Etiquette, Nom_responsable) VALUES
    (1, 'Informatique',  'Alice Kouassi'),
    (2, 'Marketing',     'Bob Traoré'),
    (3, 'Finance',       'Claire Diallo');

-- 2. Insérer des employés
INSERT INTO Employe (Num_E, Nom, Position, Salaire, Num_S_Dept) VALUES
    (101, 'David Keita',   'Développeur Senior',   2500000.00, 1),
    (102, 'Emma Sow',      'Chef de projet',       3000000.00, 1),
    (103, 'Fatou Bamba',   'Responsable Marketing',2800000.00, 2),
    (104, 'Kofi Mensah',   'Analyste Financier',   2200000.00, 3),
    (105, 'Lucas Asante',  'Développeur Junior',   1800000.00, 1);

-- 3. Insérer des projets
INSERT INTO Projet (Num_P, Titre, Date_debut, Date_fin, Num_S_FK) VALUES
    (201, 'Refonte site web',          '2024-01-15', '2024-06-30', 1),
    (202, 'Campagne réseaux sociaux',  '2024-02-01', '2024-04-30', 2),
    (203, 'Audit financier annuel',    '2024-03-01', NULL,         3),
    (204, 'Application mobile',        '2024-04-01', '2024-12-31', 1);

-- 4. Insérer les participations
INSERT INTO Employe_Projet (Num_E_FK, Num_P_FK, Role) VALUES
    (101, 201, 'Développeur principal'),
    (102, 201, 'Chef de projet'),
    (105, 201, 'Développeur front-end'),
    (103, 202, 'Responsable campagne'),
    (104, 203, 'Auditeur principal'),
    (101, 204, 'Architecte technique'),
    (102, 204, 'Chef de projet'),
    (105, 204, 'Développeur mobile');
```

---

## 6. Vérifications et requêtes de contrôle

Après avoir créé le schéma et inséré des données, voici comment vérifier que tout fonctionne.

### Vérification 1 — Structure des tables

```sql
-- Vérifier la structure de chaque table
DESCRIBE Departement;
DESCRIBE Employe;
DESCRIBE Projet;
DESCRIBE Employe_Projet;
```

### Vérification 2 — Intégrité référentielle (test de violation)

```sql
-- ❌ Tenter d'insérer un employé dans un département inexistant
-- Ceci doit ÉCHOUER grâce à la clé étrangère
INSERT INTO Employe (Num_E, Nom, Position, Salaire, Num_S_Dept)
VALUES (999, 'Test', 'Test', 1000, 999);
-- Erreur attendue : Cannot add or update a child row: a foreign key constraint fails
```

### Vérification 3 — Requêtes métier

```sql
-- Liste complète des employés avec leur département
SELECT
    e.Num_E,
    e.Nom,
    e.Position,
    e.Salaire,
    d.Etiquette AS Departement
FROM Employe e
LEFT JOIN Departement d ON e.Num_S_Dept = d.Num_S
ORDER BY d.Etiquette, e.Nom;

-- Projets avec leur département responsable
SELECT
    p.Num_P,
    p.Titre,
    p.Date_debut,
    p.Date_fin,
    d.Etiquette AS Departement_responsable,
    CASE WHEN p.Date_fin IS NULL THEN 'En cours' ELSE 'Terminé' END AS Statut
FROM Projet p
LEFT JOIN Departement d ON p.Num_S_FK = d.Num_S;

-- Employés et leurs projets avec leurs rôles
SELECT
    e.Nom       AS Employe,
    p.Titre     AS Projet,
    ep.Role     AS Role_dans_projet
FROM Employe_Projet ep
INNER JOIN Employe e ON ep.Num_E_FK = e.Num_E
INNER JOIN Projet  p ON ep.Num_P_FK = p.Num_P
ORDER BY e.Nom, p.Titre;

-- Nombre de projets par employé
SELECT
    e.Nom,
    COUNT(ep.Num_P_FK) AS Nombre_de_projets
FROM Employe e
LEFT JOIN Employe_Projet ep ON e.Num_E = ep.Num_E_FK
GROUP BY e.Num_E, e.Nom
ORDER BY Nombre_de_projets DESC;

-- Employés d'un projet spécifique (ex : projet 201)
SELECT
    e.Nom,
    e.Position,
    ep.Role
FROM Employe_Projet ep
INNER JOIN Employe e ON ep.Num_E_FK = e.Num_E
WHERE ep.Num_P_FK = 201;
```

---

## 7. Erreurs fréquentes à éviter

### ❌ Erreur 1 — Mauvais ordre de création des tables

```sql
-- ❌ Créer Employe avant Departement
CREATE TABLE Employe (
    ...
    FOREIGN KEY (Num_S_Dept) REFERENCES Departement(Num_S) -- Departement n'existe pas encore !
);
-- Erreur : Table 'Departement' doesn't exist

-- ✅ Toujours créer la table parente EN PREMIER
CREATE TABLE Departement (...);
CREATE TABLE Employe (...); -- Maintenant on peut référencer Departement
```

### ❌ Erreur 2 — Oublier la clé primaire composite

```sql
-- ❌ Deux clés primaires séparées au lieu d'une composite
CREATE TABLE Employe_Projet (
    Num_E_FK  INT  PRIMARY KEY,  -- ← FAUX : cela interdit à un employé d'être sur plusieurs projets
    Num_P_FK  INT  PRIMARY KEY,
    Role      VARCHAR(255)
);

-- ✅ Clé primaire composite
CREATE TABLE Employe_Projet (
    Num_E_FK  INT NOT NULL,
    Num_P_FK  INT NOT NULL,
    Role      VARCHAR(255),
    PRIMARY KEY (Num_E_FK, Num_P_FK)  -- ← la paire est unique
);
```

### ❌ Erreur 3 — Oublier NOT NULL sur les clés étrangères de la table de liaison

```sql
-- ❌ Clés étrangères nullables dans la table de liaison
CREATE TABLE Employe_Projet (
    Num_E_FK  INT,  -- ← NULL autorisé : une participation sans employé n'a pas de sens
    Num_P_FK  INT,
    ...
);

-- ✅ Clés étrangères NOT NULL dans la table de liaison
CREATE TABLE Employe_Projet (
    Num_E_FK  INT  NOT NULL,
    Num_P_FK  INT  NOT NULL,
    ...
);
```

### ❌ Erreur 4 — Supprimer les tables dans le mauvais ordre

```sql
-- ❌ Tenter de supprimer Departement alors qu'Employe le référence encore
DROP TABLE Departement;
-- Erreur : Cannot drop table 'Departement' (foreign key constraint)

-- ✅ Supprimer dans l'ordre inverse de la création
DROP TABLE IF EXISTS Employe_Projet;
DROP TABLE IF EXISTS Projet;
DROP TABLE IF EXISTS Employe;
DROP TABLE IF EXISTS Departement;
```

---

*📘 Correction du Checkpoint — Système de participation des employés | Bootcamp Data Science*
