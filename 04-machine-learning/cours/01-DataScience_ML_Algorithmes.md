# 🤖 Implémenter des Algorithmes de Machine Learning en Python — Cours Bootcamp Data Science

> **Module Data Science — Machine Learning** | Prérequis : NumPy, Pandas, Visualisation

---

## Table des matières

### Partie I — Introduction au Machine Learning
1. [Qu'est-ce que le Machine Learning ?](#1-quest-ce-que-le-machine-learning-)
2. [Le vocabulaire et le workflow ML](#2-le-vocabulaire-et-le-workflow-ml)
3. [Scikit-learn : la bibliothèque de référence](#3-scikit-learn--la-bibliothèque-de-référence)

### Partie II — La Régression Linéaire
4. [Qu'est-ce que la régression linéaire ?](#4-quest-ce-que-la-régression-linéaire-)
5. [Comment fonctionne la régression linéaire ?](#5-comment-fonctionne-la-régression-linéaire-)
6. [La droite de meilleur ajustement (Best-Fit Line)](#6-la-droite-de-meilleur-ajustement-best-fit-line)
7. [Les hypothèses de la régression linéaire](#7-les-hypothèses-de-la-régression-linéaire)
8. [Types de régression linéaire](#8-types-de-régression-linéaire)
9. [Métriques d'évaluation de la régression](#9-métriques-dévaluation-de-la-régression)
10. [Avantages et inconvénients de la régression linéaire](#10-avantages-et-inconvénients-de-la-régression-linéaire)

### Partie III — Les Arbres de Décision
11. [Qu'est-ce qu'un arbre de décision ?](#11-quest-ce-quun-arbre-de-décision-)
12. [Comment fonctionnent les arbres de décision ?](#12-comment-fonctionnent-les-arbres-de-décision-)
13. [Critères de division et élagage](#13-critères-de-division-et-élagage)
14. [Avantages, inconvénients et applications des arbres](#14-avantages-inconvénients-et-applications-des-arbres)

### Partie IV — Les K Plus Proches Voisins (KNN)
15. [Qu'est-ce que le KNN et le "K" ?](#15-quest-ce-que-le-knn-et-le-k-)
16. [Comment choisir la valeur de K ?](#16-comment-choisir-la-valeur-de-k-)
17. [Les métriques de distance en KNN](#17-les-métriques-de-distance-en-knn)
18. [Fonctionnement, avantages et applications du KNN](#18-fonctionnement-avantages-et-applications-du-knn)

### Partie V — Synthèse
19. [Comparaison des trois algorithmes](#19-comparaison-des-trois-algorithmes)
20. [Conclusion](#20-conclusion)
21. [✅ Point de contrôle — Machine Learning](#21--point-de-contrôle--machine-learning)

---

# PARTIE I — INTRODUCTION AU MACHINE LEARNING

## 1. Qu'est-ce que le Machine Learning ?

### 📖 Définition

Le **Machine Learning** (apprentissage automatique) est une branche de l'intelligence artificielle où un programme **apprend des schémas à partir de données** — au lieu d'être explicitement programmé avec des règles.

> 💡 **Analogie** : Imaginez apprendre à un enfant à reconnaître un chat. Vous ne lui donnez pas une liste de règles ("si 4 pattes ET moustaches ET oreilles pointues alors chat"). Vous lui **montrez des centaines d'exemples** de chats, et son cerveau apprend tout seul à les reconnaître. Le Machine Learning fonctionne pareil : on **montre des données** au modèle, et il apprend les schémas par lui-même.

### 1.1 Programmation classique vs Machine Learning

```
PROGRAMMATION CLASSIQUE                MACHINE LEARNING
─────────────────────────             ─────────────────────────
Données + Règles → Réponses           Données + Réponses → Règles
                                       (le modèle DÉCOUVRE les règles)

Exemple : calculer une TVA            Exemple : prédire un prix immobilier
(on connaît la formule)               (on montre des milliers de ventes,
                                        le modèle apprend la "formule")
```

### 1.2 Les grandes familles de Machine Learning

```
MACHINE LEARNING
│
├── 🎯 APPRENTISSAGE SUPERVISÉ (ce chapitre)
│   → On a des données AVEC les réponses (labels)
│   ├── Régression   → prédire un NOMBRE (prix, température, note)
│   └── Classification → prédire une CATÉGORIE (spam/pas spam, espèce de fleur)
│
├── 🔍 APPRENTISSAGE NON SUPERVISÉ
│   → On a des données SANS réponses
│   └── Clustering → regrouper des données similaires (segments clients)
│
└── 🎮 APPRENTISSAGE PAR RENFORCEMENT
    → Un agent apprend par essai-erreur avec des récompenses
    └── Exemples : jeux, robotique, voitures autonomes
```

### 1.3 Régression vs Classification

Les trois algorithmes de ce chapitre relèvent de l'**apprentissage supervisé** :

| Type | Objectif | Sortie | Exemple | Algorithmes du chapitre |
|------|----------|--------|---------|--------------------------|
| **Régression** | Prédire une valeur continue | Un nombre | Prédire une note (0-20) | Régression linéaire |
| **Classification** | Prédire une catégorie | Une classe | Reconnaître une espèce de fleur | Arbre de décision, KNN |

> 🔑 **Régression = combien ?** (un nombre) — **Classification = lequel ?** (une catégorie)

---

## 2. Le vocabulaire et le workflow ML

### 2.1 Le vocabulaire essentiel

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Features (X)** | Les variables d'entrée (prédicteurs) | heures d'étude, âge |
| **Target (y)** | La variable à prédire (cible) | la note obtenue |
| **Modèle** | L'algorithme entraîné | la régression linéaire |
| **Entraînement (fit)** | Apprendre les schémas sur les données | `model.fit(X, y)` |
| **Prédiction (predict)** | Utiliser le modèle sur de nouvelles données | `model.predict(X)` |
| **Train set** | Données d'apprentissage (~80%) | pour entraîner |
| **Test set** | Données de test (~20%) | pour évaluer honnêtement |
| **Overfitting** | Le modèle "mémorise" au lieu d'apprendre | mauvais sur nouvelles données |

### 2.2 Le workflow ML universel

```
WORKFLOW MACHINE LEARNING
│
1. 📂 COLLECTER les données          → (chapitres précédents : scraping, fichiers)
        │
2. 🧹 NETTOYER & EXPLORER            → (Pandas : cleaning, exploration)
        │
3. ✂️  SÉPARER train / test          → train_test_split()
        │
4. 🎓 ENTRAÎNER le modèle            → model.fit(X_train, y_train)
        │
5. 🔮 PRÉDIRE                        → model.predict(X_test)
        │
6. 📏 ÉVALUER                        → comparer prédictions vs réalité
        │
7. 🔧 AMÉLIORER                      → ajuster, changer de modèle...
```

### 2.3 Pourquoi séparer train et test ?

> 💡 **Analogie** : Séparer train/test, c'est comme réviser un examen. On étudie sur des **exercices d'entraînement** (train set), mais on est évalué sur des **questions nouvelles** (test set) qu'on n'a jamais vues. Si on donnait les questions d'examen à l'avance, la note ne refléterait pas les vraies connaissances — c'est ce qu'on appelle la **triche**, l'équivalent de l'**overfitting** en ML.

```python
from sklearn.model_selection import train_test_split

# 80% pour entraîner, 20% pour tester
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% pour le test
    random_state=42      # reproductibilité
)
```

---

## 3. Scikit-learn : la bibliothèque de référence

### 📖 Présentation

**Scikit-learn** (`sklearn`) est LA bibliothèque de Machine Learning en Python. Elle offre des dizaines d'algorithmes avec une **interface unifiée et cohérente** — une fois qu'on sait utiliser un modèle, on sait les utiliser tous.

### 3.1 L'interface unifiée de Scikit-learn

Tous les modèles suivent le **même schéma en 3 étapes** :

```python
from sklearn.un_module import UnModele

# 1. CRÉER le modèle
model = UnModele()

# 2. ENTRAÎNER (fit)
model.fit(X_train, y_train)

# 3. PRÉDIRE (predict)
predictions = model.predict(X_test)
```

> 🔑 **La grande force de Scikit-learn** : cette interface `fit()` / `predict()` est **identique** pour la régression linéaire, les arbres de décision, le KNN, et tous les autres algorithmes. Apprendre un modèle = savoir en utiliser des centaines.

### 3.2 Installation et import

```python
!pip install scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
```

---

# PARTIE II — LA RÉGRESSION LINÉAIRE

## 4. Qu'est-ce que la régression linéaire ?

### 📖 Définition

La **régression linéaire** est l'algorithme de Machine Learning le plus simple et le plus fondamental. Elle **prédit une valeur numérique** en modélisant la relation entre les variables d'entrée et la cible par une **ligne droite**.

> 💡 **Analogie** : Vous avez remarqué que plus vous étudiez, meilleures sont vos notes. Si vous traciez tous vos résultats sur un graphique (heures d'étude en X, note en Y), vous pourriez tracer **une ligne droite** qui suit la tendance générale. Cette ligne vous permet de **prédire** : "si j'étudie 10h, j'aurai probablement environ 15/20". C'est exactement ce que fait la régression linéaire.

### 4.1 Illustration visuelle

```
Note
 20 │                              •
    │                        •  ╱
 15 │                  •  ╱ •          ← la DROITE suit la tendance
    │            •  ╱ •                   des points
 10 │      •  ╱ •
    │  • ╱ •
  5 │╱ •
    └──────────────────────────────── Heures d'étude
    0    2    4    6    8   10   12

La régression linéaire trouve LA MEILLEURE droite qui passe
au plus près de tous les points.
```

### 4.2 Pourquoi la régression linéaire est-elle importante ?

```
IMPORTANCE DE LA RÉGRESSION LINÉAIRE
│
├── 🎓 Fondamentale    → base de nombreux algorithmes plus complexes
├── 💡 Interprétable   → on comprend POURQUOI le modèle prédit ce qu'il prédit
├── ⚡ Rapide          → s'entraîne quasi instantanément
├── 📊 Polyvalente     → prix, ventes, températures, notes, tendances...
└── 🧱 Pédagogique     → parfaite pour comprendre les concepts du ML
```

---

## 5. Comment fonctionne la régression linéaire ?

### 5.1 L'idée centrale

La régression linéaire cherche à tracer une **droite** qui **minimise l'écart** entre les valeurs réelles et les valeurs prédites. Cette droite devient le "modèle".

### 5.2 Premier exemple pratique

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Données : heures d'étude (X) et notes (y)
np.random.seed(42)
heures = np.random.rand(100, 1) * 12          # 100 étudiants, 0 à 12h
notes = 1.3 * heures.flatten() + 3 + np.random.randn(100) * 1.5

# Séparer train/test
X_train, X_test, y_train, y_test = train_test_split(
    heures, notes, test_size=0.2, random_state=42
)

# Créer et entraîner le modèle
modele = LinearRegression()
modele.fit(X_train, y_train)

# Le modèle a appris la droite : y = pente × x + ordonnée
print(f"Pente (coefficient) : {modele.coef_[0]:.2f}")
print(f"Ordonnée à l'origine : {modele.intercept_:.2f}")

# Prédire
nouvelle_heure = [[10]]
prediction = modele.predict(nouvelle_heure)
print(f"Note prédite pour 10h d'étude : {prediction[0]:.1f}/20")
```

**Résultat typique :**
```
Pente (coefficient) : 1.29
Ordonnée à l'origine : 3.12
Note prédite pour 10h d'étude : 16.0/20
```

> 🔑 Le modèle a **appris tout seul** que chaque heure d'étude supplémentaire ajoute environ 1.3 point à la note — c'est la **pente** de la droite.

---

## 6. La droite de meilleur ajustement (Best-Fit Line)

### 6.1 L'objectif de la droite de meilleur ajustement

La **droite de meilleur ajustement** (best-fit line) est la droite qui passe **au plus près de tous les points** de données. C'est le cœur de la régression linéaire.

> 💡 Parmi une infinité de droites possibles, une seule minimise la distance totale aux points : c'est celle que l'algorithme recherche.

### 6.2 L'équation de la droite

```
      y = β₀ + β₁ × x

où :
  y   = valeur prédite (ex : la note)
  x   = variable d'entrée (ex : heures d'étude)
  β₀  = ordonnée à l'origine (intercept) → où la droite coupe l'axe Y
  β₁  = pente (coefficient) → de combien y augmente quand x augmente de 1
```

**Correspondance avec le code :**
```python
modele.intercept_   # β₀ (ordonnée à l'origine)
modele.coef_[0]     # β₁ (pente)
```

### 6.3 Minimiser l'erreur : la méthode des moindres carrés

La droite optimale est trouvée par la **méthode des moindres carrés** (Least Squares) : on cherche la droite qui **minimise la somme des carrés des écarts** entre points réels et droite.

```
Pourquoi les CARRÉS des écarts ?

Point réel •
           │  ← écart (résidu) = distance entre le point et la droite
           │
───────────�●──────────── droite prédite
           point prédit

On élève chaque écart au CARRÉ (pour :
  1. rendre tous les écarts positifs
  2. pénaliser fortement les grosses erreurs)
puis on cherche la droite qui minimise la SOMME de ces carrés.
```

```
SSE = Σ (y_réel - y_prédit)²    ← à MINIMISER

La droite de meilleur ajustement = celle qui rend cette somme la plus petite possible.
```

### 6.4 Interprétation de la droite

```python
# Exemple d'interprétation concrète
# Si le modèle donne : note = 3.12 + 1.29 × heures

# → β₀ = 3.12 : un étudiant qui n'étudie pas (0h) aurait environ 3.12/20
# → β₁ = 1.29 : chaque heure d'étude supplémentaire ajoute ~1.29 point

# Prédiction pour 8 heures :
note_predite = 3.12 + 1.29 * 8
print(f"Note prédite : {note_predite:.1f}")   # 13.4/20
```

### 6.5 Limites de la droite de meilleur ajustement

```
⚠️ LIMITES
│
├── Suppose une relation LINÉAIRE (une droite) — inadaptée aux courbes
├── Sensible aux OUTLIERS (une valeur extrême déforme la droite)
├── Ne capture pas les relations complexes/non linéaires
└── L'extrapolation hors des données observées est risquée
```

---

## 7. Les hypothèses de la régression linéaire

Pour que la régression linéaire soit **fiable**, plusieurs hypothèses doivent idéalement être respectées.

### 7.1 Vue d'ensemble des hypothèses

| # | Hypothèse | Signification |
|---|-----------|----------------|
| 1 | **Linéarité** | La relation entre X et y est bien linéaire (une droite) |
| 2 | **Indépendance des erreurs** | Les erreurs ne sont pas liées entre elles |
| 3 | **Homoscédasticité** | La variance des erreurs est constante |
| 4 | **Normalité des erreurs** | Les erreurs suivent une distribution normale |
| 5 | **Pas de multicolinéarité** | (régression multiple) les variables X ne sont pas trop corrélées entre elles |
| 6 | **Pas d'autocorrélation** | (séries temporelles) les erreurs successives sont indépendantes |
| 7 | **Additivité** | L'effet total est la somme des effets individuels |

### 7.2 Explication des hypothèses clés

**1. Linéarité** — La relation doit ressembler à une droite. Si les données forment une courbe, la régression linéaire échouera.

**2. Indépendance des erreurs** — L'erreur sur un point ne doit pas dépendre de l'erreur sur un autre point.

**3. Homoscédasticité (variance constante)** — Les erreurs doivent avoir la même dispersion sur toute la plage de données.

```
✅ HOMOSCÉDASTICITÉ (bon)            ❌ HÉTÉROSCÉDASTICITÉ (problème)
   erreurs de taille constante        erreurs qui grandissent
   • • • • • • • •                     •  •   •    •      •
  ─────────────────                   ─────────────────────
   • • • • • • • •                     •  •   •    •      •
```

**4. Normalité des erreurs** — Les résidus (écarts) doivent suivre une courbe en cloche.

**5. Pas de multicolinéarité** — En régression multiple, deux variables d'entrée ne doivent pas être trop corrélées (ex : "taille en cm" et "taille en m" apporteraient la même information).

**6. Pas d'autocorrélation** — Important pour les séries temporelles : l'erreur d'aujourd'hui ne doit pas prédire celle de demain.

**7. Additivité** — L'effet de chaque variable s'additionne (pas d'interactions cachées non modélisées).

> 💡 En pratique, ces hypothèses sont rarement toutes parfaitement respectées. On les vérifie et on ajuste le modèle si nécessaire — mais pour débuter, l'essentiel est de comprendre la **linéarité** et l'impact des **outliers**.

---

## 8. Types de régression linéaire

### 8.1 Régression linéaire simple

**Une seule** variable d'entrée pour prédire la cible.

**Formule :**
```
y = β₀ + β₁ × x
```

**Exemple :** prédire la note (`y`) à partir des heures d'étude (`x`) uniquement.

```python
from sklearn.linear_model import LinearRegression

# UNE seule feature : les heures d'étude
X = df[["heures_etude"]]      # note : double crochet → DataFrame 2D
y = df["note_sql"]

modele = LinearRegression()
modele.fit(X, y)
print(f"note = {modele.intercept_:.2f} + {modele.coef_[0]:.2f} × heures")
```

### 8.2 Régression linéaire multiple

**Plusieurs** variables d'entrée pour prédire la cible.

**Formule :**
```
y = β₀ + β₁×x₁ + β₂×x₂ + β₃×x₃ + ... + βₙ×xₙ
```

**Cas d'usage :** prédire un prix immobilier à partir de la surface, du nombre de pièces, de l'emplacement, de l'année de construction... (plusieurs facteurs simultanés).

```python
# PLUSIEURS features
X = df[["heures_etude", "age", "note_python"]]   # 3 variables d'entrée
y = df["note_sql"]

modele = LinearRegression()
modele.fit(X, y)

# Un coefficient par variable
for nom, coef in zip(X.columns, modele.coef_):
    print(f"{nom} : {coef:.3f}")
print(f"Ordonnée : {modele.intercept_:.3f}")
```

> 🔑 En régression multiple, chaque coefficient indique l'effet d'**une** variable, **toutes les autres étant maintenues constantes**.

---

## 9. Métriques d'évaluation de la régression

Comment savoir si notre modèle de régression est bon ? On mesure l'écart entre les prédictions et la réalité.

### 9.1 Les principales métriques

| Métrique | Formule (idée) | Interprétation |
|----------|-----------------|----------------|
| **MAE** | Moyenne des \|erreurs\| | Erreur moyenne en valeur absolue |
| **MSE** | Moyenne des erreurs² | Pénalise les grosses erreurs |
| **RMSE** | √MSE | Erreur dans l'unité d'origine (interprétable) |
| **R²** | Proportion de variance expliquée | De 0 à 1 : plus proche de 1 = meilleur |

### 9.2 En pratique

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

predictions = modele.predict(X_test)

mae  = mean_absolute_error(y_test, predictions)
mse  = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, predictions)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.3f}")
```

### 9.3 Comprendre le R²

```
R² (coefficient de détermination)
│
├── R² = 1.0   → le modèle explique 100% de la variance (parfait)
├── R² = 0.8   → le modèle explique 80% de la variance (bon)
├── R² = 0.5   → le modèle explique 50% (moyen)
└── R² = 0.0   → le modèle n'explique rien (inutile)
```

> 💡 **Interprétation du R²** : un R² de 0.75 signifie que 75% de la variation de la cible est expliquée par le modèle. Les 25% restants sont dus à d'autres facteurs non capturés.

---

## 10. Avantages et inconvénients de la régression linéaire

### 10.1 Avantages

```
✅ AVANTAGES
│
├── Simple à comprendre et à implémenter
├── Très rapide à entraîner
├── Interprétable (on comprend chaque coefficient)
├── Peu de données nécessaires
└── Bonne baseline (point de comparaison de départ)
```

### 10.2 Inconvénients

```
❌ INCONVÉNIENTS
│
├── Suppose une relation linéaire (limitée pour les relations complexes)
├── Très sensible aux outliers
├── Suppose l'indépendance des variables
└── Sous-performante face à des modèles plus avancés sur des données complexes
```

---

# PARTIE III — LES ARBRES DE DÉCISION

## 11. Qu'est-ce qu'un arbre de décision ?

### 📖 Définition

Un **arbre de décision** est un algorithme qui prend des décisions en posant une **série de questions** de type "oui/non", organisées en arborescence. Il peut faire de la **classification** (prédire une catégorie) ou de la **régression** (prédire un nombre).

> 💡 **Analogie** : Un arbre de décision fonctionne comme un **jeu de "Qui est-ce ?"**. Pour deviner un personnage, vous posez une série de questions : "Porte-t-il des lunettes ?" → oui → "A-t-il une barbe ?" → non → etc. Chaque réponse vous rapproche de la bonne réponse. L'arbre de décision fait exactement ça avec les données.

### 11.1 Structure d'un arbre

```
                  [Heures d'étude > 8 ?]        ← RACINE (première question)
                    ╱              ╲
                 OUI              NON
                  ╱                ╲
        [Note Python > 15?]      [Bon niveau]   ← NŒUDS / FEUILLES
           ╱          ╲
        OUI          NON
         ╱            ╲
   [Excellent]    [Moyen]                        ← FEUILLES (décisions finales)
```

| Élément | Rôle |
|---------|------|
| **Racine** | La première question (en haut) |
| **Nœud interne** | Une question intermédiaire |
| **Branche** | Une réponse (oui/non) |
| **Feuille** | Une décision/prédiction finale |

---

## 12. Comment fonctionnent les arbres de décision ?

### 12.1 Le principe

L'arbre **divise progressivement** les données en groupes de plus en plus "purs" (homogènes), en choisissant à chaque étape la **question qui sépare le mieux** les données.

### 12.2 Exemple pratique

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Séparer train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Créer et entraîner l'arbre
arbre = DecisionTreeClassifier(max_depth=3, random_state=42)
arbre.fit(X_train, y_train)

# Prédire et évaluer
predictions = arbre.predict(X_test)
print(f"Précision : {accuracy_score(y_test, predictions):.3f}")
```

### 12.3 Visualiser l'arbre (grand atout !)

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 8))
plot_tree(arbre, filled=True, feature_names=X.columns, class_names=True)
plt.show()
```

> 🔑 L'un des grands avantages de l'arbre de décision : on peut **le visualiser entièrement** et comprendre exactement comment il prend ses décisions. C'est un modèle **"boîte blanche"** (transparent), contrairement aux réseaux de neurones ("boîte noire").

---

## 13. Critères de division et élagage

### 13.1 Critères de division (Splitting Criteria)

À chaque nœud, l'arbre doit choisir **quelle question poser**. Il utilise des critères mathématiques pour mesurer la "pureté" des groupes créés.

| Critère | Utilisé pour | Idée |
|---------|--------------|------|
| **Indice de Gini** | Classification | Mesure l'impureté (0 = pur) |
| **Entropie / Gain d'information** | Classification | Mesure le désordre |
| **MSE / variance** | Régression | Minimise l'erreur dans chaque groupe |

```
IDÉE DE LA PURETÉ (indice de Gini)
│
Groupe PUR (Gini = 0)          Groupe IMPUR (Gini élevé)
🔵🔵🔵🔵🔵                       🔵🔴🔵🔴🔵
tous identiques                mélange de classes
→ excellente division          → mauvaise division
```

> 💡 L'arbre choisit à chaque étape la question qui **maximise la pureté** des groupes résultants — c'est-à-dire celle qui sépare le mieux les classes.

### 13.2 L'élagage (Pruning) — Éviter l'overfitting

Un arbre laissé libre peut devenir **trop profond** et "mémoriser" les données d'entraînement (overfitting). L'**élagage** consiste à **limiter sa croissance** pour qu'il généralise mieux.

```
ARBRE TROP PROFOND (overfitting)      ARBRE ÉLAGUÉ (généralise mieux)
│                                      │
Mémorise chaque détail                 Capture les tendances générales
→ parfait sur le train                 → un peu moins bon sur le train
→ MAUVAIS sur le test                  → MEILLEUR sur le test
```

```python
# Techniques d'élagage via les hyperparamètres
arbre = DecisionTreeClassifier(
    max_depth=4,             # profondeur maximale
    min_samples_split=10,    # minimum d'échantillons pour diviser un nœud
    min_samples_leaf=5,      # minimum d'échantillons dans une feuille
    random_state=42
)
```

> 🔑 **Règle importante** : un arbre plus simple (élagué) est souvent **meilleur** qu'un arbre complexe, car il généralise mieux aux nouvelles données.

---

## 14. Avantages, inconvénients et applications des arbres

### 14.1 Avantages

```
✅ AVANTAGES
│
├── Très interprétable (on peut visualiser l'arbre)
├── Pas besoin de normaliser les données
├── Gère variables numériques ET catégorielles
├── Capture les relations non linéaires
└── Rapide à prédire
```

### 14.2 Inconvénients

```
❌ INCONVÉNIENTS
│
├── Tendance à l'overfitting (sans élagage)
├── Instable (un petit changement de données → arbre différent)
├── Peut créer des arbres biaisés si classes déséquilibrées
└── Moins performant seul que les versions "ensemble" (Random Forest)
```

### 14.3 Applications

```
APPLICATIONS DES ARBRES DE DÉCISION
│
├── 🏦 Finance      → accord de crédit (oui/non)
├── 🏥 Médecine     → aide au diagnostic
├── 📧 Marketing    → segmentation client, ciblage
├── 🏭 Industrie    → détection de pannes
└── 🎯 Général      → tout problème de décision avec règles claires
```

> 💡 Les arbres de décision sont la **brique de base** d'algorithmes très puissants comme les **Random Forests** (forêts d'arbres) et le **Gradient Boosting** (XGBoost), que vous découvrirez plus tard.

---

# PARTIE IV — LES K PLUS PROCHES VOISINS (KNN)

## 15. Qu'est-ce que le KNN et le "K" ?

### 📖 Définition

Le **KNN** (K-Nearest Neighbors, K plus proches voisins) classe une nouvelle donnée en regardant les **K exemples les plus proches** dans les données d'entraînement, et en prenant la **classe majoritaire** parmi eux.

> 💡 **Analogie** : "Dis-moi qui sont tes amis, je te dirai qui tu es." Pour classer un nouvel étudiant, le KNN regarde les K étudiants qui lui ressemblent le plus (ses "voisins" les plus proches en termes de caractéristiques) et lui attribue la catégorie la plus fréquente parmi eux.

### 15.1 Le "K" dans KNN

Le **K** est le **nombre de voisins** que l'on consulte pour prendre la décision.

```
EXEMPLE : classer le point ? (K=3)
│
        🔵                    Les 3 plus proches voisins de ? sont :
     🔵    ?  🔴              → 🔵 (bleu)
        🔵      🔴            → 🔵 (bleu)
                              → 🔴 (rouge)
                              Majorité = BLEU → ? est classé BLEU
```

```
Avec K=3 : on regarde les 3 voisins → vote majoritaire
Avec K=5 : on regarde les 5 voisins → vote majoritaire
Avec K=1 : on prend juste le voisin le plus proche
```

---

## 16. Comment choisir la valeur de K ?

### 16.1 L'impact de K

```
K TROP PETIT (ex: K=1)              K TROP GRAND (ex: K=100)
│                                    │
Très sensible au bruit               Trop "lissé", ignore les détails
→ overfitting                        → underfitting
→ frontières irrégulières            → frontières trop simples
```

> 🔑 Il faut trouver le **bon équilibre** : ni trop petit (sensible au bruit), ni trop grand (perd les nuances).

### 16.2 Méthodes pour choisir K

```
COMMENT CHOISIR K ?
│
├── 📏 Règle empirique  → K ≈ √(nombre d'échantillons)
├── 🔢 K impair         → évite les égalités de vote (pour 2 classes)
├── 📊 Validation croisée → tester plusieurs K et garder le meilleur
└── 📉 Courbe d'erreur   → tracer l'erreur en fonction de K (méthode du coude)
```

### 16.3 Trouver le meilleur K par validation

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Tester plusieurs valeurs de K
scores = {}
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores[k] = accuracy_score(y_test, knn.predict(X_test))

# Meilleur K
meilleur_k = max(scores, key=scores.get)
print(f"Meilleur K : {meilleur_k} (précision : {scores[meilleur_k]:.3f})")
```

### 16.4 Méthodes statistiques pour sélectionner K

- **Validation croisée (Cross-Validation)** : diviser les données en plusieurs plis, tester chaque K sur tous les plis et moyenner — la méthode la plus fiable.
- **Méthode du coude (Elbow Method)** : tracer l'erreur en fonction de K et choisir le point où l'erreur cesse de diminuer significativement.

---

## 17. Les métriques de distance en KNN

### 📖 Comment mesurer la "proximité" ?

Le KNN a besoin de mesurer la **distance** entre les points pour trouver les voisins. Plusieurs formules existent.

### 17.1 Les principales distances

| Distance | Formule (idée) | Usage |
|----------|-----------------|-------|
| **Euclidienne** | Distance "à vol d'oiseau" | La plus courante (par défaut) |
| **Manhattan** | Distance "en damier" (blocs) | Données à grille, haute dimension |
| **Minkowski** | Généralisation des deux | Paramétrable |

```
DISTANCE EUCLIDIENNE vs MANHATTAN
│
Point A •                          Euclidienne : ligne droite A→B
        │╲                          Manhattan : somme des trajets
        │ ╲ (euclidienne)                       horizontaux + verticaux
        │  ╲
        │   ╲
        └────• Point B
      (manhattan = ─── + │)
```

```python
# La distance se choisit via le paramètre "metric"
knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")   # par défaut
knn = KNeighborsClassifier(n_neighbors=5, metric="manhattan")
```

### 17.2 ⚠️ L'importance cruciale de la normalisation

Le KNN étant basé sur les **distances**, les variables à grande échelle **dominent** le calcul. Il est **essentiel** de normaliser les données.

```
SANS NORMALISATION                   AVEC NORMALISATION
│                                     │
salaire (0-750000) écrase            Toutes les variables sur la
note (0-20) dans le calcul           même échelle (0-1 ou centrées)
de distance                          → chaque variable compte équitablement
→ KNN faussé                         → KNN correct
```

```python
from sklearn.preprocessing import StandardScaler

# TOUJOURS normaliser avant un KNN !
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)   # même transformation (pas de fit !)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
```

> 🔑 **Piège classique** : on `fit_transform` sur le train, mais seulement `transform` sur le test (avec le scaler entraîné sur le train). Sinon, on "triche" en utilisant les infos du test.

---

## 18. Fonctionnement, avantages et applications du KNN

### 18.1 Le fonctionnement étape par étape

```
ALGORITHME KNN (pour classer un nouveau point)
│
1. Calculer la DISTANCE entre le nouveau point et TOUS les points d'entraînement
2. TRIER ces distances de la plus petite à la plus grande
3. SÉLECTIONNER les K points les plus proches
4. VOTER : la classe majoritaire parmi les K voisins est la prédiction
```

### 18.2 Une particularité : le "lazy learning"

> 💡 Le KNN est un algorithme "**paresseux**" (lazy learner) : il **ne construit pas de modèle** pendant l'entraînement. Il se contente de **mémoriser** toutes les données, et fait tout le calcul **au moment de la prédiction**. C'est l'inverse de la régression linéaire (qui apprend une formule) ou de l'arbre (qui construit une structure).

### 18.3 Avantages

```
✅ AVANTAGES
│
├── Très simple à comprendre
├── Aucun entraînement (mémorise juste les données)
├── S'adapte naturellement à de nouvelles données
├── Fonctionne pour classification ET régression
└── Aucune hypothèse sur la distribution des données
```

### 18.4 Inconvénients

```
❌ INCONVÉNIENTS
│
├── LENT en prédiction sur de gros jeux (calcule toutes les distances)
├── Nécessite OBLIGATOIREMENT la normalisation
├── Sensible aux variables non pertinentes
├── Consomme beaucoup de mémoire (stocke tout)
└── Souffre de la "malédiction de la dimension" (trop de features)
```

### 18.5 Applications

```
APPLICATIONS DU KNN
│
├── 🎬 Recommandation    → "les clients similaires ont aimé..."
├── 🖼️  Reconnaissance    → images, écriture manuscrite
├── 💳 Détection fraude  → transactions similaires suspectes
├── 🏥 Médecine          → diagnostic par similarité de cas
└── 📊 Imputation        → remplir les valeurs manquantes par voisins
```

---

# PARTIE V — SYNTHÈSE

## 19. Comparaison des trois algorithmes

### 19.1 Tableau comparatif

| Critère | Régression linéaire | Arbre de décision | KNN |
|---------|---------------------|---------------------|-----|
| **Type** | Régression | Classif. + Régression | Classif. + Régression |
| **Prédit** | Un nombre | Catégorie ou nombre | Catégorie ou nombre |
| **Entraînement** | Rapide | Rapide | Aucun (paresseux) |
| **Prédiction** | Très rapide | Très rapide | Lente (gros datasets) |
| **Interprétabilité** | Excellente | Excellente (visualisable) | Faible |
| **Normalisation requise** | Recommandée | Non | **Obligatoire** |
| **Relations non linéaires** | ❌ Non | ✅ Oui | ✅ Oui |
| **Sensible aux outliers** | ✅ Très | Moyennement | ✅ Oui |
| **Idéal pour débuter** | ✅✅✅ | ✅✅ | ✅✅ |

### 19.2 Quel algorithme choisir ?

```
GUIDE DE CHOIX
│
├── Prédire un NOMBRE avec relation linéaire  → RÉGRESSION LINÉAIRE
├── Besoin d'EXPLIQUER les décisions          → ARBRE DE DÉCISION
├── Classification simple, peu de données     → KNN
├── Relations complexes non linéaires         → ARBRE ou KNN
└── En pratique : TESTER plusieurs modèles et comparer !
```

> 🔑 **Principe fondamental du ML** : il n'existe pas de "meilleur algorithme universel". On teste plusieurs modèles sur ses données et on garde celui qui performe le mieux (c'est le théorème du "No Free Lunch").

---

## 20. Conclusion

### 📌 Récapitulatif du chapitre

```
ALGORITHMES DE MACHINE LEARNING
│
├── Concepts fondamentaux
│   ├── Supervisé : régression (nombre) vs classification (catégorie)
│   ├── Features (X) → Target (y)
│   ├── Workflow : collecter → nettoyer → split → fit → predict → évaluer
│   └── Interface Scikit-learn : model.fit() puis model.predict()
│
├── Régression linéaire
│   ├── Trouve la droite de meilleur ajustement (moindres carrés)
│   ├── y = β₀ + β₁x (simple) ou multiple
│   └── Évaluée par R², RMSE, MAE
│
├── Arbre de décision
│   ├── Série de questions oui/non
│   ├── Critères : Gini, entropie
│   ├── Élagage pour éviter l'overfitting
│   └── Interprétable et visualisable
│
└── KNN
    ├── Vote des K plus proches voisins
    ├── Choix de K crucial (√n, validation)
    ├── Distances : euclidienne, manhattan
    └── NORMALISATION obligatoire
```

### 🔑 Points clés à retenir

1. Le ML **apprend des schémas** à partir de données au lieu d'être programmé avec des règles.
2. Toujours **séparer train/test** pour évaluer honnêtement (éviter l'overfitting).
3. Scikit-learn offre une interface **unifiée** : `fit()` puis `predict()` pour tous les modèles.
4. La **régression linéaire** prédit des nombres via une droite (moindres carrés, R²).
5. Les **arbres de décision** posent des questions successives et sont très interprétables (attention à l'élagage).
6. Le **KNN** classe par vote des voisins — la **normalisation est obligatoire**.
7. Il n'y a **pas de meilleur algorithme universel** : on teste et on compare.

### 🗺️ Ce qui vient ensuite

Le prochain document est le **Checkpoint 5 : Entraîner et évaluer un modèle sur le dataset Iris** — un projet pratique complet où vous appliquerez ces trois algorithmes sur le jeu de données le plus célèbre du Machine Learning. Ensuite viendront les modèles plus avancés (Random Forests, régression logistique) et l'optimisation des hyperparamètres.

---

## 21. ✅ Point de contrôle — Machine Learning

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre la régression et la classification ?

<details>
<summary>👀 Voir la réponse</summary>

> La **régression** prédit une **valeur numérique continue** (un nombre : prix, température, note). La **classification** prédit une **catégorie** (une classe : spam/pas spam, espèce de fleur). Résumé : régression = "combien ?", classification = "lequel ?".
</details>

---

**Q2.** Pourquoi sépare-t-on les données en train set et test set ?

<details>
<summary>👀 Voir la réponse</summary>

> Pour évaluer **honnêtement** le modèle sur des données qu'il n'a **jamais vues** pendant l'entraînement. Si on évaluait sur les données d'entraînement, un modèle qui "mémorise" (overfitting) aurait un score parfait mais serait mauvais en réalité. Le test set simule les "nouvelles données" du monde réel.
</details>

---

**Q3.** Qu'est-ce que la droite de meilleur ajustement et comment est-elle trouvée ?

<details>
<summary>👀 Voir la réponse</summary>

> C'est la droite qui passe **au plus près de tous les points** de données. Elle est trouvée par la **méthode des moindres carrés** : on cherche la droite qui **minimise la somme des carrés des écarts** (résidus) entre les points réels et la droite. Son équation est y = β₀ + β₁x.
</details>

---

**Q4.** Qu'est-ce que l'élagage (pruning) d'un arbre de décision et pourquoi est-il utile ?

<details>
<summary>👀 Voir la réponse</summary>

> L'élagage consiste à **limiter la croissance** d'un arbre (via `max_depth`, `min_samples_leaf`...) pour l'empêcher de devenir trop profond. Un arbre trop profond **mémorise** les données d'entraînement (overfitting) et généralise mal. Un arbre élagué est plus simple, capture les tendances générales, et **performe mieux sur les nouvelles données**.
</details>

---

**Q5.** Pourquoi la normalisation est-elle obligatoire pour le KNN ?

<details>
<summary>👀 Voir la réponse</summary>

> Le KNN se base sur les **distances** entre points. Sans normalisation, les variables à grande échelle (ex : un salaire de 0 à 750000) **écrasent** les variables à petite échelle (ex : une note de 0 à 20) dans le calcul de distance. La normalisation ramène toutes les variables à la même échelle pour qu'elles contribuent **équitablement** à la mesure de proximité.
</details>

---

**Q6.** Comment choisir la valeur de K en KNN ?

<details>
<summary>👀 Voir la réponse</summary>

> Plusieurs méthodes : la **règle empirique** K ≈ √(nombre d'échantillons), choisir un **K impair** pour éviter les égalités de vote, ou surtout utiliser la **validation croisée** (tester plusieurs K et garder celui qui donne la meilleure performance moyenne). Un K trop petit sur-apprend (sensible au bruit), un K trop grand sous-apprend (trop lissé).
</details>

---

### 💻 Exercices pratiques

> Ces exercices utilisent des données synthétiques ou `bootcamp_500.csv`. Le projet complet sur Iris fait l'objet du Checkpoint 5.

---

**Exercice 1 — Régression linéaire simple**

Créez une régression linéaire prédisant `note_sql` à partir de `heures_etude` sur `bootcamp_500.csv` (nettoyé). Affichez la pente, l'ordonnée et le R².

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("bootcamp_500.csv")
df.loc[df["note_sql"] > 20, "note_sql"] = np.nan
df = df.dropna(subset=["note_sql", "heures_etude"])

X = df[["heures_etude"]]
y = df["note_sql"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modele = LinearRegression().fit(X_train, y_train)
print(f"Pente : {modele.coef_[0]:.3f}")
print(f"Ordonnée : {modele.intercept_:.3f}")
print(f"R² : {r2_score(y_test, modele.predict(X_test)):.3f}")
```
</details>

---

**Exercice 2 — Régression multiple**

Prédisez `note_sql` à partir de `heures_etude`, `age` ET `note_python`. Affichez les coefficients de chaque variable.

<details>
<summary>👀 Voir la solution</summary>

```python
df2 = df.dropna(subset=["note_sql", "note_python", "heures_etude", "age"])
X = df2[["heures_etude", "age", "note_python"]]
y = df2["note_sql"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modele = LinearRegression().fit(X_train, y_train)

for nom, coef in zip(X.columns, modele.coef_):
    print(f"{nom} : {coef:.3f}")
print(f"R² : {modele.score(X_test, y_test):.3f}")
```
</details>

---

**Exercice 3 — Arbre de décision**

Créez un arbre de décision (`max_depth=3`) pour prédire le `niveau` à partir de `heures_etude`, `note_sql`, `note_python`. Affichez la précision.

<details>
<summary>👀 Voir la solution</summary>

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df3 = df.dropna(subset=["note_sql", "note_python", "heures_etude"])
X = df3[["heures_etude", "note_sql", "note_python"]]
y = df3["niveau"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
arbre = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print(f"Précision : {accuracy_score(y_test, arbre.predict(X_test)):.3f}")
```
</details>

---

**Exercice 4 — KNN avec normalisation**

Créez un KNN (k=5) pour prédire le `niveau`, en **normalisant** les données. Comparez avec/sans normalisation.

<details>
<summary>👀 Voir la solution</summary>

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df4 = df.dropna(subset=["note_sql", "note_python", "heures_etude", "salaire_stage"])
X = df4[["heures_etude", "note_sql", "note_python", "salaire_stage"]]
y = df4["niveau"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sans normalisation
knn_brut = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
print(f"Sans normalisation : {accuracy_score(y_test, knn_brut.predict(X_test)):.3f}")

# Avec normalisation
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
knn_norm = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)
print(f"Avec normalisation : {accuracy_score(y_test, knn_norm.predict(X_test_s)):.3f}")
# → la normalisation améliore nettement le score (à cause de salaire_stage)
```
</details>

---

**Exercice 5 — Trouver le meilleur K**

Testez K de 1 à 20 pour un KNN et identifiez la valeur optimale.

<details>
<summary>👀 Voir la solution</summary>

```python
scores = {}
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
    scores[k] = accuracy_score(y_test, knn.predict(X_test_s))

meilleur_k = max(scores, key=scores.get)
print(f"Meilleur K : {meilleur_k} (précision : {scores[meilleur_k]:.3f})")
```
</details>

---

### 🏆 Challenge bonus — Comparer les trois algorithmes

Sur `bootcamp_500.csv`, prédisez le `niveau` avec les **trois** approches applicables (arbre de décision et KNN — la régression linéaire ne convient pas pour prédire une catégorie) et déterminez laquelle est la plus performante. Justifiez pourquoi la régression linéaire n'est pas adaptée ici.

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("bootcamp_500.csv")
df.loc[df["note_sql"] > 20, "note_sql"] = np.nan
df = df.dropna(subset=["note_sql", "note_python", "heures_etude"])

X = df[["heures_etude", "note_sql", "note_python"]]
y = df["niveau"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Arbre de décision
arbre = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
acc_arbre = accuracy_score(y_test, arbre.predict(X_test))

# KNN (avec normalisation)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)
acc_knn = accuracy_score(y_test, knn.predict(X_test_s))

print(f"Arbre de décision : {acc_arbre:.3f}")
print(f"KNN (k=5)         : {acc_knn:.3f}")
print(f"\nMeilleur : {'Arbre' if acc_arbre > acc_knn else 'KNN'}")

print('''
Pourquoi PAS la régression linéaire ici ?
→ 'niveau' est une CATÉGORIE (Débutant/Intermédiaire/Avancé),
  pas un nombre. La régression linéaire prédit des valeurs continues,
  elle est donc inadaptée à un problème de CLASSIFICATION.
  (Pour classer, on utiliserait plutôt la régression LOGISTIQUE.)
''')
```
</details>

---

*📘 Module Data Science — Algorithmes de Machine Learning | Bootcamp Data Science*
