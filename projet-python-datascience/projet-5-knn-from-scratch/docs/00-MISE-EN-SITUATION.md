# 🌸 Mise en situation — Projet 5 : Mini-bibliothèque ML "from scratch"

## Le contexte, en une phrase

Avant d'utiliser `scikit-learn` dans les prochains modules, le bootcamp vous met au défi : *"Codez vous-même, sans aucune bibliothèque de Machine Learning, un algorithme capable de reconnaître une fleur à partir de ses mesures."* C'est le projet le plus avancé du TP — le pont direct vers le module ML à venir.

## Le principe du KNN (K plus proches voisins), en une image

Imaginez que vous recevez une nouvelle fleur, sans savoir son espèce, mais vous connaissez ses 3 mesures (longueur du sépale, longueur et largeur du pétale). L'idée du KNN est terriblement simple :

> "Regarde les `k` fleurs déjà connues qui **ressemblent le plus** (au sens de la distance) à cette nouvelle fleur, et devine son espèce par **vote majoritaire** parmi elles."

Si `k=3` et que parmi les 3 fleurs les plus proches il y a 2 "Hibiscus" et 1 "Frangipanier", le modèle prédit "Hibiscus".

## "Ressembler", ça veut dire quoi mathématiquement ?

La **distance euclidienne**, la même formule que le théorème de Pythagore généralisé à plusieurs dimensions :

```
distance(A, B) = √( (A.sepale - B.sepale)² + (A.petale_long - B.petale_long)² + (A.petale_larg - B.petale_larg)² )
```

Plus la distance est petite, plus les deux fleurs se ressemblent.

## Pourquoi séparer "entraînement" et "test" ?

Si vous évaluez votre modèle sur les données qu'il connaît déjà par cœur, il aura toujours 100% de bonnes réponses — ça ne prouve rien. Le seul test honnête est de **cacher une partie des données** (20% ici) pendant l'entraînement, puis de vérifier si le modèle devine juste sur ces exemples qu'il n'a **jamais vus**. C'est exactement ce que fait `train_test_split()`.

## Ce que vous allez construire

```
dataset_fleurs.py  →  train_test_split()  →  ModeleKNN.entrainer()  →  ModeleKNN.predire() / evaluer()
   (60 fleurs)        (48 entraînement,        (mémorise les            (vote des k plus proches +
                        12 test)                exemples)                calcul de l'accuracy)
```

## Comment lire ce dossier

1. Essayez d'abord de coder votre version (cahier des charges : projet 5 dans `Python/06-PYTHON_TP_PROJET_FINAL.md`). C'est le projet le plus exigeant : ne passez au corrigé qu'après avoir vraiment cherché.
2. Bloqué sur la distance ou le vote majoritaire ? Lisez `01-EXPLICATION-CODE.md`.
3. Comparez avec `solution/`, puis lancez :
   ```bash
   cd solution
   python3 main.py
   ```

## Un résultat à observer et à interpréter

En lançant le corrigé, vous verrez quelque chose comme :
```
k=1 -> accuracy = 100.00%
k=3 -> accuracy = 91.67%
k=5 -> accuracy = 100.00%
k=7 -> accuracy = 100.00%
```
**Pourquoi `k=3` est-il moins bon que ses voisins `k=1` et `k=5` ?** Parce qu'avec seulement 12 exemples de test, une seule erreur de prédiction fait déjà chuter l'accuracy de 8,3 points. Ce n'est pas une règle générale ("plus petit k = pire") : c'est le rappel que sur un **petit jeu de données**, le choix de `k` (un **hyperparamètre**) peut être sensible au hasard du découpage train/test. C'est une vraie question de Machine Learning que vous recroiserez avec des jeux de données bien plus grands.

## Questions à vous poser en codant

- Pourquoi le KNN n'a-t-il "rien à apprendre" pendant `entrainer()` (juste stocker les données) ? En quoi est-ce différent d'un algorithme comme la régression linéaire (que vous verrez plus tard) ?
- Que se passerait-il si deux catégories obtenaient exactement le même nombre de votes (égalité) ? Regardez ce que fait `max(votes, key=votes.get)` dans ce cas précis.
- Pourquoi utilise-t-on une **graine aléatoire fixe** (`graine=42`) dans `train_test_split` plutôt qu'un mélange totalement aléatoire à chaque exécution ?
