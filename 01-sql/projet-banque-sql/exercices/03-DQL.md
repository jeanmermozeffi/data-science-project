# 🔍 Chapitre 3 — DQL (Data Query Language)

> **Objectif** : interroger les données — du `SELECT` simple à la requête
> analytique complète.
> `SET search_path TO banque;`

---

## 🟢 Niveau 1 — SELECT, WHERE, ORDER BY, LIMIT

1. Affichez `nom`, `prenom`, `ville` des 10 premiers clients par ordre
   alphabétique de nom.
2. Affichez les comptes dont le solde dépasse 3 000 000, du plus riche au moins
   riche.
3. Affichez les clients de sexe `'F'` habitant `'Abidjan'`.
4. Affichez le `nom` complet des employés sous la forme `'Prénom NOM'` (concaténation).

## 🟡 Niveau 2 — Agrégats & GROUP BY

5. Combien de clients la banque compte-t-elle au total ?
6. Quel est le solde **total**, **moyen**, **min** et **max** de tous les comptes ?
7. Nombre de clients **par ville**, trié du plus peuplé au moins peuplé.
8. Montant total des transactions **par type d'opération**.
9. Salaire moyen des employés **par poste**.

## 🟠 Niveau 3 — HAVING & JOIN

10. Quelles villes comptent **plus de 15 clients** ? (`GROUP BY` + `HAVING`)
11. Affichez chaque compte avec le **nom du client** propriétaire (INNER JOIN
    `comptes` × `clients`).
12. Affichez **toutes** les agences et le nombre de clients rattachés, **même
    les agences sans client** (LEFT JOIN).
13. Affichez chaque employé avec le **nom de son manager** (auto-jointure de
    `employes` sur elle-même).
14. Top 10 des clients par **solde cumulé** de leurs comptes (JOIN + GROUP BY +
    ORDER BY + LIMIT).

## 🔴 Niveau 4 — Sous-requêtes, EXISTS, CASE, COALESCE, dates

15. Affichez les comptes dont le solde est **supérieur à la moyenne** générale
    (sous-requête dans `WHERE`).
16. Affichez les clients qui possèdent **au moins un prêt** (avec `EXISTS`).
17. Affichez les clients qui n'ont **aucune** carte (`NOT EXISTS` ou `LEFT JOIN
    ... IS NULL`).
18. Classez les comptes en `'Riche'` (> 2M), `'Moyen'` (500k–2M) ou `'Modeste'`
    (< 500k) avec une expression `CASE`.
19. Affichez `profession` de chaque client en remplaçant les valeurs `NULL` par
    `'Non renseignée'` (`COALESCE`).
20. Combien de transactions ont eu lieu **par mois** sur l'année 2024 ?
    (fonctions de date)

## 🏆 Niveau Bonus — pour aller plus loin (fenêtrage & CTE)

21. Pour chaque client, classez ses comptes du plus riche au moins riche avec
    `ROW_NUMBER() OVER (PARTITION BY id_client ORDER BY solde DESC)`.
22. Avec une **CTE** (`WITH`), calculez le solde moyen par type de compte, puis
    n'affichez que les types au-dessus de la moyenne globale.

---

## ❓ Questions de compréhension

- **Q1.** Quelle est la différence entre `WHERE` et `HAVING` ?
- **Q2.** Pourquoi `INNER JOIN` peut-il « perdre » des lignes alors que
  `LEFT JOIN` les conserve ?
- **Q3.** Dans quel **ordre** SQL exécute-t-il réellement les clauses
  `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` ? Pourquoi ne
  peut-on pas utiliser un alias de `SELECT` dans le `WHERE` ?
- **Q4.** Quelle est la différence entre `COUNT(*)`, `COUNT(colonne)` et
  `COUNT(DISTINCT colonne)` ?

➡️ Corrigé : [`../solutions/03-DQL-solutions.md`](../solutions/03-DQL-solutions.md)
