"""
Mini-bibliothèque ML "from scratch" : le classifieur K-Nearest Neighbors.
Chapitre mobilisé : 05-POO (encapsulation d'un algorithme dans une classe).
"""
from analyse import distance_euclidienne


class ModeleKNN:
    """Classifieur K-Nearest Neighbors : prédit par vote majoritaire des k voisins les plus proches."""

    def __init__(self):
        self.donnees_entrainement = []

    def entrainer(self, donnees_entrainement: list) -> None:
        """Le KNN n'a rien à "apprendre" : il mémorise simplement les exemples d'entraînement."""
        self.donnees_entrainement = donnees_entrainement

    def predire(self, nouveau_point: dict, k: int = 3) -> str:
        distances = [
            (distance_euclidienne(nouveau_point, exemple), exemple["categorie"])
            for exemple in self.donnees_entrainement
        ]
        # sorted() avec key=lambda : Chapitre 04
        distances_triees = sorted(distances, key=lambda paire: paire[0])
        k_plus_proches = distances_triees[:k]

        votes = {}
        for _, categorie in k_plus_proches:
            votes[categorie] = votes.get(categorie, 0) + 1

        return max(votes, key=votes.get)  # vote majoritaire

    def evaluer(self, donnees_test: list, k: int = 3) -> float:
        """Accuracy = proportion de prédictions correctes sur le jeu de test."""
        if not donnees_test:
            return 0.0

        predictions_correctes = 0
        for exemple in donnees_test:
            prediction = self.predire(exemple, k)
            if prediction == exemple["categorie"]:
                predictions_correctes += 1

        return predictions_correctes / len(donnees_test)
