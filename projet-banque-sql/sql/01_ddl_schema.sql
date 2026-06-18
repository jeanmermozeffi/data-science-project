-- ============================================================================
--  FinBank CI — 01. DDL : Définition du schéma
--  Data Definition Language : CREATE SCHEMA, CREATE TABLE, contraintes
-- ----------------------------------------------------------------------------
--  Ce script crée toute la structure de la base (sans données).
--  Il est exécuté AUTOMATIQUEMENT par PostgreSQL au premier démarrage.
--  Pour le rejouer à la main :  \i /docker-entrypoint-initdb.d/01_ddl_schema.sql
-- ============================================================================

-- On regroupe tous les objets dans un schéma dédié 'banque'
-- (un schéma = un "dossier" logique à l'intérieur de la base finbank).
CREATE SCHEMA IF NOT EXISTS banque;

-- Toutes les commandes suivantes s'appliqueront au schéma 'banque' par défaut.
SET search_path TO banque, public;


-- ============================================================================
--  1. AGENCES — les agences physiques de la banque
-- ============================================================================
CREATE TABLE agences (
    id_agence       SERIAL          PRIMARY KEY,          -- auto-incrément
    code_agence     CHAR(5)         NOT NULL UNIQUE,      -- ex: 'AG001'
    nom             VARCHAR(60)     NOT NULL,
    ville           VARCHAR(40)     NOT NULL,
    region          VARCHAR(40)     NOT NULL,
    telephone       VARCHAR(20),                          -- facultatif (NULL autorisé)
    date_ouverture  DATE            NOT NULL DEFAULT CURRENT_DATE
);

COMMENT ON TABLE  agences IS 'Agences physiques de FinBank CI';
COMMENT ON COLUMN agences.code_agence IS 'Code interne unique de l''agence';


-- ============================================================================
--  2. TYPES_COMPTE — référentiel des types de compte
-- ============================================================================
CREATE TABLE types_compte (
    id_type         SERIAL          PRIMARY KEY,
    libelle         VARCHAR(30)     NOT NULL UNIQUE,      -- ex: 'Compte courant'
    taux_interet    NUMERIC(5,2)    NOT NULL DEFAULT 0,   -- en % annuel
    frais_mensuels  NUMERIC(10,2)   NOT NULL DEFAULT 0,   -- en FCFA (XOF)

    -- CHECK : le taux d'intérêt doit rester réaliste (0 à 25 %)
    CONSTRAINT chk_taux CHECK (taux_interet >= 0 AND taux_interet <= 25)
);


-- ============================================================================
--  3. EMPLOYES — personnel de la banque (avec hiérarchie interne)
-- ============================================================================
CREATE TABLE employes (
    id_employe      SERIAL          PRIMARY KEY,
    matricule       CHAR(7)         NOT NULL UNIQUE,      -- ex: 'EMP0001'
    nom             VARCHAR(40)     NOT NULL,
    prenom          VARCHAR(40)     NOT NULL,
    email           VARCHAR(80)     NOT NULL UNIQUE,
    poste           VARCHAR(40)     NOT NULL,
    salaire         NUMERIC(12,2)   NOT NULL,
    date_embauche   DATE            NOT NULL DEFAULT CURRENT_DATE,
    id_agence       INT             NOT NULL,
    id_manager      INT,                                  -- NULL = pas de supérieur

    -- Le salaire doit être strictement positif
    CONSTRAINT chk_salaire CHECK (salaire > 0),

    -- Clé étrangère vers l'agence d'affectation
    CONSTRAINT fk_emp_agence
        FOREIGN KEY (id_agence) REFERENCES agences (id_agence),

    -- Clé étrangère "récursive" : un employé est encadré par un autre employé
    CONSTRAINT fk_emp_manager
        FOREIGN KEY (id_manager) REFERENCES employes (id_employe)
);


-- ============================================================================
--  4. CLIENTS — les clients de la banque
-- ============================================================================
CREATE TABLE clients (
    id_client       SERIAL          PRIMARY KEY,
    nom             VARCHAR(40)     NOT NULL,
    prenom          VARCHAR(40)     NOT NULL,
    date_naissance  DATE            NOT NULL,
    sexe            CHAR(1)         NOT NULL,
    email           VARCHAR(80)     UNIQUE,               -- peut être NULL, mais unique si présent
    telephone       VARCHAR(20)     NOT NULL,
    ville           VARCHAR(40)     NOT NULL,
    profession      VARCHAR(50),
    date_inscription DATE           NOT NULL DEFAULT CURRENT_DATE,
    id_agence       INT             NOT NULL,

    -- Sexe limité à 'M' ou 'F'
    CONSTRAINT chk_sexe CHECK (sexe IN ('M', 'F')),

    -- Un client doit être majeur à l'inscription (contrôle simple sur l'année)
    CONSTRAINT chk_majeur CHECK (date_naissance <= CURRENT_DATE - INTERVAL '18 years'),

    CONSTRAINT fk_client_agence
        FOREIGN KEY (id_agence) REFERENCES agences (id_agence)
);


-- ============================================================================
--  5. COMPTES — les comptes bancaires (un client peut en avoir plusieurs)
-- ============================================================================
CREATE TABLE comptes (
    id_compte       SERIAL          PRIMARY KEY,
    numero_compte   VARCHAR(20)     NOT NULL UNIQUE,      -- IBAN simplifié
    id_client       INT             NOT NULL,
    id_type         INT             NOT NULL,
    solde           NUMERIC(15,2)   NOT NULL DEFAULT 0,
    devise          CHAR(3)         NOT NULL DEFAULT 'XOF',
    statut          VARCHAR(10)     NOT NULL DEFAULT 'actif',
    date_ouverture  DATE            NOT NULL DEFAULT CURRENT_DATE,

    -- Un solde ne peut pas être inférieur à un découvert autorisé de 50 000 FCFA
    CONSTRAINT chk_solde CHECK (solde >= -50000),

    -- Statuts autorisés
    CONSTRAINT chk_statut_compte CHECK (statut IN ('actif', 'bloque', 'cloture')),

    CONSTRAINT fk_compte_client
        FOREIGN KEY (id_client) REFERENCES clients (id_client),
    CONSTRAINT fk_compte_type
        FOREIGN KEY (id_type) REFERENCES types_compte (id_type)
);


-- ============================================================================
--  6. CARTES — cartes bancaires rattachées à un compte
-- ============================================================================
CREATE TABLE cartes (
    id_carte        SERIAL          PRIMARY KEY,
    numero_carte    CHAR(16)        NOT NULL UNIQUE,
    id_compte       INT             NOT NULL,
    type_carte      VARCHAR(15)     NOT NULL,
    plafond         NUMERIC(12,2)   NOT NULL DEFAULT 500000,
    date_emission   DATE            NOT NULL DEFAULT CURRENT_DATE,
    date_expiration DATE            NOT NULL,
    statut          VARCHAR(10)     NOT NULL DEFAULT 'active',

    CONSTRAINT chk_type_carte CHECK (type_carte IN ('Visa', 'Mastercard', 'GIM-UEMOA')),
    CONSTRAINT chk_statut_carte CHECK (statut IN ('active', 'bloquee', 'expiree')),
    CONSTRAINT chk_plafond CHECK (plafond > 0),
    CONSTRAINT chk_dates_carte CHECK (date_expiration > date_emission),

    CONSTRAINT fk_carte_compte
        FOREIGN KEY (id_compte) REFERENCES comptes (id_compte)
);


-- ============================================================================
--  7. BENEFICIAIRES — bénéficiaires enregistrés par les clients
-- ============================================================================
CREATE TABLE beneficiaires (
    id_beneficiaire SERIAL          PRIMARY KEY,
    id_client       INT             NOT NULL,
    nom_beneficiaire VARCHAR(60)    NOT NULL,
    numero_compte_externe VARCHAR(34) NOT NULL,
    banque_externe  VARCHAR(50)     NOT NULL,
    date_ajout      DATE            NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT fk_benef_client
        FOREIGN KEY (id_client) REFERENCES clients (id_client)
);


-- ============================================================================
--  8. TRANSACTIONS — mouvements financiers (table à fort volume)
-- ============================================================================
CREATE TABLE transactions (
    id_transaction  BIGSERIAL       PRIMARY KEY,          -- BIGSERIAL : gros volume
    id_compte       INT             NOT NULL,             -- compte concerné (source)
    id_compte_dest  INT,                                  -- destinataire (virement interne)
    type_operation  VARCHAR(15)     NOT NULL,
    montant         NUMERIC(15,2)   NOT NULL,
    date_operation  TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    libelle         VARCHAR(120),
    canal           VARCHAR(15)     NOT NULL DEFAULT 'mobile',

    -- Le montant d'une transaction doit toujours être strictement positif
    CONSTRAINT chk_montant CHECK (montant > 0),

    CONSTRAINT chk_type_operation
        CHECK (type_operation IN ('depot', 'retrait', 'virement', 'paiement', 'frais')),
    CONSTRAINT chk_canal
        CHECK (canal IN ('mobile', 'agence', 'gab', 'web')),

    CONSTRAINT fk_trans_compte
        FOREIGN KEY (id_compte) REFERENCES comptes (id_compte),
    CONSTRAINT fk_trans_compte_dest
        FOREIGN KEY (id_compte_dest) REFERENCES comptes (id_compte)
);

-- Index pour accélérer les recherches fréquentes par compte et par date
CREATE INDEX idx_trans_compte ON transactions (id_compte);
CREATE INDEX idx_trans_date   ON transactions (date_operation);


-- ============================================================================
--  9. PRETS — crédits accordés aux clients
-- ============================================================================
CREATE TABLE prets (
    id_pret         SERIAL          PRIMARY KEY,
    id_client       INT             NOT NULL,
    id_conseiller   INT             NOT NULL,             -- employé qui a monté le dossier
    montant         NUMERIC(15,2)   NOT NULL,
    taux            NUMERIC(5,2)    NOT NULL,
    duree_mois      INT             NOT NULL,
    date_octroi     DATE            NOT NULL DEFAULT CURRENT_DATE,
    statut          VARCHAR(12)     NOT NULL DEFAULT 'en_cours',

    CONSTRAINT chk_montant_pret CHECK (montant > 0),
    CONSTRAINT chk_duree CHECK (duree_mois BETWEEN 1 AND 360),
    CONSTRAINT chk_statut_pret CHECK (statut IN ('en_cours', 'solde', 'en_defaut')),

    CONSTRAINT fk_pret_client
        FOREIGN KEY (id_client) REFERENCES clients (id_client),
    CONSTRAINT fk_pret_conseiller
        FOREIGN KEY (id_conseiller) REFERENCES employes (id_employe)
);


-- ============================================================================
--  10. REMBOURSEMENTS — échéances de remboursement des prêts
-- ============================================================================
CREATE TABLE remboursements (
    id_remboursement SERIAL         PRIMARY KEY,
    id_pret         INT             NOT NULL,
    numero_echeance INT             NOT NULL,
    montant_echeance NUMERIC(12,2)  NOT NULL,
    date_echeance   DATE            NOT NULL,
    date_paiement   DATE,                                 -- NULL = pas encore payé
    statut          VARCHAR(10)     NOT NULL DEFAULT 'a_payer',

    CONSTRAINT chk_statut_remb CHECK (statut IN ('a_payer', 'paye', 'retard')),

    -- Une échéance est identifiée de façon unique par (prêt + numéro)
    CONSTRAINT uq_echeance UNIQUE (id_pret, numero_echeance),

    CONSTRAINT fk_remb_pret
        FOREIGN KEY (id_pret) REFERENCES prets (id_pret) ON DELETE CASCADE
);


-- ============================================================================
--  Vérification : liste des tables créées
-- ============================================================================
DO $$
BEGIN
    RAISE NOTICE '✅ Schéma "banque" créé : 10 tables prêtes à recevoir les données.';
END $$;
