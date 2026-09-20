"""
Jeu de données brut — export des ventes de la boutique fictive "CI-Shop".
Volontairement sale : doublons, valeurs manquantes, quantités/prix invalides.
"""

ventes_brutes = [
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-01-05", "client": "Awa"},
    {"produit": "Souris", "quantite": -1, "prix_unitaire": 5000, "date": "2026-01-06", "client": "Koffi"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": None, "date": "2026-01-07", "client": "Awa"},
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-01-05", "client": "Awa"},  # doublon exact
    {"produit": "Casque", "quantite": 3, "prix_unitaire": 8000, "date": "2026-01-07", "client": "Mariam"},
    {"produit": "Souris", "quantite": 2, "prix_unitaire": 5000, "date": "2026-01-08", "client": "Koffi"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-01-08", "client": "Yao"},
    {"produit": "Clavier", "quantite": 0, "prix_unitaire": 15000, "date": "2026-01-09", "client": "Fatou"},
    {"produit": "Webcam", "quantite": 1, "prix_unitaire": 12000, "date": "2026-01-09", "client": "Yao"},
    {"produit": "Casque", "quantite": 1, "prix_unitaire": 8000, "date": "2026-01-10", "client": "Awa"},
    {"produit": "Souris", "quantite": 5, "prix_unitaire": 5000, "date": "2026-01-10", "client": "Konan"},
    {"produit": "Ecran", "quantite": 2, "prix_unitaire": 95000, "date": "2026-01-11", "client": "Mariam"},
    {"produit": "Tapis souris", "quantite": 4, "prix_unitaire": 2500, "date": "2026-01-11", "client": "Koffi"},
    {"produit": "Clavier", "quantite": 1, "prix_unitaire": 15000, "date": "2026-01-12", "client": "Yao"},
    {"produit": "Casque", "quantite": 2, "prix_unitaire": None, "date": "2026-01-12", "client": "Konan"},
    {"produit": "Webcam", "quantite": -2, "prix_unitaire": 12000, "date": "2026-01-13", "client": "Fatou"},
    {"produit": "Souris", "quantite": 1, "prix_unitaire": 5000, "date": "2026-01-13", "client": "Awa"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-01-14", "client": "Yao"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-01-14", "client": "Yao"},  # doublon exact
    {"produit": "Clavier", "quantite": 3, "prix_unitaire": 15000, "date": "2026-01-15", "client": "Mariam"},
    {"produit": "Casque", "quantite": 1, "prix_unitaire": 8000, "date": "2026-01-15", "client": "Konan"},
    {"produit": "Tapis souris", "quantite": 2, "prix_unitaire": 2500, "date": "2026-01-16", "client": "Koffi"},
    {"produit": "Webcam", "quantite": 1, "prix_unitaire": 12000, "date": "2026-01-16", "client": "Awa"},
    {"produit": "Souris", "quantite": 3, "prix_unitaire": 5000, "date": "2026-01-17", "client": "Yao"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-01-17", "client": "Fatou"},
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-01-18", "client": "Konan"},
    {"produit": "Casque", "quantite": 4, "prix_unitaire": 8000, "date": "2026-01-18", "client": "Awa"},
    {"produit": "Souris", "quantite": 2, "prix_unitaire": 5000, "date": "2026-01-19", "client": "Mariam"},
    {"produit": "Webcam", "quantite": 1, "prix_unitaire": 12000, "date": "2026-01-19", "client": "Koffi"},
    {"produit": "Ecran", "quantite": 2, "prix_unitaire": 95000, "date": "2026-01-20", "client": "Awa"},
    {"produit": "Clavier", "quantite": 1, "prix_unitaire": 15000, "date": "2026-02-01", "client": "Yao"},
    {"produit": "Casque", "quantite": 2, "prix_unitaire": 8000, "date": "2026-02-01", "client": "Fatou"},
    {"produit": "Souris", "quantite": 1, "prix_unitaire": 5000, "date": "2026-02-02", "client": "Konan"},
    {"produit": "Tapis souris", "quantite": 3, "prix_unitaire": 2500, "date": "2026-02-02", "client": "Awa"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-02-03", "client": "Mariam"},
    {"produit": "Webcam", "quantite": 2, "prix_unitaire": 12000, "date": "2026-02-03", "client": "Yao"},
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-02-04", "client": "Koffi"},
    {"produit": "Casque", "quantite": 1, "prix_unitaire": 8000, "date": "2026-02-04", "client": "Konan"},
    {"produit": "Souris", "quantite": 4, "prix_unitaire": 5000, "date": "2026-02-05", "client": "Awa"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": 95000, "date": "2026-02-05", "client": "Yao"},
    {"produit": "", "quantite": 2, "prix_unitaire": 5000, "date": "2026-02-06", "client": "Fatou"},  # produit vide
    {"produit": "Webcam", "quantite": 1, "prix_unitaire": 12000, "date": "2026-02-06", "client": "Awa"},
    {"produit": "Clavier", "quantite": 1, "prix_unitaire": 15000, "date": "2026-02-07", "client": "Mariam"},
    {"produit": "Casque", "quantite": 3, "prix_unitaire": 8000, "date": "2026-02-07", "client": "Yao"},
    {"produit": "Souris", "quantite": 2, "prix_unitaire": 5000, "date": "2026-02-08", "client": "Konan"},
    {"produit": "Tapis souris", "quantite": 1, "prix_unitaire": 2500, "date": "2026-02-08", "client": "Awa"},
    {"produit": "Ecran", "quantite": 2, "prix_unitaire": 95000, "date": "2026-02-09", "client": "Koffi"},
    {"produit": "Webcam", "quantite": 1, "prix_unitaire": 12000, "date": "2026-02-09", "client": "Fatou"},
    {"produit": "Clavier", "quantite": 3, "prix_unitaire": 15000, "date": "2026-02-10", "client": "Awa"},
    {"produit": "Casque", "quantite": 2, "prix_unitaire": 8000, "date": "2026-02-10", "client": "Mariam"},
]

# Clients considérés VIP si leur montant total d'achats dépasse ce seuil (FCFA).
SEUIL_CLIENT_VIP = 100_000
