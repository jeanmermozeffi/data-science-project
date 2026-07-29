"""
Calcul du score de sentiment, avec gestion récursive de la négation.
Chapitre mobilisé : 04-FONCTIONS (récursivité, bonus).
"""


def calculer_score(tokens: list, lexique: dict, negations: set) -> int:
    """
    Parcourt la liste de tokens récursivement.
    Si un mot de négation est suivi d'un mot du lexique, on INVERSE son score.
    Ex: ["jamais", "recommande"] -> -1 au lieu de +1.
    """
    if not tokens:
        return 0  # cas de base de la récursion : plus rien à lire

    mot = tokens[0]
    reste = tokens[1:]

    if mot in negations and reste:
        mot_suivant = reste[0]
        score_inverse = -lexique.get(mot_suivant, 0)
        # on saute le mot de négation ET le mot déjà traité (reste[1:])
        return score_inverse + calculer_score(reste[1:], lexique, negations)

    return lexique.get(mot, 0) + calculer_score(reste, lexique, negations)


def mots_les_plus_frequents(liste_tokens: list, top_n: int = 10) -> list:
    """Compte les occurrences de mots (liste de listes de tokens) et retourne le top N."""
    frequences = {}
    for tokens in liste_tokens:
        for mot in tokens:
            frequences[mot] = frequences.get(mot, 0) + 1

    # sorted + lambda : Chapitre 04
    tries = sorted(frequences.items(), key=lambda paire: paire[1], reverse=True)
    return tries[:top_n]
