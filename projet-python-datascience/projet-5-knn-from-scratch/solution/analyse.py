"""
Fonctions mathématiques "from scratch" : distance, split train/test.
Chapitre mobilisé : 04-FONCTIONS.
"""
import random

COLONNES_NUMERIQUES = ["longueur_sepale", "longueur_petale", "largeur_petale"]


def distance_euclidienne(point_a: dict, point_b: dict) -> float:
    """Racine carrée de la somme des carrés des écarts, sur les colonnes numériques."""
    somme_carres = sum(
        (point_a[colonne] - point_b[colonne]) ** 2
        for colonne in COLONNES_NUMERIQUES
    )
    return somme_carres ** 0.5


def train_test_split(donnees: list, ratio: float = 0.8, graine: int = 42) -> tuple:
    """Mélange puis découpe les données en (entrainement, test) selon le ratio donné."""
    donnees_melangees = donnees.copy()
    random.Random(graine).shuffle(donnees_melangees)

    limite = int(len(donnees_melangees) * ratio)
    entrainement = donnees_melangees[:limite]
    test = donnees_melangees[limite:]
    return entrainement, test
