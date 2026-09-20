-- ============================================================================
--  FinBank CI — 02. DML : Insertion des données
--  Data Manipulation Language : INSERT (en masse, réaliste, reproductible)
-- ----------------------------------------------------------------------------
--  Stratégie :
--   • Tables de référence (agences, types_compte) → INSERT explicites
--   • Tables à fort volume → générées avec generate_series() + random()
--   • setseed() rend la génération REPRODUCTIBLE (mêmes données à chaque run)
--  Volumes : clients 250 · comptes 350 · cartes 280 · transactions 8000 ...
-- ============================================================================

SET search_path TO banque;

-- Graine de hasard fixe → données identiques à chaque exécution du script
SELECT setseed(0.4242);


-- ============================================================================
--  1. AGENCES (12 lignes — table de référence)
-- ============================================================================
INSERT INTO agences (code_agence, nom, ville, region, telephone, date_ouverture) VALUES
('AG001', 'Agence Plateau',        'Abidjan',     'Lagunes',          '+225 27 20 30 40 01', '2008-03-12'),
('AG002', 'Agence Cocody',         'Abidjan',     'Lagunes',          '+225 27 22 44 55 02', '2010-06-01'),
('AG003', 'Agence Yopougon',       'Abidjan',     'Lagunes',          '+225 27 23 45 67 03', '2011-09-15'),
('AG004', 'Agence Treichville',    'Abidjan',     'Lagunes',          '+225 27 21 35 46 04', '2009-01-20'),
('AG005', 'Agence Bouaké Centre',  'Bouaké',      'Gbêkê',            '+225 27 31 63 20 05', '2012-11-05'),
('AG006', 'Agence Yamoussoukro',   'Yamoussoukro','Bélier',           '+225 27 30 64 10 06', '2013-04-18'),
('AG007', 'Agence San-Pédro',      'San-Pédro',   'Bas-Sassandra',    '+225 27 34 71 22 07', '2014-07-30'),
('AG008', 'Agence Korhogo',        'Korhogo',     'Poro',             '+225 27 36 86 33 08', '2015-02-12'),
('AG009', 'Agence Daloa',          'Daloa',       'Haut-Sassandra',   '+225 27 32 78 44 09', '2016-10-01'),
('AG010', 'Agence Man',            'Man',         'Tonkpi',           '+225 27 33 79 55 10', '2017-05-22'),
('AG011', 'Agence Abengourou',     'Abengourou',  'Indénié-Djuablin', '+225 27 35 91 66 11', '2018-08-14'),
('AG012', 'Agence Gagnoa',         'Gagnoa',      'Gôh',              '+225 27 32 77 77 12', '2019-12-03');


-- ============================================================================
--  2. TYPES_COMPTE (5 lignes — table de référence)
-- ============================================================================
INSERT INTO types_compte (libelle, taux_interet, frais_mensuels) VALUES
('Compte courant',     0.00,  1000.00),
('Compte épargne',     3.50,     0.00),
('Compte épargne plus', 5.25,   500.00),
('Compte jeune',       2.00,     0.00),
('Compte entreprise',  1.50,  5000.00);


-- ============================================================================
--  3. EMPLOYES (60 lignes — hiérarchie auto-référencée)
--     Les 4 premiers sont des directeurs (id_manager NULL).
-- ============================================================================
INSERT INTO employes (matricule, nom, prenom, email, poste, salaire, date_embauche, id_agence, id_manager)
SELECT
    'EMP' || lpad(g::text, 4, '0'),
    (ARRAY['Kouassi','Koffi','Traoré','Bamba','Diabaté','Konaté','Yao','Touré',
           'Coulibaly','Ouattara','Diallo','Cissé','Koné','N''Guessan','Brou',
           'Fofana','Sangaré','Doumbia','Bakayoko','Adingra'])[1 + (g % 20)],
    (ARRAY['Konan','Kouadio','Aboubacar','Seydou','Moussa','Salif','Drissa',
           'Mamadou','Adama','Issouf','Patrick','Serge','Jean','Aya','Fatou',
           'Aminata','Mariam','Awa','Rokia','Bintou'])[1 + (g % 20)],
    'employe' || g || '@finbank.ci',
    (ARRAY['Directeur d''agence','Conseiller clientèle','Chargé de prêts',
           'Guichetier','Analyste','Gestionnaire de comptes'])[1 + (g % 6)],
    round((250000 + random() * 850000)::numeric, -3),     -- salaire arrondi au millier
    DATE '2015-01-01' + (random() * 3200)::int,           -- embauche entre 2015 et ~2023
    1 + (g % 12),                                          -- réparti sur les 12 agences
    CASE WHEN g <= 4 THEN NULL ELSE 1 + (floor(random() * 4))::int END
FROM generate_series(1, 60) AS g;


-- ============================================================================
--  4. CLIENTS (250 lignes)
-- ============================================================================
INSERT INTO clients (nom, prenom, date_naissance, sexe, email, telephone, ville, profession, date_inscription, id_agence)
SELECT
    (ARRAY['Kouassi','Koffi','Traoré','Bamba','Diabaté','Konaté','Yao','Touré',
           'Coulibaly','Ouattara','Diallo','Cissé','Koné','N''Guessan','Brou',
           'Fofana','Sangaré','Doumbia','Bakayoko','Adingra','Aka','Tanoh',
           'Anoma','Soro','Gnagne'])[1 + (g % 25)],
    (ARRAY['Konan','Kouadio','Aboubacar','Seydou','Moussa','Salif','Drissa',
           'Mamadou','Adama','Issouf','Patrick','Serge','Christelle','Aya',
           'Fatou','Aminata','Mariam','Awa','Rokia','Bintou','Affoué','Akissi',
           'Amani','Aurélie','Marie'])[1 + (g % 25)],
    DATE '1960-01-01' + (random() * 16000)::int,          -- naissance ~1960..2003 (majeur)
    CASE WHEN random() < 0.5 THEN 'M' ELSE 'F' END,
    'client' || g || '@mail.ci',
    '+225 0' || (1 + floor(random() * 8))::int || ' ' ||
        lpad((floor(random() * 100))::int::text, 2, '0') || ' ' ||
        lpad((floor(random() * 100))::int::text, 2, '0') || ' ' ||
        lpad((floor(random() * 100))::int::text, 2, '0') || ' ' ||
        lpad((floor(random() * 100))::int::text, 2, '0'),
    (ARRAY['Abidjan','Bouaké','Yamoussoukro','San-Pédro','Korhogo','Daloa',
           'Man','Abengourou','Gagnoa','Divo'])[1 + (g % 10)],
    (ARRAY['Commerçant','Enseignant','Fonctionnaire','Étudiant','Médecin',
           'Ingénieur','Agriculteur','Artisan','Comptable','Chauffeur',
           'Infirmier','Avocat','Entrepreneur',NULL])[1 + (g % 14)],
    DATE '2019-01-01' + (random() * 2350)::int,           -- inscrit entre 2019 et 2025
    1 + (g % 12)
FROM generate_series(1, 250) AS g;


-- ============================================================================
--  5. COMPTES (350 lignes)
--     • 250 comptes : un par client (couverture totale)
--     • 100 comptes : clients aléatoires (= clients multi-comptes)
-- ============================================================================
-- 5a. Un compte courant pour chaque client
INSERT INTO comptes (numero_compte, id_client, id_type, solde, statut, date_ouverture)
SELECT
    'CI' || lpad(g::text, 18, '0'),
    g,                                                    -- id_client = g
    1 + (g % 5),                                          -- type 1..5
    round((random() * 4500000)::numeric, 2),
    (ARRAY['actif','actif','actif','actif','bloque','cloture'])[1 + (g % 6)],
    DATE '2019-06-01' + (random() * 2000)::int
FROM generate_series(1, 250) AS g;

-- 5b. 100 comptes supplémentaires (clients déjà existants)
INSERT INTO comptes (numero_compte, id_client, id_type, solde, statut, date_ouverture)
SELECT
    'CI' || lpad((250 + g)::text, 18, '0'),
    1 + floor(random() * 250)::int,
    1 + (g % 5),
    round((random() * 4500000)::numeric, 2),
    'actif',
    DATE '2020-01-01' + (random() * 1800)::int
FROM generate_series(1, 100) AS g;


-- ============================================================================
--  6. CARTES (280 lignes)
-- ============================================================================
INSERT INTO cartes (numero_carte, id_compte, type_carte, plafond, date_emission, date_expiration, statut)
SELECT
    lpad((4000000000000000 + g)::text, 16, '0'),
    1 + floor(random() * 350)::int,
    (ARRAY['Visa','Mastercard','GIM-UEMOA'])[1 + (g % 3)],
    (ARRAY[200000,500000,1000000,2000000])[1 + (g % 4)],
    DATE '2022-01-01' + (random() * 700)::int,
    DATE '2026-01-01' + (random() * 700)::int,
    (ARRAY['active','active','active','bloquee','expiree'])[1 + (g % 5)]
FROM generate_series(1, 280) AS g;


-- ============================================================================
--  7. BENEFICIAIRES (200 lignes)
-- ============================================================================
INSERT INTO beneficiaires (id_client, nom_beneficiaire, numero_compte_externe, banque_externe, date_ajout)
SELECT
    1 + floor(random() * 250)::int,
    (ARRAY['Koffi','Traoré','Bamba','Yao','Touré','Coulibaly','Diallo','Koné'])[1 + (g % 8)]
        || ' ' ||
    (ARRAY['Jean','Awa','Salif','Marie','Adama','Fatou','Serge','Mariam'])[1 + (g % 8)],
    'CI' || lpad((900000 + g)::text, 22, '0'),
    (ARRAY['SGBCI','Ecobank','NSIA Banque','BACI','Coris Bank','Orange Bank'])[1 + (g % 6)],
    DATE '2021-01-01' + (random() * 1500)::int
FROM generate_series(1, 200) AS g;


-- ============================================================================
--  8. TRANSACTIONS (8000 lignes — table à fort volume)
-- ============================================================================
INSERT INTO transactions (id_compte, id_compte_dest, type_operation, montant, date_operation, libelle, canal)
SELECT
    src,
    CASE WHEN op = 'virement' THEN 1 + ((src + g) % 350) ELSE NULL END,
    op,
    round((1000 + random() * 750000)::numeric, 2),
    NOW() - ((random() * 730)::int || ' days')::interval
         - ((random() * 86400)::int || ' seconds')::interval,
    (ARRAY['Achat supermarché','Paiement facture CIE','Recharge mobile',
           'Retrait GAB','Dépôt espèces','Virement loyer','Salaire',
           'Paiement scolarité','Achat carburant','Transfert famille'])[1 + (g % 10)],
    (ARRAY['mobile','mobile','agence','gab','web'])[1 + (g % 5)]
FROM (
    SELECT
        g,
        1 + floor(random() * 350)::int AS src,
        (ARRAY['depot','retrait','virement','paiement','paiement','frais'])[1 + (g % 6)] AS op
    FROM generate_series(1, 8000) AS g
) t;


-- ============================================================================
--  9. PRETS (150 lignes)
-- ============================================================================
INSERT INTO prets (id_client, id_conseiller, montant, taux, duree_mois, date_octroi, statut)
SELECT
    1 + floor(random() * 250)::int,
    1 + floor(random() * 60)::int,
    round((500000 + random() * 25000000)::numeric, -3),
    round((4 + random() * 11)::numeric, 2),               -- taux 4 % à 15 %
    (ARRAY[12, 24, 36, 48, 60, 84, 120])[1 + (g % 7)],
    DATE '2021-01-01' + (random() * 1500)::int,
    (ARRAY['en_cours','en_cours','en_cours','solde','en_defaut'])[1 + (g % 5)]
FROM generate_series(1, 150) AS g;


-- ============================================================================
--  10. REMBOURSEMENTS (échéances — jusqu'à 12 par prêt)
-- ============================================================================
INSERT INTO remboursements (id_pret, numero_echeance, montant_echeance, date_echeance, date_paiement, statut)
SELECT
    p.id_pret,
    e.numero,
    round((p.montant * (1 + p.taux/100) / p.duree_mois)::numeric, 2),
    p.date_octroi + (e.numero || ' months')::interval,
    CASE WHEN random() < 0.7
         THEN (p.date_octroi + (e.numero || ' months')::interval)::date + (random() * 5)::int
         ELSE NULL END,
    (ARRAY['paye','paye','paye','a_payer','retard'])[1 + (e.numero % 5)]
FROM prets p
CROSS JOIN LATERAL generate_series(1, LEAST(p.duree_mois, 12)) AS e(numero);


-- ============================================================================
--  Récapitulatif des volumes insérés
-- ============================================================================
DO $$
DECLARE r RECORD;
BEGIN
    RAISE NOTICE '✅ Données insérées :';
    FOR r IN
        SELECT 'agences' t, count(*) n FROM agences UNION ALL
        SELECT 'types_compte', count(*) FROM types_compte UNION ALL
        SELECT 'employes', count(*) FROM employes UNION ALL
        SELECT 'clients', count(*) FROM clients UNION ALL
        SELECT 'comptes', count(*) FROM comptes UNION ALL
        SELECT 'cartes', count(*) FROM cartes UNION ALL
        SELECT 'beneficiaires', count(*) FROM beneficiaires UNION ALL
        SELECT 'transactions', count(*) FROM transactions UNION ALL
        SELECT 'prets', count(*) FROM prets UNION ALL
        SELECT 'remboursements', count(*) FROM remboursements
    LOOP
        RAISE NOTICE '   • % : % lignes', rpad(r.t, 16), r.n;
    END LOOP;
END $$;
