"""
Point d'entrée du projet 1 — Data Cleaner & Analyzer.
Lancer avec :  python3 main.py   (depuis le dossier solution/)
"""
import sys
from pathlib import Path

# Permet d'importer data/ventes_brutes.py qui se trouve dans le dossier parent.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.ventes_brutes import ventes_brutes, SEUIL_CLIENT_VIP
from nettoyage import nettoyer_ventes, est_vente_valide
from modeles import Vente, CatalogueVentes
from analyse import moyenne, mediane, ecart_type


def saisir_vente() -> Vente:
    """Demande interactivement les champs d'une vente à l'utilisateur."""
    print("\n--- Saisie d'une nouvelle vente ---")
    produit = input("Produit : ").strip()

    while True:
        try:
            quantite = int(input("Quantité : ").strip())
            break
        except ValueError:
            print("  -> Veuillez entrer un nombre entier.")

    while True:
        try:
            prix_unitaire = float(input("Prix unitaire (FCFA) : ").strip())
            break
        except ValueError:
            print("  -> Veuillez entrer un nombre.")

    client = input("Client : ").strip()
    date = input("Date (AAAA-MM-JJ), laissez vide pour aujourd'hui : ").strip() or "2026-07-24"

    return Vente(produit, quantite, prix_unitaire, date, client)


def mode_interactif(catalogue: CatalogueVentes, seuil_vip: float) -> None:
    """Boucle de test manuel : l'utilisateur saisit ses propres ventes et voit le résultat."""
    print("\n" + "=" * 50)
    print("MODE INTERACTIF — testez avec vos propres ventes")
    print("=" * 50)

    while True:
        try:
            reponse = input("\nSaisir une nouvelle vente ? (o/n, Entrée pour quitter) : ").strip().lower()
        except EOFError:
            print("\n(Aucune entrée disponible — mode interactif ignoré.)")
            return

        if reponse != "o":
            print("Fin du mode interactif. À bientôt !")
            return

        vente = saisir_vente()

        if not est_vente_valide(vente.__dict__):
            print("  ⚠️  Cette vente serait rejetée par le nettoyage (produit vide, quantité ou prix <= 0).")
            continue

        print(f"\n-> Total de cette vente : {vente.total:,.0f} FCFA".replace(",", " "))

        clients = catalogue.construire_clients(seuil_vip)
        total_existant = clients[vente.client].total_achats if vente.client in clients else 0
        nouveau_total = total_existant + vente.total
        statut = "VIP" if nouveau_total >= seuil_vip else "standard"
        print(f"-> Cumul de {vente.client} après cette vente : "
              f"{nouveau_total:,.0f} FCFA -> statut {statut}".replace(",", " "))


def main():
    print(f"Ventes brutes chargées : {len(ventes_brutes)} lignes\n")

    ventes_propres, nb_doublons, nb_invalides = nettoyer_ventes(ventes_brutes)
    print("-- Étape de nettoyage --")
    print(f"Doublons supprimés          : {nb_doublons}")
    print(f"Lignes invalides supprimées : {nb_invalides}")
    print(f"Ventes propres restantes    : {len(ventes_propres)}\n")

    objets_ventes = [Vente(**v) for v in ventes_propres]
    catalogue = CatalogueVentes(objets_ventes)

    print(catalogue.rapport(SEUIL_CLIENT_VIP))

    totaux = [v.total for v in objets_ventes]
    print("\n-- Statistiques sur le montant des ventes (calculées from scratch) --")
    print(f"Moyenne     : {moyenne(totaux):,.0f} FCFA".replace(",", " "))
    print(f"Médiane     : {mediane(totaux):,.0f} FCFA".replace(",", " "))
    print(f"Écart-type  : {ecart_type(totaux):,.0f} FCFA".replace(",", " "))

    mode_interactif(catalogue, SEUIL_CLIENT_VIP)


if __name__ == "__main__":
    main()
