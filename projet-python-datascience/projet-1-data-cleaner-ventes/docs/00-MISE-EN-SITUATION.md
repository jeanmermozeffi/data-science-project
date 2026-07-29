# 🛒 Mise en situation — Projet 1 : Data Cleaner & Analyzer

## Le contexte, en une phrase

Vous êtes recruté comme **stagiaire data** chez **CI-Shop**, une petite boutique en ligne fictive. Le gérant vous envoie un export brut de ses ventes du mois et vous demande : *"Peux-tu me dire combien j'ai vendu, quels sont mes meilleurs clients, et pourquoi mes chiffres semblent faux ?"*

## Pourquoi ses chiffres semblent faux

En ouvrant le fichier, vous remarquez immédiatement des problèmes (regardez `data/ventes_brutes.py`) :

| Problème | Exemple dans les données | Conséquence si on ne le corrige pas |
|---|---|---|
| Doublon exact | La vente "Clavier / Awa / 2026-01-05" apparaît deux fois | Le chiffre d'affaires est gonflé artificiellement |
| Quantité négative | `"quantite": -1` pour une souris | Un retour produit mal enregistré, fausse les totaux |
| Prix manquant | `"prix_unitaire": None` | Impossible de calculer un total, plante un calcul naïf |
| Produit vide | `"produit": ""` | Une ligne inexploitable, à exclure |

**C'est exactement le travail n°1 d'un data analyst** : ne jamais faire confiance aux données brutes. On nettoie **avant** d'analyser.

## Ce que vous allez construire

Un petit pipeline en 3 étapes, comme dans un vrai projet data :

```
ventes_brutes.py  →  nettoyage.py  →  modeles.py (Vente, Client, CatalogueVentes)  →  rapport final
   (données sales)      (filtre)           (objets métier + calculs)                  (texte lisible)
```

## Comment lire ce dossier

1. **Essayez d'abord seul** : reprenez le cahier des charges du projet 1 dans `Python/06-PYTHON_TP_PROJET_FINAL.md`, et codez votre propre version dans un dossier séparé.
2. **Bloqué ?** Lisez `01-EXPLICATION-CODE.md` : chaque classe et chaque fonction du corrigé y est expliquée simplement, avec le "pourquoi".
3. **Ensuite seulement**, ouvrez le code dans `solution/` et comparez avec votre propre logique — il n'y a pas qu'une seule bonne façon de faire.
4. Lancez le corrigé pour voir le résultat attendu :
   ```bash
   cd solution
   python3 main.py
   ```

## Les questions à vous poser en codant

- Si je supprime les doublons **après** avoir filtré les ventes invalides, est-ce que ça change le résultat ? (Réponse dans l'explication de code.)
- Pourquoi calcule-t-on le statut VIP **après** nettoyage et pas avant ?
- Que se passerait-il si un `Client` pouvait directement modifier `_total_achats` de l'extérieur, sans passer par `enregistrer_achat()` ? Quel principe de la POO ça viole ?
