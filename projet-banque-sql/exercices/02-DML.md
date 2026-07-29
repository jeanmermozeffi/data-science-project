# 📝 Chapitre 2 — DML (Data Manipulation Language)

> **Objectif** : insérer, modifier et supprimer des **données**.
> On travaille sur le schéma `banque` : `SET search_path TO banque;`
>
> 🛡️ **Pour ne rien casser**, encadrez vos `UPDATE`/`DELETE` d'essai par une
> transaction que vous annulez :
> ```sql
> BEGIN;
>   -- votre commande ...
>   SELECT ...;        -- vérifiez l'effet
> ROLLBACK;            -- on annule tout (les données reviennent)
> ```

---

## 🟢 Niveau 1 — INSERT

1. Insérez une nouvelle agence : code `'AG013'`, nom `'Agence Bingerville'`,
   ville `'Bingerville'`, région `'Lagunes'`.
2. Insérez **en une seule commande** trois nouveaux types de compte de votre
   choix (libellé, taux, frais).
3. Tentez d'insérer un client né en **2015** (donc mineur). Que se passe-t-il,
   et pourquoi ?

## 🟡 Niveau 2 — WHERE, BETWEEN, IN, LIKE

4. Affichez tous les clients dont la ville est `'Abidjan'` **ou** `'Bouaké'`
   (avec `IN`).
5. Affichez les comptes dont le solde est compris **entre** 1 000 000 et
   2 000 000 FCFA (avec `BETWEEN`).
6. Affichez les clients dont le nom **commence par** `'Kou'` (avec `LIKE`).
7. Affichez les transactions de type `'virement'` **ou** `'paiement'` d'un
   montant supérieur à 500 000.

## 🟠 Niveau 3 — UPDATE

8. (Sous `BEGIN ... ROLLBACK`) Passez le statut du compte `id_compte = 5` à
   `'bloque'`.
9. Augmentez de **2 %** le plafond de toutes les cartes de type `'Visa'`.
10. Pour tous les comptes `'épargne'`, appliquez un intérêt : multipliez le
    solde par `(1 + taux_interet/100)`. *(Indice : il faut joindre/retrouver le
    taux via `types_compte`.)*
11. ⚠️ Expliquez ce qui se passerait si vous lanciez
    `UPDATE comptes SET statut = 'bloque';` **sans** `WHERE`.

## 🔴 Niveau 4 — DELETE & INSERT … SELECT

12. (Sous transaction) Supprimez toutes les transactions de canal `'gab'`
    antérieures à 2024. Combien de lignes seraient supprimées ?
13. Créez une table d'archive `transactions_archive` (même structure que
    `transactions`) puis copiez-y, avec `INSERT INTO ... SELECT`, toutes les
    transactions de l'année 2023.
14. Quelle est la différence entre `DELETE FROM transactions;` et
    `TRUNCATE transactions;` en termes de vitesse, de `WHERE` possible et de
    réversibilité ?

---

## ❓ Questions de compréhension

- **Q1.** Pourquoi un `UPDATE` ou `DELETE` sans `WHERE` est-il l'une des erreurs
  les plus dangereuses en SQL ?
- **Q2.** Dans `INSERT INTO comptes (...) VALUES (...)`, que se passe-t-il si on
  omet une colonne ayant une valeur `DEFAULT` ? Et une colonne `NOT NULL` sans
  défaut ?
- **Q3.** Peut-on insérer plusieurs lignes en une seule commande `INSERT` ?
  Quel intérêt en performance ?

➡️ Corrigé : [`../solutions/02-DML-solutions.md`](../solutions/02-DML-solutions.md)
