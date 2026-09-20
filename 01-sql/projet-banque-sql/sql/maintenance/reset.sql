-- ============================================================================
--  FinBank CI — Réinitialisation manuelle
--  ⚠️ Ce script N'EST PAS exécuté automatiquement (il est dans un sous-dossier).
--  Il SUPPRIME tout le schéma puis le recrée. À lancer à la main :
--
--    docker exec -it finbank_postgres \
--      psql -U admin -d finbank -f /docker-entrypoint-initdb.d/maintenance/reset.sql
--
--  ⚠️ Le sous-dossier maintenance/ n'est PAS monté dans initdb par défaut.
--     Le plus simple pour repartir de zéro reste :  docker compose down -v
-- ============================================================================

DROP SCHEMA IF EXISTS banque CASCADE;

-- Puis rejouez dans l'ordre :
--   \i /docker-entrypoint-initdb.d/01_ddl_schema.sql
--   \i /docker-entrypoint-initdb.d/02_dml_donnees.sql
--   \i /docker-entrypoint-initdb.d/03_dcl_roles.sql
