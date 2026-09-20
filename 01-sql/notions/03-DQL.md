# 🔍 Data Query Language (DQL) — Cours Bootcamp Data Science

> **Chapitre 3** | Prérequis : Chapitre 1 (DDL) + Chapitre 2 (DML)

---

## Table des matières

1. [Introduction au DQL](#1-introduction-au-dql)
2. [Rappel — Le SELECT de base](#2-rappel--le-select-de-base)
3. [Fonctions d'agrégation](#3-fonctions-dagrégation)
4. [GROUP BY — Regrouper les données](#4-group-by--regrouper-les-données)
5. [HAVING — Filtrer les groupes](#5-having--filtrer-les-groupes)
6. [Les JOIN — Combiner plusieurs tables](#6-les-join--combiner-plusieurs-tables)
7. [Les sous-requêtes (Subqueries)](#7-les-sous-requêtes-subqueries)
8. [Les fonctions SQL utiles](#8-les-fonctions-sql-utiles)
9. [Ordre d'exécution d'un SELECT](#9-ordre-dexécution-dun-select)
10. [Exemple complet — Schéma École Bootcamp](#10-exemple-complet--schéma-école-bootcamp)
11. [Conclusion](#11-conclusion)
12. [✅ Point de contrôle — DQL](#12--point-de-contrôle--dql)

---

## 1. Introduction au DQL

### 🔍 Qu'est-ce que le DQL ?

Le **DQL (Data Query Language)** est la partie de SQL dédiée à **l'interrogation des données**. Son unique commande est `SELECT`, mais elle est extrêmement puissante grâce à ses nombreuses clauses et fonctions.

> 💡 **Analogie** : Si votre base de données est une **bibliothèque géante**, le DQL est votre **bibliothécaire expert**. Vous lui posez des questions précises et il vous ramène exactement les livres dont vous avez besoin — filtrés, triés, comptés, regroupés.

### 🎯 Ce que le DQL permet de faire

```
DQL — Data Query Language
│
├── Sélectionner des colonnes spécifiques
├── Filtrer les lignes (WHERE)
├── Regrouper et agréger (GROUP BY + fonctions)
├── Filtrer les groupes (HAVING)
├── Combiner plusieurs tables (JOIN)
├── Imbriquer des requêtes (Sous-requêtes)
└── Trier et paginer les résultats (ORDER BY + LIMIT)
```

### ⚙️ Anatomie complète d'un SELECT

```sql
SELECT   colonnes ou expressions      -- Quoi afficher
FROM     table_principale             -- D'où viennent les données
JOIN     autre_table ON condition     -- Liaison avec d'autres tables
WHERE    condition_lignes             -- Filtrer les lignes
GROUP BY colonne_de_regroupement      -- Regrouper
HAVING   condition_groupes            -- Filtrer les groupes
ORDER BY colonne [ASC|DESC]           -- Trier
LIMIT    nombre OFFSET décalage;      -- Paginer
```

---

## 2. Rappel — Le SELECT de base

Avant d'aller plus loin, voici un rappel rapide des bases vues au chapitre 2.

```sql
-- Toutes les colonnes
SELECT * FROM etudiants;

-- Colonnes spécifiques avec alias
SELECT prenom AS "Prénom", nom AS "Nom", age AS "Âge"
FROM etudiants;

-- Avec filtre et tri
SELECT prenom, nom, age
FROM etudiants
WHERE statut = 'actif'
ORDER BY age DESC
LIMIT 5;
```

> Dans ce chapitre, nous allons **aller beaucoup plus loin** avec les agrégations, les jointures et les sous-requêtes.

---

## 3. Fonctions d'agrégation

### 📖 Définition

Les **fonctions d'agrégation** calculent une valeur unique à partir d'un ensemble de lignes. Elles "résument" les données.

> 💡 **Analogie** : Vous avez une liste de notes d'élèves. Les fonctions d'agrégation vous donnent la **moyenne**, le **maximum**, le **minimum**, le **total** ou le **nombre** — sans lister chaque note.

### 3.1 Vue d'ensemble des fonctions

| Fonction | Description | Exemple |
|----------|-------------|---------|
| `COUNT()` | Compte le nombre de lignes | Nombre d'étudiants |
| `SUM()` | Calcule la somme | Total des heures de cours |
| `AVG()` | Calcule la moyenne | Note moyenne |
| `MAX()` | Trouve la valeur maximale | Meilleure note |
| `MIN()` | Trouve la valeur minimale | Étudiant le plus jeune |

### 3.2 COUNT — Compter les lignes

```sql
-- Compter tous les étudiants
SELECT COUNT(*) AS nombre_etudiants
FROM etudiants;
-- Résultat : 5

-- Compter les étudiants actifs seulement
SELECT COUNT(*) AS etudiants_actifs
FROM etudiants
WHERE statut = 'actif';
-- Résultat : 4

-- COUNT(colonne) ignore les valeurs NULL
SELECT COUNT(note_finale) AS notes_renseignees
FROM inscriptions;
```

> ⚠️ `COUNT(*)` compte toutes les lignes (même celles avec NULL).
> `COUNT(colonne)` ne compte que les lignes où la colonne n'est pas NULL.

### 3.3 SUM — Calculer une somme

```sql
-- Total des heures de tous les cours
SELECT SUM(duree_heures) AS total_heures
FROM cours;
-- Résultat : 90

-- Total des heures des cours du formateur 1
SELECT SUM(duree_heures) AS heures_formateur1
FROM cours
WHERE id_formateur = 1;
```

### 3.4 AVG — Calculer une moyenne

```sql
-- Moyenne d'âge de tous les étudiants
SELECT AVG(age) AS age_moyen
FROM etudiants;
-- Résultat : 24.6

-- Moyenne des notes finales (en ignorant les NULL)
SELECT AVG(note_finale) AS note_moyenne
FROM inscriptions;

-- Arrondir la moyenne à 2 décimales
SELECT ROUND(AVG(note_finale), 2) AS note_moyenne
FROM inscriptions;
```

### 3.5 MAX et MIN — Valeurs extrêmes

```sql
-- La meilleure et la moins bonne note
SELECT
    MAX(note_finale) AS meilleure_note,
    MIN(note_finale) AS note_minimale
FROM inscriptions;

-- L'étudiant le plus jeune et le plus âgé
SELECT
    MIN(age) AS age_minimum,
    MAX(age) AS age_maximum
FROM etudiants;

-- Durée du cours le plus long et le plus court
SELECT
    MAX(duree_heures) AS cours_le_plus_long,
    MIN(duree_heures) AS cours_le_plus_court
FROM cours;
```

### 3.6 Combiner plusieurs agrégations

```sql
-- Tableau de bord complet des étudiants
SELECT
    COUNT(*)                    AS nombre_total,
    COUNT(note_finale)          AS notes_renseignees,
    ROUND(AVG(note_finale), 2)  AS moyenne_generale,
    MAX(note_finale)            AS meilleure_note,
    MIN(note_finale)            AS note_minimale,
    SUM(note_finale)            AS total_points
FROM inscriptions;
```

**Résultat :**
```
┌───────────────┬──────────────────┬──────────────────┬───────────────┬───────────────┬──────────────┐
│ nombre_total  │ notes_renseignees│ moyenne_generale │ meilleure_note│ note_minimale │ total_points │
├───────────────┼──────────────────┼──────────────────┼───────────────┼───────────────┼──────────────┤
│      6        │        3         │      14.50       │     16.5      │     12.0      │    43.50     │
└───────────────┴──────────────────┴──────────────────┴───────────────┴───────────────┴──────────────┘
```

---

## 4. GROUP BY — Regrouper les données

### 📖 Définition

La clause `GROUP BY` permet de **regrouper les lignes** qui ont la même valeur dans une ou plusieurs colonnes, puis d'appliquer une fonction d'agrégation sur chaque groupe.

> 💡 **Analogie** : Vous avez une liste de dépenses. `GROUP BY categorie` regroupe toutes les dépenses par catégorie (alimentation, transport, loisirs…) pour calculer le total de chaque catégorie.

### Syntaxe

```sql
SELECT colonne_groupe, FONCTION_AGREGATION(colonne)
FROM table
GROUP BY colonne_groupe;
```

### 4.1 GROUP BY simple

```sql
-- Nombre d'étudiants par statut
SELECT statut, COUNT(*) AS nombre
FROM etudiants
GROUP BY statut;
```

**Résultat :**
```
┌─────────┬────────┐
│ statut  │ nombre │
├─────────┼────────┤
│ actif   │   4    │
│ inactif │   1    │
└─────────┴────────┘
```

```sql
-- Nombre d'inscriptions par cours
SELECT id_cours, COUNT(*) AS nb_inscrits
FROM inscriptions
GROUP BY id_cours;
```

**Résultat :**
```
┌──────────┬─────────────┐
│ id_cours │ nb_inscrits │
├──────────┼─────────────┤
│    1     │      2      │
│    2     │      2      │
│    3     │      1      │
│    4     │      1      │
└──────────┴─────────────┘
```

### 4.2 GROUP BY avec plusieurs agrégations

```sql
-- Statistiques des notes par cours
SELECT
    id_cours,
    COUNT(note_finale)          AS nb_notes,
    ROUND(AVG(note_finale), 2)  AS moyenne,
    MAX(note_finale)            AS meilleure,
    MIN(note_finale)            AS plus_basse
FROM inscriptions
GROUP BY id_cours;
```

### 4.3 GROUP BY sur plusieurs colonnes

```sql
-- Nombre d'étudiants par statut ET par tranche d'âge
SELECT
    statut,
    CASE
        WHEN age < 23 THEN 'Moins de 23 ans'
        WHEN age BETWEEN 23 AND 26 THEN '23 à 26 ans'
        ELSE 'Plus de 26 ans'
    END AS tranche_age,
    COUNT(*) AS nombre
FROM etudiants
GROUP BY statut, tranche_age;
```

### 4.4 ⚠️ Règle importante de GROUP BY

> Toute colonne dans le `SELECT` qui n'est **pas une fonction d'agrégation** doit être dans le `GROUP BY`.

```sql
-- ✅ Correct : prenom est dans GROUP BY
SELECT prenom, COUNT(*) AS nb_inscriptions
FROM inscriptions
JOIN etudiants USING (id_etudiant)
GROUP BY prenom;

-- ❌ Incorrect : nom n'est ni agrégé ni dans GROUP BY
SELECT prenom, nom, COUNT(*) AS nb_inscriptions
FROM inscriptions
GROUP BY prenom;
-- Erreur : 'nom' is not in GROUP BY
```

---

## 5. HAVING — Filtrer les groupes

### 📖 Définition

La clause `HAVING` filtre les **résultats d'un GROUP BY**. Elle joue le même rôle que `WHERE`, mais s'applique **après le regroupement**.

> 💡 **Analogie** :
> - `WHERE` filtre les **lignes individuelles** (avant de regrouper)
> - `HAVING` filtre les **groupes** (après avoir regroupé)

### Syntaxe

```sql
SELECT colonne, FONCTION(colonne)
FROM table
GROUP BY colonne
HAVING condition_sur_agregat;
```

### 5.1 HAVING simple

```sql
-- Cours avec plus de 1 inscrit
SELECT id_cours, COUNT(*) AS nb_inscrits
FROM inscriptions
GROUP BY id_cours
HAVING COUNT(*) > 1;
```

**Résultat :**
```
┌──────────┬─────────────┐
│ id_cours │ nb_inscrits │
├──────────┼─────────────┤
│    1     │      2      │
│    2     │      2      │
└──────────┴─────────────┘
```

```sql
-- Étudiants inscrits à plus d'un cours
SELECT id_etudiant, COUNT(*) AS nb_cours
FROM inscriptions
GROUP BY id_etudiant
HAVING COUNT(*) > 1;
```

### 5.2 HAVING avec AVG, SUM

```sql
-- Cours dont la moyenne des notes est supérieure à 13
SELECT id_cours, ROUND(AVG(note_finale), 2) AS moyenne
FROM inscriptions
GROUP BY id_cours
HAVING AVG(note_finale) > 13;

-- Formateurs avec plus de 20 heures de cours au total
SELECT id_formateur, SUM(duree_heures) AS total_heures
FROM cours
GROUP BY id_formateur
HAVING SUM(duree_heures) > 20;
```

### 5.3 WHERE vs HAVING — La différence clé

```sql
-- WHERE filtre AVANT le regroupement (sur les lignes)
SELECT id_cours, COUNT(*) AS nb_inscrits
FROM inscriptions
WHERE note_finale IS NOT NULL        -- ← filtre les lignes sans note
GROUP BY id_cours;

-- HAVING filtre APRÈS le regroupement (sur les groupes)
SELECT id_cours, COUNT(*) AS nb_inscrits
FROM inscriptions
GROUP BY id_cours
HAVING COUNT(*) >= 2;                -- ← filtre les groupes avec moins de 2

-- Les deux ensemble
SELECT id_cours, COUNT(*) AS nb_notes, AVG(note_finale) AS moyenne
FROM inscriptions
WHERE note_finale IS NOT NULL        -- ← d'abord, on exclut les lignes sans note
GROUP BY id_cours
HAVING AVG(note_finale) > 12;       -- ← ensuite, on garde seulement les cours avec moyenne > 12
```

---

## 6. Les JOIN — Combiner plusieurs tables

### 📖 Définition

Les **JOIN** permettent de **combiner des données provenant de plusieurs tables** en les reliant sur une colonne commune (généralement une clé étrangère).

> 💡 **Analogie** : Vous avez deux listes :
> - Liste A : les étudiants (id, prénom)
> - Liste B : les inscriptions (id_etudiant, cours)
>
> Un JOIN, c'est **assembler ces deux listes** en faisant correspondre l'`id_etudiant` pour obtenir "Alice → SQL", "Bob → Python", etc.

### 6.1 Les types de JOIN

```
TABLE A (etudiants)          TABLE B (inscriptions)
┌────┬────────┐              ┌────┬────────────┬──────────┐
│ id │ prenom │              │ id │ id_etudiant│ id_cours │
├────┼────────┤              ├────┼────────────┼──────────┤
│  1 │ Alice  │              │  1 │     1      │    1     │
│  2 │ Bob    │              │  2 │     1      │    2     │
│  3 │ Claire │              │  3 │     2      │    1     │
│  4 │ David  │              └────┴────────────┴──────────┘
└────┴────────┘
(David n'a pas d'inscription)
```

| Type de JOIN | Résultat |
|---|---|
| `INNER JOIN` | Lignes présentes dans **les deux tables** |
| `LEFT JOIN` | Toutes les lignes de la table **gauche** + correspondances de droite |
| `RIGHT JOIN` | Toutes les lignes de la table **droite** + correspondances de gauche |
| `FULL OUTER JOIN` | Toutes les lignes des **deux tables** |

---

### 6.2 INNER JOIN — Correspondances exactes

Retourne uniquement les lignes qui ont une correspondance dans **les deux tables**.

```sql
-- Syntaxe
SELECT colonnes
FROM table_a
INNER JOIN table_b ON table_a.cle = table_b.cle_etrangere;

-- Exemple : afficher les étudiants et leurs cours
SELECT
    e.prenom,
    e.nom,
    c.titre AS cours
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
INNER JOIN cours c        ON i.id_cours    = c.id_cours;
```

**Résultat :**
```
┌────────┬─────────┬─────────────────────────┐
│ prenom │   nom   │          cours          │
├────────┼─────────┼─────────────────────────┤
│ Alice  │ Dupont  │ Introduction à SQL      │
│ Alice  │ Dupont  │ Python pour la Data     │
│ Bob    │ Martin  │ Introduction à SQL      │
│ Awa    │ Traoré  │ Machine Learning Basics │
│ Moussa │ Keita   │ Python pour la Data     │
└────────┴─────────┴─────────────────────────┘
```

> ℹ️ David n'apparaît pas car il n'a aucune inscription. C'est le comportement de l'INNER JOIN.

---

### 6.3 LEFT JOIN — Tout garder à gauche

Retourne **toutes les lignes de la table gauche**, même si elles n'ont pas de correspondance à droite (les colonnes de droite seront `NULL`).

```sql
-- Tous les étudiants, même ceux sans inscription
SELECT
    e.prenom,
    e.nom,
    c.titre AS cours
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
LEFT JOIN cours c        ON i.id_cours    = c.id_cours;
```

**Résultat :**
```
┌────────┬─────────┬─────────────────────────┐
│ prenom │   nom   │          cours          │
├────────┼─────────┼─────────────────────────┤
│ Alice  │ Dupont  │ Introduction à SQL      │
│ Alice  │ Dupont  │ Python pour la Data     │
│ Bob    │ Martin  │ Introduction à SQL      │
│ Claire │ Leclerc │ NULL                    │ ← Pas d'inscription
│ David  │ Moreau  │ NULL                    │ ← Pas d'inscription
│ Moussa │ Keita   │ Python pour la Data     │
└────────┴─────────┴─────────────────────────┘
```

```sql
-- Trouver les étudiants qui n'ont aucune inscription
SELECT e.prenom, e.nom
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
WHERE i.id_inscription IS NULL;
```

**Résultat :**
```
┌────────┬─────────┐
│ prenom │   nom   │
├────────┼─────────┤
│ Claire │ Leclerc │
│ David  │ Moreau  │
└────────┴─────────┘
```

---

### 6.4 RIGHT JOIN — Tout garder à droite

Retourne **toutes les lignes de la table droite**, même sans correspondance à gauche.

```sql
-- Tous les cours, même ceux sans inscriptions
SELECT
    c.titre,
    e.prenom
FROM etudiants e
RIGHT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
RIGHT JOIN cours c        ON i.id_cours    = c.id_cours;
```

> 💡 En pratique, le `RIGHT JOIN` est peu utilisé. On préfère généralement inverser l'ordre des tables et utiliser un `LEFT JOIN`, plus lisible.

---

### 6.5 Schéma visuel des JOIN

```
INNER JOIN          LEFT JOIN           RIGHT JOIN        FULL OUTER JOIN
  ┌──┐ ┌──┐          ┌──┐ ┌──┐          ┌──┐ ┌──┐          ┌──┐ ┌──┐
  │  ███  │          │██████  │          │  │ ██████         │██████████│
  └──┘ └──┘          └──┘ └──┘          └──┘ └──┘          └──┘ └──┘
  Intersection       Tout A + inter.    Tout B + inter.    Tout A + Tout B
```

---

### 6.6 Alias de tables

Quand on utilise plusieurs tables, les **alias** (lettres courtes) améliorent la lisibilité.

```sql
-- Sans alias (lourd à lire)
SELECT etudiants.prenom, cours.titre
FROM etudiants
INNER JOIN inscriptions ON etudiants.id_etudiant = inscriptions.id_etudiant
INNER JOIN cours ON inscriptions.id_cours = cours.id_cours;

-- Avec alias (beaucoup plus lisible)
SELECT e.prenom, c.titre
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
INNER JOIN cours c        ON i.id_cours    = c.id_cours;
```

---

### 6.7 JOIN avec GROUP BY — Combinaison puissante

```sql
-- Nombre d'inscrits par cours (avec le nom du cours)
SELECT
    c.titre,
    COUNT(i.id_inscription) AS nb_inscrits,
    ROUND(AVG(i.note_finale), 2) AS note_moyenne
FROM cours c
LEFT JOIN inscriptions i ON c.id_cours = i.id_cours
GROUP BY c.id_cours, c.titre
ORDER BY nb_inscrits DESC;
```

**Résultat :**
```
┌─────────────────────────┬─────────────┬──────────────┐
│         titre           │ nb_inscrits │ note_moyenne │
├─────────────────────────┼─────────────┼──────────────┤
│ Introduction à SQL      │      2      │    14.75     │
│ Python pour la Data     │      2      │    NULL      │
│ Machine Learning Basics │      1      │    NULL      │
│ Visualisation de données│      1      │    NULL      │
└─────────────────────────┴─────────────┴──────────────┘
```

```sql
-- Formateur avec le plus d'étudiants
SELECT
    f.prenom,
    f.nom,
    COUNT(DISTINCT i.id_etudiant) AS nb_etudiants
FROM formateurs f
INNER JOIN cours c        ON f.id_formateur = c.id_formateur
INNER JOIN inscriptions i ON c.id_cours     = i.id_cours
GROUP BY f.id_formateur, f.prenom, f.nom
ORDER BY nb_etudiants DESC;
```

---

## 7. Les sous-requêtes (Subqueries)

### 📖 Définition

Une **sous-requête** est une requête `SELECT` imbriquée à l'intérieur d'une autre requête. Elle permet d'utiliser le résultat d'une requête comme condition ou source de données pour une autre.

> 💡 **Analogie** : Vous demandez à votre assistant "Trouve-moi les étudiants dont la note est supérieure à la moyenne". Pour répondre, il doit d'abord **calculer la moyenne** (sous-requête), puis **trouver les étudiants** qui dépassent cette valeur.

### 7.1 Sous-requête dans WHERE

```sql
-- Étudiants dont la note est supérieure à la moyenne
SELECT e.prenom, e.nom, i.note_finale
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
WHERE i.note_finale > (
    SELECT AVG(note_finale) FROM inscriptions
);
```

```sql
-- Étudiants inscrits au cours "Introduction à SQL"
SELECT prenom, nom
FROM etudiants
WHERE id_etudiant IN (
    SELECT id_etudiant
    FROM inscriptions
    WHERE id_cours = (
        SELECT id_cours FROM cours WHERE titre = 'Introduction à SQL'
    )
);
```

### 7.2 Sous-requête dans FROM

La sous-requête peut aussi servir de **table temporaire** (on l'appelle alors une table dérivée).

```sql
-- Moyenne des notes par cours, puis filtrer ceux > 13
SELECT *
FROM (
    SELECT id_cours, ROUND(AVG(note_finale), 2) AS moyenne
    FROM inscriptions
    GROUP BY id_cours
) AS stats_cours
WHERE moyenne > 13;
```

### 7.3 Sous-requête dans SELECT

```sql
-- Pour chaque étudiant, afficher sa note et la moyenne générale
SELECT
    e.prenom,
    i.note_finale,
    (SELECT ROUND(AVG(note_finale), 2) FROM inscriptions) AS moyenne_generale
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant;
```

### 7.4 EXISTS — Vérifier l'existence

`EXISTS` retourne `TRUE` si la sous-requête renvoie au moins une ligne.

```sql
-- Étudiants qui ont au moins une inscription
SELECT prenom, nom
FROM etudiants e
WHERE EXISTS (
    SELECT 1
    FROM inscriptions i
    WHERE i.id_etudiant = e.id_etudiant
);

-- Étudiants sans aucune inscription (NOT EXISTS)
SELECT prenom, nom
FROM etudiants e
WHERE NOT EXISTS (
    SELECT 1
    FROM inscriptions i
    WHERE i.id_etudiant = e.id_etudiant
);
```

---

## 8. Les fonctions SQL utiles

### 8.1 Fonctions sur les chaînes de caractères

| Fonction | Description | Exemple | Résultat |
|----------|-------------|---------|----------|
| `UPPER(str)` | Mettre en majuscules | `UPPER('alice')` | `'ALICE'` |
| `LOWER(str)` | Mettre en minuscules | `LOWER('ALICE')` | `'alice'` |
| `LENGTH(str)` | Longueur de la chaîne | `LENGTH('Alice')` | `5` |
| `CONCAT(a, b)` | Concaténer des chaînes | `CONCAT('Alice', ' Dupont')` | `'Alice Dupont'` |
| `SUBSTRING(str, pos, n)` | Extraire une partie | `SUBSTRING('Alice', 1, 3)` | `'Ali'` |
| `TRIM(str)` | Supprimer les espaces | `TRIM('  Alice  ')` | `'Alice'` |
| `REPLACE(str, a, b)` | Remplacer dans une chaîne | `REPLACE('Hello', 'o', '0')` | `'Hell0'` |

```sql
-- Afficher le nom complet en majuscules
SELECT UPPER(CONCAT(prenom, ' ', nom)) AS nom_complet
FROM etudiants;

-- Résultat : 'ALICE DUPONT', 'BOB MARTIN', ...

-- Extraire le domaine d'un email
SELECT email, SUBSTRING(email, POSITION('@' IN email) + 1) AS domaine
FROM etudiants;
```

### 8.2 Fonctions sur les nombres

| Fonction | Description | Exemple | Résultat |
|----------|-------------|---------|----------|
| `ROUND(n, d)` | Arrondir à d décimales | `ROUND(14.567, 2)` | `14.57` |
| `CEIL(n)` | Arrondir au supérieur | `CEIL(14.2)` | `15` |
| `FLOOR(n)` | Arrondir à l'inférieur | `FLOOR(14.9)` | `14` |
| `ABS(n)` | Valeur absolue | `ABS(-5)` | `5` |
| `MOD(a, b)` | Modulo (reste division) | `MOD(10, 3)` | `1` |

```sql
-- Moyenne arrondie à 1 décimale
SELECT ROUND(AVG(note_finale), 1) AS moyenne FROM inscriptions;

-- Arrondir les prix au centime supérieur
SELECT nom_produit, CEIL(prix) AS prix_arrondi FROM produits;
```

### 8.3 Fonctions sur les dates

| Fonction | Description | Exemple | Résultat |
|----------|-------------|---------|----------|
| `NOW()` | Date et heure actuelles | `NOW()` | `2024-06-15 10:30:00` |
| `CURDATE()` | Date actuelle | `CURDATE()` | `2024-06-15` |
| `YEAR(date)` | Extraire l'année | `YEAR('2024-06-15')` | `2024` |
| `MONTH(date)` | Extraire le mois | `MONTH('2024-06-15')` | `6` |
| `DAY(date)` | Extraire le jour | `DAY('2024-06-15')` | `15` |
| `DATEDIFF(a, b)` | Différence en jours | `DATEDIFF('2024-12-31', '2024-01-01')` | `365` |

```sql
-- Étudiants inscrits au cours les 30 derniers jours
SELECT e.prenom, i.date_inscription
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
WHERE DATEDIFF(CURDATE(), i.date_inscription) <= 30;

-- Année d'inscription de chaque étudiant
SELECT prenom, YEAR(date_inscription) AS annee_inscription
FROM etudiants;
```

### 8.4 CASE — Condition dans une requête

Le `CASE` permet d'ajouter une **logique conditionnelle** directement dans une requête.

```sql
-- Attribuer une mention selon la note
SELECT
    e.prenom,
    i.note_finale,
    CASE
        WHEN i.note_finale >= 16 THEN 'Très bien'
        WHEN i.note_finale >= 14 THEN 'Bien'
        WHEN i.note_finale >= 12 THEN 'Assez bien'
        WHEN i.note_finale >= 10 THEN 'Passable'
        ELSE 'Insuffisant'
    END AS mention
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
WHERE i.note_finale IS NOT NULL;
```

**Résultat :**
```
┌────────┬──────────────┬───────────┐
│ prenom │ note_finale  │  mention  │
├────────┼──────────────┼───────────┤
│ Alice  │    16.5      │ Très bien │
│ Bob    │    13.0      │ Assez bien│
│ Awa    │    12.5      │ Assez bien│
└────────┴──────────────┴───────────┘
```

### 8.5 COALESCE — Gérer les valeurs NULL

`COALESCE` retourne la **première valeur non NULL** de la liste.

```sql
-- Remplacer les notes NULL par "Non noté"
SELECT
    e.prenom,
    COALESCE(CAST(i.note_finale AS CHAR), 'Non noté') AS note
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant;

-- Résultat :
-- Alice  | 16.5
-- Claire | Non noté
-- David  | Non noté
```

---

## 9. Ordre d'exécution d'un SELECT

Un point souvent mal compris : SQL n'exécute **pas** les clauses dans l'ordre où on les écrit !

### 📋 Ordre d'écriture vs Ordre d'exécution

```
Ordre d'ÉCRITURE          Ordre d'EXÉCUTION
─────────────────         ──────────────────
1. SELECT         ←──┐   1. FROM
2. FROM           ──►│   2. JOIN ... ON
3. JOIN           ──►│   3. WHERE
4. WHERE          ──►│   4. GROUP BY
5. GROUP BY       ──►│   5. HAVING
6. HAVING         ──►│   6. SELECT
7. ORDER BY       ──►│   7. ORDER BY
8. LIMIT          ──►┘   8. LIMIT
```

> 💡 C'est pourquoi vous **ne pouvez pas** utiliser un alias défini dans `SELECT` dans une clause `WHERE` (WHERE est exécuté avant SELECT).

```sql
-- ❌ Interdit : 'age_double' n'existe pas encore au moment du WHERE
SELECT prenom, age * 2 AS age_double
FROM etudiants
WHERE age_double > 40;
-- Erreur : Unknown column 'age_double'

-- ✅ Correct : recalculer l'expression dans WHERE
SELECT prenom, age * 2 AS age_double
FROM etudiants
WHERE age * 2 > 40;

-- ✅ Ou utiliser une sous-requête
SELECT * FROM (
    SELECT prenom, age * 2 AS age_double FROM etudiants
) AS tmp
WHERE age_double > 40;
```

---

## 10. Exemple complet — Schéma École Bootcamp

Voici une série de requêtes progressives sur le schéma `ecole_bootcamp`.

### Niveau 1 — Requêtes simples

```sql
-- Tous les cours avec leur formateur
SELECT c.titre, f.prenom AS formateur
FROM cours c
INNER JOIN formateurs f ON c.id_formateur = f.id_formateur
ORDER BY c.titre;

-- Étudiants actifs triés par âge
SELECT prenom, nom, age
FROM etudiants
WHERE statut = 'actif'
ORDER BY age ASC;
```

### Niveau 2 — Agrégations

```sql
-- Nombre d'étudiants par cours
SELECT c.titre, COUNT(i.id_etudiant) AS nb_inscrits
FROM cours c
LEFT JOIN inscriptions i ON c.id_cours = i.id_cours
GROUP BY c.id_cours, c.titre
ORDER BY nb_inscrits DESC;

-- Moyenne des notes par étudiant
SELECT
    e.prenom,
    e.nom,
    COUNT(i.id_cours)               AS nb_cours,
    ROUND(AVG(i.note_finale), 2)    AS moyenne_perso
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
GROUP BY e.id_etudiant, e.prenom, e.nom
ORDER BY moyenne_perso DESC;
```

### Niveau 3 — HAVING et sous-requêtes

```sql
-- Cours suivis par au moins 2 étudiants
SELECT c.titre, COUNT(*) AS nb_inscrits
FROM cours c
INNER JOIN inscriptions i ON c.id_cours = i.id_cours
GROUP BY c.id_cours, c.titre
HAVING COUNT(*) >= 2;

-- Étudiants avec une note supérieure à la moyenne générale
SELECT e.prenom, e.nom, i.note_finale
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
WHERE i.note_finale > (SELECT AVG(note_finale) FROM inscriptions)
ORDER BY i.note_finale DESC;
```

### Niveau 4 — Requête complexe complète

```sql
-- Tableau de bord par formateur :
-- nombre de cours, total heures, nombre d'étudiants, note moyenne
SELECT
    CONCAT(f.prenom, ' ', f.nom)        AS formateur,
    f.specialite,
    COUNT(DISTINCT c.id_cours)          AS nb_cours,
    SUM(c.duree_heures)                 AS total_heures,
    COUNT(DISTINCT i.id_etudiant)       AS nb_etudiants,
    ROUND(AVG(i.note_finale), 2)        AS note_moyenne,
    CASE
        WHEN AVG(i.note_finale) >= 14 THEN '⭐ Excellent'
        WHEN AVG(i.note_finale) >= 12 THEN '✅ Bien'
        ELSE '⚠️ À améliorer'
    END AS evaluation
FROM formateurs f
LEFT JOIN cours c        ON f.id_formateur = c.id_formateur
LEFT JOIN inscriptions i ON c.id_cours     = i.id_cours
GROUP BY f.id_formateur, f.prenom, f.nom, f.specialite
ORDER BY total_heures DESC;
```

---

## 11. Conclusion

### 📌 Récapitulatif du DQL

```
DQL — Data Query Language
│
├── SELECT + FROM         → Sélectionner les données
├── WHERE                 → Filtrer les lignes
├── GROUP BY              → Regrouper les données
├── HAVING                → Filtrer les groupes
├── JOIN (INNER/LEFT...)  → Combiner plusieurs tables
├── Sous-requêtes         → Imbriquer des requêtes
├── Fonctions             → Transformer les données
└── ORDER BY + LIMIT      → Trier et paginer
```

### 🔑 Points clés à retenir

1. **GROUP BY** regroupe les lignes ; il doit contenir toutes les colonnes non agrégées du SELECT.
2. **WHERE** filtre avant le GROUP BY ; **HAVING** filtre après.
3. **INNER JOIN** = seulement les correspondances ; **LEFT JOIN** = tout de la table gauche.
4. Une **sous-requête** est un SELECT imbriqué, utilisable dans WHERE, FROM ou SELECT.
5. SQL exécute les clauses dans un **ordre différent de l'ordre d'écriture** (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT).

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, vous découvrirez le **DCL (Data Control Language)** pour gérer les **droits et permissions** des utilisateurs, ainsi que le **TCL (Transaction Control Language)** pour sécuriser vos opérations avec `COMMIT` et `ROLLBACK`.

---

## 12. ✅ Point de contrôle — DQL

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre `WHERE` et `HAVING` ?

<details>
<summary>👀 Voir la réponse</summary>

> `WHERE` filtre les **lignes individuelles** avant le regroupement. `HAVING` filtre les **groupes** après un `GROUP BY`. On ne peut pas utiliser une fonction d'agrégation dans un `WHERE`, mais on peut dans un `HAVING`.
</details>

---

**Q2.** Quelle est la différence entre `INNER JOIN` et `LEFT JOIN` ?

<details>
<summary>👀 Voir la réponse</summary>

> `INNER JOIN` retourne uniquement les lignes qui ont une **correspondance dans les deux tables**. `LEFT JOIN` retourne **toutes les lignes de la table gauche**, même celles sans correspondance à droite (les colonnes de droite seront NULL).
</details>

---

**Q3.** Dans quel ordre SQL exécute-t-il les clauses d'un SELECT ?

<details>
<summary>👀 Voir la réponse</summary>

> `FROM` → `JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`
> C'est pourquoi on ne peut pas utiliser un alias défini dans SELECT dans une clause WHERE.
</details>

---

**Q4.** À quoi sert `COALESCE` ?

<details>
<summary>👀 Voir la réponse</summary>

> `COALESCE(a, b, c, ...)` retourne la **première valeur non NULL** de la liste. C'est utile pour afficher une valeur par défaut quand une colonne contient NULL.
</details>

---

### 💻 Exercices pratiques

Utilisez le schéma `ecole_bootcamp` (formateurs, cours, etudiants, inscriptions).

---

**Exercice 1 — Agrégations simples**

a) Comptez le nombre total d'étudiants inscrits dans la table `etudiants`.

b) Calculez la durée totale et la durée moyenne des cours.

c) Affichez la meilleure et la moins bonne note finale dans `inscriptions`.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a)
SELECT COUNT(*) AS nb_etudiants FROM etudiants;

-- b)
SELECT
    SUM(duree_heures) AS total_heures,
    ROUND(AVG(duree_heures), 1) AS duree_moyenne
FROM cours;

-- c)
SELECT
    MAX(note_finale) AS meilleure_note,
    MIN(note_finale) AS note_minimale
FROM inscriptions;
```
</details>

---

**Exercice 2 — GROUP BY**

a) Affichez le nombre d'étudiants par statut.

b) Pour chaque formateur, affichez le nombre de cours qu'il enseigne et le total d'heures.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a)
SELECT statut, COUNT(*) AS nombre
FROM etudiants
GROUP BY statut;

-- b)
SELECT
    id_formateur,
    COUNT(*) AS nb_cours,
    SUM(duree_heures) AS total_heures
FROM cours
GROUP BY id_formateur;
```
</details>

---

**Exercice 3 — JOIN**

a) Affichez le prénom et nom de chaque étudiant avec le titre des cours auxquels il est inscrit.

b) Affichez tous les étudiants, qu'ils aient des inscriptions ou non. Pour ceux sans inscription, affichez `'Aucun cours'`.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a)
SELECT e.prenom, e.nom, c.titre
FROM etudiants e
INNER JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
INNER JOIN cours c        ON i.id_cours    = c.id_cours
ORDER BY e.nom;

-- b)
SELECT
    e.prenom,
    e.nom,
    COALESCE(c.titre, 'Aucun cours') AS cours
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
LEFT JOIN cours c        ON i.id_cours    = c.id_cours;
```
</details>

---

**Exercice 4 — HAVING**

a) Affichez les cours ayant au moins 2 étudiants inscrits.

b) Affichez les étudiants inscrits à plus d'un cours.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a)
SELECT id_cours, COUNT(*) AS nb_inscrits
FROM inscriptions
GROUP BY id_cours
HAVING COUNT(*) >= 2;

-- b)
SELECT id_etudiant, COUNT(*) AS nb_cours
FROM inscriptions
GROUP BY id_etudiant
HAVING COUNT(*) > 1;
```
</details>

---

**Exercice 5 — Requête complète**

Affichez pour chaque cours : le **titre**, le **nom du formateur**, le **nombre d'inscrits** et la **note moyenne**. N'affichez que les cours avec au moins 1 inscrit, triés par nombre d'inscrits décroissant.

<details>
<summary>👀 Voir la solution</summary>

```sql
SELECT
    c.titre,
    CONCAT(f.prenom, ' ', f.nom)    AS formateur,
    COUNT(i.id_inscription)         AS nb_inscrits,
    ROUND(AVG(i.note_finale), 2)    AS note_moyenne
FROM cours c
INNER JOIN formateurs f ON c.id_formateur  = f.id_formateur
INNER JOIN inscriptions i ON c.id_cours    = i.id_cours
GROUP BY c.id_cours, c.titre, f.prenom, f.nom
HAVING COUNT(i.id_inscription) >= 1
ORDER BY nb_inscrits DESC;
```
</details>

---

**Exercice 6 — Sous-requête**

Affichez les étudiants dont l'âge est supérieur à l'âge moyen de tous les étudiants.

<details>
<summary>👀 Voir la solution</summary>

```sql
SELECT prenom, nom, age
FROM etudiants
WHERE age > (SELECT AVG(age) FROM etudiants)
ORDER BY age DESC;
```
</details>

---

### 🏆 Challenge bonus

Écrivez une requête unique qui affiche un **rapport complet** par étudiant :
- Prénom et nom
- Nombre de cours suivis
- Moyenne de ses notes (ou `'Non évalué'` si aucune note)
- Sa mention globale (Très bien / Bien / Assez bien / Passable / Non évalué)
- Classé du meilleur au moins bon

<details>
<summary>👀 Voir la solution</summary>

```sql
SELECT
    CONCAT(e.prenom, ' ', e.nom)    AS etudiant,
    COUNT(i.id_cours)               AS nb_cours,
    COALESCE(
        CAST(ROUND(AVG(i.note_finale), 2) AS CHAR),
        'Non évalué'
    )                               AS moyenne,
    CASE
        WHEN AVG(i.note_finale) >= 16 THEN 'Très bien'
        WHEN AVG(i.note_finale) >= 14 THEN 'Bien'
        WHEN AVG(i.note_finale) >= 12 THEN 'Assez bien'
        WHEN AVG(i.note_finale) >= 10 THEN 'Passable'
        ELSE 'Non évalué'
    END AS mention
FROM etudiants e
LEFT JOIN inscriptions i ON e.id_etudiant = i.id_etudiant
GROUP BY e.id_etudiant, e.prenom, e.nom
ORDER BY AVG(i.note_finale) DESC;
```
</details>

---

*📘 Fin du Chapitre 3 — Data Query Language | Bootcamp Data Science*