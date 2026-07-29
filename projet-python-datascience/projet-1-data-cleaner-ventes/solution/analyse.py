"""
Statistiques calculées "from scratch" (sans statistics/numpy).
Chapitre mobilisé : 04-FONCTIONS (fonctions réutilisables de calcul).
"""


def moyenne(valeurs: list) -> float:
    if not valeurs:
        return 0.0
    return sum(valeurs) / len(valeurs)


def mediane(valeurs: list) -> float:
    if not valeurs:
        return 0.0
    valeurs_triees = sorted(valeurs)
    n = len(valeurs_triees)
    milieu = n // 2
    if n % 2 == 1:
        return valeurs_triees[milieu]
    return (valeurs_triees[milieu - 1] + valeurs_triees[milieu]) / 2


def ecart_type(valeurs: list) -> float:
    if len(valeurs) < 2:
        return 0.0
    m = moyenne(valeurs)
    variance = sum((x - m) ** 2 for x in valeurs) / len(valeurs)
    return variance ** 0.5
