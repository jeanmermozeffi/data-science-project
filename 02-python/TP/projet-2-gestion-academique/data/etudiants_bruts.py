"""
Jeu de données — promotion "Data Science Batch 7" (fictive).
Chaque étudiant a des notes par matière, avec un coefficient par matière.
"""

etudiants_bruts = [
    {
        "nom": "Awa Traoré", "type": "normal",
        "notes": {"Python": (16, 3), "Statistiques": (14, 2), "SQL": (17, 2), "Anglais": (13, 1)},
    },
    {
        "nom": "Koffi N'Guessan", "type": "boursier",
        "notes": {"Python": (12, 3), "Statistiques": (9, 2), "SQL": (11, 2), "Anglais": (14, 1)},
    },
    {
        "nom": "Mariam Cissé", "type": "normal",
        "notes": {"Python": (18, 3), "Statistiques": (17, 2), "SQL": (16, 2), "Anglais": (15, 1)},
    },
    {
        "nom": "Yao Kouassi", "type": "redoublant",
        "notes": {"Python": (8, 3), "Statistiques": (7, 2), "SQL": (9, 2), "Anglais": (10, 1)},
    },
    {
        "nom": "Fatou Diabaté", "type": "boursier",
        "notes": {"Python": (15, 3), "Statistiques": (16, 2), "SQL": (14, 2), "Anglais": (12, 1)},
    },
    {
        "nom": "Konan Brou", "type": "normal",
        "notes": {"Python": (10, 3), "Statistiques": (11, 2), "SQL": (9, 2), "Anglais": (13, 1)},
    },
    {
        "nom": "Aminata Sanogo", "type": "boursier",
        "notes": {"Python": (19, 3), "Statistiques": (18, 2), "SQL": (17, 2), "Anglais": (16, 1)},
    },
    {
        "nom": "Ibrahim Ouattara", "type": "redoublant",
        "notes": {"Python": (6, 3), "Statistiques": (8, 2), "SQL": (7, 2), "Anglais": (9, 1)},
    },
    {
        "nom": "Adjoua Kouamé", "type": "normal",
        "notes": {"Python": (13, 3), "Statistiques": (12, 2), "SQL": (13, 2), "Anglais": (11, 1)},
    },
    {
        "nom": "Sekou Camara", "type": "boursier",
        "notes": {"Python": (17, 3), "Statistiques": (15, 2), "SQL": (16, 2), "Anglais": (14, 1)},
    },
    {
        "nom": "Aya Bamba", "type": "normal",
        "notes": {"Python": (11, 3), "Statistiques": (10, 2), "SQL": (12, 2), "Anglais": (12, 1)},
    },
    {
        "nom": "Moussa Kone", "type": "redoublant",
        "notes": {"Python": (9, 3), "Statistiques": (9, 2), "SQL": (8, 2), "Anglais": (10, 1)},
    },
]

# Seuils de bourse (en % du montant plein) selon la moyenne pondérée.
BAREME_BOURSE = [
    (16, 1.0),   # >= 16/20 : bourse complète
    (14, 0.6),   # >= 14/20 : 60% de la bourse
    (12, 0.3),   # >= 12/20 : 30% de la bourse
]
MONTANT_BOURSE_PLEINE = 200_000  # FCFA/mois
