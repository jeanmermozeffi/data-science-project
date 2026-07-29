"""
Point d'entrée du projet 3 — Moteur de recommandation.
Lancer avec :  python3 main.py   (depuis le dossier solution/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.films import catalogue_films, historique_awa
from modeles import Film, Utilisateur, Recommandeur


def genres_disponibles(films: list) -> set:
    tous_genres = set()
    for film in films:
        tous_genres |= film.genres
    return tous_genres


def mode_interactif(films: list) -> None:
    """Boucle de test manuel : l'utilisateur choisit ses genres préférés et voit ses recommandations."""
    print("\n" + "=" * 55)
    print("MODE INTERACTIF — testez avec vos propres goûts")
    print("=" * 55)

    genres_possibles = sorted(genres_disponibles(films))
    print(f"Genres disponibles : {', '.join(genres_possibles)}")

    while True:
        try:
            reponse = input("\nTester vos propres genres préférés ? (o/n, Entrée pour quitter) : ").strip().lower()
        except EOFError:
            print("\n(Aucune entrée disponible — mode interactif ignoré.)")
            return

        if reponse != "o":
            print("Fin du mode interactif. À bientôt !")
            return

        saisie = input("Vos genres préférés, séparés par des virgules (ex: action,drame) : ").strip()
        genres_saisis = {g.strip().lower() for g in saisie.split(",") if g.strip()}
        genres_valides = genres_saisis & set(genres_possibles)

        if not genres_valides:
            print("  ⚠️  Aucun genre reconnu parmi la liste proposée. Réessayez.")
            continue

        # Utilisateur fictif : un film "virtuel" portant exactement les genres saisis.
        profil_fictif = Film("Vos goûts", genres_valides, note=0, annee=0)
        utilisateur_test = Utilisateur("Vous", [profil_fictif])

        recommandeur = Recommandeur(films)
        print(f"\n-> Genres retenus : {genres_valides}")
        print("-- Vos 5 recommandations --")
        for film in recommandeur.recommander(utilisateur_test, n=5):
            print(f"  {film.titre:<28} genres={film.genres}  note={film.note}")


def main():
    films = [Film(**data) for data in catalogue_films]
    films_par_titre = {f.titre: f for f in films}

    awa = Utilisateur("Awa", [films_par_titre[titre] for titre in historique_awa])

    print(f"Genres préférés d'Awa (déduits de son historique) : {awa.genres_preferes()}\n")

    recommandeur = Recommandeur(films)

    print("-- Top 5 recommandations (similarité de Jaccard puis note) --")
    for film in recommandeur.recommander(awa, n=5):
        print(f"  {film.titre:<28} genres={film.genres}  note={film.note}")

    print("\n-- Top 5 recommandations pondérées (bonus : 70% similarité + 30% note) --")
    for film in recommandeur.recommander_pondere(awa, n=5):
        print(f"  {film.titre:<28} genres={film.genres}  note={film.note}")

    mode_interactif(films)


if __name__ == "__main__":
    main()
