"""
Point d'entrée du projet 2 — Gestion académique.
Lancer avec :  python3 main.py   (depuis le dossier solution/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.etudiants_bruts import etudiants_bruts, BAREME_BOURSE, MONTANT_BOURSE_PLEINE
from modeles import Etudiant, EtudiantBoursier, EtudiantRedoublant, Promotion
from analyse import ecart_type_promotion


def construire_etudiant(donnees: dict):
    """Choisit la bonne classe (polymorphisme) selon le champ 'type' des données brutes."""
    type_etudiant = donnees["type"]
    if type_etudiant == "boursier":
        return EtudiantBoursier(donnees["nom"], donnees["notes"], BAREME_BOURSE, MONTANT_BOURSE_PLEINE)
    if type_etudiant == "redoublant":
        return EtudiantRedoublant(donnees["nom"], donnees["notes"])
    return Etudiant(donnees["nom"], donnees["notes"])


def saisir_notes() -> dict:
    """Demande interactivement une note par matière (coefficients fixés)."""
    matieres_coefs = {"Python": 3, "Statistiques": 2, "SQL": 2, "Anglais": 1}
    notes = {}
    for matiere, coef in matieres_coefs.items():
        while True:
            try:
                note = float(input(f"Note en {matiere} (coef {coef}, /20) : ").strip())
                if not (0 <= note <= 20):
                    print("  -> La note doit être comprise entre 0 et 20.")
                    continue
                notes[matiere] = (note, coef)
                break
            except ValueError:
                print("  -> Veuillez entrer un nombre.")
    return notes


def mode_interactif() -> None:
    """Boucle de test manuel : l'utilisateur saisit un étudiant fictif et voit son bulletin."""
    print("\n" + "=" * 55)
    print("MODE INTERACTIF — testez avec votre propre étudiant")
    print("=" * 55)

    while True:
        try:
            reponse = input("\nSaisir un nouvel étudiant ? (o/n, Entrée pour quitter) : ").strip().lower()
        except EOFError:
            print("\n(Aucune entrée disponible — mode interactif ignoré.)")
            return

        if reponse != "o":
            print("Fin du mode interactif. À bientôt !")
            return

        nom = input("Nom de l'étudiant : ").strip() or "Étudiant test"
        print("Type : 1) normal  2) boursier  3) redoublant")
        type_choisi = input("Votre choix (1/2/3, Entrée = normal) : ").strip()

        notes = saisir_notes()

        if type_choisi == "2":
            etudiant = EtudiantBoursier(nom, notes, BAREME_BOURSE, MONTANT_BOURSE_PLEINE)
        elif type_choisi == "3":
            etudiant = EtudiantRedoublant(nom, notes)
        else:
            etudiant = Etudiant(nom, notes)

        print()
        print(etudiant.bulletin())


def main():
    etudiants = [construire_etudiant(d) for d in etudiants_bruts]
    promotion = Promotion(etudiants)

    print(promotion.rapport())

    print(f"\nÉcart-type des moyennes de la promotion : {ecart_type_promotion(promotion):.2f}")

    print("\n-- Exemple de bulletin détaillé (1er du classement) --")
    print(promotion.classement()[0].bulletin())

    print("\n-- Exemple de bulletin d'un boursier --")
    boursier = next(e for e in etudiants if isinstance(e, EtudiantBoursier))
    print(boursier.bulletin())

    mode_interactif()


if __name__ == "__main__":
    main()
