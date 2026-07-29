"""
Fonctions de nettoyage et de validation des ventes brutes.
Chapitre mobilisé : 04-FONCTIONS (fonctions pures, lambda/filter).
"""


def est_vente_valide(vente: dict) -> bool:
    """Une vente est valide si : produit non vide, quantité > 0, prix renseigné et > 0."""
    produit = vente.get("produit", "").strip()
    quantite = vente.get("quantite")
    prix = vente.get("prix_unitaire")

    if not produit:
        return False
    if quantite is None or quantite <= 0:
        return False
    if prix is None or prix <= 0:
        return False
    return True


def cle_doublon(vente: dict) -> tuple:
    """Clé d'identité d'une vente, utilisée pour détecter les doublons exacts."""
    return (vente["produit"], vente["quantite"], vente["prix_unitaire"], vente["date"], vente["client"])


def dedupliquer(ventes: list) -> list:
    """Supprime les doublons exacts en conservant l'ordre d'apparition."""
    vues = set()
    resultat = []
    for vente in ventes:
        cle = cle_doublon(vente)
        if cle not in vues:
            vues.add(cle)
            resultat.append(vente)
    return resultat


def nettoyer_ventes(ventes_brutes: list) -> tuple:
    """
    Pipeline de nettoyage : dédoublonnage puis filtrage des lignes invalides.
    Retourne (ventes_propres, nb_doublons_supprimes, nb_invalides_supprimees).
    """
    sans_doublons = dedupliquer(ventes_brutes)
    nb_doublons = len(ventes_brutes) - len(sans_doublons)

    # filter() : Chapitre 04, section Fonctions et Data Science
    ventes_propres = list(filter(est_vente_valide, sans_doublons))
    nb_invalides = len(sans_doublons) - len(ventes_propres)

    return ventes_propres, nb_doublons, nb_invalides
