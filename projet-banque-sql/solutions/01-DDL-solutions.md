# ✅ Corrigé — Chapitre 1 : DDL

> Toutes les requêtes sont prévues pour le schéma `exo`.
> `CREATE SCHEMA IF NOT EXISTS exo; SET search_path TO exo;`

---

## 🟢 Niveau 1

**1.**
```sql
CREATE TABLE succursales (
    id    SERIAL       PRIMARY KEY,
    nom   VARCHAR(60)  NOT NULL,
    ville VARCHAR(60)  NOT NULL
);
```
💡 `SERIAL` crée automatiquement une séquence et un `DEFAULT nextval(...)`.
La syntaxe moderne équivalente est `id INT GENERATED ALWAYS AS IDENTITY`.

**2.**
```sql
CREATE TABLE conseillers (
    id            SERIAL       PRIMARY KEY,
    nom           VARCHAR(40)  NOT NULL,
    prenom        VARCHAR(40)  NOT NULL,
    email         VARCHAR(80)  UNIQUE,
    date_embauche DATE         NOT NULL DEFAULT CURRENT_DATE
);
```
💡 `CURRENT_DATE` est évalué à chaque insertion, pas au moment du `CREATE`.

**3.** Dans psql : `\d exo.conseillers`. Dans pgAdmin : clic droit sur la table
→ *Properties*. Vous y voyez colonnes, types, contraintes et la séquence.

---

## 🟡 Niveau 2

**4.**
```sql
CREATE TABLE produits_bancaires (
    id   SERIAL PRIMARY KEY,
    nom  VARCHAR(50) NOT NULL,
    taux NUMERIC(5,2) NOT NULL,
    CONSTRAINT chk_taux_positif CHECK (taux >= 0)
);
```
💡 Nommez vos contraintes (`chk_...`) : le message d'erreur devient lisible et
vous pourrez les supprimer par leur nom.

**5.**
```sql
CREATE TABLE agences_exo (
    id     SERIAL PRIMARY KEY,
    statut VARCHAR(10) NOT NULL
           CHECK (statut IN ('ouverte', 'fermee', 'travaux'))
);
```

**6.**
```sql
CREATE TABLE comptes_exo (
    id            SERIAL PRIMARY KEY,
    id_conseiller INT,
    CONSTRAINT fk_compte_conseiller
        FOREIGN KEY (id_conseiller) REFERENCES conseillers (id)
);
```
💡 Une FK garantit l'**intégrité référentielle** : impossible d'insérer un
`id_conseiller` qui n'existe pas dans `conseillers`.

---

## 🟠 Niveau 3

**7.** `ALTER TABLE succursales ADD COLUMN telephone VARCHAR(20);`

**8.**
```sql
ALTER TABLE succursales
    ADD CONSTRAINT chk_nom_non_vide CHECK (length(nom) > 0);
```

**9.** `ALTER TABLE succursales RENAME COLUMN telephone TO tel_fixe;`

**10.** `ALTER TABLE succursales DROP COLUMN tel_fixe;`

---

## 🔴 Niveau 4

**11.**
```sql
CREATE TABLE clients_exo (
    id  SERIAL PRIMARY KEY,
    nom VARCHAR(40) NOT NULL
);

CREATE TABLE comptes_full (
    id            SERIAL        PRIMARY KEY,
    numero_compte VARCHAR(20)   NOT NULL UNIQUE,
    solde         NUMERIC(15,2) NOT NULL DEFAULT 0,
    statut        VARCHAR(10)   NOT NULL DEFAULT 'actif',
    id_client     INT           NOT NULL,
    CONSTRAINT chk_solde   CHECK (solde >= -50000),
    CONSTRAINT chk_statut  CHECK (statut IN ('actif','bloque','cloture')),
    CONSTRAINT fk_client   FOREIGN KEY (id_client) REFERENCES clients_exo (id)
);
```

**12.**
```sql
TRUNCATE TABLE comptes_full RESTART IDENTITY;
```
💡 `TRUNCATE` est bien plus rapide que `DELETE` (il ne journalise pas ligne à
ligne) et `RESTART IDENTITY` remet le compteur auto à 1. C'est une commande DDL.

**13.**
```sql
DROP SCHEMA exo CASCADE;   -- supprime le schéma ET tout son contenu
```
⚠️ `CASCADE` supprime aussi les FK qui pointaient vers ces tables. À manier avec
prudence.

---

## ❓ Réponses aux questions

- **R1.** `DELETE` (DML) retire des **lignes** (avec `WHERE`), peut être annulé
  dans une transaction. `TRUNCATE` (DDL) vide **toute** la table d'un coup,
  rapidement. `DROP` (DDL) supprime la **structure** elle-même. → `TRUNCATE` et
  `DROP` relèvent du DDL.
- **R2.** Sous PostgreSQL, une commande DDL est en réalité transactionnelle
  (on *peut* la mettre dans `BEGIN/ROLLBACK`), mais dans la plupart des SGBD
  (Oracle, MySQL) le DDL déclenche un **commit implicite** : impossible de
  revenir en arrière. Règle de prudence : on ne joue **jamais** un DDL
  destructeur en production sans sauvegarde.
- **R3.** Non. Une FK doit référencer une colonne garantie **unique**
  (`PRIMARY KEY` ou `UNIQUE`), sinon la correspondance serait ambiguë.
- **R4.** Une `CHECK` protège la donnée **quel que soit** le programme qui écrit
  (script, autre appli, import manuel). La validation applicative peut être
  contournée ; la contrainte, jamais. → Les deux sont complémentaires, mais la
  base reste la dernière ligne de défense.
