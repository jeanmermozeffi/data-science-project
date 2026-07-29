-- Création de la base DataScienceDB
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'DataScienceDB')
BEGIN
    CREATE DATABASE DataScienceDB;
END
GO

USE DataScienceDB;
GO

-- Création du schéma staging
IF NOT EXISTS (SELECT schema_id FROM sys.schemas WHERE name = 'staging')
BEGIN
    EXEC('CREATE SCHEMA staging');
END
GO

-- Création de la table raw_events
IF NOT EXISTS (
    SELECT 1 FROM sys.objects
    WHERE object_id = OBJECT_ID(N'staging.raw_events') AND type = 'U'
)
BEGIN
    CREATE TABLE staging.raw_events (
        id          INT             IDENTITY(1,1) PRIMARY KEY,
        event_name  NVARCHAR(100)   NOT NULL,
        event_date  DATETIME2       NOT NULL DEFAULT GETDATE(),
        payload     NVARCHAR(MAX)   NULL
    );
END
GO

-- Données d'exemple
INSERT INTO staging.raw_events (event_name, payload) VALUES
    ('user_signup',    '{"user_id": 1001, "email": "alice@example.com", "plan": "free"}'),
    ('purchase',       '{"user_id": 1002, "amount": 49.99, "currency": "USD", "item": "pro_plan"}'),
    ('page_view',      '{"user_id": 1001, "page": "/dashboard", "duration_ms": 3420}');
GO

PRINT 'DataScienceDB initialisée avec succès.';
GO
