# 📖 Explication simplifiée du corrigé — Projet 1

> Objectif de ce document : comprendre **pourquoi** le code est écrit ainsi, pas seulement **ce qu'il fait**. Le code est dans `solution/`.

## 1. `data/ventes_brutes.py` — les données de départ

Une simple **liste de dictionnaires** (Chapitre 03). Chaque dictionnaire = une ligne de vente telle qu'elle sortirait d'un vieux logiciel de caisse. On y a glissé volontairement des erreurs pour avoir un vrai cas de nettoyage.

## 2. `solution/nettoyage.py` — filtrer avant d'analyser

### `est_vente_valide(vente)`
```python
def est_vente_valide(vente: dict) -> bool:
    produit = vente.get("produit", "").strip()
    ...
```
C'est une **fonction pure** : elle prend une vente, répond `True` ou `False`, sans rien modifier. On l'utilise avec `filter()` juste après — c'est le rôle exact de `filter()` vu au Chapitre 04 : garder uniquement les éléments qui respectent une condition.

### `dedupliquer(ventes)`
On construit une **clé unique** par vente (`cle_doublon`) — un tuple des 5 champs. Un `set` retient les clés déjà vues : si la clé existe déjà, la ligne est un doublon, on l'ignore. C'est le même principe que "supprimer les doublons d'une liste" vu au Chapitre 03 (section Sets), mais appliqué à des dictionnaires (qui eux ne sont pas hashables directement, d'où le tuple).

### Pourquoi dédoublonner **avant** de filtrer les invalides ?
Parce qu'un doublon peut aussi être invalide (ex: deux fois la même ligne à quantité négative). Peu importe l'ordre ici puisque les deux opérations sont indépendantes — mais dédoublonner en premier permet d'afficher un compteur de doublons non biaisé par le nettoyage des invalides.

## 3. `solution/modeles.py` — la partie POO (Chapitre 05)

### `Vente`
Une classe très simple : un `__init__` qui stocke les champs, et une **property** `total` (`quantite * prix_unitaire`) calculée à la demande plutôt que stockée — ça évite les incohérences si jamais `quantite` change après coup.

### `Client` et `ClientVIP` — le cœur de la POO du projet

```python
class Client:
    def __init__(self, nom):
        self.nom = nom
        self._total_achats = 0        # "protégé" par convention (underscore)

    def enregistrer_achat(self, montant):
        self._total_achats += montant  # seule façon officielle de modifier le total

    def statut(self):
        return "standard"
```

C'est de l'**encapsulation** : on ne touche jamais `_total_achats` directement depuis l'extérieur, on passe toujours par `enregistrer_achat()`. Si demain on veut logger chaque achat, on modifie une seule méthode, pas tout le code appelant.

```python
class ClientVIP(Client):
    def statut(self):
        return "VIP"
```

`ClientVIP` **hérite** de `Client` (il récupère `enregistrer_achat`, `total_achats`, `__init__` gratuitement) et **redéfinit uniquement** `statut()`. C'est le **polymorphisme** : dans `CatalogueVentes.rapport()`, on appelle `client.statut()` sans savoir si c'est un `Client` ou un `ClientVIP` — chacun répond avec son propre comportement.

> 💡 On aurait pu ajouter un `if total > seuil: statut = "VIP" else: "standard"` dans une seule classe `Client`. Ça marche aussi, mais ce n'est plus de la POO : dès qu'on ajoute un 3ᵉ statut (ex: `ClientBanni`), le `if/elif/else` grossit partout où on l'utilise, alors qu'avec l'héritage on ajoute juste une nouvelle classe.

### `CatalogueVentes`
La classe "chef d'orchestre" : elle reçoit la liste de `Vente` déjà propres et expose des méthodes de haut niveau (`chiffre_affaires_total`, `top_clients`, `rapport`...). Remarquez `construire_clients()` : c'est là que la décision `Client` vs `ClientVIP` est prise, **une seule fois**, au moment de la construction.

```python
return sorted(clients.values(), key=lambda c: c.total_achats, reverse=True)[:n]
```
`lambda c: c.total_achats` dit à `sorted()` : "trie ces objets en te basant sur leur `total_achats`". C'est l'usage typique de `lambda` vu au Chapitre 04 — une fonction jetable, utilisée une seule fois, pas besoin de la nommer avec `def`.

## 4. `solution/analyse.py` — les stats "from scratch"

Le TP interdit `statistics.mean()`. On récrit donc :
- `moyenne` : somme divisée par le nombre d'éléments (basique) ;
- `mediane` : on trie, puis on prend le milieu (ou la moyenne des deux valeurs du milieu si nombre pair) ;
- `ecart_type` : on calcule d'abord la **variance** (moyenne des carrés des écarts à la moyenne), puis sa racine carrée.

C'est la même formule que vous utiliserez plus tard avec `numpy.std()` — sauf qu'ici vous voyez ce qu'il y a "dans la boîte".

## 5. `solution/main.py` — l'orchestration

Le fichier fait exactement 4 choses, dans l'ordre : charger, nettoyer, transformer en objets, afficher. C'est un bon réflexe à garder pour tous vos futurs scripts data : **séparer clairement chargement / nettoyage / logique métier / restitution**, plutôt que tout mélanger dans un seul bloc.
