# 🗄️ Chapitre 1 — DDL (Data Definition Language)

> **Objectif** : savoir créer, modifier et supprimer des structures de données,
> et maîtriser **toutes** les contraintes.
> **Pré-requis** : le stack est démarré (`docker compose up -d`).
>
> 💡 Travaillez dans un **nouveau schéma `exo`** pour ne pas toucher au schéma
> `banque` de référence :
> ```sql
> CREATE SCHEMA IF NOT EXISTS exo;
> SET search_path TO exo;
> ```

---

## 🟢 Niveau 1 — Créer des tables

1. Créez une table `succursales` avec : `id` (clé primaire auto-incrémentée),
   `nom` (texte obligatoire, max 60 caractères), `ville` (texte obligatoire).
2. Créez une table `conseillers` avec : `id` (PK auto), `nom` et `prenom`
   obligatoires, `email` **unique**, `date_embauche` avec pour valeur par
   défaut la date du jour.
3. Affichez la structure de la table `conseillers` (commande `\d exo.conseillers`
   dans psql, ou via pgAdmin).

## 🟡 Niveau 2 — Les contraintes

4. Créez une table `produits_bancaires` avec une colonne `taux` (NUMERIC) qui
   ne peut **jamais** être négative (contrainte `CHECK`).
5. Créez une table `agences_exo` avec une colonne `statut` qui n'accepte que
   les valeurs `'ouverte'`, `'fermee'` ou `'travaux'`.
6. Créez une table `comptes_exo` qui possède une **clé étrangère** vers
   `conseillers(id)` (colonne `id_conseiller`).

## 🟠 Niveau 3 — Modifier l'existant (ALTER)

7. Ajoutez à `succursales` une colonne `telephone VARCHAR(20)`.
8. Ajoutez à `succursales` une contrainte `CHECK` imposant que `nom` ne soit
   pas vide (longueur > 0).
9. Renommez la colonne `telephone` en `tel_fixe`.
10. Supprimez la colonne `tel_fixe`.

## 🔴 Niveau 4 — Cas complet

11. Recréez **de mémoire** une mini-version de la table `comptes` du projet,
    nommée `comptes_full`, avec :
    - une clé primaire auto,
    - un `numero_compte` unique et obligatoire,
    - un `solde` avec valeur par défaut 0 et qui ne peut pas descendre sous −50 000,
    - un `statut` limité à `actif`/`bloque`/`cloture` avec défaut `actif`,
    - une clé étrangère `id_client` vers une table `clients_exo(id)` que vous
      créerez d'abord.
12. Videz entièrement `comptes_full` **sans** supprimer sa structure, en
    réinitialisant l'auto-incrément. Quelle commande utiliser ?
13. Supprimez toutes les tables de votre schéma `exo` en une seule commande.

---

## ❓ Questions de compréhension

- **Q1.** Quelle est la différence fondamentale entre `DELETE`, `TRUNCATE` et
  `DROP` ? Laquelle relève du DDL ?
- **Q2.** Pourquoi une commande DDL est-elle dite « auto-validée »
  (auto-commit) ? Quelle conséquence pour un `ROLLBACK` ?
- **Q3.** Une `FOREIGN KEY` peut-elle pointer vers une colonne qui n'est ni
  `PRIMARY KEY` ni `UNIQUE` ? Pourquoi ?
- **Q4.** Quand préférer une contrainte `CHECK` plutôt que de valider la donnée
  dans le code applicatif ?

➡️ Corrigé détaillé : [`../solutions/01-DDL-solutions.md`](../solutions/01-DDL-solutions.md)
