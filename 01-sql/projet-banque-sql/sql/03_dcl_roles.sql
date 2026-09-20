-- ============================================================================
--  FinBank CI — 03. DCL : Contrôle des accès
--  Data Control Language : CREATE ROLE, GRANT, REVOKE
-- ----------------------------------------------------------------------------
--  On modélise 4 profils métier réalistes d'une banque :
--    • analyste    → lecture seule (reporting, data science)
--    • guichetier  → enregistre des opérations, met à jour les soldes
--    • auditeur    → lecture des flux sensibles uniquement (audit/conformité)
--    • directeur   → tous les droits sur les données
--
--  💡 Différence MySQL ↔ PostgreSQL : pas besoin de FLUSH PRIVILEGES ici.
--     Sous PostgreSQL, GRANT/REVOKE prennent effet immédiatement.
-- ============================================================================

SET search_path TO banque, public;

-- ---------------------------------------------------------------------------
--  1. Rôles "groupes" (NOLOGIN) = ensembles de privilèges réutilisables
-- ---------------------------------------------------------------------------
DROP ROLE IF EXISTS role_analyste;
DROP ROLE IF EXISTS role_guichetier;
DROP ROLE IF EXISTS role_auditeur;
DROP ROLE IF EXISTS role_directeur;

CREATE ROLE role_analyste   NOLOGIN;
CREATE ROLE role_guichetier NOLOGIN;
CREATE ROLE role_auditeur   NOLOGIN;
CREATE ROLE role_directeur  NOLOGIN;

-- Tous les rôles doivent pouvoir "voir" le schéma pour accéder aux tables
GRANT USAGE ON SCHEMA banque TO
    role_analyste, role_guichetier, role_auditeur, role_directeur;


-- ---------------------------------------------------------------------------
--  2. GRANT — attribution des privilèges par profil
-- ---------------------------------------------------------------------------

-- 2a. ANALYSTE : lecture seule sur TOUTES les tables
GRANT SELECT ON ALL TABLES IN SCHEMA banque TO role_analyste;

-- 2b. GUICHETIER : lit tout, crée des transactions, ajuste les soldes
GRANT SELECT ON ALL TABLES IN SCHEMA banque TO role_guichetier;
GRANT INSERT ON banque.transactions TO role_guichetier;
-- Privilège au niveau COLONNE : ne peut modifier QUE la colonne solde
GRANT UPDATE (solde, statut) ON banque.comptes TO role_guichetier;
-- Droit d'utiliser les séquences auto-incrément des tables qu'il alimente
GRANT USAGE ON ALL SEQUENCES IN SCHEMA banque TO role_guichetier;

-- 2c. AUDITEUR : lecture des seules tables sensibles (flux & crédits)
GRANT SELECT ON banque.transactions, banque.prets, banque.remboursements
    TO role_auditeur;

-- 2d. DIRECTEUR : tous les privilèges sur les données
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA banque TO role_directeur;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA banque TO role_directeur;


-- ---------------------------------------------------------------------------
--  3. Utilisateurs réels (LOGIN) rattachés aux rôles
--     ⚠️ Mots de passe de DÉMO uniquement — à changer en production.
-- ---------------------------------------------------------------------------
DROP ROLE IF EXISTS aya_analyste;
DROP ROLE IF EXISTS koffi_guichet;
DROP ROLE IF EXISTS mariam_audit;
DROP ROLE IF EXISTS konan_dir;

CREATE ROLE aya_analyste  LOGIN PASSWORD 'analyste123';
CREATE ROLE koffi_guichet LOGIN PASSWORD 'guichet123';
CREATE ROLE mariam_audit  LOGIN PASSWORD 'audit123';
CREATE ROLE konan_dir     LOGIN PASSWORD 'directeur123';

-- Assignation des rôles (héritage des privilèges)
GRANT role_analyste   TO aya_analyste;
GRANT role_guichetier TO koffi_guichet;
GRANT role_auditeur   TO mariam_audit;
GRANT role_directeur  TO konan_dir;

-- Les utilisateurs doivent pouvoir se connecter à la base finbank
GRANT CONNECT ON DATABASE finbank TO
    aya_analyste, koffi_guichet, mariam_audit, konan_dir;


-- ---------------------------------------------------------------------------
--  4. Privilèges par défaut (pour les tables créées À L'AVENIR)
--     Sans cela, une nouvelle table ne serait visible que de son créateur.
-- ---------------------------------------------------------------------------
ALTER DEFAULT PRIVILEGES IN SCHEMA banque
    GRANT SELECT ON TABLES TO role_analyste;


-- ---------------------------------------------------------------------------
--  5. Exemple de REVOKE (retrait de privilège) — laissé en commentaire
--     Décommentez pour interdire au guichetier de modifier le statut :
-- ---------------------------------------------------------------------------
-- REVOKE UPDATE (statut) ON banque.comptes FROM role_guichetier;


DO $$
BEGIN
    RAISE NOTICE '✅ Rôles & utilisateurs créés : analyste, guichetier, auditeur, directeur.';
END $$;
