"""
Statistiques "from scratch" appliquées aux moyennes de la promotion.
Chapitre mobilisé : 04-FONCTIONS.
"""


def ecart_type(valeurs: list) -> float:
    if len(valeurs) < 2:
        return 0.0
    m = sum(valeurs) / len(valeurs)
    variance = sum((x - m) ** 2 for x in valeurs) / len(valeurs)
    return variance ** 0.5


def ecart_type_promotion(promotion) -> float:
    moyennes = [e.moyenne_ponderee() for e in promotion.etudiants]
    return ecart_type(moyennes)
