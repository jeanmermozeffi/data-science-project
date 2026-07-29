# 🔄 Transaction Control Language (TCL) — Cours Bootcamp Data Science

> **Chapitre 5** | Prérequis : Chapitres 1 (DDL), 2 (DML), 3 (DQL), 4 (DCL)

---

## Table des matières

1. [Introduction au TCL](#1-introduction-au-tcl)
2. [Qu'est-ce qu'une transaction ?](#2-quest-ce-quune-transaction-)
3. [Les propriétés ACID](#3-les-propriétés-acid)
4. [COMMIT — Valider une transaction](#4-commit--valider-une-transaction)
5. [ROLLBACK — Annuler une transaction](#5-rollback--annuler-une-transaction)
6. [SAVEPOINT — Points de sauvegarde](#6-savepoint--points-de-sauvegarde)
7. [AUTOCOMMIT — Le mode automatique](#7-autocommit--le-mode-automatique)
8. [Niveaux d'isolation](#8-niveaux-disolation)
9. [Exemple complet — École Bootcamp](#9-exemple-complet--école-bootcamp)
10. [Conclusion](#10-conclusion)
11. [✅ Point de contrôle — TCL](#11--point-de-contrôle--tcl)

---

## 1. Introduction au TCL

### 🔍 Qu'est-ce que le TCL ?

Le **TCL (Transaction Control Language)** est la famille de commandes SQL qui permet de **gérer les transactions** — c'est-à-dire des groupes d'opérations qui doivent réussir ou échouer **ensemble**, comme un tout indivisible.

> 💡 **Analogie** : Imaginez un **virement bancaire** entre deux comptes :
> 1. Retirer 100 € du compte A
> 2. Ajouter 100 € au compte B
>
> Que se passe-t-il si le système plante **entre** ces deux étapes ? Les 100 € disparaîtraient ! La transaction garantit que **soit les deux opérations réussissent, soit aucune** — jamais l'une sans l'autre.

### 🔑 Les commandes fondamentales du TCL

```
┌─────────────────────────────────────────────────────────┐
│               COMMANDES TCL                             │
├──────────────┬──────────────────────────────────────────┤
│  COMMIT      │  Valider (rendre permanent) les changements│
│  ROLLBACK    │  Annuler les changements                  │
│  SAVEPOINT   │  Créer un point de restauration partiel   │
│  SET TRANS.  │  Configurer la transaction                │
└──────────────┴──────────────────────────────────────────┘
```

### 🗺️ Où se situe le TCL ?

| Catégorie | Commandes | Rôle |
|-----------|-----------|------|
| **DDL** | `CREATE`, `ALTER`, `DROP` | Définir la **structure** |
| **DML** | `INSERT`, `UPDATE`, `DELETE` | Manipuler les **données** |
| **DQL** | `SELECT` | **Interroger** les données |
| **DCL** | `GRANT`, `REVOKE` | Contrôler les **accès** |
| ➡️ **TCL** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Gérer les **transactions** |

> 📌 Le TCL fonctionne main dans la main avec le **DML**. Une transaction encadre des `INSERT`, `UPDATE`, `DELETE` pour les sécuriser.

---

## 2. Qu'est-ce qu'une transaction ?

### 📖 Définition

Une **transaction** est une **séquence d'une ou plusieurs opérations SQL** traitée comme une **unité logique de travail unique et indivisible**.

Le principe est **« tout ou rien »** : soit toutes les opérations de la transaction réussissent et sont validées, soit, en cas de problème, toutes sont annulées.

### 2.1 Le cycle de vie d'une transaction

```
    DÉBUT
      │
      ▼
┌─────────────────┐
│  START / BEGIN  │  ← Démarrage de la transaction
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  Opérations DML │  ← INSERT, UPDATE, DELETE...
│  (modifications │     (changements temporaires)
│   temporaires)  │
└─────────────────┘
      │
      ├──────────────────┬───────────────────┐
      ▼                  ▼                   ▼
┌──────────┐      ┌──────────┐       ┌──────────┐
│  COMMIT  │      │ ROLLBACK │       │  ERREUR  │
│ (valider)│      │ (annuler)│       │ (annule  │
└──────────┘      └──────────┘       │  auto)   │
      │                  │           └──────────┘
      ▼                  ▼                   │
 Permanent          Tout annulé              ▼
                                       Tout annulé
```

### 2.2 Démarrer une transaction

```sql
-- Plusieurs syntaxes équivalentes selon le SGBD

-- Standard SQL / MySQL
START TRANSACTION;

-- MySQL / MariaDB (alternative)
BEGIN;

-- PostgreSQL
BEGIN TRANSACTION;
```

### 2.3 Exemple simple

```sql
-- Démarrer la transaction
START TRANSACTION;

-- Faire des modifications (temporaires pour l'instant)
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Sophie', 'Bernard', 'sophie.b@email.com', 24);

UPDATE etudiants
SET statut = 'actif'
WHERE prenom = 'Sophie';

-- Valider les changements (les rendre permanents)
COMMIT;
```

---

## 3. Les propriétés ACID

Les transactions respectent **4 propriétés fondamentales**, résumées par l'acronyme **ACID**. C'est le socle de la fiabilité des bases de données relationnelles.

### 🔑 ACID en détail

```
A — Atomicité     (Atomicity)
C — Cohérence     (Consistency)
I — Isolation     (Isolation)
D — Durabilité    (Durability)
```

| Propriété | Signification | Exemple |
|-----------|---------------|---------|
| **A**tomicité | Tout ou rien : la transaction est indivisible | Le virement débite ET crédite, ou rien |
| **C**ohérence | La base reste dans un état valide | Les contraintes restent toujours respectées |
| **I**solation | Les transactions simultanées ne se gênent pas | Deux virements en parallèle ne se mélangent pas |
| **D**urabilité | Une fois validé, c'est permanent (même après un crash) | Après COMMIT, les données survivent à une panne |

### 3.1 Atomicité — « Tout ou rien »

> 💡 **Analogie** : Un atome était considéré comme indivisible. Une transaction atomique l'est aussi : on ne peut pas exécuter « la moitié » d'un virement.

```sql
START TRANSACTION;

-- Étape 1 : débiter le compte A
UPDATE comptes SET solde = solde - 100 WHERE id = 'A';

-- Étape 2 : créditer le compte B
UPDATE comptes SET solde = solde + 100 WHERE id = 'B';

-- Si TOUT se passe bien
COMMIT;
-- Si une erreur survient entre les deux étapes → ROLLBACK automatique
```

### 3.2 Cohérence — Un état toujours valide

La base passe d'un état valide à un autre état valide. Les contraintes (clés étrangères, CHECK, NOT NULL…) sont toujours respectées.

```sql
-- Si une contrainte est violée pendant la transaction,
-- la transaction échoue et la cohérence est préservée
START TRANSACTION;
INSERT INTO inscriptions (id_etudiant, id_cours) VALUES (1, 999);
-- ❌ Si id_cours = 999 n'existe pas → erreur de clé étrangère
-- → la transaction peut être annulée pour garder la cohérence
ROLLBACK;
```

### 3.3 Isolation — Les transactions ne se gênent pas

Plusieurs transactions peuvent s'exécuter en même temps sans interférer. Chacune voit les données comme si elle était seule (selon le niveau d'isolation choisi — voir section 8).

### 3.4 Durabilité — Permanence garantie

Une fois qu'un `COMMIT` est effectué, les changements sont **enregistrés de façon permanente**, même si le serveur plante juste après.

---

## 4. COMMIT — Valider une transaction

### 📖 Définition

La commande `COMMIT` **valide définitivement** tous les changements effectués pendant la transaction. Les modifications deviennent **permanentes** et visibles par tous les utilisateurs.

> 💡 Tant qu'un `COMMIT` n'a pas été exécuté, les changements sont **temporaires** et invisibles pour les autres utilisateurs.

### Syntaxe

```sql
COMMIT;
```

### 4.1 Exemple — Inscription validée

```sql
START TRANSACTION;

-- Inscrire un nouvel étudiant
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Lucas', 'Petit', 'lucas.petit@email.com', 22);

-- Inscrire ce nouvel étudiant à un cours
INSERT INTO inscriptions (id_etudiant, id_cours)
VALUES (LAST_INSERT_ID(), 1);

-- Tout est correct → on valide
COMMIT;

-- ✅ À partir d'ici, les changements sont permanents
```

### 4.2 Visualisation — Avant et après COMMIT

```
AVANT COMMIT                      APRÈS COMMIT
─────────────                     ─────────────
Modifications visibles            Modifications visibles
SEULEMENT dans votre session      par TOUS les utilisateurs

Possibilité d'annuler             Plus possible d'annuler
avec ROLLBACK                     (sauf nouvelle transaction)

État "en attente"                 État "permanent"
```

---

## 5. ROLLBACK — Annuler une transaction

### 📖 Définition

La commande `ROLLBACK` **annule tous les changements** effectués depuis le début de la transaction (ou depuis un point de sauvegarde). La base revient à son état précédent.

> 💡 **Analogie** : C'est le bouton « Annuler » (Ctrl+Z) géant. Tant que vous n'avez pas validé (`COMMIT`), vous pouvez tout annuler.

### Syntaxe

```sql
ROLLBACK;
```

### 5.1 Exemple — Annuler une erreur

```sql
START TRANSACTION;

-- Oups, on supprime par erreur tous les étudiants !
DELETE FROM etudiants;

-- On se rend compte de l'erreur → on annule TOUT
ROLLBACK;

-- ✅ Les étudiants sont toujours là, rien n'a été supprimé
```

### 5.2 Exemple — Vérification avant validation

```sql
START TRANSACTION;

-- Augmenter les notes de 2 points pour un cours
UPDATE inscriptions
SET note_finale = note_finale + 2
WHERE id_cours = 1;

-- Vérifier le résultat AVANT de valider
SELECT * FROM inscriptions WHERE id_cours = 1;

-- Si le résultat est correct :
COMMIT;

-- Si le résultat est incorrect :
-- ROLLBACK;
```

### 5.3 ROLLBACK automatique

En cas d'**erreur grave** ou de **déconnexion** pendant une transaction, la plupart des SGBD effectuent un `ROLLBACK` automatique pour préserver l'intégrité des données.

```sql
START TRANSACTION;
UPDATE comptes SET solde = solde - 100 WHERE id = 'A';
-- 💥 Le serveur plante ici, avant le COMMIT
-- → Au redémarrage, la transaction est automatiquement annulée
-- → Le compte A n'a PAS été débité
```

### 5.4 COMMIT vs ROLLBACK — Comparaison

```
              COMMIT                    ROLLBACK
         ┌──────────────┐          ┌──────────────┐
         │   VALIDER    │          │   ANNULER    │
         └──────────────┘          └──────────────┘
                │                          │
                ▼                          ▼
      Changements permanents      Retour à l'état initial
      Visibles par tous           Aucune trace des changements
      Irréversibles               Comme si rien ne s'était passé
```

---

## 6. SAVEPOINT — Points de sauvegarde

### 📖 Définition

Un **SAVEPOINT** (point de sauvegarde) est un **marqueur** placé à l'intérieur d'une transaction. Il permet d'annuler **partiellement** une transaction jusqu'à ce point précis, sans tout annuler.

> 💡 **Analogie** : Dans un jeu vidéo, les **points de sauvegarde** vous permettent de revenir à un endroit précis sans recommencer tout le niveau depuis le début.

### Syntaxe

```sql
-- Créer un point de sauvegarde
SAVEPOINT nom_du_point;

-- Revenir à un point de sauvegarde (annule ce qui suit ce point)
ROLLBACK TO nom_du_point;

-- Supprimer un point de sauvegarde
RELEASE SAVEPOINT nom_du_point;
```

### 6.1 Exemple détaillé

```sql
START TRANSACTION;

-- Insérer le premier étudiant
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Alice', 'Martin', 'alice.m@email.com', 23);

SAVEPOINT point1;  -- 📌 Point de sauvegarde 1

-- Insérer le deuxième étudiant
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Bob', 'Durand', 'bob.d@email.com', 25);

SAVEPOINT point2;  -- 📌 Point de sauvegarde 2

-- Insérer le troisième étudiant
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Charlie', 'Leroy', 'charlie.l@email.com', 27);

-- ⚠️ On veut annuler SEULEMENT Charlie, mais garder Alice et Bob
ROLLBACK TO point2;

-- Valider Alice et Bob (Charlie a été annulé)
COMMIT;

-- Résultat final : Alice et Bob sont enregistrés, pas Charlie
```

### 6.2 Visualisation des SAVEPOINT

```
START TRANSACTION
       │
       ▼
   INSERT Alice  ─────────────────────┐
       │                              │
   SAVEPOINT point1  📌               │  Conservé
       │                              │  après
   INSERT Bob  ───────────────────────┤  ROLLBACK TO point2
       │                              │
   SAVEPOINT point2  📌               │
       │                              │
   INSERT Charlie  ──────┐            │
       │                 │ Annulé par │
   ROLLBACK TO point2 ◄──┘ ROLLBACK   │
       │                   TO point2  │
   COMMIT  ───────────────────────────┘
       │
       ▼
  Alice ✅ + Bob ✅ enregistrés, Charlie ❌ annulé
```

### 6.3 Cas d'usage — Traitement par lots

```sql
START TRANSACTION;

-- Lot 1 : inscriptions
INSERT INTO inscriptions (id_etudiant, id_cours) VALUES (1, 1);
SAVEPOINT apres_inscriptions;

-- Lot 2 : mise à jour des notes (peut échouer)
UPDATE inscriptions SET note_finale = 15 WHERE id_etudiant = 1;

-- Si le lot 2 pose problème, on revient au point après les inscriptions
-- ROLLBACK TO apres_inscriptions;

COMMIT;
```

---

## 7. AUTOCOMMIT — Le mode automatique

### 📖 Définition

Par défaut, beaucoup de SGBD fonctionnent en mode **AUTOCOMMIT** : chaque commande SQL est **automatiquement validée** immédiatement, comme si elle était entourée d'un `COMMIT` invisible.

### 7.1 Comprendre l'AUTOCOMMIT

```sql
-- Avec AUTOCOMMIT activé (par défaut)
INSERT INTO etudiants (prenom, nom) VALUES ('Test', 'User');
-- ↑ Cette ligne est IMMÉDIATEMENT et automatiquement validée (COMMIT implicite)
-- → Impossible de l'annuler ensuite
```

### 7.2 Désactiver l'AUTOCOMMIT

Pour contrôler manuellement les transactions, on désactive l'AUTOCOMMIT.

```sql
-- MySQL : désactiver l'autocommit
SET autocommit = 0;

-- Maintenant, les changements ne sont PAS validés automatiquement
INSERT INTO etudiants (prenom, nom) VALUES ('Test', 'User');
-- ↑ Changement temporaire, PAS encore validé

-- Il faut valider explicitement
COMMIT;
-- ou annuler
-- ROLLBACK;

-- Réactiver l'autocommit
SET autocommit = 1;
```

### 7.3 AUTOCOMMIT activé vs désactivé

```
AUTOCOMMIT = 1 (ACTIVÉ)              AUTOCOMMIT = 0 (DÉSACTIVÉ)
─────────────────────────           ──────────────────────────
Chaque commande est validée         Les changements attendent
automatiquement                     un COMMIT explicite

Pas besoin de COMMIT                 COMMIT obligatoire pour valider

Impossible d'annuler                 ROLLBACK possible
après exécution                      avant le COMMIT

Pratique pour des requêtes           Indispensable pour des
simples et isolées                   opérations groupées sécurisées
```

> ⚠️ **Note importante** : `START TRANSACTION` désactive temporairement l'autocommit jusqu'au prochain `COMMIT` ou `ROLLBACK`, même si l'autocommit est activé globalement.

---

## 8. Niveaux d'isolation

### 📖 Définition

Quand plusieurs transactions s'exécutent **simultanément**, des conflits peuvent survenir. Les **niveaux d'isolation** déterminent à quel point une transaction est protégée des effets des autres transactions concurrentes.

### 8.1 Les problèmes de concurrence

| Problème | Description |
|----------|-------------|
| **Dirty Read** (lecture sale) | Lire des données modifiées par une transaction non encore validée |
| **Non-Repeatable Read** | Relire une même ligne et obtenir une valeur différente |
| **Phantom Read** (lecture fantôme) | Une nouvelle ligne apparaît entre deux lectures identiques |

### 8.2 Les 4 niveaux d'isolation

```
Niveau d'isolation       Dirty Read   Non-Repeatable   Phantom
─────────────────────    ──────────   ──────────────   ───────
READ UNCOMMITTED            ❌ Oui        ❌ Oui         ❌ Oui
READ COMMITTED              ✅ Non        ❌ Oui         ❌ Oui
REPEATABLE READ             ✅ Non        ✅ Non         ❌ Oui
SERIALIZABLE                ✅ Non        ✅ Non         ✅ Non

(❌ Oui = le problème peut se produire)
(✅ Non = le problème est évité)
```

| Niveau | Protection | Performance |
|--------|-----------|-------------|
| `READ UNCOMMITTED` | La plus faible | La plus rapide |
| `READ COMMITTED` | Faible | Rapide |
| `REPEATABLE READ` | Forte (défaut MySQL) | Moyenne |
| `SERIALIZABLE` | La plus forte | La plus lente |

### 8.3 Définir le niveau d'isolation

```sql
-- Définir le niveau d'isolation pour la session
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Définir pour la prochaine transaction seulement
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Vérifier le niveau actuel (MySQL)
SELECT @@transaction_isolation;
```

> 💡 **Compromis** : Plus le niveau d'isolation est élevé, plus les données sont protégées, mais plus les performances diminuent (car les transactions s'attendent les unes les autres). Le niveau `REPEATABLE READ` (défaut MySQL) est un bon équilibre pour la plupart des cas.

---

## 9. Exemple complet — École Bootcamp

Voici des scénarios réalistes de transactions sur notre schéma `ecole_bootcamp`.

### Scénario 1 — Inscription complète et sécurisée

Quand un étudiant s'inscrit, on veut créer l'étudiant **ET** l'inscrire à un cours. Si l'une des opérations échoue, on annule tout.

```sql
START TRANSACTION;

-- 1. Créer l'étudiant
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Aïcha', 'Touré', 'aicha.toure@email.com', 24);

-- 2. Récupérer son id et l'inscrire au cours SQL
INSERT INTO inscriptions (id_etudiant, id_cours)
VALUES (LAST_INSERT_ID(), 1);

-- 3. Tout s'est bien passé → valider
COMMIT;

-- Si une étape échoue, on annulerait avec ROLLBACK
-- pour éviter d'avoir un étudiant sans inscription ou l'inverse
```

### Scénario 2 — Transfert d'un étudiant entre deux cours

```sql
START TRANSACTION;

-- Désinscrire l'étudiant 1 du cours 1
DELETE FROM inscriptions
WHERE id_etudiant = 1 AND id_cours = 1;

-- L'inscrire au cours 2
INSERT INTO inscriptions (id_etudiant, id_cours)
VALUES (1, 2);

-- Vérifier avant de valider
SELECT * FROM inscriptions WHERE id_etudiant = 1;

-- Valider le transfert
COMMIT;
```

### Scénario 3 — Saisie de notes avec SAVEPOINT

```sql
START TRANSACTION;

-- Saisir les notes du cours 1
UPDATE inscriptions SET note_finale = 16 WHERE id_etudiant = 1 AND id_cours = 1;
SAVEPOINT notes_cours1;

-- Saisir les notes du cours 2
UPDATE inscriptions SET note_finale = 14 WHERE id_etudiant = 2 AND id_cours = 2;
SAVEPOINT notes_cours2;

-- Erreur détectée sur le cours 2 → revenir au point précédent
ROLLBACK TO notes_cours1;

-- On garde les notes du cours 1, on annule le cours 2
COMMIT;
```

### Scénario 4 — Annulation complète sur erreur

```sql
SET autocommit = 0;
START TRANSACTION;

-- Tentative de mise à jour massive
UPDATE etudiants SET statut = 'diplômé';  -- ⚠️ Oubli du WHERE !

-- On vérifie...
SELECT statut, COUNT(*) FROM etudiants GROUP BY statut;
-- 😱 TOUS les étudiants sont passés "diplômé" !

-- Heureusement, on peut tout annuler
ROLLBACK;

-- ✅ Les statuts sont revenus à la normale
SET autocommit = 1;
```

### Modèle type d'une transaction sécurisée

```sql
-- 1. Désactiver l'autocommit (optionnel)
SET autocommit = 0;

-- 2. Démarrer la transaction
START TRANSACTION;

-- 3. Effectuer les opérations DML
INSERT INTO ...;
UPDATE ...;
DELETE FROM ...;

-- 4. (Optionnel) Placer des SAVEPOINT pour les opérations critiques
SAVEPOINT etape_critique;

-- 5. Vérifier le résultat avec SELECT
SELECT ...;

-- 6. Décider : valider ou annuler
COMMIT;     -- si tout est correct
-- ROLLBACK; -- si problème

-- 7. Réactiver l'autocommit
SET autocommit = 1;
```

---

## 10. Conclusion

### 📌 Récapitulatif des commandes TCL

```
TCL — Transaction Control Language
│
├── START TRANSACTION / BEGIN  → Démarrer une transaction
├── COMMIT                     → Valider (rendre permanent)
├── ROLLBACK                   → Annuler tous les changements
├── SAVEPOINT nom              → Créer un point de sauvegarde
├── ROLLBACK TO nom            → Annuler jusqu'à un point
├── RELEASE SAVEPOINT nom      → Supprimer un point de sauvegarde
└── SET TRANSACTION            → Configurer (niveau d'isolation...)
```

### 🔑 Points clés à retenir

1. Une **transaction** regroupe des opérations en une unité « tout ou rien ».
2. **COMMIT** valide définitivement, **ROLLBACK** annule tout.
3. Les **propriétés ACID** (Atomicité, Cohérence, Isolation, Durabilité) garantissent la fiabilité.
4. Les **SAVEPOINT** permettent des annulations partielles.
5. L'**AUTOCOMMIT** valide chaque commande automatiquement ; le désactiver permet le contrôle manuel.
6. Les **niveaux d'isolation** gèrent les conflits entre transactions concurrentes (compromis sécurité/performance).
7. **Bonne habitude** : vérifier avec un `SELECT` avant de faire `COMMIT`.

### 🎓 Félicitations — Fin du parcours SQL !

Vous avez maintenant parcouru les **5 grandes catégories** du langage SQL :

```
✅ Chapitre 1 — DDL : Définir la structure       (CREATE, ALTER, DROP)
✅ Chapitre 2 — DML : Manipuler les données       (INSERT, UPDATE, DELETE)
✅ Chapitre 3 — DQL : Interroger les données       (SELECT, JOIN, GROUP BY)
✅ Chapitre 4 — DCL : Contrôler les accès          (GRANT, REVOKE)
✅ Chapitre 5 — TCL : Gérer les transactions       (COMMIT, ROLLBACK)
```

Vous possédez désormais les fondations complètes pour travailler avec les bases de données relationnelles dans vos projets de data science !

---

## 11. ✅ Point de contrôle — TCL

### 📝 Questions théoriques

**Q1.** Que signifie l'acronyme ACID et que représente chaque lettre ?

<details>
<summary>👀 Voir la réponse</summary>

> **ACID** = **A**tomicité (tout ou rien), **C**ohérence (état toujours valide), **I**solation (les transactions concurrentes ne se gênent pas), **D**urabilité (les changements validés sont permanents).
</details>

---

**Q2.** Quelle est la différence entre `COMMIT` et `ROLLBACK` ?

<details>
<summary>👀 Voir la réponse</summary>

> `COMMIT` **valide** définitivement tous les changements de la transaction (ils deviennent permanents). `ROLLBACK` **annule** tous les changements et ramène la base à son état initial (avant la transaction).
</details>

---

**Q3.** À quoi sert un `SAVEPOINT` ?

<details>
<summary>👀 Voir la réponse</summary>

> Un `SAVEPOINT` est un marqueur placé dans une transaction. Il permet d'annuler **partiellement** une transaction (`ROLLBACK TO savepoint`) jusqu'à ce point précis, sans annuler la totalité de la transaction.
</details>

---

**Q4.** Que se passe-t-il si l'AUTOCOMMIT est activé et que vous exécutez un `INSERT` ?

<details>
<summary>👀 Voir la réponse</summary>

> Avec l'AUTOCOMMIT activé, l'`INSERT` est **immédiatement et automatiquement validé** (comme un COMMIT implicite). Il devient permanent aussitôt et ne peut plus être annulé avec un `ROLLBACK`.
</details>

---

**Q5.** Pourquoi le niveau d'isolation `SERIALIZABLE` est-il le plus sûr mais le moins performant ?

<details>
<summary>👀 Voir la réponse</summary>

> `SERIALIZABLE` empêche **tous** les problèmes de concurrence (dirty read, non-repeatable read, phantom read) en traitant les transactions comme si elles s'exécutaient l'une après l'autre. Cette sécurité maximale oblige les transactions à s'attendre mutuellement, ce qui réduit les performances.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Transaction simple**

Écrivez une transaction qui insère un nouvel étudiant `('Karim', 'Hassan', 'karim.h@email.com', 26)` puis valide le changement.

<details>
<summary>👀 Voir la solution</summary>

```sql
START TRANSACTION;

INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Karim', 'Hassan', 'karim.h@email.com', 26);

COMMIT;
```
</details>

---

**Exercice 2 — ROLLBACK**

Écrivez une transaction qui augmente toutes les notes du cours 1 de 3 points, vérifie le résultat avec un SELECT, puis **annule** la modification.

<details>
<summary>👀 Voir la solution</summary>

```sql
START TRANSACTION;

UPDATE inscriptions
SET note_finale = note_finale + 3
WHERE id_cours = 1;

-- Vérifier
SELECT * FROM inscriptions WHERE id_cours = 1;

-- Annuler
ROLLBACK;
```
</details>

---

**Exercice 3 — SAVEPOINT**

Dans une seule transaction :
1. Insérez l'étudiant `('Nadia', 'Cherif', 'nadia.c@email.com', 23)`
2. Créez un SAVEPOINT nommé `apres_nadia`
3. Insérez l'étudiant `('Omar', 'Benali', 'omar.b@email.com', 28)`
4. Annulez **seulement** l'insertion d'Omar (gardez Nadia)
5. Validez

<details>
<summary>👀 Voir la solution</summary>

```sql
START TRANSACTION;

-- 1. Insérer Nadia
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Nadia', 'Cherif', 'nadia.c@email.com', 23);

-- 2. Point de sauvegarde
SAVEPOINT apres_nadia;

-- 3. Insérer Omar
INSERT INTO etudiants (prenom, nom, email, age)
VALUES ('Omar', 'Benali', 'omar.b@email.com', 28);

-- 4. Annuler seulement Omar
ROLLBACK TO apres_nadia;

-- 5. Valider (Nadia est gardée, Omar annulé)
COMMIT;
```
</details>

---

**Exercice 4 — Transaction de transfert**

Écrivez une transaction qui transfère l'étudiant 3 du cours 3 vers le cours 4 (désinscription puis réinscription), de façon sécurisée.

<details>
<summary>👀 Voir la solution</summary>

```sql
START TRANSACTION;

-- Désinscrire du cours 3
DELETE FROM inscriptions
WHERE id_etudiant = 3 AND id_cours = 3;

-- Inscrire au cours 4
INSERT INTO inscriptions (id_etudiant, id_cours)
VALUES (3, 4);

-- Vérifier
SELECT * FROM inscriptions WHERE id_etudiant = 3;

-- Valider
COMMIT;
```
</details>

---

**Exercice 5 — AUTOCOMMIT**

Écrivez la séquence de commandes pour : désactiver l'autocommit, supprimer tous les étudiants inactifs, constater le résultat, puis tout annuler, et enfin réactiver l'autocommit.

<details>
<summary>👀 Voir la solution</summary>

```sql
-- Désactiver l'autocommit
SET autocommit = 0;

START TRANSACTION;

-- Supprimer les étudiants inactifs
DELETE FROM etudiants WHERE statut = 'inactif';

-- Constater
SELECT COUNT(*) FROM etudiants;

-- Tout annuler
ROLLBACK;

-- Réactiver l'autocommit
SET autocommit = 1;
```
</details>

---

### 🏆 Challenge bonus

Vous gérez une **boutique en ligne** avec les tables `produits` (avec une colonne `stock`) et `commandes`.

Écrivez une transaction qui simule un **achat sécurisé** :
1. Vérifier que le stock du produit est suffisant
2. Diminuer le stock du produit
3. Créer la commande
4. Si le stock devient négatif → annuler toute la transaction (`ROLLBACK`)
5. Sinon → valider (`COMMIT`)

Réfléchissez à comment les propriétés **ACID** garantissent qu'un client ne puisse jamais acheter un produit en rupture de stock, même si deux clients commandent en même temps.

<details>
<summary>👀 Voir une piste de solution</summary>

```sql
START TRANSACTION;

-- 1. Vérifier le stock disponible
SELECT stock FROM produits WHERE id_produit = 1;

-- 2. Diminuer le stock (par exemple, commande de 2 unités)
UPDATE produits
SET stock = stock - 2
WHERE id_produit = 1;

-- 3. Créer la commande
INSERT INTO commandes (id_produit, quantite, date_commande)
VALUES (1, 2, CURRENT_DATE);

-- 4. Vérifier que le stock n'est pas devenu négatif
SELECT stock FROM produits WHERE id_produit = 1;

-- 5. Décision :
--    - Si stock >= 0 → COMMIT;
--    - Si stock < 0  → ROLLBACK;
COMMIT;
```

> 💡 L'**isolation** garantit que deux clients commandant simultanément ne liront pas le même stock disponible et ne pourront pas le rendre négatif tous les deux. L'**atomicité** garantit que le stock et la commande sont mis à jour ensemble, ou pas du tout.
</details>

---

*📘 Fin du Chapitre 5 — Transaction Control Language | Bootcamp Data Science*

---

## 🎯 Le parcours SQL complet

| Chapitre | Catégorie | Commandes clés |
|----------|-----------|----------------|
| 1 | **DDL** — Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| 2 | **DML** — Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE` |
| 3 | **DQL** — Data Query Language | `SELECT`, `JOIN`, `GROUP BY`, `HAVING` |
| 4 | **DCL** — Data Control Language | `GRANT`, `REVOKE` |
| 5 | **TCL** — Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

**Bravo pour avoir complété l'ensemble du parcours SQL ! 🎓**