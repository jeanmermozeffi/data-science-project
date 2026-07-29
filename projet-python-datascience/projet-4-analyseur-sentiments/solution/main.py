"""
Point d'entrée du projet 4 — Analyseur de sentiments.
Lancer avec :  python3 main.py   (depuis le dossier solution/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.avis_clients import avis_clients
from data.lexique import LEXIQUE, NEGATIONS, SEUIL_POSITIF, SEUIL_NEGATIF
from modeles import Avis, AnalyseurSentiment


def mode_interactif(analyseur: AnalyseurSentiment) -> None:
    """Boucle de test manuel : l'utilisateur écrit un avis et voit le sentiment détecté."""
    print("\n" + "=" * 55)
    print("MODE INTERACTIF — testez avec votre propre avis")
    print("=" * 55)

    while True:
        try:
            reponse = input("\nSaisir un avis à analyser ? (o/n, Entrée pour quitter) : ").strip().lower()
        except EOFError:
            print("\n(Aucune entrée disponible — mode interactif ignoré.)")
            return

        if reponse != "o":
            print("Fin du mode interactif. À bientôt !")
            return

        texte = input("Votre avis (en français) : ").strip()
        if not texte:
            print("  ⚠️  Avis vide, réessayez.")
            continue

        avis_test = Avis(texte, client="Vous", note_etoiles=0)
        score = analyseur.score(avis_test)
        sentiment = analyseur.classifier(avis_test)

        mots_reconnus = [mot for mot in avis_test.tokens if mot in analyseur.lexique]

        print(f"\n  Tokens             : {avis_test.tokens}")
        print(f"  Mots du lexique trouvés : {mots_reconnus if mots_reconnus else '(aucun)'}")
        print(f"  Score total        : {score:+d}")
        print(f"  Sentiment détecté  : {sentiment}")


def main():
    avis_liste = [Avis(**a) for a in avis_clients]
    analyseur = AnalyseurSentiment(LEXIQUE, NEGATIONS, SEUIL_POSITIF, SEUIL_NEGATIF)

    print(analyseur.rapport(avis_liste))

    print("\n-- Détail avis par avis --")
    for avis in avis_liste:
        print(f"  [{analyseur.classifier(avis):<8}] score={analyseur.score(avis):+d}  "
              f"{avis.note_etoiles}★  {avis.client:<8} : {avis.texte}")

    mode_interactif(analyseur)


if __name__ == "__main__":
    main()
