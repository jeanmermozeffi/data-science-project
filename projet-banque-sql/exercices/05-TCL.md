# 🔄 Chapitre 5 — TCL (Transaction Control Language)

> **Objectif** : garantir qu'une suite d'opérations s'exécute « **tout ou
> rien** » (atomicité). En banque, c'est **vital** : un virement débite un
> compte ET crédite l'autre — jamais l'un sans l'autre.
> `SET search_path TO banque;`
>
> **Les commandes TCL** : `BEGIN` (démarrer), `COMMIT` (valider),
> `ROLLBACK` (annuler), `SAVEPOINT` (point de reprise intermédiaire).
>
> 💡 Le mémo **ACID** : **A**tomicité · **C**ohérence · **I**solation ·
> **D**urabilité.

---

## 🟢 Niveau 1 — COMMIT vs ROLLBACK

1. Ouvrez une transaction, créez un compte de test, puis **annulez** :
   ```sql
   BEGIN;
     INSERT INTO comptes (numero_compte, id_client, id_type, solde)
     VALUES ('CI-TEST-001', 1, 1, 100000);
   ROLLBACK;
   -- Le compte CI-TEST-001 existe-t-il ? (faites un SELECT)
   ```
2. Recommencez mais terminez par `COMMIT`. Le compte existe-t-il cette fois ?
   *(Puis supprimez-le proprement pour nettoyer.)*
3. En une phrase : que fait `ROLLBACK` à toutes les modifications depuis le
   `BEGIN` ?

## 🟡 Niveau 2 — Le virement atomique

4. Écrivez une transaction qui **transfère 50 000 FCFA** du compte `id = 1` vers
   le compte `id = 2` :
   - débiter le compte 1 (`solde - 50000`),
   - créditer le compte 2 (`solde + 50000`),
   - enregistrer une ligne dans `transactions` (type `'virement'`),
   - **valider** avec `COMMIT`.
5. Pourquoi est-il **dangereux** de faire ces 3 ordres SANS transaction (chacun
   auto-validé séparément) ? Imaginez une coupure de courant entre le débit et
   le crédit.

## 🟠 Niveau 3 — SAVEPOINT

6. Dans une transaction, faites un dépôt sur le compte 1, posez un
   `SAVEPOINT apres_depot`, faites un retrait, puis annulez **seulement le
   retrait** avec `ROLLBACK TO SAVEPOINT apres_depot`, et enfin `COMMIT`.
   Vérifiez que le dépôt est conservé mais pas le retrait.
7. Tentez un virement qui ferait passer le solde **sous −50 000** (violation de
   la contrainte `chk_solde`). Que renvoie PostgreSQL ? Que devient la
   transaction ? Utilisez un `SAVEPOINT` pour récupérer la main proprement.

## 🔴 Niveau 4 — Robustesse & isolation

8. Écrivez un virement « sécurisé » qui **vérifie d'abord** que le compte source
   a un solde suffisant, et qui n'effectue le mouvement que si c'est le cas
   (avec un bloc `DO $$ ... $$` PL/pgSQL et `RAISE EXCEPTION`).
9. **Lecture** : expliquez ce qu'est une *lecture sale* (dirty read) et pourquoi
   le niveau d'isolation par défaut de PostgreSQL (`READ COMMITTED`) l'empêche.
10. Que se passe-t-il si vous ouvrez `BEGIN;`, lancez quelques `UPDATE`, puis
    **fermez la fenêtre** sans `COMMIT` ni `ROLLBACK` ?

---

## ❓ Questions de compréhension

- **Q1.** Décrivez les 4 propriétés **ACID** avec, pour chacune, un exemple
  bancaire concret.
- **Q2.** Quelle est la différence entre `ROLLBACK` et `ROLLBACK TO SAVEPOINT` ?
- **Q3.** Qu'est-ce que l'**autocommit** ? Dans psql, chaque commande hors
  `BEGIN` est-elle validée automatiquement ?
- **Q4.** Une commande **DDL** (`CREATE TABLE`) au milieu d'une transaction :
  est-elle annulable par `ROLLBACK` sous PostgreSQL ? Et sous Oracle/MySQL ?

➡️ Corrigé : [`../solutions/05-TCL-solutions.md`](../solutions/05-TCL-solutions.md)
