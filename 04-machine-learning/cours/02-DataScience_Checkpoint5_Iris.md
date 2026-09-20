# 🌸 Checkpoint 5 — Entraîner et Évaluer un Modèle (Dataset Iris)

> **Module Data Science — Machine Learning** | Prérequis : cours "Algorithmes de Machine Learning"

---

## Table des matières

1. [Objectif du checkpoint](#1-objectif-du-checkpoint)
2. [Le dataset Iris](#2-le-dataset-iris)
3. [Étape 1 — Charger et explorer les données](#3-étape-1--charger-et-explorer-les-données)
4. [Étape 2 — Visualiser les données](#4-étape-2--visualiser-les-données)
5. [Étape 3 — Préparer les données](#5-étape-3--préparer-les-données)
6. [Étape 4 — Entraîner les modèles](#6-étape-4--entraîner-les-modèles)
7. [Étape 5 — Évaluer les modèles](#7-étape-5--évaluer-les-modèles)
8. [Étape 6 — Optimiser et comparer](#8-étape-6--optimiser-et-comparer)
9. [Solution complète commentée](#9-solution-complète-commentée)
10. [Questions de compréhension](#10-questions-de-compréhension)

---

## 1. Objectif du checkpoint

### 🎯 Ce que vous allez réaliser

Dans ce checkpoint, vous allez mettre en pratique **tout le workflow de Machine Learning** sur le jeu de données le plus célèbre du domaine : **Iris**. Vous allez :

```
OBJECTIFS DU CHECKPOINT
│
├── ✅ Charger et explorer un vrai dataset
├── ✅ Visualiser les données pour comprendre les classes
├── ✅ Séparer les données en train/test
├── ✅ Entraîner 3 modèles (Arbre, KNN, et un bonus)
├── ✅ Évaluer avec précision, matrice de confusion, rapport de classification
├── ✅ Optimiser (trouver le meilleur K, la meilleure profondeur)
└── ✅ Comparer et choisir le meilleur modèle
```

> 💡 C'est un **projet complet de bout en bout** — exactement le type de tâche que réalise un Data Scientist au quotidien.

---

## 2. Le dataset Iris

### 📖 Présentation

Le dataset **Iris** contient les mesures de **150 fleurs d'iris** réparties en **3 espèces** (50 fleurs chacune). C'est le "Hello World" du Machine Learning — parfait pour apprendre la classification.

### 2.1 Structure du dataset

```
DATASET IRIS
│
├── 150 fleurs (observations)
│
├── 4 features (mesures en cm) :
│   ├── sepal length  (longueur du sépale)
│   ├── sepal width   (largeur du sépale)
│   ├── petal length  (longueur du pétale)
│   └── petal width   (largeur du pétale)
│
└── 3 classes (espèces à prédire) :
    ├── Setosa       (facile à distinguer)
    ├── Versicolor   (parfois confondue avec Virginica)
    └── Virginica    (parfois confondue avec Versicolor)
```

### 2.2 Pourquoi Iris est parfait pour apprendre

```
✅ Petit (150 lignes) → rapide à traiter
✅ Propre (aucune valeur manquante) → focus sur le ML
✅ Équilibré (50 par classe) → pas de biais
✅ 3 classes → vraie classification multi-classes
✅ Intégré à Scikit-learn → aucun téléchargement nécessaire
```

> 💡 **Le petit défi** : Setosa est très facile à identifier, mais Versicolor et Virginica se ressemblent — c'est là que les modèles font leurs quelques erreurs. Un bon modèle atteint généralement **93-97%** de précision.

---

## 3. Étape 1 — Charger et explorer les données

### 3.1 Charger Iris depuis Scikit-learn

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Charger le dataset intégré
iris = load_iris()

# Créer un DataFrame pour l'exploration
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

print(df.head())
print(f"\nDimensions : {df.shape}")
```

### 3.2 Explorer avec les réflexes des chapitres précédents

```python
# Vue d'ensemble
df.info()
df.describe()

# Répartition des classes (doit être équilibré : 50/50/50)
print(df["species"].value_counts())

# Vérifier les valeurs manquantes (aucune dans Iris)
print(df.isna().sum())
```

**Résultat attendu de `value_counts()` :**
```
setosa        50
versicolor    50
virginica     50
```

> 🔑 Le dataset est parfaitement **équilibré** (50 fleurs par espèce) — idéal pour la classification.

---

## 4. Étape 2 — Visualiser les données

### 4.1 Pairplot — Voir la séparation des classes

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# Le pairplot montre toutes les relations entre features, colorées par espèce
sns.pairplot(df, hue="species", height=2)
plt.suptitle("Relations entre les mesures des iris", y=1.02)
plt.show()
```

> 💡 Sur le pairplot, vous verrez que **Setosa (une couleur) est bien isolée** des deux autres, tandis que Versicolor et Virginica **se chevauchent** légèrement — ce qui explique les rares erreurs des modèles.

### 4.2 Heatmap de corrélation

```python
plt.figure(figsize=(8, 6))
correlation = df.drop(columns=["species"]).corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Corrélation entre les mesures")
plt.show()
```

> 💡 On observe que `petal length` et `petal width` sont **très corrélées** (~0.96) — les pétales sont les meilleurs indicateurs pour distinguer les espèces.

---

## 5. Étape 3 — Préparer les données

### 5.1 Séparer features (X) et target (y)

```python
# X = les 4 mesures, y = l'espèce (sous forme numérique 0/1/2)
X = iris.data      # les features
y = iris.target    # la cible (0=setosa, 1=versicolor, 2=virginica)

print("Features (X) :", X.shape)   # (150, 4)
print("Target (y)   :", y.shape)   # (150,)
```

### 5.2 Séparer train et test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% pour le test
    random_state=42,     # reproductibilité
    stratify=y           # garde les proportions de classes équilibrées
)

print(f"Train : {X_train.shape[0]} fleurs")   # 120
print(f"Test  : {X_test.shape[0]} fleurs")    # 30
```

> 🔑 Le paramètre `stratify=y` garantit que le train et le test contiennent **la même proportion** de chaque espèce — crucial pour une évaluation juste.

### 5.3 Normaliser (essentiel pour le KNN)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit + transform sur le train
X_test_scaled  = scaler.transform(X_test)        # transform seul sur le test
```

> ⚠️ Rappel : on `fit_transform` sur le train, mais seulement `transform` sur le test. Ne jamais réajuster le scaler sur le test !

---

## 6. Étape 4 — Entraîner les modèles

### 6.1 Modèle 1 — Arbre de décision

```python
from sklearn.tree import DecisionTreeClassifier

arbre = DecisionTreeClassifier(max_depth=3, random_state=42)
arbre.fit(X_train, y_train)   # l'arbre n'a pas besoin de normalisation
```

### 6.2 Modèle 2 — KNN

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)   # KNN utilise les données NORMALISÉES
```

### 6.3 Modèle 3 (bonus) — Régression logistique

```python
from sklearn.linear_model import LogisticRegression

# La régression LOGISTIQUE est adaptée à la CLASSIFICATION
# (contrairement à la régression linéaire qui prédit des nombres)
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train_scaled, y_train)
```

> 💡 **Note importante** : pour classer (prédire une catégorie), on n'utilise **pas** la régression linéaire mais la **régression logistique**, spécialement conçue pour la classification.

---

## 7. Étape 5 — Évaluer les modèles

### 7.1 La précision (accuracy)

```python
from sklearn.metrics import accuracy_score

# Prédictions
pred_arbre  = arbre.predict(X_test)
pred_knn    = knn.predict(X_test_scaled)
pred_logreg = logreg.predict(X_test_scaled)

print(f"Arbre de décision : {accuracy_score(y_test, pred_arbre):.3f}")
print(f"KNN (k=5)         : {accuracy_score(y_test, pred_knn):.3f}")
print(f"Régression log.   : {accuracy_score(y_test, pred_logreg):.3f}")
```

**Résultat typique :**
```
Arbre de décision : 0.967
KNN (k=5)         : 0.933
Régression log.   : 0.967
```

### 7.2 La matrice de confusion

La matrice de confusion montre **quelles classes sont confondues** entre elles.

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, pred_arbre)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap="Blues")
plt.title("Matrice de confusion — Arbre de décision")
plt.show()
```

```
COMMENT LIRE UNE MATRICE DE CONFUSION
│
                 Prédit
              set  ver  vir
     set  [  10    0    0  ]   ← 10 setosa bien classées
Réel ver  [   0    9    1  ]   ← 1 versicolor confondue avec virginica
     vir  [   0    0   10  ]   ← 10 virginica bien classées

La DIAGONALE = bonnes prédictions
Hors diagonale = erreurs (confusions entre classes)
```

### 7.3 Le rapport de classification

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, pred_arbre, target_names=iris.target_names))
```

**Résultat :**
```
              precision    recall  f1-score   support
   setosa        1.00      1.00      1.00        10
versicolor       1.00      0.90      0.95        10
 virginica       0.91      1.00      0.95        10
   accuracy                          0.97        30
```

| Métrique | Signification |
|----------|----------------|
| **Precision** | Parmi les prédictions "classe X", combien étaient correctes ? |
| **Recall** | Parmi les vraies "classe X", combien ont été trouvées ? |
| **F1-score** | Moyenne équilibrée entre precision et recall |
| **Support** | Nombre de vrais exemples de chaque classe |

---

## 8. Étape 6 — Optimiser et comparer

### 8.1 Trouver le meilleur K pour le KNN

```python
scores_k = {}
for k in range(1, 21):
    knn_test = KNeighborsClassifier(n_neighbors=k)
    knn_test.fit(X_train_scaled, y_train)
    scores_k[k] = accuracy_score(y_test, knn_test.predict(X_test_scaled))

meilleur_k = max(scores_k, key=scores_k.get)
print(f"Meilleur K : {meilleur_k} (précision : {scores_k[meilleur_k]:.3f})")

# Visualiser
import matplotlib.pyplot as plt
plt.plot(list(scores_k.keys()), list(scores_k.values()), marker="o")
plt.xlabel("Valeur de K")
plt.ylabel("Précision")
plt.title("Précision du KNN selon K")
plt.grid(alpha=0.3)
plt.show()
```

### 8.2 Validation croisée (évaluation plus robuste)

```python
from sklearn.model_selection import cross_val_score

# La validation croisée teste le modèle sur plusieurs découpages
scores_cv = cross_val_score(arbre, X, y, cv=5)   # 5 plis
print(f"Précision moyenne (5-fold) : {scores_cv.mean():.3f} ± {scores_cv.std():.3f}")
```

> 🔑 La **validation croisée** est plus fiable qu'un simple train/test : elle teste le modèle sur **plusieurs découpages** des données et moyenne les résultats, réduisant la dépendance à un découpage particulier.

### 8.3 Tableau comparatif final

```python
resultats = {
    "Arbre de décision"    : accuracy_score(y_test, pred_arbre),
    "KNN (k=5)"            : accuracy_score(y_test, pred_knn),
    "Régression logistique": accuracy_score(y_test, pred_logreg)
}

print("=== COMPARAISON FINALE ===")
for modele, score in sorted(resultats.items(), key=lambda x: x[1], reverse=True):
    print(f"{modele:25} : {score:.3f}")

meilleur = max(resultats, key=resultats.get)
print(f"\n🏆 Meilleur modèle : {meilleur}")
```

---

## 9. Solution complète commentée

Voici le **script complet** du checkpoint, prêt à exécuter d'un seul bloc.

```python
# ============================================================
# CHECKPOINT 5 : Entraîner et évaluer un modèle sur Iris
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

sns.set_theme(style="whitegrid")

# --- ÉTAPE 1 : Charger et explorer ---
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]
print("=== EXPLORATION ===")
print(f"Dimensions : {df.shape}")
print(df["species"].value_counts())

# --- ÉTAPE 2 : Préparer ---
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# --- ÉTAPE 3 : Entraîner les 3 modèles ---
arbre  = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
knn    = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)
logreg = LogisticRegression(max_iter=200).fit(X_train_s, y_train)

# --- ÉTAPE 4 : Évaluer ---
print("\n=== RÉSULTATS ===")
resultats = {
    "Arbre de décision"     : accuracy_score(y_test, arbre.predict(X_test)),
    "KNN (k=5)"             : accuracy_score(y_test, knn.predict(X_test_s)),
    "Régression logistique" : accuracy_score(y_test, logreg.predict(X_test_s)),
}
for modele, score in sorted(resultats.items(), key=lambda x: x[1], reverse=True):
    print(f"{modele:25} : {score:.3f}")

# --- ÉTAPE 5 : Détail du meilleur modèle ---
print("\n=== RAPPORT DÉTAILLÉ (Arbre) ===")
print(classification_report(y_test, arbre.predict(X_test),
                            target_names=iris.target_names))

# --- ÉTAPE 6 : Optimiser le KNN ---
scores_k = {}
for k in range(1, 21):
    knn_k = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
    scores_k[k] = accuracy_score(y_test, knn_k.predict(X_test_s))
meilleur_k = max(scores_k, key=scores_k.get)
print(f"Meilleur K pour le KNN : {meilleur_k} ({scores_k[meilleur_k]:.3f})")

# --- ÉTAPE 7 : Validation croisée ---
cv = cross_val_score(arbre, X, y, cv=5)
print(f"Validation croisée (arbre) : {cv.mean():.3f} ± {cv.std():.3f}")

# --- Conclusion ---
meilleur = max(resultats, key=resultats.get)
print(f"\n🏆 Meilleur modèle : {meilleur} ({resultats[meilleur]:.3f})")
```

**Sortie attendue :**
```
=== EXPLORATION ===
Dimensions : (150, 5)
setosa        50
versicolor    50
virginica     50

=== RÉSULTATS ===
Arbre de décision       : 0.967
Régression logistique   : 0.967
KNN (k=5)               : 0.933

🏆 Meilleur modèle : Arbre de décision (0.967)
```

---

## 10. Questions de compréhension

Après avoir exécuté le checkpoint, répondez à ces questions.

**Q1.** Pourquoi utilise-t-on `stratify=y` lors du `train_test_split` ?

<details>
<summary>👀 Voir la réponse</summary>

> `stratify=y` garantit que les proportions de chaque classe (espèce) sont **identiques** dans le train et le test. Sans cela, un découpage aléatoire pourrait, par malchance, mettre trop de setosa dans le train et pas assez dans le test, faussant l'évaluation. Avec Iris (50/50/50), on veut retrouver ~10/10/10 dans le test.
</details>

---

**Q2.** Pourquoi le KNN utilise-t-il `X_train_scaled` alors que l'arbre utilise `X_train` (non normalisé) ?

<details>
<summary>👀 Voir la réponse</summary>

> Le KNN se base sur les **distances**, donc les échelles des variables doivent être uniformisées (normalisation obligatoire). L'arbre de décision, lui, fonctionne par **seuils sur chaque variable indépendamment** (ex : "petal length > 2.5 ?") — il n'est donc **pas affecté** par les échelles et n'a pas besoin de normalisation.
</details>

---

**Q3.** Dans la matrice de confusion, entre quelles espèces les confusions se produisent-elles généralement, et pourquoi ?

<details>
<summary>👀 Voir la réponse</summary>

> Les confusions se produisent presque toujours entre **Versicolor et Virginica**, car leurs mesures se chevauchent (visible sur le pairplot). Setosa est toujours parfaitement classée car elle est nettement séparée des deux autres. C'est pourquoi les modèles atteignent ~93-97% mais rarement 100%.
</details>

---

**Q4.** Quelle est la différence entre la régression linéaire et la régression logistique ?

<details>
<summary>👀 Voir la réponse</summary>

> La **régression linéaire** prédit une **valeur numérique continue** (régression). La **régression logistique**, malgré son nom, sert à la **classification** : elle prédit la **probabilité d'appartenance à une classe**. Pour Iris (prédire une espèce = catégorie), c'est la régression logistique qui convient, pas la linéaire.
</details>

---

**Q5.** Pourquoi la validation croisée est-elle plus fiable qu'un simple train/test split ?

<details>
<summary>👀 Voir la réponse</summary>

> Un simple train/test split évalue le modèle sur **un seul découpage** — le résultat peut varier selon la "chance" du découpage. La validation croisée découpe les données en plusieurs plis (ex : 5), entraîne et teste le modèle **plusieurs fois** sur des découpages différents, puis **moyenne** les scores. Cela donne une estimation plus **robuste et fiable** de la vraie performance du modèle.
</details>

---

### 🏆 Extension du checkpoint

Pour aller plus loin, essayez de :

1. **Visualiser l'arbre de décision** avec `plot_tree()` pour comprendre ses règles
2. **Tester différentes profondeurs** d'arbre (`max_depth` de 1 à 10) et tracer la précision
3. **Utiliser seulement 2 features** (petal length + petal width) et voir si la précision reste bonne
4. **Créer une fonction** `predire_espece(sepal_l, sepal_w, petal_l, petal_w)` qui prédit l'espèce d'une nouvelle fleur

<details>
<summary>👀 Voir une piste pour l'extension 4</summary>

```python
def predire_espece(sepal_l, sepal_w, petal_l, petal_w, modele=arbre):
    """Prédit l'espèce d'une fleur à partir de ses 4 mesures."""
    mesures = [[sepal_l, sepal_w, petal_l, petal_w]]
    prediction = modele.predict(mesures)[0]
    return iris.target_names[prediction]

# Test
espece = predire_espece(5.1, 3.5, 1.4, 0.2)
print(f"Espèce prédite : {espece}")   # setosa (petits pétales)

espece2 = predire_espece(6.7, 3.0, 5.2, 2.3)
print(f"Espèce prédite : {espece2}")  # virginica (grands pétales)
```
</details>

---

*📘 Module Data Science — Checkpoint 5 : Iris | Bootcamp Data Science*
