"""
Classes du domaine "ventes".
Chapitre mobilisé : 05-POO (encapsulation, héritage, polymorphisme).
"""


class Vente:
    """Une ligne de vente unique et déjà validée."""

    def __init__(self, produit: str, quantite: int, prix_unitaire: float, date: str, client: str):
        self.produit = produit
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
        self.date = date
        self.client = client

    @property
    def total(self) -> float:
        return self.quantite * self.prix_unitaire

    @property
    def mois(self) -> str:
        # date au format "AAAA-MM-JJ" -> "AAAA-MM"
        return self.date[:7]

    def __repr__(self):
        return f"Vente({self.produit}, x{self.quantite}, {self.total} FCFA, {self.client})"


class Client:
    """Client standard : encapsule son historique d'achats."""

    def __init__(self, nom: str):
        self.nom = nom
        self._total_achats = 0  # attribut "protégé" : on passe par la méthode dédiée

    def enregistrer_achat(self, montant: float) -> None:
        self._total_achats += montant

    @property
    def total_achats(self) -> float:
        return self._total_achats

    def statut(self) -> str:
        """Méthode polymorphe : redéfinie différemment dans ClientVIP."""
        return "standard"

    def __repr__(self):
        return f"Client({self.nom}, {self.total_achats} FCFA, statut={self.statut()})"


class ClientVIP(Client):
    """Client dont le total d'achats dépasse le seuil VIP : hérite de Client, redéfinit statut()."""

    REDUCTION_FIDELITE = 0.05  # 5% de réduction symbolique sur les futurs achats

    def statut(self) -> str:
        return "VIP"

    def avantage(self) -> str:
        return f"-{int(self.REDUCTION_FIDELITE * 100)}% sur le prochain achat"


class CatalogueVentes:
    """Agrège une liste de Vente et fournit les analyses demandées par le TP."""

    def __init__(self, ventes: list):
        self.ventes = ventes

    def chiffre_affaires_total(self) -> float:
        return sum(v.total for v in self.ventes)

    def produit_plus_vendu(self) -> str:
        quantites_par_produit = {}
        for v in self.ventes:
            quantites_par_produit[v.produit] = quantites_par_produit.get(v.produit, 0) + v.quantite
        return max(quantites_par_produit, key=quantites_par_produit.get)

    def construire_clients(self, seuil_vip: float) -> dict:
        """Reconstruit les objets Client/ClientVIP à partir des ventes (encapsulation + polymorphisme)."""
        totaux = {}
        for v in self.ventes:
            totaux[v.client] = totaux.get(v.client, 0) + v.total

        clients = {}
        for nom, total in totaux.items():
            client = ClientVIP(nom) if total >= seuil_vip else Client(nom)
            client.enregistrer_achat(total)
            clients[nom] = client
        return clients

    def top_clients(self, seuil_vip: float, n: int = 5) -> list:
        clients = self.construire_clients(seuil_vip)
        # lambda + sorted() : Chapitre 04
        return sorted(clients.values(), key=lambda c: c.total_achats, reverse=True)[:n]

    def ventes_par_mois(self) -> dict:
        totaux = {}
        for v in self.ventes:
            totaux[v.mois] = totaux.get(v.mois, 0) + v.total
        return dict(sorted(totaux.items()))

    def panier_moyen(self) -> float:
        if not self.ventes:
            return 0.0
        return self.chiffre_affaires_total() / len(self.ventes)

    def rapport(self, seuil_vip: float) -> str:
        lignes = []
        lignes.append("=" * 50)
        lignes.append("RAPPORT D'ANALYSE — CI-SHOP")
        lignes.append("=" * 50)
        lignes.append(f"Nombre de ventes valides   : {len(self.ventes)}")
        lignes.append(f"Chiffre d'affaires total   : {self.chiffre_affaires_total():,.0f} FCFA".replace(",", " "))
        lignes.append(f"Panier moyen               : {self.panier_moyen():,.0f} FCFA".replace(",", " "))
        lignes.append(f"Produit le plus vendu      : {self.produit_plus_vendu()}")

        lignes.append("\n-- Ventes par mois --")
        for mois, total in self.ventes_par_mois().items():
            lignes.append(f"  {mois} : {total:,.0f} FCFA".replace(",", " "))

        lignes.append("\n-- Top clients --")
        for client in self.top_clients(seuil_vip):
            lignes.append(f"  {client}")

        lignes.append("=" * 50)
        return "\n".join(lignes)
