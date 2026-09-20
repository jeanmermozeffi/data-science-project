# ✅ Corrigé — Chapitre 3 : DQL

> `SET search_path TO banque;` — toutes les requêtes ont été **testées** sur le
> jeu de données du projet.

---

## 🟢 Niveau 1

**1.**
```sql
SELECT nom, prenom, ville
FROM clients
ORDER BY nom
LIMIT 10;
```

**2.**
```sql
SELECT numero_compte, solde
FROM comptes
WHERE solde > 3000000
ORDER BY solde DESC;
```

**3.**
```sql
SELECT nom, prenom, ville
FROM clients
WHERE sexe = 'F' AND ville = 'Abidjan';
```

**4.**
```sql
SELECT prenom || ' ' || upper(nom) AS nom_complet
FROM employes;
```
💡 `||` concatène ; `upper()` met en majuscules.

---

## 🟡 Niveau 2

**5.** `SELECT count(*) FROM clients;`  → **250**

**6.**
```sql
SELECT sum(solde) AS total, round(avg(solde)) AS moyenne,
       min(solde) AS minimum, max(solde) AS maximum
FROM comptes;
```

**7.**
```sql
SELECT ville, count(*) AS nb_clients
FROM clients
GROUP BY ville
ORDER BY nb_clients DESC;
```

**8.**
```sql
SELECT type_operation, count(*) AS nb, sum(montant) AS total
FROM transactions
GROUP BY type_operation
ORDER BY total DESC;
```

**9.**
```sql
SELECT poste, round(avg(salaire)) AS salaire_moyen
FROM employes
GROUP BY poste
ORDER BY salaire_moyen DESC;
```

---

## 🟠 Niveau 3

**10.**
```sql
SELECT ville, count(*) AS nb_clients
FROM clients
GROUP BY ville
HAVING count(*) > 15
ORDER BY nb_clients DESC;
```
💡 `WHERE` filtre **les lignes** (avant regroupement) ; `HAVING` filtre
**les groupes** (après agrégation).

**11.**
```sql
SELECT cp.numero_compte, cp.solde, cl.nom, cl.prenom
FROM comptes cp
INNER JOIN clients cl ON cl.id_client = cp.id_client;
```

**12.**
```sql
SELECT a.nom AS agence, count(c.id_client) AS nb_clients
FROM agences a
LEFT JOIN clients c ON c.id_agence = a.id_agence
GROUP BY a.nom
ORDER BY nb_clients DESC;
```
💡 Avec `LEFT JOIN`, une agence sans client apparaît quand même, avec
`count = 0` (car `count(c.id_client)` ne compte pas les `NULL`).

**13.**
```sql
SELECT e.prenom || ' ' || e.nom AS employe,
       m.prenom || ' ' || m.nom AS manager
FROM employes e
LEFT JOIN employes m ON m.id_employe = e.id_manager
ORDER BY manager NULLS FIRST;
```
💡 **Auto-jointure** : la même table jouée deux fois avec deux alias (`e` et
`m`). `LEFT JOIN` garde les directeurs (sans manager).

**14.**
```sql
SELECT cl.nom, cl.prenom, sum(cp.solde) AS solde_cumule
FROM clients cl
JOIN comptes cp ON cp.id_client = cl.id_client
GROUP BY cl.id_client, cl.nom, cl.prenom
ORDER BY solde_cumule DESC
LIMIT 10;
```

---

## 🔴 Niveau 4

**15.**
```sql
SELECT numero_compte, solde
FROM comptes
WHERE solde > (SELECT avg(solde) FROM comptes)
ORDER BY solde DESC;
```
💡 La sous-requête renvoie **une seule valeur** (la moyenne), comparée à chaque
ligne.

**16.**
```sql
SELECT cl.nom, cl.prenom
FROM clients cl
WHERE EXISTS (SELECT 1 FROM prets p WHERE p.id_client = cl.id_client);
```
💡 `EXISTS` s'arrête dès qu'une ligne correspond → très efficace. On écrit
`SELECT 1` car la valeur projetée n'a aucune importance.

**17.**
```sql
-- Variante NOT EXISTS
SELECT cl.nom, cl.prenom
FROM clients cl
WHERE NOT EXISTS (
    SELECT 1 FROM comptes cp
    JOIN cartes ca ON ca.id_compte = cp.id_compte
    WHERE cp.id_client = cl.id_client
);
```

**18.**
```sql
SELECT numero_compte, solde,
       CASE
           WHEN solde > 2000000           THEN 'Riche'
           WHEN solde >= 500000           THEN 'Moyen'
           ELSE                                'Modeste'
       END AS categorie
FROM comptes;
```

**19.**
```sql
SELECT nom, prenom, COALESCE(profession, 'Non renseignée') AS profession
FROM clients;
```

**20.**
```sql
SELECT to_char(date_operation, 'YYYY-MM') AS mois, count(*) AS nb
FROM transactions
WHERE date_operation >= DATE '2024-01-01'
  AND date_operation <  DATE '2025-01-01'
GROUP BY mois
ORDER BY mois;
```
💡 `to_char(date, 'YYYY-MM')` regroupe par mois. On peut aussi utiliser
`date_trunc('month', date_operation)`.

---

## 🏆 Bonus

**21.**
```sql
SELECT id_client, numero_compte, solde,
       ROW_NUMBER() OVER (PARTITION BY id_client ORDER BY solde DESC) AS rang
FROM comptes
ORDER BY id_client, rang;
```
💡 Une **fonction fenêtre** calcule une valeur par ligne *sans* regrouper :
chaque client garde ses comptes, numérotés du plus riche au moins riche.

**22.**
```sql
WITH solde_par_type AS (
    SELECT t.libelle, avg(c.solde) AS solde_moyen
    FROM comptes c
    JOIN types_compte t ON t.id_type = c.id_type
    GROUP BY t.libelle
)
SELECT *
FROM solde_par_type
WHERE solde_moyen > (SELECT avg(solde) FROM comptes);
```
💡 Une **CTE** (`WITH`) nomme un résultat intermédiaire → la requête se lit comme
des étapes successives.

---

## ❓ Réponses

- **R1.** `WHERE` filtre les lignes **avant** le `GROUP BY` ; `HAVING` filtre les
  groupes **après** agrégation. On ne peut pas mettre `count(*) > 15` dans un
  `WHERE`.
- **R2.** `INNER JOIN` ne garde que les lignes ayant une correspondance des
  **deux** côtés. `LEFT JOIN` garde **toutes** les lignes de gauche, complétées
  par des `NULL` quand il n'y a pas de correspondance à droite.
- **R3.** Ordre réel : `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY →
  LIMIT`. Comme `SELECT` est évalué **après** `WHERE`, les alias définis dans le
  `SELECT` n'existent pas encore au moment du `WHERE`.
- **R4.** `COUNT(*)` compte toutes les lignes ; `COUNT(colonne)` ignore les
  `NULL` de cette colonne ; `COUNT(DISTINCT colonne)` compte les valeurs
  **distinctes** non nulles.
