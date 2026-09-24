# 🎯 Train/Test Split et Validation Croisée — Cours Bootcamp Data Science

> **Module Data Science — Machine Learning** | Prérequis : cours "Algorithmes de Machine Learning" (scikit-learn, fit/predict, overfitting)

---

## Table des matières

### Partie I — Pourquoi séparer les données ?
1. [Le problème : évaluer honnêtement un modèle](#1-le-problème--évaluer-honnêtement-un-modèle)
2. [Overfitting, underfitting et généralisation](#2-overfitting-underfitting-et-généralisation)

### Partie II — Train/Test Split
3. [Le principe du Train/Test Split](#3-le-principe-du-traintest-split)
4. [`train_test_split` en pratique](#4-train_test_split-en-pratique)
5. [Les paramètres clés (`test_size`, `random_state`, `stratify`, `shuffle`)](#5-les-paramètres-clés)
6. [Le piège de la fuite de données (data leakage)](#6-le-piège-de-la-fuite-de-données-data-leakage)
7. [Train / Validation / Test : la séparation à trois](#7-train--validation--test--la-séparation-à-trois)

### Partie III — La Validation Croisée (Cross-Validation)
8. [Pourquoi la validation croisée ?](#8-pourquoi-la-validation-croisée-)
9. [Le K-Fold Cross-Validation](#9-le-k-fold-cross-validation)
10. [`cross_val_score` et `cross_validate`](#10-cross_val_score-et-cross_validate)
11. [Les variantes de validation croisée](#11-les-variantes-de-validation-croisée)
12. [Combiner cross-validation et réglage d'hyperparamètres (GridSearchCV)](#12-combiner-cross-validation-et-réglage-dhyperparamètres-gridsearchcv)
13. [Éviter la fuite de données avec un Pipeline](#13-éviter-la-fuite-de-données-avec-un-pipeline)

### Partie IV — Synthèse
14. [Train/Test Split vs Cross-Validation : que choisir ?](#14-traintest-split-vs-cross-validation--que-choisir-)
15. [Conclusion](#15-conclusion)
16. [✅ Point de contrôle — Évaluation d'un modèle](#16--point-de-contrôle--évaluation-dun-modèle)

---

# PARTIE I — POURQUOI SÉPARER LES DONNÉES ?

## 1. Le problème : évaluer honnêtement un modèle

### 📖 La question fondamentale

Vous avez entraîné un modèle. Il faut maintenant répondre à **une seule question** :

> 🔑 **« Mon modèle sera-t-il bon sur des données qu'il n'a JAMAIS vues ? »**

Car c'est bien là tout l'intérêt du Machine Learning : prédire l'**avenir**, sur de **nouveaux** clients, de **nouvelles** transactions, de **nouvelles** photos. Un modèle qui ne fonctionne que sur les données d'entraînement ne sert à rien.

### 1.1 L'erreur du débutant : évaluer sur les données d'entraînement

> 💡 **Analogie de l'examen** : Imaginez un professeur qui donne à ses élèves **exactement les mêmes exercices** à l'examen que ceux corrigés en cours. Tout le monde a 20/20… mais cette note ne prouve **rien**. Les élèves ont peut-être juste **mémorisé** les réponses sans rien comprendre. Le vrai test, c'est de donner des exercices **nouveaux**.

Évaluer un modèle sur les données qui ont servi à l'entraîner, c'est exactement cette erreur :

```
❌ CE QU'IL NE FAUT PAS FAIRE
─────────────────────────────
model.fit(X, y)          # entraîner sur TOUTES les données
model.score(X, y)        # évaluer sur LES MÊMES données
→ score = 0.99 🎉         # illusion ! le modèle a "révisé le sujet"
```

Le score obtenu est **trop optimiste** : il mesure la capacité du modèle à **mémoriser**, pas à **généraliser**.

### 1.2 La solution : garder des données « au secret »

L'idée centrale de ce cours tient en une phrase :

> 🎯 **On met de côté une partie des données AVANT l'entraînement, et on ne les montre au modèle qu'au moment de l'évaluer.**

Ces données mises de côté jouent le rôle de l'**examen surprise** : le modèle ne les a jamais vues, donc son score sur ces données reflète honnêtement ses performances **dans le monde réel**.

---

## 2. Overfitting, underfitting et généralisation

Avant de séparer les données, il faut comprendre les trois comportements possibles d'un modèle.

### 2.1 Les trois régimes

```
UNDERFITTING              BON MODÈLE               OVERFITTING
(sous-apprentissage)      (généralisation)         (sur-apprentissage)
────────────────          ────────────────         ────────────────
Trop SIMPLE               Juste ce qu'il faut      Trop COMPLEXE
                                                    
   o   o                     o   o                     o   o
 ────────                   ╱‾‾‾‾╲                    ╱╲ ╱╲╱╲
o   o   o                  o  o  o                  o╱  V  ╲o
                                                    (colle au bruit)

Rate sur train ET test    Bon sur train ET test    Parfait sur train,
                                                    MAUVAIS sur test
```

| Comportement | Erreur sur Train | Erreur sur Test | Diagnostic |
|--------------|------------------|-----------------|------------|
| **Underfitting** | Élevée | Élevée | Modèle trop simple, il n'apprend pas assez |
| **Bon modèle** | Faible | Faible | ✅ Il généralise bien |
| **Overfitting** | Très faible | Élevée | Modèle trop complexe, il mémorise le bruit |

> 🔑 **On détecte l'overfitting UNIQUEMENT en comparant le score sur train et sur test.** Sans données de test, l'overfitting est invisible — d'où la nécessité absolue de séparer les données.

### 2.2 Le compromis biais-variance (en une phrase)

- **Biais élevé** = le modèle fait des hypothèses trop simples → **underfitting**.
- **Variance élevée** = le modèle est trop sensible aux détails des données d'entraînement → **overfitting**.

Le bon modèle est celui qui **équilibre** les deux. Toutes les techniques de ce cours (split, validation croisée) servent à **mesurer** cet équilibre.

---

# PARTIE II — TRAIN/TEST SPLIT

## 3. Le principe du Train/Test Split

### 📖 Définition

Le **Train/Test Split** consiste à découper le jeu de données en **deux** parties disjointes :

```
JEU DE DONNÉES COMPLET (100%)
┌───────────────────────────────────────────────────────┐
│                                                        │
└───────────────────────────────────────────────────────┘
                          │
                     ✂️ découpe
                          │
        ┌─────────────────┴──────────────┐
        ▼                                ▼
┌──────────────────────┐        ┌─────────────────┐
│   TRAIN SET (~80%)    │        │  TEST SET (~20%)│
│                       │        │                 │
│  Sert à ENTRAÎNER     │        │ Sert à ÉVALUER  │
│  model.fit(X_train)   │        │ model.score(... │
│                       │        │                 │
│  Le modèle APPREND    │        │ Jamais vu       │
│  sur ces données      │        │ pendant le fit  │
└──────────────────────┘        └─────────────────┘
```

| Ensemble | Proportion typique | Rôle | Le modèle le voit-il ? |
|----------|--------------------|------|------------------------|
| **Train set** | 70 – 80 % | Apprentissage (`fit`) | ✅ Oui |
| **Test set** | 20 – 30 % | Évaluation finale (`score`, `predict`) | ❌ Non — uniquement à la fin |

> ⚠️ **Règle d'or** : le test set est **sacré**. On ne l'utilise **qu'une seule fois**, tout à la fin, pour mesurer la performance finale. On ne l'utilise **jamais** pour choisir un modèle ou régler des paramètres (sinon il perd son statut de « données jamais vues »).

### 3.1 Les quatre morceaux : X_train, X_test, y_train, y_test

Rappel : `X` = les features (variables d'entrée), `y` = la target (ce qu'on veut prédire). Le split coupe **les deux en même temps**, en gardant les lignes alignées :

```
     X (features)          y (target)
   ┌────────────┐         ┌────────┐
   │ ligne 1    │         │ y_1    │
   │ ligne 2    │  ────►  │ y_2    │   split en gardant
   │ ...        │         │ ...    │   X et y ALIGNÉS
   │ ligne N    │         │ y_N    │
   └────────────┘         └────────┘

Résultat : 4 objets
  X_train, y_train  (mêmes lignes)  → pour fit
  X_test,  y_test   (mêmes lignes)  → pour évaluer
```

---

## 4. `train_test_split` en pratique

Scikit-learn fournit la fonction `train_test_split` qui fait tout le travail.

```python
from sklearn.model_selection import train_test_split

# X = features, y = target
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20 % pour le test
    random_state=42     # reproductibilité (voir §5)
)

print(f"Total      : {len(X)} lignes")
print(f"Train      : {len(X_train)} lignes ({len(X_train)/len(X):.0%})")
print(f"Test       : {len(X_test)} lignes ({len(X_test)/len(X):.0%})")
```

> ⚠️ **L'ordre de sortie compte !** `train_test_split` renvoie toujours dans cet ordre : `X_train, X_test, y_train, y_test`. Une inversion (`X_train, y_train, X_test, y_test`) est le bug le plus fréquent des débutants.

### 4.1 Exemple complet de bout en bout

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# 1. Charger les données (ex. loyers d'Abidjan)
df = pd.read_csv("loyers_abidjan.csv")
X = df[["surface", "nb_pieces", "distance_centre"]]
y = df["loyer"]

# 2. SÉPARER avant tout entraînement
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Entraîner UNIQUEMENT sur le train
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Évaluer sur le test (données jamais vues)
y_pred = model.predict(X_test)
print(f"R² test  : {r2_score(y_test, y_pred):.3f}")
print(f"MAE test : {mean_absolute_error(y_test, y_pred):,.0f} FCFA")

# 5. Comparer train vs test pour détecter l'overfitting
print(f"\nScore train : {model.score(X_train, y_train):.3f}")
print(f"Score test  : {model.score(X_test, y_test):.3f}")
# Si train >> test  → overfitting
```

---

## 5. Les paramètres clés

### 5.1 `test_size` (et `train_size`)

Contrôle la proportion réservée au test.

```python
train_test_split(X, y, test_size=0.2)   # 20 % test, 80 % train
train_test_split(X, y, test_size=0.3)   # 30 % test, 70 % train
train_test_split(X, y, test_size=100)   # 100 lignes exactement en test
```

| Situation | `test_size` conseillé | Pourquoi |
|-----------|-----------------------|----------|
| Beaucoup de données (> 100 000) | 0.1 ou moins | 10 % suffisent pour une mesure fiable |
| Taille moyenne | 0.2 – 0.25 | Le standard |
| Peu de données (< 1 000) | 0.3, ou plutôt **validation croisée** | Un split unique devient instable (voir §8) |

### 5.2 `random_state` — la reproductibilité

Le split est **aléatoire** : sans le fixer, vous obtenez un découpage différent à chaque exécution, donc un score différent à chaque fois.

```python
# Sans random_state → résultat différent à chaque exécution
train_test_split(X, y, test_size=0.2)

# Avec random_state → TOUJOURS le même découpage
train_test_split(X, y, test_size=0.2, random_state=42)
```

> 💡 `random_state=42` est une convention (clin d'œil au *Guide du voyageur galactique*). N'importe quel entier convient — l'important est de **fixer** une valeur pour que vos résultats soient **reproductibles** (par vous, par un collègue, par le correcteur).

### 5.3 `stratify` — préserver les proportions (classification)

En **classification**, si une classe est rare, un split aléatoire peut la répartir de travers (voire l'oublier complètement dans le test). `stratify=y` garantit que **chaque classe garde la même proportion** dans le train et le test.

```
SANS stratify (aléatoire)         AVEC stratify=y
─────────────────────────         ─────────────────────
Global : 90 % A / 10 % B          Global : 90 % A / 10 % B
Train  : 88 % A / 12 % B          Train  : 90 % A / 10 % B  ✅
Test   : 95 % A /  5 % B  ⚠️       Test   : 90 % A / 10 % B  ✅
(proportions déformées)           (proportions préservées)
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y          # ⭐ INDISPENSABLE en classification déséquilibrée
)
```

> 🔑 **Réflexe** : en classification, mettez presque toujours `stratify=y`. C'est particulièrement critique pour les données déséquilibrées (fraude, maladie rare, churn).

### 5.4 `shuffle` — mélanger avant de couper

Par défaut `shuffle=True` : les lignes sont mélangées avant la découpe. **Gardez ce comportement** dans le cas général — sinon, si vos données sont triées (ex. par date ou par classe), le test ne contiendrait qu'un bout non représentatif.

> ⚠️ **Exception : les séries temporelles.** Pour prédire l'avenir à partir du passé, on ne doit **pas** mélanger : le train doit être le *passé* et le test le *futur*. On utilise alors `shuffle=False` ou, mieux, `TimeSeriesSplit` (voir §11).

### 📋 Récapitulatif des paramètres

| Paramètre | Rôle | Valeur typique |
|-----------|------|----------------|
| `test_size` | Part réservée au test | `0.2` |
| `random_state` | Reproductibilité | `42` |
| `stratify` | Préserver les proportions de classes | `y` (classification) |
| `shuffle` | Mélanger avant de couper | `True` (sauf séries temporelles) |

---

## 6. Le piège de la fuite de données (data leakage)

### 📖 Définition

La **fuite de données** (*data leakage*) survient quand des informations du **test** « fuitent » dans l'entraînement. Le score devient artificiellement excellent… et s'effondre en production.

### 6.1 L'erreur la plus courante : normaliser avant de splitter

```python
# ❌ MAUVAIS — fuite de données
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)          # apprend moyenne/écart-type sur TOUT
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
# → le scaler a "vu" les données de test. FUITE.
```

Le problème : `fit_transform` calcule la moyenne et l'écart-type sur **l'ensemble des données**, y compris le test. Le modèle bénéficie donc, indirectement, d'informations sur le test.

```python
# ✅ BON — on splitte D'ABORD, puis on ajuste le scaler sur le train SEUL
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)   # fit UNIQUEMENT sur le train
X_test_s  = scaler.transform(X_test)        # on APPLIQUE (transform) sur le test
```

> 🔑 **La règle absolue** : tout ce qui *apprend* quelque chose des données (normalisation, imputation de valeurs manquantes, encodage, sélection de variables) doit être **ajusté sur le train uniquement**, puis **appliqué** au test. Le test ne doit **rien** enseigner au pipeline.

> 💡 **La solution robuste** à ce piège est le **`Pipeline`** de scikit-learn (voir §13), qui automatise ce « fit sur train / transform sur test » et empêche la fuite par construction.

### 6.2 Autres sources de fuite fréquentes

| Source de fuite | Exemple | Correction |
|-----------------|---------|------------|
| Prétraitement global | `scaler.fit_transform(X)` avant split | Fit sur train seul |
| Feature « du futur » | Utiliser une colonne connue seulement après la prédiction | La supprimer |
| Doublons | Mêmes lignes dans train et test | Dédupliquer avant split |
| Réglages sur le test | Choisir les hyperparamètres en regardant le score de test | Utiliser un set de validation / la CV |

---

## 7. Train / Validation / Test : la séparation à trois

### 📖 Le problème du réglage d'hyperparamètres

Dès qu'on veut **choisir** quelque chose (quel modèle ? quelle profondeur d'arbre ? quel `k` en KNN ?), on a besoin de **comparer** des scores. Mais si on compare sur le test set, on « use » notre examen surprise : à force de choisir ce qui marche le mieux sur le test, on finit par **s'adapter au test** (une forme d'overfitting indirect).

La solution : découper en **trois**.

```
JEU DE DONNÉES COMPLET
┌─────────────────────────────────────────────────────────┐
└─────────────────────────────────────────────────────────┘
        │
   ┌────┴──────────────┬─────────────────┐
   ▼                   ▼                 ▼
┌────────────┐  ┌───────────────┐  ┌──────────────┐
│ TRAIN 60%  │  │ VALIDATION 20%│  │  TEST 20%    │
│            │  │               │  │              │
│ Entraîner  │  │ Choisir le    │  │ Mesure finale│
│ les modèles│  │ meilleur      │  │ UNE SEULE    │
│            │  │ modèle /      │  │ fois, à la   │
│            │  │ régler les    │  │ toute fin    │
│            │  │ hyperparams   │  │              │
└────────────┘  └───────────────┘  └──────────────┘
```

| Ensemble | Rôle | Combien de fois utilisé ? |
|----------|------|---------------------------|
| **Train** | Entraîner chaque modèle candidat | À chaque essai |
| **Validation** | Comparer les candidats, régler les hyperparamètres | À chaque essai |
| **Test** | Mesure finale, honnête et unique | **Une seule fois**, à la fin |

```python
# Découpe à trois : 60 / 20 / 20
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)          # 20 % test

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42)  # 0.25 × 80 % = 20 % val
# → Train 60 %, Val 20 %, Test 20 %
```

> ⚠️ **Limite** : réserver 20 % pour la validation, c'est autant de données en moins pour entraîner. Sur de petits jeux de données, c'est coûteux. **La validation croisée (Partie III) résout élégamment ce problème** en réutilisant toutes les données à tour de rôle.

---

# PARTIE III — LA VALIDATION CROISÉE (CROSS-VALIDATION)

## 8. Pourquoi la validation croisée ?

### 📖 Le défaut du split unique

Un simple train/test split repose sur **UN seul découpage aléatoire**. Or, selon les lignes qui tombent dans le test, le score peut varier — parfois beaucoup, surtout sur peu de données.

```
Split A (random_state=1)  → score test = 0.82
Split B (random_state=2)  → score test = 0.91
Split C (random_state=3)  → score test = 0.85
        ...
Quel est le VRAI score du modèle ? 🤔
```

Le score d'un split unique est une **estimation bruitée**. On aimerait une mesure **plus stable et plus fiable**.

### 💡 L'idée de la validation croisée

> 🎯 **Au lieu d'un seul test, on en fait plusieurs — et on fait la moyenne.**

Chaque ligne des données sert **tantôt à l'entraînement, tantôt à l'évaluation**. On obtient ainsi plusieurs scores, dont la **moyenne** est une bien meilleure estimation de la performance réelle, et dont l'**écart-type** mesure la **stabilité** du modèle.

---

## 9. Le K-Fold Cross-Validation

### 📖 Le principe

La méthode la plus courante est le **K-Fold** : on découpe les données en **K blocs** (*folds*) de taille égale, puis on répète K fois :

- **1 fold** sert de test,
- les **K−1 autres** servent d'entraînement.

Chaque fold joue le rôle du test **exactement une fois**.

```
K-FOLD CROSS-VALIDATION (K = 5)
Données découpées en 5 blocs égaux : [ 1 | 2 | 3 | 4 | 5 ]

Itération 1 :  [🟦TEST][ train ][ train ][ train ][ train ]  → score₁
Itération 2 :  [ train ][🟦TEST][ train ][ train ][ train ]  → score₂
Itération 3 :  [ train ][ train ][🟦TEST][ train ][ train ]  → score₃
Itération 4 :  [ train ][ train ][ train ][🟦TEST][ train ]  → score₄
Itération 5 :  [ train ][ train ][ train ][ train ][🟦TEST]  → score₅
                                                              ─────────
                        Score final = moyenne(score₁…score₅)
                        ± écart-type (mesure la stabilité)
```

### 9.1 Comment choisir K ?

| Valeur de K | Effet | Quand l'utiliser |
|-------------|-------|------------------|
| **K = 5** | Bon compromis (standard) | Cas général ✅ |
| **K = 10** | Estimation plus fine, plus coûteuse | Jeux de données moyens |
| **K = N** (LOO) | Un test par ligne (*Leave-One-Out*) | Très petits jeux de données |

> 🔑 **Par défaut, prenez K = 5 ou K = 10.** Plus K est grand, plus l'estimation est fiable, mais plus le calcul est long (on entraîne le modèle K fois).

### 9.2 Le compromis de la validation croisée

- ✅ **Avantage** : estimation fiable, chaque ligne sert à évaluer, utilise **toutes** les données.
- ⚠️ **Inconvénient** : **coûteux** — le modèle est entraîné **K fois** au lieu d'une.

---

## 10. `cross_val_score` et `cross_validate`

### 10.1 `cross_val_score` — la version simple

```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=4, random_state=42)

scores = cross_val_score(model, X, y, cv=5)   # cv=5 → 5 folds

print("Scores par fold :", scores.round(3))
print(f"Moyenne  : {scores.mean():.3f}")
print(f"Écart-type : {scores.std():.3f}")   # stabilité du modèle
print(f"\nPerformance estimée : {scores.mean():.3f} ± {scores.std():.3f}")
```

```
Scores par fold : [0.85 0.88 0.83 0.90 0.86]
Moyenne  : 0.864
Écart-type : 0.024
Performance estimée : 0.864 ± 0.024
```

> 💡 On rapporte toujours **moyenne ± écart-type**. Un petit écart-type = modèle **stable** (performance homogène quel que soit le découpage). Un grand écart-type = modèle **instable** ou données trop peu nombreuses.

**Choisir la métrique** avec `scoring` :

```python
# Classification
cross_val_score(model, X, y, cv=5, scoring="accuracy")
cross_val_score(model, X, y, cv=5, scoring="f1")
cross_val_score(model, X, y, cv=5, scoring="roc_auc")

# Régression
cross_val_score(model, X, y, cv=5, scoring="r2")
cross_val_score(model, X, y, cv=5, scoring="neg_mean_absolute_error")
```

> ⚠️ Pour les erreurs (MAE, MSE), scikit-learn utilise des scores **négatifs** (`neg_...`) car sa convention est « plus grand = mieux ». Pensez à re-multiplier par −1 pour lire l'erreur réelle.

### 10.2 `cross_validate` — la version détaillée

Quand on veut **plusieurs métriques**, les **temps de calcul** ou les **scores de train** :

```python
from sklearn.model_selection import cross_validate

resultats = cross_validate(
    model, X, y, cv=5,
    scoring=["accuracy", "f1"],
    return_train_score=True         # pour comparer train vs test → overfitting
)

print("Test accuracy :", resultats["test_accuracy"].mean().round(3))
print("Test F1       :", resultats["test_f1"].mean().round(3))
print("Train accuracy:", resultats["train_accuracy"].mean().round(3))
# Si train_accuracy >> test_accuracy → overfitting
```

---

## 11. Les variantes de validation croisée

Le K-Fold de base ne convient pas à tous les cas. Scikit-learn propose des variantes adaptées.

| Variante | À utiliser quand… | Idée |
|----------|-------------------|------|
| **`KFold`** | Régression, cas général | K blocs, mélange aléatoire |
| **`StratifiedKFold`** | **Classification** | Préserve les proportions de classes dans chaque fold |
| **`TimeSeriesSplit`** | **Séries temporelles** | Le train est toujours le *passé*, le test le *futur* |
| **`GroupKFold`** | Données groupées (mêmes patients, mêmes utilisateurs) | Un même groupe n'est jamais à la fois en train et en test |
| **`LeaveOneOut`** | Très peu de données | K = N (un test par ligne) |

> 🔑 **Bonne nouvelle** : pour un problème de **classification**, `cross_val_score(clf, X, y, cv=5)` utilise **automatiquement** un `StratifiedKFold`. La stratification est gérée pour vous par défaut.

### 11.1 `StratifiedKFold` explicite

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)
```

### 11.2 `TimeSeriesSplit` — ne jamais prédire le passé avec le futur

```
TIME SERIES SPLIT (le test est toujours APRÈS le train)
Itération 1 : [train][🟦test]· · · · · ·
Itération 2 : [  train  ][🟦test]· · · ·
Itération 3 : [    train    ][🟦test]· ·
Itération 4 : [      train      ][🟦test]
              → le train grandit, le test avance vers le futur
```

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
scores = cross_val_score(model, X, y, cv=tscv)   # X, y triés par date, PAS mélangés
```

---

## 12. Combiner cross-validation et réglage d'hyperparamètres (GridSearchCV)

### 📖 L'idée

La validation croisée sert surtout à **choisir les meilleurs hyperparamètres**. `GridSearchCV` teste **toutes les combinaisons** d'une grille de paramètres, en évaluant chacune par **validation croisée**, et retient la meilleure.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# 1. On garde un test set à part (mesure finale)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 2. Grille d'hyperparamètres à explorer
grille = {
    "n_neighbors": [3, 5, 7, 9, 11],
    "weights": ["uniform", "distance"],
}

# 3. Recherche : chaque combinaison évaluée par CV à 5 folds
grid = GridSearchCV(
    KNeighborsClassifier(),
    param_grid=grille,
    cv=5,
    scoring="accuracy",
    n_jobs=-1              # paralléliser sur tous les cœurs
)
grid.fit(X_train, y_train)   # ⚠️ CV faite SUR LE TRAIN uniquement

# 4. Résultats
print("Meilleurs paramètres :", grid.best_params_)
print(f"Meilleur score CV    : {grid.best_score_:.3f}")

# 5. Mesure FINALE sur le test (jamais vu pendant la recherche)
print(f"Score test final     : {grid.score(X_test, y_test):.3f}")
```

```
Meilleurs paramètres : {'n_neighbors': 7, 'weights': 'distance'}
Meilleur score CV    : 0.891
Score test final     : 0.885
```

> 🔑 **Le schéma gagnant** : on règle les hyperparamètres par **validation croisée sur le train**, puis on mesure la performance finale **une seule fois** sur le test. Le test reste vierge → score honnête.

> 💡 **`RandomizedSearchCV`** : quand la grille est énorme, cette variante teste un **échantillon aléatoire** de combinaisons — beaucoup plus rapide, souvent presque aussi bon.

---

## 13. Éviter la fuite de données avec un Pipeline

### 📖 Le problème avec la validation croisée

Rappel du §6 : le prétraitement (normalisation, imputation) doit être ajusté **sur le train seul**. Mais en validation croisée, le « train » change à **chaque fold** ! Impossible de normaliser une fois pour toutes à la main sans fuite.

### 💡 La solution : le `Pipeline`

Un **`Pipeline`** enchaîne prétraitement + modèle en **un seul objet**. Scikit-learn ré-ajuste alors **tout le pipeline sur le train de chaque fold** — la fuite est impossible **par construction**.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Le prétraitement est DANS le pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),              # étape 1 : normaliser
    ("knn", KNeighborsClassifier(n_neighbors=5)) # étape 2 : classifier
])

# À chaque fold, le scaler est ré-ajusté sur le train du fold uniquement → zéro fuite
scores = cross_val_score(pipe, X, y, cv=5)
print(f"Accuracy : {scores.mean():.3f} ± {scores.std():.3f}")
```

> 🔑 **Réflexe professionnel** : dès qu'il y a du prétraitement **+** de la validation croisée (ou un `GridSearchCV`), passez par un **`Pipeline`**. C'est la seule manière propre d'éviter la fuite de données. On peut même régler les hyperparamètres du prétraitement dans la grille : `param_grid={"knn__n_neighbors": [3, 5, 7]}`.

---

# PARTIE IV — SYNTHÈSE

## 14. Train/Test Split vs Cross-Validation : que choisir ?

### 14.1 Tableau comparatif

| Critère | Train/Test Split | Validation croisée (K-Fold) |
|---------|------------------|------------------------------|
| **Nombre de découpages** | 1 | K (ex. 5 ou 10) |
| **Coût de calcul** | Faible (1 entraînement) | Élevé (K entraînements) |
| **Fiabilité de l'estimation** | Moyenne (dépend du tirage) | Élevée (moyenne + écart-type) |
| **Mesure la stabilité ?** | Non | ✅ Oui (écart-type) |
| **Idéal pour** | Beaucoup de données, prototypage rapide | Peu/moyennement de données, choix de modèle |
| **Utilise toutes les données pour évaluer ?** | Non | ✅ Oui (chaque ligne testée une fois) |

### 14.2 Comment les combiner en pratique

Dans un vrai projet, on utilise **les deux, ensemble** :

```
WORKFLOW D'ÉVALUATION COMPLET
│
1. ✂️  train_test_split → mettre le TEST de côté (sacré, on n'y touche plus)
        │
2. 🔁  Sur le TRAIN : validation croisée + GridSearchCV
        → comparer les modèles, régler les hyperparamètres
        │
3. 🏆  Choisir le meilleur modèle (meilleur score CV moyen)
        │
4. 🎓  Ré-entraîner ce modèle sur TOUT le train
        │
5. 📊  Mesure FINALE sur le TEST (une seule fois) → score honnête à annoncer
```

> 🔑 **La règle qui résume tout** : la **validation croisée sur le train** sert à **choisir**, le **test** sert à **annoncer** la performance finale — une seule fois.

### 14.3 Arbre de décision : quelle méthode ?

```
Combien de données ?
│
├── Beaucoup (> 100 000)
│   └── Train/Test Split simple suffit (rapide, fiable)
│
├── Moyen (1 000 – 100 000)
│   └── Split + validation croisée sur le train (choix de modèle)
│
└── Peu (< 1 000)
    └── Validation croisée (K=5/10), voire LeaveOneOut
        (un split unique serait trop instable)

Classification ?      → stratify=y  et  StratifiedKFold
Série temporelle ?    → shuffle=False  et  TimeSeriesSplit
Prétraitement + CV ?  → Pipeline (obligatoire, anti-fuite)
```

---

## 15. Conclusion

### 🎓 Ce qu'il faut absolument retenir

1. **On n'évalue jamais un modèle sur ses données d'entraînement.** Ce serait comme donner à l'examen les corrigés déjà vus en cours : la note ne mesure rien.

2. **Le Train/Test Split** met une partie des données (~20 %) « au secret ». Le modèle apprend sur le train, et son score sur le **test** — des données jamais vues — reflète sa vraie performance.

3. **Comparer train et test** est le seul moyen de détecter l'**overfitting** (train ≫ test) ou l'**underfitting** (les deux mauvais).

4. **Le test set est sacré** : utilisé **une seule fois**, tout à la fin. Pour choisir un modèle ou régler des hyperparamètres, on utilise un set de **validation** ou la **validation croisée**.

5. **La validation croisée (K-Fold)** remplace un tirage unique par **K découpages** : elle donne une estimation **plus fiable** (moyenne) et mesure la **stabilité** (écart-type). Indispensable quand les données sont **peu nombreuses**.

6. **La fuite de données** (normaliser avant de splitter) gonfle artificiellement les scores. La parade : ajuster tout prétraitement **sur le train seul**, ou — mieux — utiliser un **`Pipeline`**.

7. **`GridSearchCV`** combine validation croisée et réglage d'hyperparamètres : il choisit la meilleure configuration **sur le train**, avant la mesure finale **sur le test**.

### 🧭 Le mémo en une image

```
┌────────────────────────────────────────────────────────────┐
│  TRAIN  →  apprendre  (fit)                                 │
│  VALIDATION / CROSS-VAL  →  choisir & régler                │
│  TEST   →  annoncer la performance finale (UNE fois)        │
│                                                             │
│  Toujours : stratify en classif · Pipeline si prétraitement │
│             · comparer train vs test pour voir l'overfitting│
└────────────────────────────────────────────────────────────┘
```

> 🔑 **En une phrase** : *séparer les données, c'est la différence entre un modèle qui **impressionne** sur le papier et un modèle qui **fonctionne** dans le monde réel.*

---

## 16. ✅ Point de contrôle — Évaluation d'un modèle

### 🧠 Questions de compréhension

<details>
<summary><b>1. Pourquoi ne peut-on pas évaluer un modèle sur les données qui ont servi à l'entraîner ?</b></summary>

Parce que le modèle a déjà « vu » ces données : il peut les avoir **mémorisées** plutôt qu'appris à généraliser. Le score serait trop optimiste et ne dirait rien de sa performance sur de **nouvelles** données — le seul cas qui compte réellement.
</details>

<details>
<summary><b>2. Que renvoie <code>train_test_split(X, y)</code>, et dans quel ordre ?</b></summary>

Quatre objets, dans cet ordre exact : `X_train, X_test, y_train, y_test`. Inverser cet ordre est le bug classique.
</details>

<details>
<summary><b>3. À quoi sert <code>random_state</code> ?</b></summary>

À **fixer** le découpage aléatoire pour rendre les résultats **reproductibles** : la même valeur (ex. `42`) donne toujours le même split, donc les mêmes scores d'une exécution à l'autre.
</details>

<details>
<summary><b>4. Dans quel cas met-on <code>stratify=y</code> ?</b></summary>

En **classification**, surtout si les classes sont **déséquilibrées**. Cela garantit que chaque classe conserve la **même proportion** dans le train et le test.
</details>

<details>
<summary><b>5. Un modèle a 0.99 sur le train et 0.62 sur le test. Que se passe-t-il ?</b></summary>

C'est de l'**overfitting** (sur-apprentissage) : le modèle a mémorisé le train (y compris le bruit) mais ne généralise pas. Pistes : simplifier le modèle, plus de données, régularisation, réduire le nombre de features.
</details>

<details>
<summary><b>6. Quel est l'avantage de la validation croisée par rapport à un seul train/test split ?</b></summary>

Elle donne une estimation **plus fiable** (moyenne sur K découpages, moins sensible au hasard du tirage) et mesure la **stabilité** du modèle via l'**écart-type**. Elle utilise aussi **toutes** les données pour l'évaluation.
</details>

<details>
<summary><b>7. Pourquoi normaliser avant <code>train_test_split</code> est une erreur ?</b></summary>

Parce que le scaler calcule alors moyenne/écart-type sur **toutes** les données, y compris le test : c'est une **fuite de données** (*data leakage*). Il faut ajuster le scaler sur le **train seul** (`fit` sur train, `transform` sur test), idéalement via un **`Pipeline`**.
</details>

<details>
<summary><b>8. À quoi sert le set de validation, distinct du test ?</b></summary>

À **choisir** le modèle et **régler les hyperparamètres** sans « user » le test. Le test reste ainsi vierge pour une mesure finale **honnête et unique**. La validation croisée joue ce rôle sans sacrifier de données.
</details>

### 🛠️ Exercice pratique

Sur le fichier `demandes_credit.csv` (dossier `TP/`), on veut prédire l'octroi d'un crédit (classification).

1. Séparez les données en train/test (20 % de test, `random_state=42`, stratifié).
2. Entraînez un `DecisionTreeClassifier` et comparez le score train vs test. Y a-t-il de l'overfitting ?
3. Estimez la performance par **validation croisée à 5 folds** sur le train (moyenne ± écart-type).
4. Utilisez `GridSearchCV` pour trouver la meilleure `max_depth` parmi `[2, 3, 4, 5, 8, 12]`.
5. Donnez le **score final** sur le test avec le meilleur modèle.

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# Données
df = pd.read_csv("demandes_credit.csv")
X = df.drop(columns=["credit_accorde"])   # adapter au vrai nom de la cible
y = df["credit_accorde"]

# 1. Split stratifié
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 2. Overfitting ?
arbre = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print(f"Train : {arbre.score(X_train, y_train):.3f}")
print(f"Test  : {arbre.score(X_test, y_test):.3f}")
# Un arbre sans max_depth → souvent 1.00 en train ≫ test = overfitting

# 3. Validation croisée
scores = cross_val_score(
    DecisionTreeClassifier(max_depth=4, random_state=42), X_train, y_train, cv=5)
print(f"\nCV : {scores.mean():.3f} ± {scores.std():.3f}")

# 4. GridSearchCV
grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"max_depth": [2, 3, 4, 5, 8, 12]},
    cv=5, scoring="accuracy", n_jobs=-1)
grid.fit(X_train, y_train)
print(f"\nMeilleure max_depth : {grid.best_params_['max_depth']}")
print(f"Meilleur score CV   : {grid.best_score_:.3f}")

# 5. Score final sur le test
print(f"Score test final    : {grid.score(X_test, y_test):.3f}")
```
</details>

---

*📘 Module Data Science — Train/Test Split et Validation Croisée | Bootcamp Data Science*
