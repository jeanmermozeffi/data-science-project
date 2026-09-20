"""
Classes du domaine "recommandation de films".
Chapitre mobilisé : 05-POO + 03-DATA_STRUCTURES (sets).
"""
from analyse import similarite_jaccard, normaliser_note


class Film:
    def __init__(self, titre: str, genres: set, note: float, annee: int):
        self.titre = titre
        self.genres = set(genres)
        self.note = note
        self.annee = annee

    def __repr__(self):
        return f"Film({self.titre}, genres={self.genres}, note={self.note})"

    def __eq__(self, other):
        return isinstance(other, Film) and self.titre == other.titre


class Utilisateur:
    def __init__(self, nom: str, films_vus: list):
        self.nom = nom
        self.films_vus = films_vus

    def genres_preferes(self) -> set:
        """Union de tous les genres des films déjà vus par l'utilisateur."""
        preferes = set()
        for film in self.films_vus:
            preferes |= film.genres  # union ensembliste, Chapitre 03
        return preferes

    def a_vu(self, film: Film) -> bool:
        return any(f.titre == film.titre for f in self.films_vus)


class Recommandeur:
    """Recommande des films non vus, par similarité de genres avec les goûts de l'utilisateur."""

    def __init__(self, catalogue: list):
        self.catalogue = catalogue

    def films_non_vus(self, utilisateur: Utilisateur) -> list:
        return [f for f in self.catalogue if not utilisateur.a_vu(f)]

    def recommander(self, utilisateur: Utilisateur, n: int = 5) -> list:
        """Tri par similarité de Jaccard (goûts vs genres du film), puis par note en cas d'égalité."""
        genres_utilisateur = utilisateur.genres_preferes()
        candidats = self.films_non_vus(utilisateur)

        # lambda + sorted() : Chapitre 04
        candidats_tries = sorted(
            candidats,
            key=lambda film: (similarite_jaccard(genres_utilisateur, film.genres), film.note),
            reverse=True,
        )
        return candidats_tries[:n]

    def recommander_pondere(self, utilisateur: Utilisateur, n: int = 5,
                             poids_similarite: float = 0.7, poids_note: float = 0.3) -> list:
        """Bonus : score combiné = similarité pondérée + note normalisée pondérée."""
        genres_utilisateur = utilisateur.genres_preferes()
        candidats = self.films_non_vus(utilisateur)

        def score(film: Film) -> float:
            sim = similarite_jaccard(genres_utilisateur, film.genres)
            note_norm = normaliser_note(film.note)
            return poids_similarite * sim + poids_note * note_norm

        candidats_tries = sorted(candidats, key=score, reverse=True)
        return candidats_tries[:n]
