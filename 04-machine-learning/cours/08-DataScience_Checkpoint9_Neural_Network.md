# 🧠 Checkpoint 9 — Un Réseau de Neurones Simple, Expliqué

> **Module Data Science — Intelligence Artificielle** | Prérequis : cours "Fondamentaux IA/ML/DL" (`07-...md`)

---

## Table des matières

1. [Objectif du checkpoint](#1-objectif-du-checkpoint)
2. [Partie A — Un neurone en NumPy (de zéro)](#2-partie-a--un-neurone-en-numpy-de-zéro)
3. [Partie B — Un réseau à une couche cachée (forward)](#3-partie-b--un-réseau-à-une-couche-cachée-forward)
4. [Partie C — Comprendre l'apprentissage : la descente de gradient](#4-partie-c--comprendre-lapprentissage--la-descente-de-gradient)
5. [Partie D — Un vrai réseau avec `MLPClassifier`](#5-partie-d--un-vrai-réseau-avec-mlpclassifier)
6. [Solution complète commentée](#6-solution-complète-commentée)
7. [Barème et critères de réussite](#7-barème-et-critères-de-réussite)
8. [Questions de compréhension](#8-questions-de-compréhension)

---

## 1. Objectif du checkpoint

### 🎯 Ce que vous allez réaliser

```
OBJECTIFS DU CHECKPOINT 9
│
├── ✅ Coder un NEURONE à la main (somme pondérée + activation)
├── ✅ Assembler un petit RÉSEAU et faire une propagation avant
├── ✅ COMPRENDRE l'apprentissage : loss, gradient, mise à jour des poids
├── ✅ Entraîner un vrai réseau (MLPClassifier) sur un dataset réel
└── ✅ EXPLIQUER chaque étape avec vos mots
```

> 💡 Objectif pédagogique : **démystifier** le réseau de neurones. À la fin, vous saurez qu'il ne s'agit que de « somme pondérée + activation », répété et ajusté. Pas de magie.

> ⚠️ **Note technique** : ce checkpoint n'utilise **que NumPy et scikit-learn** (pas de TensorFlow/PyTorch). Le but est de comprendre les **mécanismes**, pas de manier un framework lourd.

---

## 2. Partie A — Un neurone en NumPy (de zéro)

> 🎯 **But** : implémenter le calcul d'un seul neurone et comprendre le rôle de chaque élément.

### 📋 Consignes

1. Définissez les fonctions d'activation **sigmoïde** et **ReLU**.
2. Créez un neurone à 3 entrées : calculez `z = Σ wᵢxᵢ + b` puis `a = f(z)`.
3. Faites varier un **poids** et le **biais** : observez l'effet sur la sortie.
4. **Expliquez** : que représentent les poids ? le biais ? l'activation ?

> 💡 **Indice** : `z = np.dot(w, x) + b`. La sigmoïde : `1/(1+np.exp(-z))`.

---

## 3. Partie B — Un réseau à une couche cachée (forward)

> 🎯 **But** : enchaîner des couches et réaliser une **propagation avant** complète.

### 📋 Consignes

Construisez un réseau **3 entrées → 4 neurones cachés (ReLU) → 1 sortie (sigmoïde)** :

1. Initialisez les matrices de poids `W1` (4×3), `W2` (1×4) et les biais `b1`, `b2` **aléatoirement**.
2. Écrivez une fonction `forward(x)` qui calcule : `a1 = ReLU(W1·x + b1)` puis `y = sigmoïde(W2·a1 + b2)`.
3. Testez sur une entrée et **interprétez** la sortie (probabilité entre 0 et 1).
4. **Question** : pourquoi la sortie est-elle « n'importe quoi » à ce stade ? (poids aléatoires, réseau non entraîné)

---

## 4. Partie C — Comprendre l'apprentissage : la descente de gradient

> 🎯 **But** : voir **concrètement** comment ajuster un poids réduit l'erreur, sur un cas minimal.

### 📋 Consignes

Sur un neurone à **une entrée** (`y = sigmoïde(w·x + b)`) et un exemple cible :

1. Choisissez un `x`, une cible `y_vrai`, des `w`, `b` initiaux.
2. Calculez la prédiction et la **loss** (erreur quadratique `(y_pred - y_vrai)²`).
3. Faites **10 itérations** de descente de gradient manuelle : à chaque pas, calculez le gradient de la loss par rapport à `w` et `b`, puis mettez à jour `w ← w - η·grad`.
4. **Tracez** la loss au fil des itérations : elle doit **diminuer**.
5. **Expliquez** ce que vous observez.

> 💡 **Indice (dérivée en chaîne)** : pour la loss `L=(a-y)²` avec `a=σ(z)`, `z=wx+b` :
> `dL/dw = 2(a-y)·a(1-a)·x` et `dL/db = 2(a-y)·a(1-a)`.

---

## 5. Partie D — Un vrai réseau avec `MLPClassifier`

> 🎯 **But** : entraîner un réseau de neurones opérationnel sur un dataset réel et l'évaluer.

### 📋 Consignes

Sur un dataset de classification (ex. `load_breast_cancer` de scikit-learn) :

1. Chargez les données, séparez **train/test** (stratifié).
2. **Standardisez** les features (⚠️ indispensable pour un réseau — cours 05).
3. Entraînez un `MLPClassifier` (ex. `hidden_layer_sizes=(16, 8)`, `max_iter=500`).
4. Évaluez : accuracy, matrice de confusion, F1 (cours 04).
5. Tracez la **courbe de loss** (`mlp.loss_curve_`) : observez la descente.
6. **Expliquez** : combien de couches ? de neurones ? que montre la courbe de loss ?

---

## 6. Solution complète commentée

<details>
<summary>👀 <b>Partie A — Un neurone en NumPy</b></summary>

```python
import numpy as np

def sigmoid(z): return 1 / (1 + np.exp(-z))
def relu(z):    return np.maximum(0, z)

# Un neurone à 3 entrées
x = np.array([0.5, 0.3, 0.2])     # entrées (features)
w = np.array([0.4, 0.7, 0.1])     # poids : importance de chaque entrée
b = 0.1                            # biais : décalage / seuil

z = np.dot(w, x) + b               # 1) somme pondérée + biais
a = sigmoid(z)                     # 2) activation
print(f"z = {z:.3f}  ->  a = {a:.3f}")

# Effet d'un poids plus fort sur la 2e entrée
w2 = np.array([0.4, 2.0, 0.1])
print("Sortie si w₂ augmente :", round(sigmoid(np.dot(w2, x) + b), 3))

# Effet du biais
print("Sortie si b = -1 :", round(sigmoid(np.dot(w, x) - 1), 3))

# EXPLICATION :
# - poids  = combien chaque entrée compte (ce que le réseau APPREND)
# - biais  = rend le neurone plus/moins facile à activer
# - activation = transforme z en un signal borné (ici une "probabilité")
```
</details>

<details>
<summary>👀 <b>Partie B — Réseau 3 → 4 → 1 (forward)</b></summary>

```python
import numpy as np
np.random.seed(42)

def sigmoid(z): return 1 / (1 + np.exp(-z))
def relu(z):    return np.maximum(0, z)

# Poids et biais initialisés ALÉATOIREMENT (réseau non entraîné)
W1 = np.random.randn(4, 3) * 0.5   # couche cachée : 4 neurones, 3 entrées
b1 = np.zeros(4)
W2 = np.random.randn(1, 4) * 0.5   # sortie : 1 neurone, 4 entrées
b2 = np.zeros(1)

def forward(x):
    a1 = relu(W1 @ x + b1)         # couche cachée (ReLU)
    y  = sigmoid(W2 @ a1 + b2)     # sortie (sigmoïde -> proba)
    return y, a1

x = np.array([0.5, 0.3, 0.2])
y, a1 = forward(x)
print("Activations cachées :", a1.round(3))
print("Prédiction (proba)  :", y.round(3))

# EXPLICATION : la sortie est "au hasard" car les poids sont aléatoires.
# Il faut ENTRAÎNER le réseau (ajuster W1, W2, b1, b2) pour qu'elle ait du sens.
```
</details>

<details>
<summary>👀 <b>Partie C — Descente de gradient manuelle</b></summary>

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z): return 1 / (1 + np.exp(-z))

# Un neurone à 1 entrée, un seul exemple à apprendre
x, y_vrai = 1.5, 1.0      # on veut que le réseau sorte ~1 pour x=1.5
w, b = 0.0, 0.0           # poids initiaux
eta = 0.5                 # learning rate

pertes = []
for i in range(30):
    z = w * x + b
    a = sigmoid(z)                    # prédiction
    loss = (a - y_vrai) ** 2          # erreur quadratique
    pertes.append(loss)

    # Gradients (dérivée en chaîne)
    d = 2 * (a - y_vrai) * a * (1 - a)
    dw, db = d * x, d

    # Mise à jour : descente de gradient
    w -= eta * dw
    b -= eta * db

print(f"Après entraînement : w={w:.3f}, b={b:.3f}")
print(f"Prédiction finale  : {sigmoid(w*x + b):.3f}  (cible = {y_vrai})")

plt.plot(pertes, marker='o')
plt.xlabel("Itération"); plt.ylabel("Loss")
plt.title("La loss diminue → le neurone apprend"); plt.show()

# EXPLICATION : à chaque pas, on corrige w et b dans le sens qui réduit
# l'erreur. La courbe de loss descend : c'est exactement ce que fait un
# réseau, mais sur des millions de poids à la fois (via la backpropagation).
```
</details>

<details>
<summary>👀 <b>Partie D — MLPClassifier sur un dataset réel</b></summary>

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt

# 1. Données + split
X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 2. Standardisation (INDISPENSABLE pour un réseau)
scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_tr)     # fit sur le train uniquement
X_te_s = scaler.transform(X_te)

# 3. Réseau : 2 couches cachées (16 puis 8 neurones)
mlp = MLPClassifier(hidden_layer_sizes=(16, 8), activation="relu",
                    max_iter=500, random_state=42)
mlp.fit(X_tr_s, y_tr)

# 4. Évaluation
y_pred = mlp.predict(X_te_s)
print(f"Accuracy : {accuracy_score(y_te, y_pred):.3f}")
print(f"F1       : {f1_score(y_te, y_pred):.3f}")
print("Matrice de confusion :\n", confusion_matrix(y_te, y_pred))
print(f"Couches : {mlp.n_layers_} | neurones cachés : {mlp.hidden_layer_sizes}")

# 5. Courbe de loss (la descente de gradient en action)
plt.plot(mlp.loss_curve_)
plt.xlabel("Epoch"); plt.ylabel("Loss")
plt.title("Descente de la loss pendant l'entraînement"); plt.show()

# EXPLICATION : le réseau a 2 couches cachées (16, 8) + 1 sortie. La courbe
# de loss descend puis se stabilise = le réseau a convergé. Sans la
# standardisation (étape 2), l'entraînement serait bien plus lent/instable.
```
</details>

---

## 7. Barème et critères de réussite

| Critère | Points | Attendu |
|---------|--------|---------|
| Neurone en NumPy (A) | 20 % | Somme pondérée + activation correctes, rôle de w/b/f expliqué |
| Forward du réseau (B) | 20 % | Enchaînement des couches correct, sortie interprétée |
| Descente de gradient (C) | 25 % | Loss qui **diminue**, mécanisme expliqué avec ses mots |
| MLPClassifier (D) | 25 % | Standardisation + entraînement + évaluation + courbe de loss |
| Explications & clarté | 10 % | Chaque étape commentée, vocabulaire maîtrisé |

> ✅ **Réussite** : ≥ 60 %. **Excellence** : les explications montrent une **compréhension réelle** (pas seulement du code qui tourne).

---

## 8. Questions de compréhension

<details>
<summary><b>1. Dans la Partie A, à quoi servent respectivement le poids et le biais ?</b></summary>

Le **poids** fixe l'importance d'une entrée dans la somme. Le **biais** décale la somme, rendant le neurone plus ou moins facile à activer (c'est un seuil ajustable). Les deux sont **appris** pendant l'entraînement.
</details>

<details>
<summary><b>2. Pourquoi la sortie du réseau de la Partie B n'a-t-elle aucun sens au départ ?</b></summary>

Parce que les poids sont **initialisés au hasard** : le réseau n'a rien appris. Seul l'entraînement (ajustement des poids pour minimiser la loss) rend les prédictions pertinentes.
</details>

<details>
<summary><b>3. Dans la Partie C, que représente la courbe de loss qui descend ?</b></summary>

Elle montre que, à chaque itération, la correction des poids **réduit l'erreur** entre la prédiction et la cible. C'est la descente de gradient : le neurone « apprend » à sortir la bonne valeur.
</details>

<details>
<summary><b>4. Qu'est-ce que le learning rate `eta` contrôle dans la Partie C ?</b></summary>

La **taille du pas** de mise à jour des poids. Trop grand → la loss oscille ou diverge ; trop petit → l'apprentissage est très lent. Il faut un compromis.
</details>

<details>
<summary><b>5. Pourquoi standardise-t-on les features avant le MLPClassifier (Partie D) ?</b></summary>

Un réseau apprend par **descente de gradient**, sensible à l'échelle des variables. Sans standardisation, les variables de grande amplitude dominent et l'entraînement devient lent/instable. On `fit` le scaler sur le **train seul** (anti-fuite, cours 05).
</details>

<details>
<summary><b>6. Que vous apprend `mlp.loss_curve_` sur l'entraînement ?</b></summary>

Elle trace la loss à chaque epoch. Une courbe qui **descend puis se stabilise** indique une **convergence** réussie. Si elle stagne haut, le modèle n'apprend pas ; si la loss de validation remonte, c'est de l'**overfitting**.
</details>

<details>
<summary><b>7. Le réseau de la Partie D a `hidden_layer_sizes=(16, 8)`. Que signifie ce réglage ?</b></summary>

Deux couches cachées : la première a **16 neurones**, la seconde **8**. S'y ajoutent la couche d'entrée (une par feature) et la couche de sortie. Plus de couches/neurones = plus de capacité, mais aussi plus de risque d'overfitting.
</details>

<details>
<summary><b>8. En une phrase, qu'est-ce qu'un réseau de neurones « au fond » ?</b></summary>

Un empilement de « somme pondérée + activation non linéaire » dont on ajuste les poids par descente de gradient (via la backpropagation) pour minimiser une erreur — répété à grande échelle.
</details>

---

*📘 Module Data Science — Checkpoint 9 : Réseau de Neurones Simple | Bootcamp Data Science*
