"""
Nettoyage et tokenisation d'un texte libre.
Chapitre mobilisé : 04-FONCTIONS (map/filter).
"""
import string
import unicodedata


def enlever_accents(mot: str) -> str:
    """Ex: 'décu' -> 'decu'. Non utilisé par défaut (le lexique garde les accents),
    utile si vous voulez rendre l'analyse insensible aux accents."""
    normalise = unicodedata.normalize("NFD", mot)
    return "".join(c for c in normalise if unicodedata.category(c) != "Mn")


def nettoyer_texte(texte: str) -> list:
    """
    Minuscule -> découpage en mots -> suppression de la ponctuation -> suppression des mots vides.
    Retourne une liste de tokens (mots).
    """
    texte_minuscule = texte.lower()
    mots_bruts = texte_minuscule.split()

    # map() : retire la ponctuation en début/fin de chaque mot (Chapitre 04)
    mots_sans_ponctuation = list(map(lambda mot: mot.strip(string.punctuation), mots_bruts))

    # filter() : élimine les tokens devenus vides après nettoyage (Chapitre 04)
    tokens = list(filter(lambda mot: mot != "", mots_sans_ponctuation))

    return tokens
