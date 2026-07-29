"""
Point d'entrée du projet 5 — Mini-bibliothèque ML KNN "from scratch".
Lancer avec :  python3 main.py   (depuis le dossier solution/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.dataset_fleurs import dataset_fleurs
from modeles import ModeleKNN
from analyse import train_test_split


def main():
    entrainement, test = train_test_split(dataset_fleurs, ratio=0.8)
    print(f"Jeu d'entraînement : {len(entrainement)} exemples")
    print(f"Jeu de test         : {len(test)} exemples\n")

    modele = ModeleKNN()
    modele.entrainer(entrainement)

    print("-- Recherche du meilleur k --")
    meilleur_k, meilleure_accuracy = None, -1
    for k in (1, 3, 5, 7):
        accuracy = modele.evaluer(test, k=k)
        print(f"  k={k} -> accuracy = {accuracy:.2%}")
        if accuracy > meilleure_accuracy:
            meilleur_k, meilleure_accuracy = k, accuracy

    print(f"\nMeilleur k trouvé : {meilleur_k} (accuracy = {meilleure_accuracy:.2%})")

    print("\n-- Prédiction sur une nouvelle fleur inconnue --")
    nouvelle_fleur = {"longueur_sepale": 6.4, "longueur_petale": 4.9, "largeur_petale": 3.0}
    prediction = modele.predire(nouvelle_fleur, k=meilleur_k)
    print(f"  Mesures  : {nouvelle_fleur}")
    print(f"  Prédiction ({meilleur_k}-NN) : {prediction}")

    mode_interactif(modele, meilleur_k)


def saisir_mesures() -> dict:
    """Demande interactivement les 3 mesures d'une fleur inconnue."""
    mesures = {}
    for colonne in ("longueur_sepale", "longueur_petale", "largeur_petale"):
        while True:
            try:
                mesures[colonne] = float(input(f"{colonne.replace('_', ' ')} (cm) : ").strip())
                break
            except ValueError:
                print("  -> Veuillez entrer un nombre.")
    return mesures


def mode_interactif(modele: ModeleKNN, meilleur_k: int) -> None:
    """Boucle de test manuel : l'utilisateur saisit une fleur et voit la prédiction du modèle."""
    print("\n" + "=" * 55)
    print("MODE INTERACTIF — testez avec votre propre fleur")
    print("=" * 55)

    while True:
        try:
            reponse = input("\nSaisir une nouvelle fleur ? (o/n, Entrée pour quitter) : ").strip().lower()
        except EOFError:
            print("\n(Aucune entrée disponible — mode interactif ignoré.)")
            return

        if reponse != "o":
            print("Fin du mode interactif. À bientôt !")
            return

        mesures = saisir_mesures()

        while True:
            try:
                k_saisi = input(f"Valeur de k (Entrée = {meilleur_k}) : ").strip()
                k = int(k_saisi) if k_saisi else meilleur_k
                break
            except ValueError:
                print("  -> Veuillez entrer un nombre entier.")

        prediction = modele.predire(mesures, k=k)
        print(f"\n-> Prédiction ({k}-NN) : {prediction}")


if __name__ == "__main__":
    main()
