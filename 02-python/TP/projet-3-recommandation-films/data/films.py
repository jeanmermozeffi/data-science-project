"""
Catalogue de films fictif + historique de visionnage d'un utilisateur.
Chapitre mobilisé : 03-DATA_STRUCTURES (sets, genres = ensembles de tags).
"""

catalogue_films = [
    {"titre": "Abidjan Nights", "genres": {"drame", "romance"}, "note": 7.8, "annee": 2021},
    {"titre": "Le Dernier Baobab", "genres": {"drame", "aventure"}, "note": 8.1, "annee": 2019},
    {"titre": "Sanaga Speed", "genres": {"action", "thriller"}, "note": 7.2, "annee": 2022},
    {"titre": "Rire à Yamoussoukro", "genres": {"comedie", "romance"}, "note": 6.9, "annee": 2020},
    {"titre": "Zone Rouge", "genres": {"action", "guerre"}, "note": 8.4, "annee": 2018},
    {"titre": "La Sorcière de Man", "genres": {"horreur", "thriller"}, "note": 7.0, "annee": 2023},
    {"titre": "Coeur d'Or", "genres": {"romance", "drame"}, "note": 7.5, "annee": 2021},
    {"titre": "Les Génies du Plateau", "genres": {"comedie", "famille"}, "note": 6.5, "annee": 2020},
    {"titre": "Braquage à Treichville", "genres": {"action", "thriller", "comedie"}, "note": 8.0, "annee": 2022},
    {"titre": "L'Appel du Fleuve", "genres": {"aventure", "drame"}, "note": 8.6, "annee": 2017},
    {"titre": "Nuit Blanche à Bouaké", "genres": {"horreur", "action"}, "note": 6.2, "annee": 2019},
    {"titre": "Amour et Cacao", "genres": {"romance", "comedie"}, "note": 7.1, "annee": 2021},
    {"titre": "Les Fils du Griot", "genres": {"drame", "famille"}, "note": 8.3, "annee": 2016},
    {"titre": "Poursuite à San-Pedro", "genres": {"action", "thriller"}, "note": 7.6, "annee": 2023},
    {"titre": "Rêves de Comoé", "genres": {"aventure", "famille"}, "note": 7.9, "annee": 2020},
    {"titre": "Le Rire du Zombie", "genres": {"horreur", "comedie"}, "note": 6.0, "annee": 2022},
    {"titre": "Trahison à Korhogo", "genres": {"thriller", "drame"}, "note": 8.2, "annee": 2018},
    {"titre": "Le Prince de Grand-Bassam", "genres": {"drame", "romance", "aventure"}, "note": 8.5, "annee": 2019},
    {"titre": "Explosifs à Vridi", "genres": {"action", "guerre"}, "note": 7.3, "annee": 2021},
    {"titre": "Vacances à Assinie", "genres": {"comedie", "famille", "romance"}, "note": 6.8, "annee": 2022},
    {"titre": "Le Secret des Lagunes", "genres": {"aventure", "thriller"}, "note": 7.7, "annee": 2020},
    {"titre": "Deuil à Daloa", "genres": {"drame", "guerre"}, "note": 8.0, "annee": 2017},
    {"titre": "Comédie du Marché", "genres": {"comedie"}, "note": 6.4, "annee": 2023},
    {"titre": "Chasse à l'Homme", "genres": {"action", "thriller", "horreur"}, "note": 7.4, "annee": 2021},
    {"titre": "Le Baiser d'Abengourou", "genres": {"romance"}, "note": 7.0, "annee": 2019},
]

# Films déjà vus par l'utilisatrice "Awa" (elle aime clairement le drame/romance/aventure).
historique_awa = ["Abidjan Nights", "Le Dernier Baobab", "Coeur d'Or", "L'Appel du Fleuve"]
