# ✅ Corrigé — Chapitre 4 : DCL

> À exécuter connecté en tant que `admin`. Testé sur le projet.

---

## 🟢 Niveau 1

**1.** `CREATE ROLE stagiaire LOGIN PASSWORD 'stage2026';`
💡 Sous PostgreSQL, `CREATE USER` = `CREATE ROLE ... LOGIN`. Tout est « rôle ».

**2.** `\du` (psql) ou `SELECT rolname, rolcanlogin FROM pg_roles ORDER BY 1;`

**3.** `ALTER ROLE stagiaire PASSWORD 'nouveau_mdp';`

---

## 🟡 Niveau 2

**4.**
```sql
GRANT USAGE ON SCHEMA banque TO stagiaire;
GRANT SELECT ON banque.clients TO stagiaire;
```
💡 `USAGE` sur le schéma est **obligatoire** : sans lui, même avec un `SELECT`
accordé, l'utilisateur ne « voit » pas la table.

**5.** Test (en ligne de commande) :
```bash
docker exec -e PGPASSWORD=nouveau_mdp finbank_postgres \
  psql -U stagiaire -d finbank -c "SELECT count(*) FROM banque.clients;"   # ✅ 250
docker exec -e PGPASSWORD=nouveau_mdp finbank_postgres \
  psql -U stagiaire -d finbank -c "SELECT count(*) FROM banque.comptes;"   # ❌ permission denied
```

**6.** `GRANT INSERT ON banque.beneficiaires TO stagiaire;`

---

## 🟠 Niveau 3

**7.**
```sql
CREATE ROLE role_reporting NOLOGIN;
GRANT USAGE ON SCHEMA banque TO role_reporting;
GRANT SELECT ON ALL TABLES IN SCHEMA banque TO role_reporting;
```

**8.**
```sql
GRANT role_reporting TO stagiaire;
```
Désormais `stagiaire` **hérite** des droits du rôle → il peut lire **toutes**
les tables (clients, comptes, transactions, …), pas seulement `clients`.

**9.**
```sql
GRANT UPDATE (telephone) ON banque.clients TO stagiaire;
```
Vérification (en tant que stagiaire) :
```sql
UPDATE banque.clients SET telephone = '+225 0700000000' WHERE id_client = 1; -- ✅
UPDATE banque.clients SET email = 'x@x.ci'              WHERE id_client = 1; -- ❌ denied
```
💡 Le privilège colonne limite l'écriture aux seules colonnes autorisées.

---

## 🔴 Niveau 4

**10.** `REVOKE INSERT ON banque.beneficiaires FROM stagiaire;`

**11.** `REVOKE role_reporting FROM stagiaire;`

**12.**
```sql
SELECT grantee, privilege_type
FROM information_schema.role_table_grants
WHERE table_schema = 'banque' AND table_name = 'clients'
ORDER BY grantee, privilege_type;
```

**13.**
```sql
-- On retire d'abord TOUS les privilèges, sinon DROP échoue
REVOKE ALL ON ALL TABLES IN SCHEMA banque FROM stagiaire;
REVOKE ALL ON SCHEMA banque FROM stagiaire;
REVOKE role_reporting FROM stagiaire;        -- si encore membre
DROP ROLE stagiaire;
```
💡 PostgreSQL refuse de supprimer un rôle qui détient encore des privilèges ou
possède des objets. Pratique : `DROP OWNED BY stagiaire;` puis `DROP ROLE`.

---

## ❓ Réponses

- **R1.** Un **utilisateur** (LOGIN) sert à se connecter ; un **rôle de groupe**
  (NOLOGIN) sert à regrouper des privilèges. On accorde les droits **au rôle**,
  puis on rattache les utilisateurs au rôle → maintenance simplifiée : changer
  le rôle met à jour tous ses membres d'un coup.
- **R2.** `WITH GRANT OPTION` permet au bénéficiaire de **re-distribuer** le
  privilège à d'autres. Risqué : on perd le contrôle de la diffusion des droits
  (effet de cascade difficile à révoquer).
- **R3.** Pour appliquer le **moindre privilège** : un guichetier doit pouvoir
  corriger un solde, mais jamais réécrire un numéro de compte ou un email
  sensible. Le privilège colonne réduit la surface d'erreur et de fraude.
- **R4.** **Moindre privilège** = n'accorder que les droits **strictement
  nécessaires** à chaque profil. En banque, cela limite les fuites de données,
  les fraudes internes et les erreurs accidentelles. C'est une exigence
  réglementaire (conformité).
