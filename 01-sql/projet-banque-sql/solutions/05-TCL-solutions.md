# ✅ Corrigé — Chapitre 5 : TCL

> `SET search_path TO banque;` — scénarios testés sur le projet.

---

## 🟢 Niveau 1

**1.**
```sql
BEGIN;
  INSERT INTO comptes (numero_compte, id_client, id_type, solde)
  VALUES ('CI-TEST-001', 1, 1, 100000);
ROLLBACK;

SELECT * FROM comptes WHERE numero_compte = 'CI-TEST-001';  -- 0 ligne
```
Le `ROLLBACK` annule l'insertion : **le compte n'existe pas**.

**2.**
```sql
BEGIN;
  INSERT INTO comptes (numero_compte, id_client, id_type, solde)
  VALUES ('CI-TEST-001', 1, 1, 100000);
COMMIT;

SELECT * FROM comptes WHERE numero_compte = 'CI-TEST-001';  -- 1 ligne

-- Nettoyage :
DELETE FROM comptes WHERE numero_compte = 'CI-TEST-001';
```

**3.** `ROLLBACK` **annule toutes** les modifications effectuées depuis le
`BEGIN` : la base revient exactement à son état d'avant la transaction.

---

## 🟡 Niveau 2 — Le virement atomique

**4.**
```sql
BEGIN;
  UPDATE comptes SET solde = solde - 50000 WHERE id_compte = 1;   -- débit
  UPDATE comptes SET solde = solde + 50000 WHERE id_compte = 2;   -- crédit
  INSERT INTO transactions (id_compte, id_compte_dest, type_operation, montant, libelle)
  VALUES (1, 2, 'virement', 50000, 'Virement compte 1 -> 2');
COMMIT;
```
💡 Les **trois** ordres forment **une** unité. `COMMIT` ne valide que si tout a
réussi → impossible de débiter sans créditer.

**5.** Sans transaction, chaque ordre est validé **immédiatement et
séparément**. Si une panne survient juste après le débit, l'argent disparaît du
compte 1 **sans** arriver sur le compte 2 → incohérence comptable. La
transaction garantit l'**atomicité** : les 3 ordres réussissent ensemble ou
sont tous annulés.

---

## 🟠 Niveau 3 — SAVEPOINT

**6.**
```sql
BEGIN;
  UPDATE comptes SET solde = solde + 20000 WHERE id_compte = 1;   -- dépôt
  SAVEPOINT apres_depot;
  UPDATE comptes SET solde = solde - 999999999 WHERE id_compte = 1; -- retrait à annuler
  ROLLBACK TO SAVEPOINT apres_depot;        -- on annule SEULEMENT le retrait
COMMIT;                                     -- le dépôt, lui, est conservé
```
💡 `ROLLBACK TO SAVEPOINT` revient au point posé **sans** annuler toute la
transaction. Le dépôt validé avant le savepoint survit.

**7.**
```sql
BEGIN;
  SAVEPOINT avant_virement;
  -- Ce retrait viole chk_solde (solde >= -50000) :
  UPDATE comptes SET solde = solde - 999999999 WHERE id_compte = 3;
  -- ERROR: new row for relation "comptes" violates check constraint "chk_solde"
ROLLBACK TO SAVEPOINT avant_virement;   -- on récupère la main
-- ... on peut continuer d'autres opérations ...
COMMIT;
```
Après l'erreur, la transaction est en état « **aborted** » : toute commande
suivante échoue tant qu'on n'a pas fait `ROLLBACK` (total) ou `ROLLBACK TO
SAVEPOINT`. Le savepoint permet de poursuivre proprement.

---

## 🔴 Niveau 4 — Robustesse & isolation

**8.** Virement sécurisé avec contrôle de solde (PL/pgSQL) :
```sql
DO $$
DECLARE
    v_source  INT := 1;
    v_dest    INT := 2;
    v_montant NUMERIC := 75000;
    v_solde   NUMERIC;
BEGIN
    -- 1. Lire le solde du compte source
    SELECT solde INTO v_solde FROM comptes WHERE id_compte = v_source;

    -- 2. Vérifier la provision
    IF v_solde < v_montant THEN
        RAISE EXCEPTION 'Solde insuffisant : % dispo, % demandé', v_solde, v_montant;
    END IF;

    -- 3. Effectuer le virement
    UPDATE comptes SET solde = solde - v_montant WHERE id_compte = v_source;
    UPDATE comptes SET solde = solde + v_montant WHERE id_compte = v_dest;
    INSERT INTO transactions (id_compte, id_compte_dest, type_operation, montant, libelle)
    VALUES (v_source, v_dest, 'virement', v_montant, 'Virement sécurisé');

    RAISE NOTICE 'Virement de % effectué.', v_montant;
END $$;
```
💡 Un bloc `DO $$ ... $$` s'exécute dans **une seule transaction implicite** :
si `RAISE EXCEPTION` se déclenche, **tout** est annulé automatiquement.

**9.** Une **lecture sale** (*dirty read*) = lire une donnée modifiée par une
autre transaction **non encore validée** (qui pourrait être annulée). Exemple :
lire un solde crédité par un virement qui sera ensuite annulé → on aurait vu de
l'argent qui n'a jamais existé. Le niveau `READ COMMITTED` (défaut PostgreSQL)
ne montre **que** les données déjà `COMMIT`-ées → pas de lecture sale.

**10.** Si la session se ferme sans `COMMIT` ni `ROLLBACK`, PostgreSQL effectue
un **`ROLLBACK` automatique** à la déconnexion : les modifications non validées
sont perdues. Rien n'est jamais à moitié écrit.

---

## ❓ Réponses

- **R1. ACID :**
  - **Atomicité** — un virement débite ET crédite, ou rien (tout ou rien).
  - **Cohérence** — après la transaction, les contraintes (ex. `chk_solde`)
    restent respectées.
  - **Isolation** — deux virements simultanés ne se corrompent pas mutuellement.
  - **Durabilité** — une fois `COMMIT` fait, la donnée survit même à une coupure
    de courant (écrite sur disque / journal).
- **R2.** `ROLLBACK` annule **toute** la transaction. `ROLLBACK TO SAVEPOINT s`
  annule **seulement** ce qui a été fait après le savepoint `s` ; la transaction
  reste ouverte.
- **R3.** L'**autocommit** valide automatiquement chaque commande isolée. Dans
  psql, oui : hors `BEGIN`, chaque ordre est sa propre transaction validée
  immédiatement. Dès qu'on tape `BEGIN`, l'autocommit est suspendu jusqu'au
  `COMMIT`/`ROLLBACK`.
- **R4.** Sous **PostgreSQL**, le DDL est transactionnel : un `CREATE TABLE`
  dans un `BEGIN` est **annulable** par `ROLLBACK`. Sous **Oracle/MySQL**, le
  DDL provoque un **commit implicite** → non annulable.
