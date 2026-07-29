# 🔐 Data Control Language (DCL) — Cours Bootcamp Data Science

> **Chapitre 4** | Prérequis : Chapitres 1 (DDL), 2 (DML), 3 (DQL)

---

## Table des matières

1. [Introduction au DCL](#1-introduction-au-dcl)
2. [Rappel — Les utilisateurs et la sécurité](#2-rappel--les-utilisateurs-et-la-sécurité)
3. [Créer et gérer des utilisateurs](#3-créer-et-gérer-des-utilisateurs)
4. [GRANT — Accorder des privilèges](#4-grant--accorder-des-privilèges)
5. [REVOKE — Retirer des privilèges](#5-revoke--retirer-des-privilèges)
6. [Les rôles (ROLE)](#6-les-rôles-role)
7. [Niveaux de privilèges](#7-niveaux-de-privilèges)
8. [Bonnes pratiques de sécurité](#8-bonnes-pratiques-de-sécurité)
9. [Exemple complet — École Bootcamp](#9-exemple-complet--école-bootcamp)
10. [Conclusion](#10-conclusion)
11. [✅ Point de contrôle — DCL](#11--point-de-contrôle--dcl)

---

## 1. Introduction au DCL

### 🔍 Qu'est-ce que le DCL ?

Le **DCL (Data Control Language)** est la famille de commandes SQL qui permet de **contrôler les accès et les permissions** sur une base de données. Il définit **qui peut faire quoi** sur quelles données.

> 💡 **Analogie** : Imaginez un immeuble de bureaux. La base de données, c'est l'immeuble. Le DCL, c'est le **système de badges d'accès** :
> - Certains employés ont accès à tous les étages (**administrateur**)
> - D'autres peuvent seulement lire des documents dans certaines salles (**lecteur**)
> - D'autres encore peuvent modifier des fichiers dans leur département (**éditeur**)
> - Le DCL permet de **donner** (`GRANT`) ou **retirer** (`REVOKE`) ces badges

### 🔑 Les deux commandes fondamentales

```
┌────────────────────────────────────────────────────────┐
│               COMMANDES DCL                            │
├──────────┬─────────────────────────────────────────────┤
│  GRANT   │  Accorder des privilèges à un utilisateur   │
│  REVOKE  │  Retirer des privilèges à un utilisateur    │
└──────────┴─────────────────────────────────────────────┘
```

### 🗺️ Où se situe le DCL ?

| Catégorie | Commandes | Rôle |
|-----------|-----------|------|
| **DDL** | `CREATE`, `ALTER`, `DROP` | Définir la **structure** |
| **DML** | `INSERT`, `UPDATE`, `DELETE` | Manipuler les **données** |
| **DQL** | `SELECT` | **Interroger** les données |
| ➡️ **DCL** | `GRANT`, `REVOKE` | Contrôler les **accès** |
| **TCL** | `COMMIT`, `ROLLBACK` | Gérer les **transactions** |

### ⚠️ Pourquoi le DCL est essentiel ?

Sans contrôle d'accès, n'importe qui pourrait :
- Lire des données confidentielles (salaires, données personnelles)
- Modifier ou supprimer des données critiques
- Accéder à toute la base de données

Le DCL est la **première ligne de défense** pour protéger vos données.

---

## 2. Rappel — Les utilisateurs et la sécurité

### 2.1 Le modèle de sécurité SQL

```
SERVEUR DE BASE DE DONNÉES
│
├── Utilisateur root / admin  ← Accès total (superutilisateur)
│
├── Utilisateur jean          ← Accès limité à certaines bases/tables
│   ├── Peut lire ecole_bootcamp.etudiants
│   └── Ne peut pas modifier ou supprimer
│
└── Utilisateur app_user      ← Accès applicatif restreint
    ├── INSERT sur inscriptions
    ├── SELECT sur cours
    └── Aucun accès aux autres tables
```

### 2.2 Les types de privilèges

| Privilège | Description | Commande SQL concernée |
|-----------|-------------|------------------------|
| `SELECT` | Lire les données | `SELECT` |
| `INSERT` | Insérer des données | `INSERT` |
| `UPDATE` | Modifier des données | `UPDATE` |
| `DELETE` | Supprimer des données | `DELETE` |
| `CREATE` | Créer des objets | `CREATE TABLE`, `CREATE DATABASE` |
| `ALTER` | Modifier des objets | `ALTER TABLE` |
| `DROP` | Supprimer des objets | `DROP TABLE` |
| `INDEX` | Créer des index | `CREATE INDEX` |
| `EXECUTE` | Exécuter des procédures | `CALL` |
| `ALL PRIVILEGES` | Tous les privilèges | Tout |

---

## 3. Créer et gérer des utilisateurs

Avant d'accorder des privilèges, il faut **créer des utilisateurs**.

> ⚠️ La syntaxe varie légèrement selon le SGBD. Les exemples suivants sont en **MySQL/MariaDB**.

### 3.1 Créer un utilisateur

```sql
-- Syntaxe
CREATE USER 'nom_utilisateur'@'hote' IDENTIFIED BY 'mot_de_passe';

-- Exemples

-- Utilisateur local (connexion depuis le même serveur)
CREATE USER 'jean'@'localhost' IDENTIFIED BY 'MotDePasse123!';

-- Utilisateur distant (connexion depuis n'importe quelle machine)
CREATE USER 'app_user'@'%' IDENTIFIED BY 'AppPass456!';

-- Utilisateur depuis une IP spécifique
CREATE USER 'admin_rh'@'192.168.1.10' IDENTIFIED BY 'RH_Secure789!';
```

> 💡 Le `@'hote'` précise **d'où** l'utilisateur peut se connecter :
> - `@'localhost'` → uniquement depuis le serveur lui-même
> - `@'%'` → depuis n'importe quelle machine
> - `@'192.168.1.10'` → depuis une IP précise

### 3.2 Lister les utilisateurs existants

```sql
-- Afficher tous les utilisateurs (MySQL)
SELECT user, host FROM mysql.user;
```

**Résultat :**
```
┌──────────┬─────────────┐
│   user   │    host     │
├──────────┼─────────────┤
│  root    │  localhost  │
│  jean    │  localhost  │
│ app_user │      %      │
│ admin_rh │192.168.1.10 │
└──────────┴─────────────┘
```

### 3.3 Modifier le mot de passe

```sql
-- MySQL 8+
ALTER USER 'jean'@'localhost' IDENTIFIED BY 'NouveauMotDePasse!';

-- Forcer le changement au prochain login
ALTER USER 'jean'@'localhost' PASSWORD EXPIRE;
```

### 3.4 Supprimer un utilisateur

```sql
DROP USER 'jean'@'localhost';

-- Vérifier l'existence avant suppression
DROP USER IF EXISTS 'jean'@'localhost';
```

---

## 4. GRANT — Accorder des privilèges

### 📖 Définition

La commande `GRANT` permet d'**accorder des droits** à un utilisateur sur une base de données, une table, ou même une colonne spécifique.

### Syntaxe générale

```sql
GRANT privilege1, privilege2, ...
ON base_de_donnees.table
TO 'utilisateur'@'hote';
```

### 4.1 Accorder un privilège sur une table

```sql
-- Donner le droit de lecture sur la table etudiants
GRANT SELECT ON ecole_bootcamp.etudiants TO 'jean'@'localhost';

-- Donner lecture et insertion sur les inscriptions
GRANT SELECT, INSERT ON ecole_bootcamp.inscriptions TO 'jean'@'localhost';
```

### 4.2 Accorder des privilèges sur toute une base

```sql
-- L'utilisateur peut tout lire dans ecole_bootcamp
GRANT SELECT ON ecole_bootcamp.* TO 'jean'@'localhost';

-- L'utilisateur peut lire et modifier dans ecole_bootcamp
GRANT SELECT, INSERT, UPDATE ON ecole_bootcamp.* TO 'jean'@'localhost';
```

### 4.3 Accorder tous les privilèges

```sql
-- Tous les droits sur une base spécifique
GRANT ALL PRIVILEGES ON ecole_bootcamp.* TO 'admin_bootcamp'@'localhost';

-- Tous les droits sur toutes les bases (niveau superadmin)
GRANT ALL PRIVILEGES ON *.* TO 'super_admin'@'localhost';
```

> ⚠️ `ALL PRIVILEGES ON *.*` donne un accès total au serveur. À utiliser avec la plus grande prudence.

### 4.4 WITH GRANT OPTION — Déléguer les droits

```sql
-- jean peut donner ses propres droits à d'autres utilisateurs
GRANT SELECT ON ecole_bootcamp.* TO 'jean'@'localhost'
WITH GRANT OPTION;
```

### 4.5 Accorder des droits sur des colonnes spécifiques

```sql
-- L'utilisateur ne peut lire que le prénom et le nom (pas l'email ni l'âge)
GRANT SELECT (prenom, nom) ON ecole_bootcamp.etudiants TO 'lecteur_rh'@'localhost';

-- L'utilisateur peut seulement modifier la note finale
GRANT UPDATE (note_finale) ON ecole_bootcamp.inscriptions TO 'correcteur'@'localhost';
```

### 4.6 Appliquer les changements — FLUSH PRIVILEGES

```sql
-- Recharger les privilèges en mémoire (nécessaire dans certains cas)
FLUSH PRIVILEGES;
```

> 💡 Après un `GRANT` ou `REVOKE` direct, il est recommandé d'exécuter `FLUSH PRIVILEGES` pour s'assurer que les changements sont bien pris en compte.

### 4.7 Vérifier les privilèges accordés

```sql
-- Voir les droits d'un utilisateur
SHOW GRANTS FOR 'jean'@'localhost';
```

**Résultat :**
```
┌────────────────────────────────────────────────────────────────────────┐
│ Grants for jean@localhost                                              │
├────────────────────────────────────────────────────────────────────────┤
│ GRANT USAGE ON *.* TO `jean`@`localhost`                               │
│ GRANT SELECT ON `ecole_bootcamp`.`etudiants` TO `jean`@`localhost`     │
│ GRANT SELECT, INSERT ON `ecole_bootcamp`.`inscriptions` TO `jean`@`localhost` │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. REVOKE — Retirer des privilèges

### 📖 Définition

La commande `REVOKE` permet de **retirer des droits** précédemment accordés à un utilisateur.

### Syntaxe générale

```sql
REVOKE privilege1, privilege2, ...
ON base_de_donnees.table
FROM 'utilisateur'@'hote';
```

### 5.1 Retirer un privilège spécifique

```sql
-- Retirer le droit d'insertion à jean
REVOKE INSERT ON ecole_bootcamp.inscriptions FROM 'jean'@'localhost';

-- Retirer le droit de lecture sur les étudiants
REVOKE SELECT ON ecole_bootcamp.etudiants FROM 'jean'@'localhost';
```

### 5.2 Retirer tous les privilèges

```sql
-- Retirer tous les droits sur une base
REVOKE ALL PRIVILEGES ON ecole_bootcamp.* FROM 'jean'@'localhost';

-- Retirer tous les droits sur toutes les bases
REVOKE ALL PRIVILEGES ON *.* FROM 'jean'@'localhost';
```

### 5.3 Retirer la capacité de déléguer

```sql
-- Retirer le WITH GRANT OPTION
REVOKE GRANT OPTION ON ecole_bootcamp.* FROM 'jean'@'localhost';
```

### 5.4 Cycle complet GRANT → REVOKE

```sql
-- 1. Créer l'utilisateur
CREATE USER 'stagiaire'@'localhost' IDENTIFIED BY 'Stage2024!';

-- 2. Accorder des droits limités
GRANT SELECT ON ecole_bootcamp.etudiants TO 'stagiaire'@'localhost';
GRANT SELECT ON ecole_bootcamp.cours TO 'stagiaire'@'localhost';

-- 3. Vérifier
SHOW GRANTS FOR 'stagiaire'@'localhost';

-- 4. Le stage est terminé, retirer les droits
REVOKE ALL PRIVILEGES ON ecole_bootcamp.* FROM 'stagiaire'@'localhost';

-- 5. Supprimer le compte
DROP USER 'stagiaire'@'localhost';
```

---

## 6. Les rôles (ROLE)

### 📖 Définition

Un **rôle** est un **ensemble de privilèges nommé et réutilisable**. Plutôt que d'accorder les mêmes droits à chaque utilisateur un par un, on crée un rôle avec ces droits, puis on l'assigne aux utilisateurs concernés.

> 💡 **Analogie** : Dans une entreprise, plutôt que de configurer les accès badge de chaque nouvel employé un par un, on crée des **profils** (Comptable, RH, Développeur) avec les accès prédéfinis, puis on assigne le profil à chaque nouvel arrivant.

> ⚠️ Les rôles sont disponibles dans **MySQL 8+**, **PostgreSQL**, **Oracle**. Pas dans les versions plus anciennes de MySQL/MariaDB.

### 6.1 Créer un rôle

```sql
-- Créer des rôles pour l'école bootcamp
CREATE ROLE 'lecteur_bootcamp';
CREATE ROLE 'gestionnaire_bootcamp';
CREATE ROLE 'admin_bootcamp';
```

### 6.2 Accorder des privilèges au rôle

```sql
-- Rôle lecteur : lecture seule
GRANT SELECT ON ecole_bootcamp.* TO 'lecteur_bootcamp';

-- Rôle gestionnaire : lecture + modification des inscriptions et notes
GRANT SELECT ON ecole_bootcamp.* TO 'gestionnaire_bootcamp';
GRANT INSERT, UPDATE ON ecole_bootcamp.inscriptions TO 'gestionnaire_bootcamp';
GRANT UPDATE (note_finale) ON ecole_bootcamp.inscriptions TO 'gestionnaire_bootcamp';

-- Rôle admin : tous les droits
GRANT ALL PRIVILEGES ON ecole_bootcamp.* TO 'admin_bootcamp';
```

### 6.3 Assigner un rôle à un utilisateur

```sql
-- Créer les utilisateurs
CREATE USER 'marie'@'localhost'   IDENTIFIED BY 'Marie2024!';
CREATE USER 'kofi'@'localhost'    IDENTIFIED BY 'Kofi2024!';
CREATE USER 'fatou'@'localhost'   IDENTIFIED BY 'Fatou2024!';

-- Assigner les rôles
GRANT 'lecteur_bootcamp'      TO 'marie'@'localhost';   -- Marie peut seulement lire
GRANT 'gestionnaire_bootcamp' TO 'kofi'@'localhost';    -- Kofi peut gérer les inscriptions
GRANT 'admin_bootcamp'        TO 'fatou'@'localhost';   -- Fatou a tous les droits
```

### 6.4 Activer un rôle

```sql
-- L'utilisateur doit activer son rôle après connexion
SET ROLE 'lecteur_bootcamp';

-- Activer tous les rôles assignés
SET ROLE ALL;

-- Définir le rôle par défaut (activé automatiquement à la connexion)
SET DEFAULT ROLE 'lecteur_bootcamp' TO 'marie'@'localhost';
```

### 6.5 Visualisation — Rôles vs Droits directs

```
SANS RÔLES (fastidieux)          AVEC RÔLES (efficace)
────────────────────────         ─────────────────────
GRANT SELECT ON ...              CREATE ROLE 'lecteur'
  TO 'marie'@'localhost';        GRANT SELECT ON ... TO 'lecteur'
GRANT SELECT ON ...              
  TO 'kofi'@'localhost';         GRANT 'lecteur' TO 'marie'
GRANT SELECT ON ...              GRANT 'lecteur' TO 'kofi'
  TO 'pierre'@'localhost';       GRANT 'lecteur' TO 'pierre'
...                              ...
(répété pour chaque table        (une seule fois pour le rôle,
et chaque utilisateur)           puis assigné à chaque user)
```

### 6.6 Retirer un rôle

```sql
-- Retirer un rôle à un utilisateur
REVOKE 'lecteur_bootcamp' FROM 'marie'@'localhost';

-- Supprimer un rôle
DROP ROLE 'lecteur_bootcamp';
```

---

## 7. Niveaux de privilèges

Les privilèges peuvent être accordés à différents **niveaux de granularité**.

```
NIVEAU GLOBAL         →  ON *.*
NIVEAU BASE           →  ON ma_base.*
NIVEAU TABLE          →  ON ma_base.ma_table
NIVEAU COLONNE        →  GRANT SELECT (col1, col2) ON ma_base.ma_table
NIVEAU PROCÉDURE      →  ON PROCEDURE ma_base.ma_procedure
```

### 7.1 Tableau récapitulatif

| Niveau | Syntaxe | Portée |
|--------|---------|--------|
| **Global** | `ON *.*` | Toutes les bases, toutes les tables |
| **Base de données** | `ON ma_base.*` | Toutes les tables d'une base |
| **Table** | `ON ma_base.ma_table` | Une seule table |
| **Colonne** | `GRANT SELECT (col) ON ...` | Une ou plusieurs colonnes |
| **Procédure** | `ON PROCEDURE ma_base.proc` | Une procédure stockée |

### 7.2 Exemple — Plusieurs niveaux pour un utilisateur

```sql
-- app_user : accès applicatif précis et sécurisé
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'AppSecure!';

-- Peut lire tous les cours
GRANT SELECT ON ecole_bootcamp.cours TO 'app_user'@'localhost';

-- Peut lire et inscrire des étudiants
GRANT SELECT, INSERT ON ecole_bootcamp.inscriptions TO 'app_user'@'localhost';

-- Peut seulement lire le prénom et le nom des étudiants (pas l'email !)
GRANT SELECT (prenom, nom) ON ecole_bootcamp.etudiants TO 'app_user'@'localhost';
```

---

## 8. Bonnes pratiques de sécurité

### 8.1 Le principe du moindre privilège

> 🔑 **Règle d'or** : N'accordez que les droits **strictement nécessaires** à chaque utilisateur pour accomplir sa tâche — pas plus.

```sql
-- ❌ Mauvaise pratique : donner ALL PRIVILEGES par facilité
GRANT ALL PRIVILEGES ON *.* TO 'app_user'@'%';

-- ✅ Bonne pratique : droits minimaux et ciblés
GRANT SELECT, INSERT ON ecole_bootcamp.inscriptions TO 'app_user'@'localhost';
GRANT SELECT ON ecole_bootcamp.cours TO 'app_user'@'localhost';
```

### 8.2 Ne jamais utiliser root pour les applications

```
❌ Application connectée en root
   → Une faille = accès total au serveur

✅ Application connectée avec un utilisateur dédié aux droits limités
   → Une faille = accès limité à ce que l'application utilise
```

### 8.3 Restreindre l'hôte de connexion

```sql
-- ❌ Connexion depuis n'importe où (risque élevé)
CREATE USER 'admin'@'%' IDENTIFIED BY 'pass';

-- ✅ Connexion uniquement depuis le serveur local
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'pass';

-- ✅ Connexion depuis le réseau interne seulement
CREATE USER 'admin'@'192.168.1.%' IDENTIFIED BY 'pass';
```

### 8.4 Utiliser des mots de passe forts

```sql
-- ❌ Mot de passe faible
CREATE USER 'user1'@'localhost' IDENTIFIED BY '123456';

-- ✅ Mot de passe fort (majuscules, minuscules, chiffres, symboles, 12+ caractères)
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'B0otcamp@2024!';
```

### 8.5 Auditer régulièrement les accès

```sql
-- Vérifier régulièrement qui a accès à quoi
SELECT user, host FROM mysql.user;

-- Vérifier les droits d'un utilisateur spécifique
SHOW GRANTS FOR 'jean'@'localhost';

-- Révoquer les accès des utilisateurs qui n'en ont plus besoin
REVOKE ALL PRIVILEGES ON ecole_bootcamp.* FROM 'ancien_stagiaire'@'localhost';
DROP USER IF EXISTS 'ancien_stagiaire'@'localhost';
```

### 8.6 Résumé des bonnes pratiques

```
✅ FAIRE                              ❌ NE PAS FAIRE
────────────────────────────          ───────────────────────────
Principe du moindre privilège         GRANT ALL PRIVILEGES par défaut
Utilisateurs dédiés par rôle          Partager le compte root
Restreindre l'hôte (@localhost)       Utiliser @'%' sans raison
Mots de passe forts                   Mots de passe simples
Auditer régulièrement                 Oublier les anciens comptes
Utiliser des rôles                    Répéter les GRANT manuellement
```

---

## 9. Exemple complet — École Bootcamp

Voici un exemple réaliste de gestion des accès pour notre école bootcamp.

### Scénario

L'école `ecole_bootcamp` a plusieurs types d'utilisateurs :

| Profil | Besoins |
|--------|---------|
| **Administrateur** | Accès total à la base |
| **Formateur** | Voir les étudiants, mettre à jour les notes |
| **Étudiant** | Voir ses propres cours et ses notes |
| **Application web** | Inscrire des étudiants, lire les cours |
| **Auditeur** | Lecture seule sur toute la base |

### Étape 1 — Créer les rôles

```sql
-- Définir les rôles
CREATE ROLE 'role_admin_ecole';
CREATE ROLE 'role_formateur';
CREATE ROLE 'role_auditeur';
CREATE ROLE 'role_app_web';
```

### Étape 2 — Attribuer les privilèges aux rôles

```sql
-- Administrateur : tous les droits
GRANT ALL PRIVILEGES ON ecole_bootcamp.* TO 'role_admin_ecole';

-- Auditeur : lecture seule sur toute la base
GRANT SELECT ON ecole_bootcamp.* TO 'role_auditeur';

-- Formateur : lecture sur tout + modification des notes
GRANT SELECT ON ecole_bootcamp.* TO 'role_formateur';
GRANT UPDATE (note_finale) ON ecole_bootcamp.inscriptions TO 'role_formateur';

-- Application web : opérations métier
GRANT SELECT ON ecole_bootcamp.cours        TO 'role_app_web';
GRANT SELECT ON ecole_bootcamp.etudiants    TO 'role_app_web';
GRANT SELECT, INSERT ON ecole_bootcamp.inscriptions TO 'role_app_web';
GRANT INSERT ON ecole_bootcamp.etudiants    TO 'role_app_web';
```

### Étape 3 — Créer les utilisateurs et assigner les rôles

```sql
-- Administrateur de la base
CREATE USER 'admin_ecole'@'localhost'  IDENTIFIED BY 'Admin@Ecole2024!';
GRANT 'role_admin_ecole' TO 'admin_ecole'@'localhost';
SET DEFAULT ROLE 'role_admin_ecole' TO 'admin_ecole'@'localhost';

-- Formateurs
CREATE USER 'jean_formateur'@'localhost'  IDENTIFIED BY 'Jean@Form2024!';
CREATE USER 'marie_formateur'@'localhost' IDENTIFIED BY 'Marie@Form2024!';
GRANT 'role_formateur' TO 'jean_formateur'@'localhost';
GRANT 'role_formateur' TO 'marie_formateur'@'localhost';
SET DEFAULT ROLE 'role_formateur' TO 'jean_formateur'@'localhost';
SET DEFAULT ROLE 'role_formateur' TO 'marie_formateur'@'localhost';

-- Auditeur externe
CREATE USER 'auditeur'@'192.168.1.50' IDENTIFIED BY 'Audit@2024!';
GRANT 'role_auditeur' TO 'auditeur'@'192.168.1.50';
SET DEFAULT ROLE 'role_auditeur' TO 'auditeur'@'192.168.1.50';

-- Compte applicatif
CREATE USER 'app_web'@'localhost' IDENTIFIED BY 'App@Web2024!';
GRANT 'role_app_web' TO 'app_web'@'localhost';
SET DEFAULT ROLE 'role_app_web' TO 'app_web'@'localhost';
```

### Étape 4 — Vérifier les accès

```sql
-- Vérifier les droits de chaque compte
SHOW GRANTS FOR 'jean_formateur'@'localhost';
SHOW GRANTS FOR 'app_web'@'localhost';
SHOW GRANTS FOR 'auditeur'@'192.168.1.50';
```

### Étape 5 — Gérer les changements (un formateur part)

```sql
-- Jean quitte l'école : retirer ses droits et supprimer son compte
REVOKE 'role_formateur' FROM 'jean_formateur'@'localhost';
DROP USER 'jean_formateur'@'localhost';

-- Un nouveau formateur arrive
CREATE USER 'pierre_formateur'@'localhost' IDENTIFIED BY 'Pierre@Form2024!';
GRANT 'role_formateur' TO 'pierre_formateur'@'localhost';
SET DEFAULT ROLE 'role_formateur' TO 'pierre_formateur'@'localhost';
```

### Schéma final des accès

```
ecole_bootcamp
│
├── admin_ecole        → role_admin_ecole    → ALL PRIVILEGES
│
├── jean_formateur     → role_formateur      → SELECT (tout)
├── marie_formateur    → role_formateur         UPDATE (note_finale)
│
├── auditeur           → role_auditeur       → SELECT (tout, lecture seule)
│
└── app_web            → role_app_web        → SELECT cours, etudiants
                                               SELECT, INSERT inscriptions
                                               INSERT etudiants
```

---

## 10. Conclusion

### 📌 Récapitulatif des commandes DCL

```
DCL — Data Control Language
│
├── CREATE USER      → Créer un utilisateur
├── DROP USER        → Supprimer un utilisateur
├── ALTER USER       → Modifier un utilisateur (mot de passe...)
│
├── GRANT            → Accorder des privilèges
├── REVOKE           → Retirer des privilèges
│
├── CREATE ROLE      → Créer un rôle
├── DROP ROLE        → Supprimer un rôle
├── SET ROLE         → Activer un rôle
│
└── SHOW GRANTS      → Visualiser les privilèges d'un utilisateur
```

### 🔑 Points clés à retenir

1. **GRANT** accorde des droits, **REVOKE** les retire.
2. Le **principe du moindre privilège** : n'accorder que ce qui est nécessaire.
3. Les **rôles** simplifient la gestion en regroupant des privilèges réutilisables.
4. Toujours **restreindre l'hôte** de connexion (`@localhost` plutôt que `@'%'`).
5. Ne jamais utiliser **root** pour les connexions applicatives.
6. **Auditer régulièrement** les accès et supprimer les comptes inutilisés.

### 🗺️ Ce qui vient ensuite

Dans le prochain et dernier chapitre, vous découvrirez le **TCL (Transaction Control Language)** — la gestion des transactions avec `COMMIT`, `ROLLBACK` et `SAVEPOINT` pour garantir l'intégrité de vos données lors d'opérations complexes.

---

## 11. ✅ Point de contrôle — DCL

### 📝 Questions théoriques

**Q1.** Que signifie DCL et quelles sont ses deux commandes principales ?

<details>
<summary>👀 Voir la réponse</summary>

> **DCL** = Data Control Language. Ses deux commandes principales sont `GRANT` (accorder des privilèges) et `REVOKE` (retirer des privilèges). On y associe aussi la gestion des utilisateurs (`CREATE USER`, `DROP USER`) et des rôles (`CREATE ROLE`).
</details>

---

**Q2.** Qu'est-ce que le principe du moindre privilège ?

<details>
<summary>👀 Voir la réponse</summary>

> C'est le principe selon lequel chaque utilisateur ne doit disposer que des **droits strictement nécessaires** à l'exécution de ses tâches — pas plus. Cela limite les risques en cas de compromission d'un compte.
</details>

---

**Q3.** Quelle est la différence entre `GRANT SELECT ON ecole_bootcamp.*` et `GRANT SELECT ON *.*` ?

<details>
<summary>👀 Voir la réponse</summary>

> `ON ecole_bootcamp.*` accorde le droit `SELECT` uniquement sur **toutes les tables de la base `ecole_bootcamp`**. `ON *.*` accorde le droit `SELECT` sur **toutes les tables de toutes les bases de données** du serveur — un accès bien plus large et plus dangereux.
</details>

---

**Q4.** Quel est l'avantage des rôles par rapport aux GRANT directs ?

<details>
<summary>👀 Voir la réponse</summary>

> Les rôles permettent de **regrouper un ensemble de privilèges** sous un nom réutilisable. Au lieu de répéter les mêmes `GRANT` pour chaque utilisateur, on assigne simplement le rôle. Si les droits du rôle changent, tous les utilisateurs qui ont ce rôle sont mis à jour automatiquement.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Créer des utilisateurs**

Créez les deux utilisateurs suivants :
- `data_analyst` connecté depuis `localhost`, mot de passe `Analyst@2024!`
- `etudiant_api` connecté depuis n'importe quelle machine, mot de passe `Api@2024!`

<details>
<summary>👀 Voir la solution</summary>

```sql
CREATE USER 'data_analyst'@'localhost' IDENTIFIED BY 'Analyst@2024!';
CREATE USER 'etudiant_api'@'%' IDENTIFIED BY 'Api@2024!';
```
</details>

---

**Exercice 2 — Accorder des privilèges**

Pour l'utilisateur `data_analyst` :
- Accorder la lecture sur toute la base `ecole_bootcamp`
- Accorder la lecture et l'insertion sur la table `inscriptions` uniquement

<details>
<summary>👀 Voir la solution</summary>

```sql
GRANT SELECT ON ecole_bootcamp.* TO 'data_analyst'@'localhost';
GRANT SELECT, INSERT ON ecole_bootcamp.inscriptions TO 'data_analyst'@'localhost';
FLUSH PRIVILEGES;
```
</details>

---

**Exercice 3 — Retirer des privilèges**

Retirez le droit d'insertion sur `inscriptions` à `data_analyst`, puis vérifiez ses droits restants.

<details>
<summary>👀 Voir la solution</summary>

```sql
REVOKE INSERT ON ecole_bootcamp.inscriptions FROM 'data_analyst'@'localhost';
SHOW GRANTS FOR 'data_analyst'@'localhost';
```
</details>

---

**Exercice 4 — Rôles**

Créez un rôle `role_correcteur` qui peut uniquement mettre à jour la colonne `note_finale` dans la table `inscriptions`. Puis assignez ce rôle à l'utilisateur `data_analyst`.

<details>
<summary>👀 Voir la solution</summary>

```sql
CREATE ROLE 'role_correcteur';
GRANT UPDATE (note_finale) ON ecole_bootcamp.inscriptions TO 'role_correcteur';
GRANT 'role_correcteur' TO 'data_analyst'@'localhost';
SET DEFAULT ROLE 'role_correcteur' TO 'data_analyst'@'localhost';
```
</details>

---

**Exercice 5 — Cycle complet**

Un stagiaire `stage_user` rejoint l'école pour 3 mois. Il doit pouvoir :
- Lire les cours et les formateurs
- Ne pas avoir accès aux données des étudiants

À la fin du stage, supprimez son compte proprement.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- Création
CREATE USER 'stage_user'@'localhost' IDENTIFIED BY 'Stage@3Mois!';

-- Droits
GRANT SELECT ON ecole_bootcamp.cours       TO 'stage_user'@'localhost';
GRANT SELECT ON ecole_bootcamp.formateurs  TO 'stage_user'@'localhost';

-- Vérification
SHOW GRANTS FOR 'stage_user'@'localhost';

-- Fin de stage : nettoyage
REVOKE ALL PRIVILEGES ON ecole_bootcamp.* FROM 'stage_user'@'localhost';
DROP USER 'stage_user'@'localhost';
```
</details>

---

### 🏆 Challenge bonus

Concevez un système de gestion des accès complet pour une **clinique médicale** avec une base `clinique` contenant les tables : `patients`, `medecins`, `consultations`, `ordonnances`.

Définissez les rôles et les droits pour :
- Un **médecin** (peut voir et modifier ses propres patients et consultations)
- Une **secrétaire** (peut gérer les rendez-vous, pas les données médicales)
- Un **pharmacien** (peut seulement lire les ordonnances)
- Un **administrateur système** (accès total)

Justifiez chaque choix de privilège en pensant à la **confidentialité des données médicales**.

---

*📘 Fin du Chapitre 4 — Data Control Language | Bootcamp Data Science*