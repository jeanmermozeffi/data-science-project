"""
Lexique de sentiment : mot -> score (+ = positif, - = négatif).
Chapitre mobilisé : 03-DATA_STRUCTURES (dictionnaire).
"""

LEXIQUE = {
    # positifs forts
    "excellent": 2, "parfait": 2, "génial": 2, "incroyable": 2, "top": 2,
    "parfaitement": 2, "impeccable": 2, "adore": 2, "magnifique": 2,
    # positifs modérés
    "bien": 1, "correct": 1, "satisfait": 1, "rapide": 1, "agréable": 1,
    "recommande": 1, "fiable": 1, "sérieux": 1, "professionnel": 1, "attentionné": 1,
    # négatifs forts
    "nul": -2, "horrible": -2, "catastrophique": -2, "mauvais": -2,
    "arnaque": -2, "défectueux": -2, "lamentable": -2,
    # négatifs modérés
    "déçu": -1, "lent": -1, "médiocre": -1, "cher": -1, "problème": -1,
    "erreur": -1, "inutile": -1, "regrette": -1, "terrible": -1,
}

# Mots qui inversent le score du mot suivant (négation).
NEGATIONS = {"pas", "jamais", "aucun", "aucune"}

SEUIL_POSITIF = 1
SEUIL_NEGATIF = -1
