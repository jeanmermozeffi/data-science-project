# 🔢 Numerical and Data Analysis with NumPy — Cours Bootcamp Data Science

> **Module 2 — Data Science | Chapitre 1** | Prérequis : Module Python Pur (Chapitres 1 à 5)

---

## Table des matières

1. [What's NumPy ? — Introduction](#1-whats-numpy--introduction)
2. [Pourquoi NumPy et pas des listes Python ?](#2-pourquoi-numpy-et-pas-des-listes-python-)
3. [NumPy Arrays Creation — Créer des tableaux](#3-numpy-arrays-creation--créer-des-tableaux)
4. [Anatomie d'un tableau NumPy](#4-anatomie-dun-tableau-numpy)
5. [Types de données NumPy (dtype)](#5-types-de-données-numpy-dtype)
6. [Array Reshaping — Remodeler un tableau](#6-array-reshaping--remodeler-un-tableau)
7. [Array Indexing — Accéder aux éléments](#7-array-indexing--accéder-aux-éléments)
8. [Array Slicing — Découper un tableau](#8-array-slicing--découper-un-tableau)
9. [Indexation booléenne et Fancy Indexing](#9-indexation-booléenne-et-fancy-indexing)
10. [NumPy Random — Génération aléatoire](#10-numpy-random--génération-aléatoire)
11. [NumPy Addition/Soustraction et le Broadcasting](#11-numpy-additionsoustraction-et-le-broadcasting)
12. [Fonctions d'agrégation](#12-fonctions-dagrégation)
13. [Some NumPy Functions — Fonctions utiles](#13-some-numpy-functions--fonctions-utiles)
14. [Algèbre linéaire avec NumPy](#14-algèbre-linéaire-avec-numpy)
15. [Conclusion](#15-conclusion)
16. [✅ Point de contrôle — NumPy](#16--point-de-contrôle--numpy)

---

## 1. What's NumPy ? — Introduction

### 📖 Définition

**NumPy** (Numerical Python) est **la bibliothèque fondamentale** du calcul scientifique et numérique en Python. Elle introduit un nouvel objet central, le **`ndarray`** (N-dimensional array), et propose des milliers de fonctions optimisées pour manipuler des données numériques à grande vitesse.

> 💡 **Analogie** : Si Python pur est une **calculatrice de poche**, NumPy est une **calculatrice scientifique industrielle**. Les deux font des calculs, mais NumPy est conçu pour traiter des **millions de nombres simultanément**, à une vitesse que les listes Python classiques ne peuvent pas égaler.

### 1.1 Pourquoi NumPy est-il si important en Data Science ?

```
NUMPY EST LE SOCLE DE TOUT L'ÉCOSYSTÈME DATA SCIENCE PYTHON
│
├── 🐼 Pandas          → construit directement SUR NumPy
├── 📊 Matplotlib       → utilise des tableaux NumPy pour tracer des graphiques
├── 🤖 Scikit-learn     → attend des tableaux NumPy en entrée de ses modèles
├── 🧠 TensorFlow/PyTorch → leurs "tenseurs" s'inspirent directement des ndarray
└── 📐 SciPy            → calcul scientifique avancé, construit sur NumPy
```

> 🔑 **Comprendre NumPy en profondeur, c'est comprendre les fondations sur lesquelles reposent TOUS les autres outils du bootcamp.**

### 1.2 Installer et importer NumPy

```python
# Installation (une seule fois, dans un terminal ou une cellule Colab)
!pip install numpy

# Importation (convention universelle : alias "np")
import numpy as np

print(np.__version__)   # Vérifier la version installée
```

> 💡 **Convention universelle** : Tout le monde importe NumPy avec l'alias `np`. Vous verrez `np.array()`, `np.zeros()`, etc. dans absolument tous les codes Data Science en Python — c'est presque une signature du langage.

---

## 2. Pourquoi NumPy et pas des listes Python ?

### 2.1 La différence de performance

```python
import numpy as np
import time

# Liste Python classique
liste = list(range(1_000_000))

debut = time.time()
liste_carre = [x**2 for x in liste]
print(f"Liste Python : {time.time() - debut:.4f} secondes")

# Tableau NumPy
tableau = np.arange(1_000_000)

debut = time.time()
tableau_carre = tableau ** 2
print(f"Tableau NumPy : {time.time() - debut:.4f} secondes")

# NumPy est généralement 10 à 100 FOIS plus rapide !
```

### 2.2 Pourquoi cette différence ?

```
LISTE PYTHON                          TABLEAU NUMPY (ndarray)
─────────────────                     ─────────────────────────
[1, "texte", 3.14, True]              [1, 2, 3, 4, 5]
    ↓                                      ↓
Types MÉLANGÉS possibles              Type UNIQUE et FIXE (ex: tous des int64)
    ↓                                      ↓
Chaque élément = un objet Python      Données stockées en bloc CONTIGU
  séparé en mémoire, avec               en mémoire (comme un tableau en C)
  overhead (poids supplémentaire)         ↓
    ↓                                 Calculs VECTORISÉS
Boucles Python nécessaires              (opérations exécutées en code C
  (lentes)                              optimisé, pas en boucle Python)
```

> 💡 **Analogie** : Une liste Python, c'est comme une **file de casiers de tailles différentes**, chacun pouvant contenir n'importe quoi — il faut ouvrir chaque casier un par un pour voir ce qu'il contient. Un tableau NumPy, c'est comme une **rangée de casiers identiques, alignés et de même taille** — on peut traiter tous les casiers d'un coup, comme une chaîne de montage.

### 2.3 Vectorisation — Le concept clé

```python
notes = [14, 16, 12, 18, 10]

# ❌ Avec une liste Python — boucle nécessaire
notes_sur_100 = [n * 5 for n in notes]
print(notes_sur_100)   # [70, 80, 60, 90, 50]

# ✅ Avec NumPy — opération VECTORISÉE (pas de boucle explicite)
import numpy as np
notes_np = np.array([14, 16, 12, 18, 10])
notes_sur_100_np = notes_np * 5
print(notes_sur_100_np)   # [70 80 60 90 50]
```

> 🔑 **Vectorisation** = appliquer une opération à **tout un tableau en une seule instruction**, sans écrire de boucle `for` explicite. C'est plus rapide ET plus lisible.

---

## 3. NumPy Arrays Creation — Créer des tableaux

### 3.1 Depuis une liste Python — `np.array()`

```python
import numpy as np

# Tableau 1D (vecteur)
notes = np.array([14, 16, 12, 18, 15])
print(notes)          # [14 16 12 18 15]
print(type(notes))    # <class 'numpy.ndarray'>

# Tableau 2D (matrice) — depuis une liste de listes
ventes = np.array([
    [4, 8, 12],
    [6, 10, 15],
    [5, 7, 9]
])
print(ventes)
```

### 3.2 Tableaux pré-remplis

```python
# Tableau de zéros
zeros = np.zeros(5)
print(zeros)              # [0. 0. 0. 0. 0.]

zeros_2d = np.zeros((3, 4))     # 3 lignes, 4 colonnes
print(zeros_2d)

# Tableau de uns
uns = np.ones((2, 3))
print(uns)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Tableau rempli d'une valeur constante
constante = np.full((2, 2), 7)
print(constante)
# [[7 7]
#  [7 7]]

# Matrice identité (diagonale de 1, utile en algèbre linéaire)
identite = np.eye(3)
print(identite)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### 3.3 Séquences de nombres

```python
# np.arange() — équivalent NumPy de range(), mais retourne un tableau
sequence = np.arange(0, 10, 2)    # début, fin (exclue), pas
print(sequence)   # [0 2 4 6 8]

sequence2 = np.arange(5)          # de 0 à 4
print(sequence2)  # [0 1 2 3 4]

# np.linspace() — génère N valeurs ÉQUIRÉPARTIES entre deux bornes (incluses)
lineaire = np.linspace(0, 1, 5)   # 5 valeurs entre 0 et 1
print(lineaire)   # [0.   0.25 0.5  0.75 1.  ]
```

**Différence arange vs linspace :**

| Fonction | Vous spécifiez | Exemple | Résultat |
|----------|-----------------|---------|----------|
| `np.arange(0, 10, 2)` | Le **pas** entre les valeurs | pas=2 | `[0, 2, 4, 6, 8]` |
| `np.linspace(0, 10, 5)` | Le **nombre** de valeurs voulues | 5 valeurs | `[0, 2.5, 5, 7.5, 10]` |

### 3.4 Tableaux aléatoires (aperçu — détaillé en section 10)

```python
# Tableau de nombres aléatoires entre 0 et 1
alea = np.random.rand(3)
print(alea)   # ex: [0.42 0.71 0.19]
```

### 3.5 Tableau récapitulatif des créations

| Fonction | Description | Exemple |
|----------|-------------|---------|
| `np.array(liste)` | Depuis une liste Python | `np.array([1,2,3])` |
| `np.zeros(n)` | Tableau de zéros | `np.zeros(5)` |
| `np.ones(n)` | Tableau de uns | `np.ones((2,3))` |
| `np.full(shape, val)` | Tableau rempli d'une valeur | `np.full((2,2), 7)` |
| `np.eye(n)` | Matrice identité | `np.eye(3)` |
| `np.arange(deb, fin, pas)` | Séquence par pas | `np.arange(0,10,2)` |
| `np.linspace(deb, fin, n)` | N valeurs équiréparties | `np.linspace(0,1,5)` |

---

## 4. Anatomie d'un tableau NumPy

Chaque `ndarray` possède des **attributs** qui décrivent sa structure.

```python
tableau = np.array([[4, 8, 12], [6, 10, 15]])

print("Contenu    :", tableau)
print("ndim (dim.) :", tableau.ndim)    # 2  → nombre de dimensions
print("shape      :", tableau.shape)   # (2, 3) → (lignes, colonnes)
print("size       :", tableau.size)    # 6  → nombre total d'éléments
print("dtype      :", tableau.dtype)   # int64 → type des éléments
```

### Visualisation des dimensions

```
1D — Vecteur                2D — Matrice                 3D — Tenseur
─────────────                ─────────────                ─────────────
[1, 2, 3, 4]                [[1, 2, 3],                  [[[1,2],[3,4]],
                              [4, 5, 6]]                    [[5,6],[7,8]]]

shape: (4,)                 shape: (2, 3)                shape: (2, 2, 2)
ndim: 1                     ndim: 2                      ndim: 3

Exemple : une              Exemple : un tableau          Exemple : une pile
liste de notes             de ventes (régions            d'images en couleur
                            × produits)                  (hauteur × largeur × couleur)
```

```python
# Exemples pratiques
notes_1d = np.array([14, 16, 12])
print(notes_1d.shape)   # (3,)

ventes_2d = np.array([[4, 8, 12], [6, 10, 15]])
print(ventes_2d.shape)  # (2, 3) → 2 régions, 3 produits
```

---

## 5. Types de données NumPy (dtype)

Contrairement à une liste Python (qui peut mélanger les types), **tous les éléments d'un tableau NumPy ont le même type**.

### 5.1 Les types principaux

| dtype | Description | Exemple |
|-------|-------------|---------|
| `int32` / `int64` | Entiers | `1, -5, 100` |
| `float32` / `float64` | Décimaux | `3.14, -0.5` |
| `bool` | Booléens | `True, False` |
| `object` | Type générique (ex : chaînes) | `"texte"` |

```python
entiers  = np.array([1, 2, 3])
print(entiers.dtype)          # int64

decimaux = np.array([1.5, 2.5, 3.5])
print(decimaux.dtype)         # float64

# Si on mélange int et float, NumPy convertit TOUT en float
mixte = np.array([1, 2, 3.5])
print(mixte)                  # [1.  2.  3.5]
print(mixte.dtype)            # float64 ← conversion automatique
```

### 5.2 Spécifier ou convertir le type

```python
# Spécifier le type à la création
notes = np.array([14, 16, 18], dtype=np.float64)
print(notes)         # [14. 16. 18.]

# Convertir un tableau existant avec .astype()
entiers = np.array([1.9, 2.7, 3.1])
convertis = entiers.astype(int)
print(convertis)     # [1 2 3]  ← troncature, pas arrondi !
```

---

## 6. Array Reshaping — Remodeler un tableau

### 📖 Définition

`reshape()` permet de **changer la forme (dimensions)** d'un tableau **sans changer ses données**. Le nombre total d'éléments doit rester identique.

> 💡 **Analogie** : Remodeler un tableau, c'est comme réorganiser **12 œufs** : vous pouvez les ranger en une ligne de 12, en 2 rangées de 6, ou en 3 rangées de 4 — le nombre d'œufs ne change jamais, seulement leur disposition.

### 6.1 reshape() de base

```python
donnees = np.arange(12)     # [0 1 2 3 4 5 6 7 8 9 10 11]
print("Original :", donnees.shape)   # (12,)

# Remodeler en 3 lignes x 4 colonnes
matrice = donnees.reshape(3, 4)
print(matrice)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Remodeler en 4 lignes x 3 colonnes
matrice2 = donnees.reshape(4, 3)
print(matrice2)

# ❌ Erreur si le nombre d'éléments ne correspond pas
# donnees.reshape(5, 3)  # ValueError : 12 éléments ≠ 5×3=15
```

### 6.2 La valeur -1 — Laisser NumPy calculer automatiquement

```python
donnees = np.arange(12)

# -1 signifie "calcule cette dimension automatiquement"
matrice = donnees.reshape(3, -1)   # NumPy déduit : 12/3 = 4 colonnes
print(matrice.shape)   # (3, 4)

matrice2 = donnees.reshape(-1, 6)  # NumPy déduit : 12/6 = 2 lignes
print(matrice2.shape)  # (2, 6)
```

### 6.3 Aplatir un tableau — flatten() et ravel()

```python
matrice = np.array([[1, 2, 3], [4, 5, 6]])

# flatten() — retourne une COPIE aplatie en 1D
plat = matrice.flatten()
print(plat)    # [1 2 3 4 5 6]

# ravel() — retourne une VUE aplatie (plus rapide, lié à l'original)
plat2 = matrice.ravel()
print(plat2)   # [1 2 3 4 5 6]
```

### 6.4 Transposer un tableau

```python
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Original :", matrice.shape)    # (2, 3)

transposee = matrice.T          # ou np.transpose(matrice)
print(transposee)
# [[1 4]
#  [2 5]
#  [3 6]]
print("Transposée :", transposee.shape)  # (3, 2)
```

---

## 7. Array Indexing — Accéder aux éléments

### 7.1 Indexation en 1D (comme une liste)

```python
notes = np.array([14, 16, 12, 18, 15])
#                   0   1   2   3   4

print(notes[0])    # 14 (premier élément)
print(notes[2])    # 12
print(notes[-1])   # 15 (dernier élément)
```

### 7.2 Indexation en 2D — `[ligne, colonne]`

```python
ventes = np.array([
    [4,  8,  12],   # Région 1
    [6,  10, 15],   # Région 2
    [5,  7,  9]     # Région 3
])
#         Prod A  B   C

# Syntaxe : tableau[ligne, colonne]
print(ventes[0, 0])   # 4   (Région 1, Produit A)
print(ventes[1, 2])   # 15  (Région 2, Produit C)
print(ventes[2, 1])   # 7   (Région 3, Produit B)

# Accéder à toute une ligne
print(ventes[0])      # [4 8 12]  — toute la Région 1
print(ventes[0, :])   # équivalent, plus explicite

# Accéder à toute une colonne
print(ventes[:, 0])   # [4 6 5]  — tout le Produit A (toutes régions)
```

### 7.3 Modifier des éléments par indexation

```python
notes = np.array([14, 16, 12, 18, 15])

notes[0] = 20            # modifier un seul élément
print(notes)              # [20 16 12 18 15]

ventes = np.array([[4, 8, 12], [6, 10, 15]])
ventes[0, 1] = 100        # modifier un élément 2D
print(ventes)
# [[  4 100  12]
#  [  6  10  15]]
```

---

## 8. Array Slicing — Découper un tableau

### 📖 Rappel de la syntaxe

`tableau[début:fin:pas]` — comme pour les listes Python, la borne `fin` est **exclue**.

### 8.1 Slicing en 1D

```python
notes = np.array([14, 16, 12, 18, 15, 10, 19])
#                   0   1   2   3   4   5   6

print(notes[1:4])     # [16 12 18]
print(notes[:3])      # [14 16 12]
print(notes[3:])      # [18 15 10 19]
print(notes[::2])     # [14 12 15 19]  (un sur deux)
print(notes[::-1])    # tableau inversé
```

### 8.2 Slicing en 2D

```python
ventes = np.array([
    [4,  8,  12, 20],
    [6,  10, 15, 22],
    [5,  7,  9,  18],
    [3,  6,  9,  14]
])

# tableau[lignes, colonnes]
print(ventes[0:2, 0:2])
# [[ 4  8]
#  [ 6 10]]   → 2 premières lignes, 2 premières colonnes

print(ventes[:, 1:3])
# Toutes les lignes, colonnes 1 et 2
# [[ 8 12]
#  [10 15]
#  [ 7  9]
#  [ 6  9]]

print(ventes[1:3, :])
# Lignes 1 et 2, toutes les colonnes
# [[ 6 10 15 22]
#  [ 5  7  9 18]]
```

### 8.3 ⚠️ Le slicing crée une VUE, pas une copie !

C'est un piège classique pour les débutants : contrairement aux listes Python, le slicing NumPy **ne copie pas** les données — il retourne une **référence** vers les mêmes données en mémoire.

```python
original = np.array([1, 2, 3, 4, 5])
extrait  = original[1:4]     # extrait = [2, 3, 4]

extrait[0] = 999             # modifier l'extrait...

print(extrait)                # [999   3   4]
print(original)               # [  1 999   3   4   5]  ← l'original a changé aussi !

# ✅ Pour éviter ça, utiliser .copy()
original2 = np.array([1, 2, 3, 4, 5])
copie = original2[1:4].copy()
copie[0] = 999
print(original2)              # [1 2 3 4 5]  ← inchangé
```

---

## 9. Indexation booléenne et Fancy Indexing

### 📖 Indexation booléenne (Boolean Masking)

L'une des fonctionnalités **les plus puissantes** de NumPy : filtrer un tableau à l'aide d'une **condition**.

```python
notes = np.array([8, 14, 16, 9, 18, 11, 20])

# Créer un masque booléen
masque = notes >= 10
print(masque)   # [False  True  True False  True  True  True]

# Utiliser le masque pour filtrer
notes_admises = notes[masque]
print(notes_admises)   # [14 16 18 11 20]

# En une seule ligne (façon la plus courante)
notes_admises2 = notes[notes >= 10]
print(notes_admises2)  # [14 16 18 11 20]
```

### 9.1 Combiner plusieurs conditions

```python
notes = np.array([8, 14, 16, 9, 18, 11, 20])

# ET logique : &  (pas "and")
entre_12_et_18 = notes[(notes >= 12) & (notes <= 18)]
print(entre_12_et_18)   # [14 16 18]

# OU logique : |  (pas "or")
extremes = notes[(notes < 10) | (notes > 18)]
print(extremes)         # [8 9 20]

# ⚠️ Toujours mettre des parenthèses autour de chaque condition !
```

### 9.2 Modifier des valeurs avec un masque

```python
notes = np.array([8, 14, 16, 9, 18])

# Remplacer toutes les notes < 10 par 0 (ajourné)
notes[notes < 10] = 0
print(notes)   # [ 0 14 16  0 18]

# np.where() — alternative plus flexible (si/sinon vectorisé)
notes2 = np.array([8, 14, 16, 9, 18])
resultat = np.where(notes2 >= 10, "Admis", "Ajourné")
print(resultat)   # ['Ajourné' 'Admis' 'Admis' 'Ajourné' 'Admis']
```

### 9.3 Fancy Indexing — Sélectionner via une liste d'indices

```python
notes = np.array([14, 16, 12, 18, 10, 20, 8])

# Sélectionner des indices spécifiques
indices = [0, 2, 4]
print(notes[indices])   # [14 12 10]

# Utile pour réordonner un tableau
ordre_personnalise = [3, 0, 1]
print(notes[ordre_personnalise])   # [18 14 16]
```

---

## 10. NumPy Random — Génération aléatoire

Le module `np.random` génère des données aléatoires — indispensable pour simuler des données, mélanger un jeu de données, ou initialiser des modèles de Machine Learning.

### 10.1 Nombres aléatoires uniformes

```python
# Flottants aléatoires entre 0 et 1
alea = np.random.rand(5)
print(alea)   # ex: [0.37 0.95 0.14 0.68 0.22]

# Matrice aléatoire
matrice_alea = np.random.rand(2, 3)
print(matrice_alea)
```

### 10.2 Entiers aléatoires

```python
# np.random.randint(min, max, taille) — max EXCLU
entiers = np.random.randint(1, 21, size=10)   # 10 entiers entre 1 et 20
print(entiers)

# Simuler un lancer de dé (100 lancers)
des = np.random.randint(1, 7, size=100)
print(des[:10])   # les 10 premiers résultats
```

### 10.3 Distribution normale (gaussienne)

```python
# np.random.randn() — distribution normale centrée réduite (moyenne=0, écart-type=1)
normal = np.random.randn(5)
print(normal)   # ex: [-0.23  1.14 -0.87  0.45  0.02]

# Distribution normale personnalisée (moyenne, écart-type)
notes_simulees = np.random.normal(loc=14, scale=3, size=1000)
print(f"Moyenne simulée : {notes_simulees.mean():.2f}")   # proche de 14
print(f"Écart type simulé : {notes_simulees.std():.2f}")  # proche de 3
```

### 10.4 Choisir aléatoirement dans un tableau

```python
etudiants = np.array(["Alice", "Bob", "Claire", "David", "Emma"])

# Choisir 1 élément au hasard
choix = np.random.choice(etudiants)
print(choix)

# Choisir 3 éléments SANS remise (pas de doublon)
groupe = np.random.choice(etudiants, size=3, replace=False)
print(groupe)

# Mélanger un tableau (in-place)
np.random.shuffle(etudiants)
print(etudiants)
```

### 10.5 `seed()` — Rendre l'aléatoire reproductible

> 🔑 **Crucial en Data Science** : Pour que vos résultats soient **reproductibles** (vous et vos collègues obtenez le même résultat "aléatoire"), on fixe une **graine (seed)**.

```python
np.random.seed(42)         # fixe la graine
print(np.random.rand(3))   # toujours le MÊME résultat à chaque exécution

np.random.seed(42)         # même graine
print(np.random.rand(3))   # → résultat identique au précédent !
```

> 💡 **Analogie** : `seed()` c'est comme donner **le même point de départ** à un jeu de dés truqué — tant que la graine est identique, la séquence de nombres "aléatoires" générée sera toujours exactement la même, ce qui permet de reproduire une expérience.

---

## 11. NumPy Addition/Soustraction et le Broadcasting

### 11.1 Opérations élément par élément

Les opérations arithmétiques sur des tableaux NumPy s'appliquent **élément par élément** (contrairement aux listes Python où `+` concatène).

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)    # [11 22 33]  (addition élément par élément)
print(a - b)    # [-9 -18 -27]
print(a * b)    # [10 40 90]
print(b / a)    # [10. 10. 10.]

# ⚠️ Comparaison avec les listes Python
liste_a = [1, 2, 3]
liste_b = [10, 20, 30]
print(liste_a + liste_b)   # [1, 2, 3, 10, 20, 30] ← CONCATÉNATION, pas addition !
```

### 11.2 Opérations avec un scalaire

```python
notes = np.array([14, 16, 12, 18])

print(notes + 2)     # [16 18 14 20]  → ajouté à CHAQUE élément
print(notes - 1)     # [13 15 11 17]
print(notes * 5)     # [70 80 60 90]  (conversion sur 100)
print(notes / 2)     # [7.  8.  6.  9.]
```

### 11.3 Le Broadcasting — Concept clé de NumPy

Le **broadcasting** est le mécanisme qui permet à NumPy d'effectuer des opérations entre tableaux de **formes différentes**, en "étirant" automatiquement le plus petit tableau.

> 💡 **Analogie** : Le broadcasting, c'est comme **distribuer une même prime** à toutes les régions d'un tableau de ventes — vous n'avez pas besoin de répéter manuellement la valeur pour chaque ligne, NumPy le fait automatiquement "en arrière-plan".

```python
ventes = np.array([
    [4,  8,  12],
    [6,  10, 15],
    [5,  7,  9]
])

# Ajouter 100 à TOUTE la matrice (scalaire "broadcasté" sur toute la matrice)
print(ventes + 100)
# [[104 108 112]
#  [106 110 115]
#  [105 107 109]]

# Ajouter un vecteur ligne à chaque ligne de la matrice
prime_par_produit = np.array([1, 2, 3])   # shape (3,)
print(ventes + prime_par_produit)
# [[ 5 10 15]
#  [ 7 12 18]
#  [ 6  9 12]]
# → [1,2,3] est "broadcasté" (répété) sur chacune des 3 lignes
```

**Visualisation du broadcasting :**
```
ventes (3x3)              prime_par_produit (3,)         Résultat
┌───┬───┬───┐              ┌───┬───┬───┐                 ┌───┬───┬───┐
│ 4 │ 8 │12 │              │ 1 │ 2 │ 3 │                 │ 5 │10 │15 │
├───┼───┼───┤        +     └───┴───┴───┘        =        ├───┼───┼───┤
│ 6 │10 │15 │              (répété virtuellement          │ 7 │12 │18 │
├───┼───┼───┤               sur chaque ligne)             ├───┼───┼───┤
│ 5 │ 7 │ 9 │                                             │ 6 │ 9 │12 │
└───┴───┴───┘                                             └───┴───┴───┘
```

> ⚠️ **Règle du broadcasting** : les dimensions doivent être **compatibles** — soit identiques, soit égales à 1. Sinon, NumPy lève une erreur `ValueError: operands could not be broadcast together`.

---

## 12. Fonctions d'agrégation

### 12.1 Agrégations globales

```python
notes = np.array([14, 16, 12, 18, 10])

print(notes.sum())     # 70   — somme
print(notes.mean())    # 14.0 — moyenne
print(notes.std())     # écart type
print(notes.var())     # variance
print(notes.min())     # 10   — minimum
print(notes.max())     # 18   — maximum
print(notes.argmin())  # 4    — INDICE du minimum
print(notes.argmax())  # 3    — INDICE du maximum
```

### 12.2 Agrégations par axe (2D) — Concept essentiel

```python
ventes = np.array([
    [4,  8,  12],   # Région 1
    [6,  10, 15],   # Région 2
    [5,  7,  9]     # Région 3
])

# axis=0 → calcule le long des LIGNES (résultat par COLONNE)
print(ventes.sum(axis=0))    # [15 25 36]  → total par produit (A, B, C)

# axis=1 → calcule le long des COLONNES (résultat par LIGNE)
print(ventes.sum(axis=1))    # [24 31 21]  → total par région
```

**Visualisation du concept d'axe (le point le plus mal compris de NumPy !) :**
```
                    axis=0 (vertical ↓)
                         │
              Produit A  Produit B  Produit C
Région 1    [    4    ,    8     ,   12    ]  ─┐
Région 2    [    6    ,   10     ,   15    ]   ├── axis=1 (horizontal →)
Région 3    [    5    ,    7     ,    9    ]  ─┘

sum(axis=0) → additionne VERTICALEMENT → [15, 25, 36]  (par produit)
sum(axis=1) → additionne HORIZONTALEMENT → [24, 31, 21] (par région)
```

> 🔑 **Astuce mnémotechnique** : `axis=0` "écrase" les lignes (le résultat a la forme des colonnes) ; `axis=1` "écrase" les colonnes (le résultat a la forme des lignes).

```python
# Autres agrégations avec axis
print(ventes.mean(axis=0))   # moyenne par produit
print(ventes.max(axis=1))    # maximum par région
```

---

## 13. Some NumPy Functions — Fonctions utiles

### 13.1 Fonctions mathématiques

```python
tableau = np.array([1, 4, 9, 16, 25])

print(np.sqrt(tableau))    # [1. 2. 3. 4. 5.]     — racine carrée
print(np.exp([1, 2]))      # exponentielle
print(np.log([1, np.e]))   # logarithme népérien → [0. 1.]
print(np.abs([-5, 3, -2])) # [5 3 2]              — valeur absolue
print(np.round([3.456, 7.891], 1))  # [3.5 7.9]   — arrondi
```

### 13.2 Tri et recherche

```python
notes = np.array([14, 8, 20, 12, 16])

print(np.sort(notes))          # [ 8 12 14 16 20]  — trié (nouvelle copie)
print(np.argsort(notes))       # [1 3 0 4 2]  — INDICES qui trient le tableau

# Valeurs uniques
doublons = np.array([1, 2, 2, 3, 1, 4, 3])
print(np.unique(doublons))     # [1 2 3 4]

# Rechercher l'indice d'insertion (tableau déjà trié)
trie = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(trie, 6))  # 3 (position où insérer 6)
```

### 13.3 Concaténer et empiler des tableaux

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concaténer (bout à bout)
print(np.concatenate([a, b]))    # [1 2 3 4 5 6]

# Empiler verticalement (nouvelle dimension)
print(np.vstack([a, b]))
# [[1 2 3]
#  [4 5 6]]

# Empiler horizontalement
print(np.hstack([a, b]))         # [1 2 3 4 5 6]
```

### 13.4 Conditions vectorisées avec np.where

```python
notes = np.array([8, 14, 16, 9, 18])

# np.where(condition, si_vrai, si_faux)
mentions = np.where(notes >= 14, "Admis", "Ajourné")
print(mentions)  # ['Ajourné' 'Admis' 'Admis' 'Ajourné' 'Admis']

# np.where imbriqué pour plusieurs conditions
mentions2 = np.where(notes >= 16, "Très bien",
              np.where(notes >= 14, "Bien", "Insuffisant"))
print(mentions2)
```

### 13.5 Tableau récapitulatif des fonctions utiles

| Fonction | Description |
|----------|-------------|
| `np.sqrt()`, `np.exp()`, `np.log()` | Fonctions mathématiques |
| `np.round()`, `np.abs()` | Arrondi, valeur absolue |
| `np.sort()`, `np.argsort()` | Tri, indices de tri |
| `np.unique()` | Valeurs uniques |
| `np.concatenate()`, `np.vstack()`, `np.hstack()` | Fusionner des tableaux |
| `np.where()` | Condition vectorisée (if/else) |
| `np.isnan()` | Détecter les valeurs manquantes (NaN) |

---

## 14. Algèbre linéaire avec NumPy

NumPy permet de retrouver directement les opérations matricielles vues au **checkpoint de mathématiques** !

### 14.1 Produit matriciel

```python
D = np.array([
    [4,  8,  12],
    [6,  10, 15],
    [5,  7,  9],
    [3,  6,  9]
])

P = np.array([5, 10, 15])   # vecteur de prix

# Produit matriciel (comme au checkpoint Maths !)
revenus = D @ P              # ou np.dot(D, P)
print(revenus)                # [280 355 230 210]
```

> 💡 Vous reconnaissez ce calcul ? C'est exactement le même exercice que dans le **checkpoint de mathématiques pour Data Science**, mais résolu ici en **une seule ligne** grâce à NumPy, au lieu de calculer chaque région manuellement !

### 14.2 Transposée

```python
D = np.array([[4, 8, 12], [6, 10, 15]])
print(D.T)
# [[ 4  6]
#  [ 8 10]
#  [12 15]]
```

### 14.3 Autres opérations d'algèbre linéaire

```python
A = np.array([[1, 2], [3, 4]])

print(np.linalg.det(A))       # déterminant
print(np.linalg.inv(A))       # matrice inverse
print(np.trace(A))            # trace (somme de la diagonale)

# Résoudre un système d'équations linéaires Ax = b
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print(x)
```

---

## 15. Conclusion

### 📌 Récapitulatif du chapitre

```
NUMPY — CALCUL NUMÉRIQUE
│
├── Création           → array(), zeros(), ones(), arange(), linspace()
├── Anatomie            → .shape, .ndim, .size, .dtype
├── Reshaping           → .reshape(), .flatten(), .T (transposée)
├── Indexing            → tableau[ligne, colonne]
├── Slicing             → tableau[deb:fin] → VUE, pas copie !
├── Indexation booléenne→ tableau[tableau > seuil]
├── Random              → rand(), randint(), randn(), seed()
├── Opérations          → +, -, *, / (élément par élément) + Broadcasting
├── Agrégations         → sum(), mean(), std() + axis=0/1
├── Fonctions utiles     → sqrt(), sort(), unique(), where(), concatenate()
└── Algèbre linéaire     → @ (produit matriciel), .T, linalg.inv()
```

### 🔑 Points clés à retenir

1. NumPy est **le socle** de tout l'écosystème Data Science Python (Pandas, Scikit-learn, TensorFlow...).
2. Les tableaux NumPy sont **plus rapides** que les listes Python grâce à la **vectorisation**.
3. Le **slicing crée une vue**, pas une copie — utilisez `.copy()` si besoin d'indépendance.
4. Le **broadcasting** permet d'opérer entre tableaux de formes différentes automatiquement.
5. `axis=0` agit **verticalement** (résultat par colonne) ; `axis=1` agit **horizontalement** (résultat par ligne).
6. `np.random.seed()` garantit la **reproductibilité** des résultats aléatoires — essentiel en Data Science.
7. Le produit matriciel `@` retrouve directement les concepts d'algèbre linéaire vus en mathématiques.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons **Pandas**, la bibliothèque construite sur NumPy pour manipuler des **données tabulaires** (DataFrames) — lecture de fichiers CSV, nettoyage de données, filtres, agrégations par groupe (`groupby`), fusion de tableaux (`merge`) — les outils quotidiens de tout Data Scientist.

---

## 16. ✅ Point de contrôle — NumPy

### 📝 Questions théoriques

**Q1.** Pourquoi NumPy est-il plus rapide que les listes Python pour les calculs numériques ?

<details>
<summary>👀 Voir la réponse</summary>

> NumPy stocke les données de **type unique** de façon **contiguë en mémoire** (comme un tableau en C), et exécute les opérations via des instructions **vectorisées** en code C optimisé, sans passer par des boucles Python interprétées ligne par ligne. Les listes Python, elles, stockent des objets hétérogènes dispersés en mémoire, ce qui ajoute un surcoût à chaque opération.
</details>

---

**Q2.** Quelle est la différence entre `np.arange()` et `np.linspace()` ?

<details>
<summary>👀 Voir la réponse</summary>

> `np.arange(debut, fin, pas)` génère des valeurs en spécifiant le **pas** entre elles (la fin est exclue). `np.linspace(debut, fin, n)` génère un **nombre précis** `n` de valeurs équiréparties entre deux bornes (les deux bornes sont incluses).
</details>

---

**Q3.** Que se passe-t-il si on modifie un tableau obtenu par slicing (`tableau[1:4]`) ?

<details>
<summary>👀 Voir la réponse</summary>

> Le slicing NumPy retourne une **vue** (pas une copie) : les données sont partagées avec le tableau original. Modifier le tableau extrait **modifie aussi l'original**. Pour obtenir une copie indépendante, il faut utiliser explicitement `.copy()`.
</details>

---

**Q4.** Qu'est-ce que le broadcasting en NumPy ?

<details>
<summary>👀 Voir la réponse</summary>

> Le broadcasting est le mécanisme qui permet à NumPy d'effectuer des opérations arithmétiques entre des tableaux de **formes différentes**, en étirant virtuellement le plus petit tableau pour qu'il corresponde à la forme du plus grand — sans dupliquer réellement les données en mémoire.
</details>

---

**Q5.** Quelle est la différence entre `axis=0` et `axis=1` dans une fonction d'agrégation sur un tableau 2D ?

<details>
<summary>👀 Voir la réponse</summary>

> `axis=0` agrège **verticalement**, le long des lignes — le résultat a la forme des colonnes (une valeur par colonne). `axis=1` agrège **horizontalement**, le long des colonnes — le résultat a la forme des lignes (une valeur par ligne).
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Création et anatomie**

Créez un tableau NumPy à partir de la liste `[12, 18, 15, 9, 14, 16, 11, 18]`. Affichez sa forme (`shape`), son nombre de dimensions (`ndim`) et son type (`dtype`).

<details>
<summary>👀 Voir la solution</summary>

```python
import numpy as np

notes = np.array([12, 18, 15, 9, 14, 16, 11, 18])
print("Shape :", notes.shape)   # (8,)
print("Ndim  :", notes.ndim)    # 1
print("Dtype :", notes.dtype)   # int64
```
</details>

---

**Exercice 2 — Reshape**

Créez un tableau de 0 à 15 avec `np.arange()`, puis remodelez-le en matrice 4x4.

<details>
<summary>👀 Voir la solution</summary>

```python
tableau = np.arange(16)
matrice = tableau.reshape(4, 4)
print(matrice)
```
</details>

---

**Exercice 3 — Indexation booléenne**

Avec `temperatures = np.array([22, 35, 18, 40, 25, 15, 30])`, sélectionnez uniquement les températures entre 20 et 30 (inclus).

<details>
<summary>👀 Voir la solution</summary>

```python
temperatures = np.array([22, 35, 18, 40, 25, 15, 30])
resultat = temperatures[(temperatures >= 20) & (temperatures <= 30)]
print(resultat)   # [22 25 30]
```
</details>

---

**Exercice 4 — Broadcasting**

Créez une matrice de ventes 3x3 quelconque, puis appliquez une augmentation de 10% sur toutes les valeurs en une seule opération.

<details>
<summary>👀 Voir la solution</summary>

```python
ventes = np.array([[100, 200, 150], [120, 180, 90], [200, 220, 300]])
ventes_augmentees = ventes * 1.10
print(ventes_augmentees)
```
</details>

---

**Exercice 5 — Agrégation par axe**

Avec la matrice suivante (régions en lignes, produits en colonnes) :
```python
ventes = np.array([
    [4, 8, 12],
    [6, 10, 15],
    [5, 7, 9],
    [3, 6, 9]
])
```
Calculez le total par produit ET le total par région.

<details>
<summary>👀 Voir la solution</summary>

```python
ventes = np.array([
    [4, 8, 12],
    [6, 10, 15],
    [5, 7, 9],
    [3, 6, 9]
])

total_par_produit = ventes.sum(axis=0)
total_par_region  = ventes.sum(axis=1)

print("Total par produit :", total_par_produit)  # [18 31 45]
print("Total par région  :", total_par_region)   # [24 31 21 18]
```
</details>

---

**Exercice 6 — NumPy Random**

Fixez la graine aléatoire à 42, puis générez un tableau de 5 entiers aléatoires entre 1 et 100.

<details>
<summary>👀 Voir la solution</summary>

```python
np.random.seed(42)
entiers_aleatoires = np.random.randint(1, 101, size=5)
print(entiers_aleatoires)
```
</details>

---

### 🏆 Challenge bonus — Reprendre le checkpoint Maths avec NumPy

Reprenez l'exercice du **checkpoint Mathématiques pour Data Science** (la matrice D et le vecteur de prix P), mais résolvez-le entièrement avec NumPy :

1. Créez la matrice D et le vecteur P avec NumPy
2. Calculez la moyenne, la médiane et l'écart type de chaque colonne (produit)
3. Calculez la transposée de D
4. Calculez les revenus par région avec le produit matriciel `@`
5. Trouvez la région avec le revenu maximal (indice : `np.argmax()`)

```python
D = [[4, 8, 12], [6, 10, 15], [5, 7, 9], [3, 6, 9]]
P = [5, 10, 15]
```

<details>
<summary>👀 Voir la solution</summary>

```python
import numpy as np

D = np.array([[4, 8, 12], [6, 10, 15], [5, 7, 9], [3, 6, 9]])
P = np.array([5, 10, 15])

# 2. Statistiques par colonne (axis=0)
print("Moyenne :", D.mean(axis=0))
print("Médiane :", np.median(D, axis=0))
print("Écart type :", D.std(axis=0))

# 3. Transposée
print("Transposée :\n", D.T)

# 4. Revenus par région
revenus = D @ P
print("Revenus par région :", revenus)

# 5. Région avec le revenu maximal
region_max = np.argmax(revenus)
print(f"Région avec le + gros revenu : Région {region_max + 1} ({revenus[region_max]})")
```
</details>

---

*📘 Fin du Chapitre 1 (Module Data Science) — Numerical and Data Analysis with NumPy | Bootcamp Data Science*
