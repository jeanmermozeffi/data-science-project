# 🔐 Chapitre 4 — DCL (Data Control Language)

> **Objectif** : gérer **qui** a le droit de faire **quoi** sur les données.
> Ces commandes demandent les droits d'administration → connectez-vous avec
> l'utilisateur `admin` (superutilisateur).
>
> 💡 Le projet crée déjà 4 profils (`role_analyste`, `role_guichetier`,
> `role_auditeur`, `role_directeur`) dans `03_dcl_roles.sql`. Ici, vous en créez
> de nouveaux pour vous entraîner.
>
> ⚠️ **MySQL vs PostgreSQL** : sous PostgreSQL il n'y a **pas** de
> `FLUSH PRIVILEGES`. Les `GRANT`/`REVOKE` sont effectifs immédiatement.

---

## 🟢 Niveau 1 — Utilisateurs & connexion

1. Créez un utilisateur `stagiaire` pouvant se connecter, avec le mot de passe
   `stage2026`.
2. Listez tous les rôles/utilisateurs existants (`\du` dans psql, ou
   `SELECT rolname FROM pg_roles;`).
3. Modifiez le mot de passe de `stagiaire` en `nouveau_mdp`.

## 🟡 Niveau 2 — GRANT

4. Autorisez `stagiaire` à utiliser le schéma `banque` (`USAGE`) puis à **lire**
   uniquement la table `clients`.
5. Connectez-vous en tant que `stagiaire` et vérifiez : `SELECT` sur `clients`
   doit marcher, `SELECT` sur `comptes` doit **échouer**.
6. Donnez à `stagiaire` le droit d'**insérer** dans `beneficiaires`.

## 🟠 Niveau 3 — Rôles & privilèges fins

7. Créez un rôle de groupe `role_reporting` (NOLOGIN) ayant le droit de
   **lecture sur toutes les tables** du schéma `banque`.
8. Rattachez `stagiaire` au rôle `role_reporting`. Que peut-il lire désormais ?
9. Donnez à `stagiaire` le droit de modifier **uniquement la colonne
   `telephone`** de la table `clients` (privilège au niveau colonne). Vérifiez
   qu'il ne peut **pas** modifier `email`.

## 🔴 Niveau 4 — REVOKE & audit

10. Retirez à `stagiaire` le droit d'insérer dans `beneficiaires`.
11. Retirez-lui complètement l'appartenance au rôle `role_reporting`.
12. Affichez la liste des privilèges accordés sur la table `clients`
    (`information_schema.role_table_grants`).
13. Supprimez l'utilisateur `stagiaire`. *(Indice : il faut d'abord lui retirer
    ses privilèges/objets.)*

---

## ❓ Questions de compréhension

- **Q1.** Quelle est la différence entre un **utilisateur** (LOGIN) et un
  **rôle** de groupe (NOLOGIN) ? Pourquoi passe-t-on par des rôles ?
- **Q2.** À quoi sert `WITH GRANT OPTION` et pourquoi est-ce risqué ?
- **Q3.** Pourquoi accorder un privilège au niveau **colonne** (ex. `UPDATE
  (telephone)`) plutôt que sur toute la table ?
- **Q4.** Le principe du **moindre privilège** : qu'est-ce que c'est et pourquoi
  est-il central en sécurité bancaire ?

➡️ Corrigé : [`../solutions/04-DCL-solutions.md`](../solutions/04-DCL-solutions.md)
