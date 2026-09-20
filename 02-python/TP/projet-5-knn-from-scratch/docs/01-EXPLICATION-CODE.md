# 📖 Explication simplifiée du corrigé — Projet 5

## 1. `solution/analyse.py` — les briques mathématiques

### `distance_euclidienne`
```python
somme_carres = sum(
    (point_a[colonne] - point_b[colonne]) ** 2
    for colonne in COLONNES_NUMERIQUES
)
return somme_carres ** 0.5
```
Une compréhension de générateur (Chapitre 03) qui parcourt les 3 colonnes numériques, calcule l'écart au carré pour chacune, additionne le tout, puis prend la racine carrée (`** 0.5`). C'est du Pythagore en 3 dimensions au lieu de 2.

### `train_test_split`
```python
def train_test_split(donnees, ratio=0.8, graine=42):
    donnees_melangees = donnees.copy()
    random.Random(graine).shuffle(donnees_melangees)
    limite = int(len(donnees_melangees) * ratio)
    return donnees_melangees[:limite], donnees_melangees[limite:]
```
- `donnees.copy()` : **très important** — on ne mélange jamais la liste originale en place, sinon on la modifierait de façon invisible pour le reste du programme.
- `random.Random(graine)` crée un générateur aléatoire **indépendant**, initialisé avec une graine fixe : le mélange est aléatoire mais **toujours le même** d'une exécution à l'autre. C'est ce qu'on entend par "reproductible" en data science — indispensable pour comparer deux expériences (ex: k=3 vs k=5) sur exactement le même découpage.
- Le slicing `[:limite]` / `[limite:]` (Chapitre 03) découpe la liste mélangée en deux parties sans chevauchement.

## 2. `solution/modeles.py` — `ModeleKNN`, pas à pas

### `entrainer()` — le KNN "n'apprend" rien
```python
def entrainer(self, donnees_entrainement):
    self.donnees_entrainement = donnees_entrainement
```
Contrairement à la plupart des algorithmes de Machine Learning (qui ajustent des paramètres internes, ex: les coefficients d'une droite en régression linéaire), le KNN est un algorithme **"paresseux"** (*lazy learning*) : il se contente de **mémoriser** tous les exemples. Tout le calcul a lieu au moment de la prédiction.

### `predire()` — les 3 étapes du vote
```python
distances = [(distance_euclidienne(nouveau_point, exemple), exemple["categorie"])
             for exemple in self.donnees_entrainement]
distances_triees = sorted(distances, key=lambda paire: paire[0])
k_plus_proches = distances_triees[:k]
```
1. On calcule la distance entre le nouveau point et **chaque** exemple connu → liste de tuples `(distance, categorie)`.
2. On trie cette liste par distance croissante (`key=lambda paire: paire[0]` prend le premier élément du tuple, la distance).
3. On garde les `k` premiers (les plus proches).

```python
votes = {}
for _, categorie in k_plus_proches:
    votes[categorie] = votes.get(categorie, 0) + 1
return max(votes, key=votes.get)
```
On compte combien de fois chaque catégorie apparaît parmi les k plus proches voisins (`votes.get(categorie, 0) + 1` : pattern classique de comptage vu au Chapitre 03), puis `max(votes, key=votes.get)` retourne la **clé** (la catégorie) dont la **valeur** (le nombre de votes) est la plus grande — c'est le vote majoritaire.

> 💡 En cas d'égalité parfaite entre deux catégories, `max()` retourne la première rencontrée selon l'ordre d'insertion du dictionnaire — ce n'est pas un vrai "hasard contrôlé". Sur un projet réel, on gérerait ce cas explicitement (par exemple en réduisant `k` de 1 jusqu'à lever l'égalité).

### `evaluer()` — mesurer sans tricher
```python
for exemple in donnees_test:
    prediction = self.predire(exemple, k)
    if prediction == exemple["categorie"]:
        predictions_correctes += 1
return predictions_correctes / len(donnees_test)
```
On prédit un par un chaque exemple du jeu de **test** (jamais vu pendant `entrainer()`), on compare à la vraie catégorie connue, et on calcule le pourcentage de bonnes réponses — l'**accuracy**. C'est la métrique la plus simple pour évaluer un classifieur.

## 3. `solution/main.py` — balayer plusieurs valeurs de k

```python
for k in (1, 3, 5, 7):
    accuracy = modele.evaluer(test, k=k)
    if accuracy > meilleure_accuracy:
        meilleur_k, meilleure_accuracy = k, accuracy
```
On teste plusieurs valeurs de l'**hyperparamètre** `k` sur le **même** jeu de test (grâce à la graine fixe de `train_test_split`), et on garde celle qui donne la meilleure accuracy. C'est une version minimaliste de ce qu'on appelle la "recherche d'hyperparamètres" (*hyperparameter tuning*) en Machine Learning — vous en reverrez des versions bien plus sophistiquées (`GridSearchCV` de scikit-learn, par exemple) dans les modules suivants.
