# 📝 Data Manipulation Language (DML) — Cours Bootcamp Data Science

> **Chapitre 2** | Prérequis : Chapitre 1 — Data Definition Language (DDL)

---

## Table des matières

1. [Introduction au DML](#1-introduction-au-dml)
2. [Rappel — Où se situe le DML ?](#2-rappel--où-se-situe-le-dml-)
3. [INSERT — Insérer des données](#3-insert--insérer-des-données)
4. [SELECT — Lire des données](#4-select--lire-des-données)
5. [UPDATE — Modifier des données](#5-update--modifier-des-données)
6. [DELETE — Supprimer des données](#6-delete--supprimer-des-données)
7. [Filtrer avec WHERE](#7-filtrer-avec-where)
8. [Trier et limiter les résultats](#8-trier-et-limiter-les-résultats)
9. [Exemple complet — Schéma École Bootcamp](#9-exemple-complet--schéma-école-bootcamp)
10. [Conclusion](#10-conclusion)
11. [✅ Point de contrôle — DML](#11--point-de-contrôle--dml)

---

## 1. Introduction au DML

### 🔍 Qu'est-ce que le DML ?

Le **DML (Data Manipulation Language)** est la famille de commandes SQL qui permet d'**interagir avec les données** contenues dans une base de données.

Si le DDL construit la **structure** (les étagères), le DML s'occupe du **contenu** (les livres sur les étagères).

> 💡 **Analogie** : Imaginez un tableau blanc (la table). Le DDL a créé ce tableau. Maintenant avec le DML, vous pouvez :
> - **Écrire** dessus → `INSERT`
> - **Lire** ce qui est écrit → `SELECT`
> - **Corriger** ce qui est écrit → `UPDATE`
> - **Effacer** certaines lignes → `DELETE`

### 🔑 Les 4 commandes fondamentales du DML

```
┌─────────────────────────────────────────────────┐
│               COMMANDES DML                     │
├───────────┬─────────────────────────────────────┤
│  INSERT   │  Ajouter de nouvelles lignes        │
│  SELECT   │  Lire / Interroger les données      │
│  UPDATE   │  Modifier des données existantes    │
│  DELETE   │  Supprimer des lignes               │
└───────────┴─────────────────────────────────────┘
```

Ces 4 opérations correspondent au concept universel **CRUD** utilisé en développement :

| CRUD | SQL | Action |
|------|-----|--------|
| **C**reate | `INSERT` | Créer / Ajouter |
| **R**ead | `SELECT` | Lire / Consulter |
| **U**pdate | `UPDATE` | Modifier |
| **D**elete | `DELETE` | Supprimer |

---

## 2. Rappel — Où se situe le DML ?

| Catégorie | Commandes | Rôle |
|-----------|-----------|------|
| **DDL** | `CREATE`, `ALTER`, `DROP` | Définir la **structure** |
| ➡️ **DML** | `INSERT`, `SELECT`, `UPDATE`, `DELETE` | Manipuler les **données** |
| **DCL** | `GRANT`, `REVOKE` | Gérer les **droits** |
| **TCL** | `COMMIT`, `ROLLBACK` | Gérer les **transactions** |

> ⚠️ **Différence clé avec le DDL** : Les commandes DML sont **annulables** avec un `ROLLBACK` (si elles sont dans une transaction). C'est une sécurité importante avant de valider avec `COMMIT`.

---

## 3. INSERT — Insérer des données

### 📖 Définition

La commande `INSERT INTO` permet d'**ajouter une ou plusieurs lignes** dans une table.

### Syntaxe de base

```sql
-- Insérer une seule ligne en spécifiant les colonnes
INSERT INTO nom_table (colonne1, colonne2, colonne3)
VALUES (valeur1, valeur2, valeur3);
```

### 3.1 Insérer une seule ligne

```sql
-- On utilise notre table etudiants du chapitre 1
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Alice', 'Dupont', 'alice.dupont@email.com', 22);
```

**Résultat dans la table :**
```
┌────────────┬────────┬────────┬───────────────────────┬─────┐
│ id_etudiant│ prenom │  nom   │         email         │ age │
├────────────┼────────┼────────┼───────────────────────┼─────┤
│     1      │ Alice  │ Dupont │ alice.dupont@email.com│ 22  │
└────────────┴────────┴────────┴───────────────────────┴─────┘
```

> 💡 `id_etudiant` a été généré automatiquement par `AUTO_INCREMENT` (valeur = 1).

### 3.2 Insérer plusieurs lignes en une seule commande

```sql
INSERT INTO etudiants (prenom, nom, email, age)
VALUES
    ('Bob',     'Martin',  'bob.martin@email.com',   25),
    ('Claire',  'Leclerc', 'claire.lec@email.com',   23),
    ('David',   'Moreau',  'david.moreau@email.com', 28),
    ('Emma',    'Petit',   'emma.petit@email.com',   21);
```

**Résultat :**
```
┌────────────┬────────┬─────────┬───────────────────────┬─────┐
│ id_etudiant│ prenom │   nom   │         email         │ age │
├────────────┼────────┼─────────┼───────────────────────┼─────┤
│     1      │ Alice  │ Dupont  │ alice.dupont@email.com│ 22  │
│     2      │ Bob    │ Martin  │ bob.martin@email.com  │ 25  │
│     3      │ Claire │ Leclerc │ claire.lec@email.com  │ 23  │
│     4      │ David  │ Moreau  │ david.moreau@email.com│ 28  │
│     5      │ Emma   │ Petit   │ emma.petit@email.com  │ 21  │
└────────────┴────────┴─────────┴───────────────────────┴─────┘
```

### 3.3 INSERT sans spécifier les colonnes

Si vous fournissez des valeurs **pour toutes les colonnes dans l'ordre**, vous pouvez omettre les noms de colonnes. C'est cependant **déconseillé** car fragile.

```sql
-- ✅ Avec colonnes (recommandé — lisible et sûr)
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Alice', 'Dupont', 'alice@email.com', 22);

-- ⚠️ Sans colonnes (à éviter — risque d'erreur si la structure change)
INSERT INTO etudiants
VALUES (NULL, 'Alice', 'Dupont', 'alice@email.com', 22, '2024-01-15', 'actif');
```

### 3.4 Erreurs fréquentes avec INSERT

```sql
-- ❌ Erreur : email dupliqué (contrainte UNIQUE)
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Autre', 'Personne', 'alice.dupont@email.com', 30);
-- Erreur : Duplicate entry for key 'email'

-- ❌ Erreur : champ NOT NULL non fourni
INSERT INTO etudiants (nom, email, age)
VALUES ('Dupont', 'test@email.com', 25);
-- Erreur : Field 'prenom' doesn't have a default value

-- ❌ Erreur : contrainte CHECK violée
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Tom', 'Dupont', 'tom@email.com', 15);
-- Erreur : Check constraint 'age' is violated (age doit être >= 18)
```

---

## 4. SELECT — Lire des données

### 📖 Définition

La commande `SELECT` est la **plus utilisée en SQL**. Elle permet de **lire et afficher** les données d'une ou plusieurs tables.

> 💡 Certains considèrent `SELECT` comme faisant partie du **DQL** (Data Query Language), mais il est souvent présenté avec le DML car il est indissociable de la manipulation de données.

### Syntaxe de base

```sql
SELECT colonne1, colonne2, ...
FROM nom_table;
```

### 4.1 Sélectionner toutes les colonnes

```sql
-- Le * signifie "toutes les colonnes"
SELECT * FROM etudiants;
```

**Résultat :** Affiche l'intégralité de la table.

### 4.2 Sélectionner des colonnes spécifiques

```sql
-- Afficher seulement le prénom et le nom
SELECT prenom, nom FROM etudiants;
```

**Résultat :**
```
┌────────┬─────────┐
│ prenom │   nom   │
├────────┼─────────┤
│ Alice  │ Dupont  │
│ Bob    │ Martin  │
│ Claire │ Leclerc │
│ David  │ Moreau  │
│ Emma   │ Petit   │
└────────┴─────────┘
```

### 4.3 Utiliser des alias avec AS

Les alias permettent de **renommer une colonne** dans l'affichage des résultats.

```sql
SELECT
    prenom      AS "Prénom",
    nom         AS "Nom de famille",
    age         AS "Âge (années)"
FROM etudiants;
```

**Résultat :**
```
┌────────┬────────────────┬──────────────┐
│ Prénom │ Nom de famille │ Âge (années) │
├────────┼────────────────┼──────────────┤
│ Alice  │ Dupont         │ 22           │
│ Bob    │ Martin         │ 25           │
└────────┴────────────────┴──────────────┘
```

### 4.4 SELECT avec calculs

```sql
-- Calculer l'année de naissance approximative
SELECT
    prenom,
    age,
    (2024 - age) AS annee_naissance_approx
FROM etudiants;
```

### 4.5 SELECT DISTINCT — Éviter les doublons

```sql
-- Afficher les villes sans répétition
SELECT DISTINCT statut FROM etudiants;
```

---

## 5. UPDATE — Modifier des données

### 📖 Définition

La commande `UPDATE` permet de **modifier les valeurs existantes** dans une ou plusieurs lignes d'une table.

### Syntaxe de base

```sql
UPDATE nom_table
SET colonne1 = nouvelle_valeur1,
    colonne2 = nouvelle_valeur2
WHERE condition;
```

> 🚨 **RÈGLE D'OR : Toujours utiliser WHERE avec UPDATE !**
> Sans clause `WHERE`, vous modifiez **TOUTES les lignes** de la table !

### 5.1 Modifier une seule ligne

```sql
-- Corriger l'email d'Alice (id = 1)
UPDATE etudiants
SET email = 'alice.new@email.com'
WHERE id_etudiant = 1;
```

**Avant :**
```
id=1 | Alice | Dupont | alice.dupont@email.com | 22
```
**Après :**
```
id=1 | Alice | Dupont | alice.new@email.com | 22
```

### 5.2 Modifier plusieurs colonnes à la fois

```sql
-- Mettre à jour plusieurs informations pour Bob (id = 2)
UPDATE etudiants
SET
    email  = 'bob.nouveau@email.com',
    age    = 26,
    statut = 'inactif'
WHERE id_etudiant = 2;
```

### 5.3 Modifier plusieurs lignes avec une condition

```sql
-- Passer tous les étudiants de plus de 25 ans en statut "senior"
UPDATE etudiants
SET statut = 'senior'
WHERE age > 25;
```

### 5.4 ⚠️ Le danger de l'UPDATE sans WHERE

```sql
-- ✅ Avec WHERE : modifie seulement Alice
UPDATE etudiants
SET statut = 'inactif'
WHERE id_etudiant = 1;

-- ❌ Sans WHERE : modifie TOUS les étudiants !
UPDATE etudiants
SET statut = 'inactif';
-- Résultat : tous les étudiants passent à 'inactif' !
```

> 💡 **Bonne pratique** : Avant d'exécuter un `UPDATE`, faites d'abord un `SELECT` avec la même condition `WHERE` pour vérifier quelles lignes seront affectées.

```sql
-- 1. D'abord, vérifier avec SELECT
SELECT * FROM etudiants WHERE age > 25;

-- 2. Si le résultat est correct, alors faire l'UPDATE
UPDATE etudiants SET statut = 'senior' WHERE age > 25;
```

---

## 6. DELETE — Supprimer des données

### 📖 Définition

La commande `DELETE` permet de **supprimer une ou plusieurs lignes** d'une table. La structure de la table est **conservée**.

### Syntaxe de base

```sql
DELETE FROM nom_table
WHERE condition;
```

> 🚨 **RÈGLE D'OR : Toujours utiliser WHERE avec DELETE !**
> Sans clause `WHERE`, vous supprimez **TOUTES les lignes** de la table !

### 6.1 Supprimer une seule ligne

```sql
-- Supprimer l'étudiant avec l'id 5 (Emma)
DELETE FROM etudiants
WHERE id_etudiant = 5;
```

### 6.2 Supprimer plusieurs lignes avec une condition

```sql
-- Supprimer tous les étudiants inactifs
DELETE FROM etudiants
WHERE statut = 'inactif';
```

### 6.3 ⚠️ Le danger du DELETE sans WHERE

```sql
-- ✅ Avec WHERE : supprime seulement Emma
DELETE FROM etudiants WHERE id_etudiant = 5;

-- ❌ Sans WHERE : supprime TOUTES les lignes !
DELETE FROM etudiants;
-- La table est maintenant vide (mais la structure existe encore)
```

### 6.4 DELETE vs TRUNCATE — Rappel

| | `DELETE FROM` | `TRUNCATE TABLE` |
|-|---------------|-----------------|
| Catégorie | DML | DDL |
| Filtre WHERE | ✅ Oui | ❌ Non (tout supprime) |
| Annulable (ROLLBACK) | ✅ Oui | ❌ Non (en général) |
| Vitesse | Plus lente (ligne par ligne) | Plus rapide |
| Réinitialise AUTO_INCREMENT | ❌ Non | ✅ Oui |

```sql
-- Supprimer uniquement les étudiants inactifs (DELETE)
DELETE FROM etudiants WHERE statut = 'inactif';

-- Vider toute la table d'un coup (TRUNCATE)
TRUNCATE TABLE etudiants;
```

---

## 7. Filtrer avec WHERE

La clause `WHERE` est utilisée avec `SELECT`, `UPDATE` et `DELETE` pour **cibler des lignes précises** selon une ou plusieurs conditions.

### 7.1 Opérateurs de comparaison

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `=` | Égal à | `age = 22` |
| `!=` ou `<>` | Différent de | `statut != 'inactif'` |
| `>` | Supérieur à | `age > 20` |
| `<` | Inférieur à | `age < 30` |
| `>=` | Supérieur ou égal | `age >= 18` |
| `<=` | Inférieur ou égal | `note <= 10` |

```sql
-- Étudiants de plus de 23 ans
SELECT * FROM etudiants WHERE age > 23;

-- Étudiants actifs seulement
SELECT * FROM etudiants WHERE statut = 'actif';
```

### 7.2 Opérateurs logiques — AND, OR, NOT

```sql
-- AND : les deux conditions doivent être vraies
SELECT * FROM etudiants
WHERE age > 20 AND statut = 'actif';

-- OR : au moins une condition doit être vraie
SELECT * FROM etudiants
WHERE age < 22 OR age > 26;

-- NOT : inverse la condition
SELECT * FROM etudiants
WHERE NOT statut = 'inactif';
```

### 7.3 BETWEEN — Dans un intervalle

```sql
-- Étudiants entre 20 et 25 ans (inclus)
SELECT * FROM etudiants
WHERE age BETWEEN 20 AND 25;

-- Équivalent à :
SELECT * FROM etudiants
WHERE age >= 20 AND age <= 25;
```

### 7.4 IN — Parmi une liste de valeurs

```sql
-- Étudiants dont le statut est 'actif' ou 'senior'
SELECT * FROM etudiants
WHERE statut IN ('actif', 'senior');

-- Équivalent à :
SELECT * FROM etudiants
WHERE statut = 'actif' OR statut = 'senior';
```

### 7.5 LIKE — Recherche par motif

`LIKE` permet de rechercher des **valeurs partielles** dans une colonne texte.

| Caractère | Signification |
|-----------|---------------|
| `%` | N'importe quel nombre de caractères (0 ou plus) |
| `_` | Exactement un caractère |

```sql
-- Prénoms commençant par 'A'
SELECT * FROM etudiants WHERE prenom LIKE 'A%';
-- Résultat : Alice

-- Emails se terminant par '@gmail.com'
SELECT * FROM etudiants WHERE email LIKE '%@gmail.com';

-- Prénoms de 5 lettres commençant par 'C'
SELECT * FROM etudiants WHERE prenom LIKE 'C____';
-- Résultat : Claire

-- Noms contenant 'mar' (n'importe où)
SELECT * FROM etudiants WHERE nom LIKE '%mar%';
-- Résultat : Martin
```

### 7.6 IS NULL / IS NOT NULL

```sql
-- Étudiants sans email renseigné
SELECT * FROM etudiants WHERE email IS NULL;

-- Étudiants avec un email renseigné
SELECT * FROM etudiants WHERE email IS NOT NULL;
```

---

## 8. Trier et limiter les résultats

### 8.1 ORDER BY — Trier les résultats

```sql
-- Trier par âge croissant (ASC = par défaut)
SELECT prenom, nom, age FROM etudiants
ORDER BY age ASC;

-- Trier par âge décroissant
SELECT prenom, nom, age FROM etudiants
ORDER BY age DESC;

-- Trier d'abord par statut, puis par nom alphabétique
SELECT prenom, nom, statut FROM etudiants
ORDER BY statut ASC, nom ASC;
```

**Résultat (ORDER BY age ASC) :**
```
┌────────┬─────────┬─────┐
│ prenom │   nom   │ age │
├────────┼─────────┼─────┤
│ Emma   │ Petit   │ 21  │
│ Alice  │ Dupont  │ 22  │
│ Claire │ Leclerc │ 23  │
│ Bob    │ Martin  │ 25  │
│ David  │ Moreau  │ 28  │
└────────┴─────────┴─────┘
```

### 8.2 LIMIT — Limiter le nombre de résultats

```sql
-- Afficher seulement les 3 premiers résultats
SELECT prenom, nom, age FROM etudiants
ORDER BY age ASC
LIMIT 3;
```

**Résultat :**
```
┌────────┬─────────┬─────┐
│ prenom │   nom   │ age │
├────────┼─────────┼─────┤
│ Emma   │ Petit   │ 21  │
│ Alice  │ Dupont  │ 22  │
│ Claire │ Leclerc │ 23  │
└────────┴─────────┴─────┘
```

```sql
-- LIMIT avec OFFSET : ignorer les 2 premiers, afficher les 3 suivants
SELECT prenom, nom, age FROM etudiants
ORDER BY age ASC
LIMIT 3 OFFSET 2;
```

> 💡 `LIMIT` + `OFFSET` est très utile pour la **pagination** (afficher par pages dans une application).

### 8.3 Combiner WHERE + ORDER BY + LIMIT

```sql
-- Les 2 étudiants actifs les plus jeunes
SELECT prenom, nom, age FROM etudiants
WHERE statut = 'actif'
ORDER BY age ASC
LIMIT 2;
```

> 📌 **Ordre des clauses dans un SELECT :**
> ```sql
> SELECT   [colonnes]
> FROM     [table]
> WHERE    [condition]
> ORDER BY [colonne] [ASC|DESC]
> LIMIT    [nombre]
> OFFSET   [décalage];
> ```

---

## 9. Exemple complet — Schéma École Bootcamp

Reprenons le schéma `ecole_bootcamp` du chapitre 1 et appliquons les commandes DML.

### Étape 1 — Insérer les données

```sql
-- Insérer des formateurs
INSERT INTO formateurs (prenom, nom, email, specialite) VALUES
    ('Jean',   'Konan',   'jean.konan@bootcamp.ci',   'Data Science'),
    ('Marie',  'Bamba',   'marie.bamba@bootcamp.ci',  'SQL & Bases de données'),
    ('Pierre', 'Coulibaly','pierre.c@bootcamp.ci',    'Machine Learning');

-- Insérer des cours
INSERT INTO cours (titre, duree_heures, id_formateur) VALUES
    ('Introduction à SQL',        20, 2),
    ('Python pour la Data',       30, 1),
    ('Machine Learning Basics',   25, 3),
    ('Visualisation de données',  15, 1);

-- Insérer des étudiants
INSERT INTO etudiants (prenom, nom, email, age) VALUES
    ('Fatou',   'Diallo',  'fatou.diallo@email.com',  23),
    ('Kofi',    'Asante',  'kofi.asante@email.com',   26),
    ('Awa',     'Traoré',  'awa.traore@email.com',    22),
    ('Moussa',  'Keita',   'moussa.keita@email.com',  29),
    ('Aminata', 'Sow',     'aminata.sow@email.com',   24);

-- Inscrire des étudiants à des cours
INSERT INTO inscriptions (id_etudiant, id_cours) VALUES
    (1, 1),  -- Fatou → SQL
    (1, 2),  -- Fatou → Python
    (2, 1),  -- Kofi → SQL
    (3, 3),  -- Awa → ML
    (4, 2),  -- Moussa → Python
    (5, 4);  -- Aminata → Visualisation
```

### Étape 2 — Lire et explorer les données

```sql
-- Voir tous les étudiants
SELECT * FROM etudiants;

-- Voir les étudiants actifs de moins de 25 ans, triés par prénom
SELECT prenom, nom, age FROM etudiants
WHERE statut = 'actif' AND age < 25
ORDER BY prenom ASC;

-- Voir les cours avec leur durée, du plus long au plus court
SELECT titre, duree_heures FROM cours
ORDER BY duree_heures DESC;

-- Voir les 3 étudiants les plus jeunes
SELECT prenom, nom, age FROM etudiants
ORDER BY age ASC
LIMIT 3;
```

### Étape 3 — Modifier des données

```sql
-- Kofi a changé d'email
UPDATE etudiants
SET email = 'kofi.asante.new@email.com'
WHERE id_etudiant = 2;

-- Le cours SQL passe à 25 heures
UPDATE cours
SET duree_heures = 25
WHERE titre = 'Introduction à SQL';

-- Ajouter une note à Fatou pour le cours SQL
UPDATE inscriptions
SET note_finale = 16.5
WHERE id_etudiant = 1 AND id_cours = 1;
```

### Étape 4 — Supprimer des données

```sql
-- Supprimer un étudiant qui s'est désinscrit
DELETE FROM inscriptions WHERE id_etudiant = 5;
DELETE FROM etudiants WHERE id_etudiant = 5;

-- Supprimer les cours sans formateur assigné
DELETE FROM cours WHERE id_formateur IS NULL;
```

---

## 10. Conclusion

### 📌 Récapitulatif des commandes DML

```
DML — Data Manipulation Language
│
├── INSERT INTO  → Ajouter des lignes dans une table
├── SELECT       → Lire et afficher des données
├── UPDATE       → Modifier des données existantes
└── DELETE FROM  → Supprimer des lignes
```

### 🔑 Points clés à retenir

1. **CRUD = INSERT / SELECT / UPDATE / DELETE** : les 4 opérations de base sur les données.
2. **Toujours utiliser WHERE** avec `UPDATE` et `DELETE` pour éviter les modifications massives non souhaitées.
3. **Tester avec SELECT d'abord** avant d'exécuter un `UPDATE` ou `DELETE`.
4. **WHERE** permet de filtrer les lignes avec des opérateurs : `=`, `!=`, `>`, `<`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`.
5. **ORDER BY** trie les résultats, **LIMIT** les restreint en nombre.
6. Les commandes DML sont **annulables** avec `ROLLBACK` (contrairement au DDL).

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, vous découvrirez le **DQL avancé** : les **jointures** (`JOIN`) pour combiner plusieurs tables, les **fonctions d'agrégation** (`COUNT`, `SUM`, `AVG`…) et le **regroupement** (`GROUP BY`).

---

## 11. ✅ Point de contrôle — DML

### 📝 Questions théoriques

**Q1.** Que signifie l'acronyme CRUD et à quelles commandes SQL correspond-il ?

<details>
<summary>👀 Voir la réponse</summary>

> **CRUD** = **C**reate (`INSERT`), **R**ead (`SELECT`), **U**pdate (`UPDATE`), **D**elete (`DELETE`).
</details>

---

**Q2.** Pourquoi est-il dangereux d'exécuter `UPDATE etudiants SET statut = 'inactif';` sans clause `WHERE` ?

<details>
<summary>👀 Voir la réponse</summary>

> Sans `WHERE`, la commande modifie **toutes les lignes** de la table. Tous les étudiants passeraient en statut `'inactif'`, ce qui est rarement l'intention souhaitée.
</details>

---

**Q3.** Quelle est la différence entre `DELETE FROM etudiants` et `TRUNCATE TABLE etudiants` ?

<details>
<summary>👀 Voir la réponse</summary>

> Les deux suppriment toutes les données, mais `DELETE` est une commande **DML** (annulable avec ROLLBACK, plus lente, ne réinitialise pas l'AUTO_INCREMENT), tandis que `TRUNCATE` est **DDL** (non annulable, plus rapide, réinitialise l'AUTO_INCREMENT).
</details>

---

**Q4.** À quoi servent les caractères `%` et `_` dans une clause `LIKE` ?

<details>
<summary>👀 Voir la réponse</summary>

> `%` représente **n'importe quel nombre de caractères** (zéro ou plus). `_` représente **exactement un caractère**. Exemple : `LIKE 'A%'` trouve tout ce qui commence par A ; `LIKE 'A_i'` trouve "Ani", "Ali", etc.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — INSERT**

Utilisez la table `produits` créée au chapitre 1 (exercice 1) et insérez les 4 produits suivants :

| nom_produit | prix | stock | categorie |
|-------------|------|-------|-----------|
| Ordinateur portable | 850.00 | 10 | Informatique |
| Souris sans fil | 25.50 | 50 | Informatique |
| Cahier A4 | 3.99 | 200 | Papeterie |
| Stylo bille | 1.20 | 500 | Papeterie |

<details>
<summary>👀 Voir la solution</summary>

```sql
INSERT INTO produits (nom_produit, prix, stock, categorie) VALUES
    ('Ordinateur portable', 850.00, 10,  'Informatique'),
    ('Souris sans fil',      25.50, 50,  'Informatique'),
    ('Cahier A4',             3.99, 200, 'Papeterie'),
    ('Stylo bille',           1.20, 500, 'Papeterie');
```
</details>

---

**Exercice 2 — SELECT et WHERE**

À partir de la table `produits`, écrivez les requêtes pour :

a) Afficher tous les produits de la catégorie `'Informatique'`

b) Afficher les produits dont le prix est inférieur à `10.00`, triés par prix croissant

c) Afficher le nom et le prix des 2 produits les plus chers

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a) Produits informatique
SELECT * FROM produits WHERE categorie = 'Informatique';

-- b) Produits moins de 10€, triés par prix
SELECT * FROM produits
WHERE prix < 10.00
ORDER BY prix ASC;

-- c) Les 2 produits les plus chers
SELECT nom_produit, prix FROM produits
ORDER BY prix DESC
LIMIT 2;
```
</details>

---

**Exercice 3 — UPDATE**

a) Le prix de la `'Souris sans fil'` passe à `29.99`. Mettez-le à jour.

b) Tous les produits de la catégorie `'Papeterie'` ont leur stock augmenté de 100 unités.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- a) Mise à jour du prix de la souris
UPDATE produits
SET prix = 29.99
WHERE nom_produit = 'Souris sans fil';

-- b) Augmenter le stock de la papeterie
UPDATE produits
SET stock = stock + 100
WHERE categorie = 'Papeterie';
```
</details>

---

**Exercice 4 — DELETE**

Supprimez tous les produits dont le stock est égal à 0.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- Vérifier d'abord avec SELECT
SELECT * FROM produits WHERE stock = 0;

-- Puis supprimer
DELETE FROM produits WHERE stock = 0;
```
</details>

---

**Exercice 5 — Requête combinée**

Écrivez une seule requête `SELECT` qui affiche le `nom_produit`, le `prix` et le `stock` de tous les produits dont :
- La catégorie est `'Informatique'` **OU** le prix est supérieur à `20`
- Le stock est supérieur à `0`
- Triés par prix décroissant

<details>
<summary>👀 Voir la solution</summary>

```sql
SELECT nom_produit, prix, stock
FROM produits
WHERE (categorie = 'Informatique' OR prix > 20)
  AND stock > 0
ORDER BY prix DESC;
```
</details>

---

### 🏆 Challenge bonus

Créez une base de données `boutique` avec les tables `clients`, `produits` et `commandes`.
Puis :
1. Insérez au moins 5 clients, 5 produits et 8 commandes
2. Affichez les commandes passées par un client spécifique
3. Mettez à jour le stock des produits après chaque commande
4. Supprimez les commandes de plus de 30 jours

---

*📘 Fin du Chapitre 2 — Data Manipulation Language | Bootcamp Data Science*