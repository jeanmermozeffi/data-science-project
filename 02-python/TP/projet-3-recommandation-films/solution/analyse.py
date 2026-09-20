"""
Calcul de similarité "from scratch".
Chapitre mobilisé : 03-DATA_STRUCTURES (opérations ensemblistes sur les sets).
"""


def similarite_jaccard(set_a: set, set_b: set) -> float:
    """Indice de Jaccard = taille de l'intersection / taille de l'union."""
    if not set_a and not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)


def normaliser_note(note: float, note_min: float = 0.0, note_max: float = 10.0) -> float:
    """Ramène une note (ex: /10) sur une échelle 0-1."""
    if note_max == note_min:
        return 0.0
    return (note - note_min) / (note_max - note_min)
