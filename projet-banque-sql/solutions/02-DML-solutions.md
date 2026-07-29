# ✅ Corrigé — Chapitre 2 : DML

> `SET search_path TO banque;`

---

## 🟢 Niveau 1

**1.**
```sql
INSERT INTO agences (code_agence, nom, ville, region)
VALUES ('AG013', 'Agence Bingerville', 'Bingerville', 'Lagunes');
```
💡 On omet `id_agence` (auto) et `date_ouverture` (DEFAULT = aujourd'hui).

**2.**
```sql
INSERT INTO types_compte (libelle, taux_interet, frais_mensuels) VALUES
('Compte devise',    0.50,  2000.00),
('Compte retraite',  6.00,     0.00),
('Compte mineur',    1.00,     0.00);
```
💡 Insérer N lignes en **une** commande = un seul aller-retour réseau + une
seule validation → bien plus rapide que N `INSERT` séparés.

**3.**
```sql
INSERT INTO clients (nom, prenom, date_naissance, sexe, telephone, ville, id_agence)
VALUES ('Test', 'Mineur', '2015-01-01', 'M', '+225 0700000000', 'Abidjan', 1);
-- ERROR: new row violates check constraint "chk_majeur"
```
La contrainte `chk_majeur` (`date_naissance <= today - 18 ans`) **rejette**
l'insertion. C'est le DDL qui protège l'intégrité du DML.

---

## 🟡 Niveau 2

**4.** `SELECT * FROM clients WHERE ville IN ('Abidjan', 'Bouaké');`

**5.** `SELECT * FROM comptes WHERE solde BETWEEN 1000000 AND 2000000;`
💡 `BETWEEN` est **inclusif** des deux bornes.

**6.** `SELECT * FROM clients WHERE nom LIKE 'Kou%';`
💡 `%` = n'importe quelle suite de caractères, `_` = un seul caractère.
Pour ignorer la casse, utilisez `ILIKE` (spécifique PostgreSQL).

**7.**
```sql
SELECT * FROM transactions
WHERE type_operation IN ('virement', 'paiement') AND montant > 500000;
```

---

## 🟠 Niveau 3

**8.**
```sql
BEGIN;
  UPDATE comptes SET statut = 'bloque' WHERE id_compte = 5;
  SELECT id_compte, statut FROM comptes WHERE id_compte = 5;  -- bloque
ROLLBACK;  -- on annule : le compte redevient 'actif'
```

**9.**
```sql
UPDATE cartes SET plafond = plafond * 1.02 WHERE type_carte = 'Visa';
```

**10.**
```sql
UPDATE comptes c
SET solde = solde * (1 + t.taux_interet / 100)
FROM types_compte t
WHERE c.id_type = t.id_type
  AND t.libelle LIKE 'Compte épargne%';
```
💡 PostgreSQL autorise un `FROM` dans `UPDATE` pour aller chercher une valeur
dans une autre table — pratique et performant.

**11.** Sans `WHERE`, **tous** les comptes (350) passeraient à `'bloque'` : la
clause `WHERE` est ce qui cible les lignes. C'est l'erreur classique à éviter.
→ Réflexe : écrire d'abord un `SELECT` avec le même `WHERE`, vérifier le nombre
de lignes, puis transformer en `UPDATE`.

---

## 🔴 Niveau 4

**12.**
```sql
BEGIN;
  -- D'abord COMPTER avant de supprimer (bon réflexe) :
  SELECT count(*) FROM transactions
  WHERE canal = 'gab' AND date_operation < DATE '2024-01-01';

  DELETE FROM transactions
  WHERE canal = 'gab' AND date_operation < DATE '2024-01-01';
ROLLBACK;
```

**13.**
```sql
CREATE TABLE transactions_archive (LIKE transactions INCLUDING ALL);

INSERT INTO transactions_archive
SELECT * FROM transactions
WHERE date_operation >= DATE '2023-01-01'
  AND date_operation <  DATE '2024-01-01';
```
💡 `CREATE TABLE ... (LIKE ... INCLUDING ALL)` recopie structure, contraintes et
index sans les données. `INSERT ... SELECT` est la façon idiomatique de copier
des lignes d'une table à l'autre.

**14.**
| | `DELETE FROM t;` | `TRUNCATE t;` |
|---|---|---|
| Clause `WHERE` | ✅ possible | ❌ impossible (tout ou rien) |
| Vitesse sur grosse table | lent (ligne à ligne) | quasi instantané |
| Réversible (`ROLLBACK`) | ✅ oui (DML) | ✅ sous PostgreSQL, ❌ ailleurs |
| Remet l'auto-incrément | non | oui avec `RESTART IDENTITY` |

---

## ❓ Réponses

- **R1.** `WHERE` est le **filtre** qui désigne les lignes visées. Sans lui,
  l'opération s'applique à **toute** la table — perte de données massive et
  souvent irréversible en production.
- **R2.** Colonne avec `DEFAULT` omise → la valeur par défaut est utilisée.
  Colonne `NOT NULL` sans défaut omise → **erreur** (`null value ... violates
  not-null constraint`).
- **R3.** Oui : `INSERT ... VALUES (...), (...), (...);`. Avantage : un seul
  parsing, une seule transaction, un seul aller-retour → gain de performance
  important sur de gros volumes.
