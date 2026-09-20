# 🔎 Data Exploration with Pandas — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : NumPy, File Handling, Data Cleaning with Pandas

---

## Table des matières

1. [Introduction to Data Exploration](#1-introduction-to-data-exploration)
2. [Initial Data Analysis with Pandas](#2-initial-data-analysis-with-pandas)
3. [Handling Missing Data — Valeurs manquantes](#3-handling-missing-data--valeurs-manquantes)
4. [Outliers — Valeurs aberrantes](#4-outliers--valeurs-aberrantes)
5. [Data Anomalies — Anomalies de données](#5-data-anomalies--anomalies-de-données)
6. [Data Encoding — Encodage des variables](#6-data-encoding--encodage-des-variables)
7. [Exploratory Data Analysis (EDA) with Pandas](#7-exploratory-data-analysis-eda-with-pandas)
8. [Conclusion](#8-conclusion)
9. [Data Pre-processing Checkpoint — Projet](#9-data-pre-processing-checkpoint--projet)
10. [✅ Point de contrôle — Data Exploration](#10--point-de-contrôle--data-exploration)

---

## 1. Introduction to Data Exploration

### 📖 Qu'est-ce que l'exploration de données ?

L'**exploration de données** (Data Exploration) est l'étape où l'on **examine, comprend et diagnostique** un jeu de données **avant** de l'analyser en profondeur ou de construire un modèle. C'est le moment où l'on "fait connaissance" avec ses données.

> 💡 **Analogie** : L'exploration de données, c'est comme un **médecin qui examine un patient avant tout traitement**. Il prend la température, écoute le cœur, pose des questions, fait des analyses. Il ne prescrit pas de médicament avant d'avoir posé un diagnostic. De même, un Data Scientist n'entraîne pas de modèle avant d'avoir exploré et compris ses données.

### 1.1 Data Cleaning vs Data Exploration — Quelle différence ?

```
CHAPITRE PRÉCÉDENT              CE CHAPITRE
─────────────────────           ─────────────────────
Data Cleaning                   Data Exploration
(corriger les problèmes)        (comprendre et diagnostiquer)
    │                                │
    ▼                                ▼
COMMENT réparer :               QUOI regarder et POURQUOI :
- supprimer les doublons        - quelles distributions ?
- remplir les manquants         - quelles corrélations ?
- convertir les types           - quelles anomalies/outliers ?
                                - quelle structure globale ?
```

> 🔑 En pratique, exploration et nettoyage sont **entremêlés** : on explore pour découvrir les problèmes, on nettoie pour les corriger, puis on ré-explore pour vérifier. C'est un **cycle itératif**.

### 1.2 Le pipeline Data Science — Où se situe l'exploration ?

```
1. COLLECTE       → scraping, fichiers, bases de données
        │
        ▼
2. EXPLORATION    → 🔎 CE CHAPITRE : comprendre les données
        │
        ▼
3. NETTOYAGE      → corriger les problèmes découverts
        │
        ▼
4. PRÉPARATION    → encodage, normalisation
        │
        ▼
5. MODÉLISATION   → Machine Learning
        │
        ▼
6. ÉVALUATION     → mesurer la performance
```

### 1.3 Les questions clés de l'exploration

```
QUESTIONS À SE POSER LORS DE L'EXPLORATION
│
├── 📏 Structure     → Combien de lignes/colonnes ? Quels types ?
├── 🕳️  Complétude    → Y a-t-il des valeurs manquantes ? Combien ?
├── 📊 Distribution  → Comment les valeurs sont-elles réparties ?
├── 🎯 Anomalies     → Y a-t-il des valeurs aberrantes ou incohérentes ?
├── 🔗 Relations     → Les variables sont-elles corrélées entre elles ?
└── ⚖️  Équilibre     → Les catégories sont-elles bien représentées ?
```

---

## 2. Initial Data Analysis with Pandas

L'**analyse initiale** (Initial Data Analysis, IDA) consiste à obtenir une **vue d'ensemble rapide** du jeu de données avec quelques commandes Pandas essentielles.

### 2.1 Le jeu de données d'exemple

Pour ce chapitre, nous utilisons un **vrai jeu de données de 510 lignes** : `bootcamp_500.csv`. Il simule les inscriptions d'un bootcamp Data Science en Afrique de l'Ouest, avec de **véritables problèmes** (valeurs manquantes, outliers, doublons, anomalies de casse...) — bien plus représentatif que quelques lignes écrites à la main.

> 💡 **Pourquoi un gros fichier ?** Les outils d'exploration (statistiques, distributions, détection d'outliers, corrélations) ne révèlent leur véritable utilité que sur un **volume conséquent** de données. Sur 7 lignes, un histogramme ou une matrice de corrélation n'ont aucun sens.

```python
import pandas as pd
import numpy as np

# Charger le jeu de données (téléchargez d'abord bootcamp_500.csv dans Colab)
df = pd.read_csv("bootcamp_500.csv")

# Les 10 colonnes :
# id_etudiant, prenom, nom, age, ville, niveau,
# heures_etude, note_sql, note_python, salaire_stage
```

### 2.2 Les commandes d'analyse initiale

```python
# Dimensions du jeu de données
print(df.shape)          # (510, 10) → 510 lignes, 10 colonnes

# Aperçu des premières/dernières lignes
df.head()
df.tail()

# Résumé technique : types, valeurs non nulles, mémoire
df.info()

# Statistiques descriptives des colonnes numériques
df.describe()

# Statistiques des colonnes textuelles (catégorielles)
df.describe(include="object")

# Noms et types de chaque colonne
df.dtypes
```

**`df.info()` — le diagnostic n°1 :**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 510 entries, 0 to 509
Data columns (total 10 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   id_etudiant    510 non-null    int64
 1   prenom         510 non-null    object
 2   nom            510 non-null    object
 3   age            510 non-null    int64
 4   ville          495 non-null    object    ← 495 sur 510 → 15 valeurs manquantes !
 5   niveau         510 non-null    object
 6   heures_etude   510 non-null    float64
 7   note_sql       485 non-null    float64   ← 485 sur 510 → 25 valeurs manquantes !
 8   note_python    490 non-null    float64   ← 490 sur 510 → 20 valeurs manquantes !
 9   salaire_stage  510 non-null    int64
```

**`df.describe()` — les statistiques révèlent déjà les outliers :**
```
              age  heures_etude  note_sql  note_python  salaire_stage
count      510.00        510.00    485.00       490.00         510.00
mean        31.41          8.09      9.03         8.93       78358.48
std         13.94          2.96      4.10         3.91       52505.96
min         -5.00          0.00      0.00         0.00       22956.00   ← age = -5 impossible !
25%         24.00          6.10      6.30         6.30       55181.25
50%         31.00          8.05      8.80         9.00       73499.00
max        200.00         17.60     30.00        20.00      750000.00   ← age=200, note=30 !
```

> 🔑 **Rien qu'avec `describe()`**, on repère déjà plusieurs anomalies : un âge minimum de **-5** et maximum de **200** (impossibles), une note SQL max de **30** (alors que le maximum devrait être 20), et un salaire max de **750 000** très éloigné de la médiane (73 499) — des outliers à investiguer.

> 🔑 `df.info()` révèle immédiatement **deux informations cruciales** : les types de chaque colonne, et le nombre de valeurs non nulles (qui trahit les valeurs manquantes).

### 2.3 Explorer les variables catégorielles

```python
# Compter les valeurs uniques d'une colonne catégorielle
print(df["ville"].value_counts())

# Nombre de valeurs uniques
print(df["ville"].nunique())

# Liste des valeurs uniques
print(df["niveau"].unique())

# Proportion de chaque catégorie (%)
print(df["niveau"].value_counts(normalize=True) * 100)
```

**`df["ville"].value_counts()` — les anomalies sautent aux yeux :**
```
Abidjan        126
Dakar           83
Bamako          60
Cotonou         49
Accra           42
Lomé            37
Conakry         29
Ouagadougou     29
  Abidjan        9    ← même ville, avec des espaces !
ABIDJAN          6    ← même ville, en majuscules !
abidjan          5    ← même ville, en minuscules !
  Dakar          4
bamako           3
  Bamako         2
```

> 🔑 `value_counts()` révèle immédiatement un problème **d'anomalie de casse/espaces** : "Abidjan", "  Abidjan", "ABIDJAN" et "abidjan" sont comptés comme **4 villes différentes**, alors que c'est la même ! Nous corrigerons cela en section 5 (Data Anomalies).

### 2.4 Explorer les variables numériques

```python
# Statistiques individuelles
print("Moyenne âge :", df["age"].mean())
print("Médiane âge :", df["age"].median())
print("Écart type  :", df["age"].std())
print("Min / Max   :", df["age"].min(), "/", df["age"].max())

# Quartiles
print(df["age"].quantile([0.25, 0.5, 0.75]))
```

---

## 3. Handling Missing Data — Valeurs manquantes

### 📖 Pourquoi les valeurs manquantes posent-elles problème ?

Les valeurs manquantes (`NaN`, `None`) sont **omniprésentes** dans les données réelles (erreurs de saisie, capteurs défaillants, réponses non fournies...). Elles peuvent **fausser les calculs** et **faire échouer** les algorithmes de Machine Learning, qui n'acceptent généralement pas de valeurs manquantes.

### 3.1 Détecter les valeurs manquantes

```python
# Combien de valeurs manquantes par colonne ?
print(df.isna().sum())

# Pourcentage de valeurs manquantes par colonne
print((df.isna().sum() / len(df) * 100).round(2))

# Y a-t-il AU MOINS une valeur manquante dans le DataFrame ?
print(df.isna().any().any())

# Visualiser les lignes contenant des valeurs manquantes
print(df[df.isna().any(axis=1)])
```

**Résultat sur `bootcamp_500.csv` :**
```
isna().sum()              % manquants
─────────────             ─────────────
ville           15        ville           2.94
note_sql        25        note_sql        4.90
note_python     20        note_python     3.92
(les autres à 0)          (les autres à 0.00)
```

> 🔑 Sur un vrai jeu de données, on voit tout de suite que trois colonnes ont des valeurs manquantes : `ville` (2.94%), `note_sql` (4.90%) et `note_python` (3.92%). Des pourcentages faibles (< 5%) qui permettent l'imputation sans trop de risque.

### 3.2 Les stratégies de traitement

```
QUE FAIRE DES VALEURS MANQUANTES ?
│
├── 🗑️  SUPPRIMER
│   ├── dropna()  → supprimer les lignes concernées
│   └── Quand : peu de manquants, ou données non critiques
│
├── 🩹 IMPUTER (remplacer)
│   ├── Numérique   → moyenne, médiane
│   ├── Catégoriel  → mode (valeur la plus fréquente)
│   └── Temporel    → valeur précédente/suivante (ffill/bfill)
│
└── 🏷️  MARQUER
    └── Créer une colonne "était_manquant" (True/False)
        pour ne pas perdre l'information de l'absence
```

### 3.3 Imputation numérique — Moyenne vs Médiane

```python
# Imputer par la MOYENNE (sensible aux valeurs extrêmes)
df["note_python_moy"] = df["note_python"].fillna(df["note_python"].mean())

# Imputer par la MÉDIANE (robuste aux valeurs extrêmes — souvent préférable)
df["note_python_med"] = df["note_python"].fillna(df["note_python"].median())
```

> 💡 **Moyenne ou médiane ?** Si la colonne contient des **valeurs aberrantes** (outliers), la **médiane** est préférable car elle n'est pas tirée vers le haut/bas par les extrêmes. Exemple : pour des salaires où quelques personnes gagnent des millions, la médiane représente mieux le "salaire typique" que la moyenne.

### 3.4 Imputation catégorielle — Le mode

```python
# Pour une colonne catégorielle, on impute par le MODE (valeur la plus fréquente)
mode_ville = df["ville"].mode()[0]     # [0] car mode() retourne une Series
df["ville"] = df["ville"].fillna(mode_ville)
print(f"Ville imputée par le mode : {mode_ville}")
```

### 3.5 Marquer avant d'imputer (bonne pratique)

```python
# Conserver l'information que la valeur était manquante
df["python_etait_manquant"] = df["note_python"].isna()

# Puis imputer
df["note_python"] = df["note_python"].fillna(df["note_python"].median())
```

> 🔑 Marquer l'absence **avant** d'imputer permet au modèle de Machine Learning de savoir que cette valeur a été "inventée" — parfois, le fait qu'une donnée soit manquante est en soi une information utile !

---

## 4. Outliers — Valeurs aberrantes

### 📖 Qu'est-ce qu'un outlier ?

Un **outlier** (valeur aberrante) est une valeur **anormalement éloignée** des autres. Cela peut être une **erreur** (un âge de 150 ans) ou une **vraie valeur extrême mais rare** (un salaire de PDG).

> 💡 **Analogie** : Dans une classe où tout le monde mesure entre 1m50 et 1m90, une personne enregistrée à **12 mètres** est clairement une erreur de saisie (outlier). Mais si dans un jeu de données de salaires, une personne gagne 100× la moyenne, ce n'est pas forcément une erreur — c'est un outlier **réel** qu'il faut traiter avec prudence.

### 4.1 Détecter visuellement — Le boxplot (boîte à moustaches)

```python
import matplotlib.pyplot as plt

# Le boxplot révèle visuellement les outliers (points isolés)
df.boxplot(column=["age"])
plt.title("Détection d'outliers sur l'âge")
plt.show()
```

```
STRUCTURE D'UN BOXPLOT
                    outlier
                       •           ← point isolé = valeur aberrante
        ┌─────┬─────┐
   ─────┤     │     ├─────         ← "moustaches" (min/max normaux)
        └─────┴─────┘
        Q1   médiane  Q3
        └── 50% des données ──┘
```

### 4.2 Détecter avec la méthode IQR (Interquartile Range)

La méthode la plus courante pour détecter les outliers numériquement.

```python
# Calcul de l'IQR (écart interquartile)
Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)
IQR = Q3 - Q1

# Bornes : au-delà, une valeur est considérée comme outlier
borne_basse = Q1 - 1.5 * IQR
borne_haute = Q3 + 1.5 * IQR

print(f"Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}")
print(f"Bornes normales : [{borne_basse}, {borne_haute}]")

# Identifier les outliers
outliers = df[(df["age"] < borne_basse) | (df["age"] > borne_haute)]
print("Outliers détectés :")
print(outliers[["prenom", "nom", "age"]])
```

**Résultat sur `bootcamp_500.csv` :**
```
Q1 = 24.0, Q3 = 38.0, IQR = 14.0
Bornes normales : [3.0, 59.0]

Outliers détectés (âges) : -5, -1, 0, 150, 175, 200
→ 6 valeurs aberrantes, toutes des âges impossibles (erreurs de saisie évidentes)
```

**Visualisation de la règle IQR :**
```
   borne_basse                              borne_haute
   Q1 - 1.5×IQR         Q1 ─── Q3          Q3 + 1.5×IQR
        │                │       │               │
────────┼────────────────█████████────────────────┼──────────•───►
     OUTLIERS        (données normales)        OUTLIERS    outlier
     (trop bas)                                (trop haut)  (age=150)
```

### 4.3 Détecter avec le Z-score

Le Z-score mesure **à combien d'écarts-types** une valeur se situe de la moyenne. Au-delà de ±3, on parle généralement d'outlier.

```python
# Z-score = (valeur - moyenne) / écart-type
df["z_score_age"] = (df["age"] - df["age"].mean()) / df["age"].std()

# Outliers : |z-score| > 3
outliers_z = df[df["z_score_age"].abs() > 3]
print(outliers_z[["nom", "age", "z_score_age"]])
```

### 4.4 Traiter les outliers

```
QUE FAIRE DES OUTLIERS ?
│
├── 🔍 INVESTIGUER d'abord  → Erreur de saisie ou vraie valeur ?
│
├── 🗑️  SUPPRIMER            → Si c'est une erreur manifeste (age=150)
│
├── 🔧 CORRIGER             → Si on connaît la vraie valeur
│
├── 📐 PLAFONNER (capping)  → Remplacer par la borne (winsorisation)
│
└── ✋ CONSERVER            → Si c'est une vraie valeur importante
```

```python
# Exemple : supprimer un outlier manifeste (age=150)
df_propre = df[df["age"] <= borne_haute]

# Exemple : plafonner (capping) au lieu de supprimer
df["age_plafonne"] = df["age"].clip(lower=borne_basse, upper=borne_haute)
print(df[["nom", "age", "age_plafonne"]])
```

> ⚠️ **Ne supprimez JAMAIS un outlier sans réfléchir.** Demandez-vous toujours : est-ce une erreur, ou une vraie valeur rare mais légitime ? Supprimer de vraies valeurs extrêmes peut biaiser votre analyse.

---

## 5. Data Anomalies — Anomalies de données

### 📖 Au-delà des outliers : les incohérences

Les **anomalies de données** englobent tous les problèmes de **qualité** qui ne sont pas forcément des valeurs numériques aberrantes : incohérences de format, valeurs impossibles, doublons cachés, catégories mal orthographiées...

### 5.1 Types d'anomalies courantes

| Type d'anomalie | Exemple | Comment détecter |
|-------------------|---------|-------------------|
| **Incohérence de casse** | `"abidjan"`, `"Abidjan"`, `"ABIDJAN"` | `.value_counts()` |
| **Espaces superflus** | `"  Abidjan  "` | `.str.strip()` puis comparer |
| **Valeurs impossibles** | âge négatif, note > 20 | filtres booléens |
| **Format incohérent** | dates `"2024-01-15"` vs `"15/01/2024"` | inspection visuelle |
| **Doublons cachés** | même personne, orthographe différente | `.duplicated()` |
| **Catégories rares/typos** | `"Débutant"` vs `"debutant"` | `.value_counts()` |

### 5.2 Détecter les incohérences de casse et d'espaces

```python
villes = pd.Series(["Abidjan", "abidjan", "ABIDJAN", "  Abidjan", "Dakar"])

# Avant nettoyage : 5 valeurs "différentes"
print("Avant :")
print(villes.value_counts())

# Après normalisation : les variantes fusionnent
villes_propres = villes.str.strip().str.title()
print("\nAprès :")
print(villes_propres.value_counts())
```

### 5.3 Détecter les valeurs impossibles (règles métier)

```python
df = pd.DataFrame({
    "nom"  : ["Alice", "Bob", "Claire", "David"],
    "age"  : [23, -5, 22, 200],           # -5 et 200 impossibles
    "note" : [16, 14, 25, 18]             # 25 impossible (max = 20)
})

# Détecter les âges impossibles
ages_invalides = df[(df["age"] < 0) | (df["age"] > 120)]
print("Âges invalides :\n", ages_invalides)

# Détecter les notes impossibles
notes_invalides = df[(df["note"] < 0) | (df["note"] > 20)]
print("\nNotes invalides :\n", notes_invalides)
```

### 5.4 Détecter les catégories mal orthographiées

```python
niveaux = pd.Series(["Débutant", "debutant", "Débutant", "Avancé", "avance", "Intermédiaire"])

# value_counts() révèle les variantes d'une même catégorie
print(niveaux.value_counts())
# "Débutant" et "debutant" devraient être la même catégorie !

# Corriger via un dictionnaire de mapping
correction = {"debutant": "Débutant", "avance": "Avancé"}
niveaux_propres = niveaux.replace(correction)
print("\nAprès correction :")
print(niveaux_propres.value_counts())
```

---

## 6. Data Encoding — Encodage des variables

### 📖 Pourquoi encoder ?

Les algorithmes de Machine Learning ne comprennent **que des nombres**. Il faut donc **convertir les variables catégorielles** (texte) en représentations numériques. C'est l'**encodage**.

> 💡 **Analogie** : Un modèle de Machine Learning est comme une **calculatrice** — il ne sait faire que des maths. Vous ne pouvez pas lui demander de calculer avec le mot "Abidjan". Il faut d'abord **traduire** "Abidjan" en un nombre qu'il peut manipuler.

### 6.1 Variables catégorielles — Deux types

```
VARIABLES CATÉGORIELLES
│
├── ORDINALES (avec un ORDRE naturel)
│   → "Débutant" < "Intermédiaire" < "Avancé"
│   → Encodage : Label Encoding (0, 1, 2)
│
└── NOMINALES (SANS ordre)
    → "Abidjan", "Dakar", "Accra" (aucune n'est "supérieure")
    → Encodage : One-Hot Encoding
```

### 6.2 Label Encoding — Pour les variables ordinales

Attribue un **nombre entier** à chaque catégorie, en respectant l'ordre.

```python
df = pd.DataFrame({
    "nom"    : ["Alice", "Bob", "Claire", "David"],
    "niveau" : ["Débutant", "Avancé", "Intermédiaire", "Avancé"]
})

# Méthode 1 : mapping manuel (contrôle total de l'ordre)
ordre_niveaux = {"Débutant": 0, "Intermédiaire": 1, "Avancé": 2}
df["niveau_encode"] = df["niveau"].map(ordre_niveaux)
print(df)
```

**Résultat :**
```
      nom          niveau  niveau_encode
0   Alice        Débutant              0
1     Bob          Avancé              2
2  Claire   Intermédiaire              1
3   David          Avancé              2
```

```python
# Méthode 2 : type catégoriel ordonné de Pandas
df["niveau"] = pd.Categorical(
    df["niveau"],
    categories=["Débutant", "Intermédiaire", "Avancé"],
    ordered=True
)
df["niveau_code"] = df["niveau"].cat.codes
print(df)
```

### 6.3 One-Hot Encoding — Pour les variables nominales

Crée une **colonne binaire (0/1) par catégorie**. Utilisé quand il n'y a **pas d'ordre** entre les catégories.

```python
df = pd.DataFrame({
    "nom"   : ["Alice", "Bob", "Claire", "David"],
    "ville" : ["Abidjan", "Dakar", "Accra", "Abidjan"]
})

# pd.get_dummies() fait le One-Hot Encoding
df_encode = pd.get_dummies(df, columns=["ville"])
print(df_encode)
```

**Résultat :**
```
      nom  ville_Abidjan  ville_Accra  ville_Dakar
0   Alice           True        False        False
1     Bob          False        False         True
2  Claire          False         True        False
3   David           True        False        False
```

> 💡 Chaque ville devient une colonne. Pour Alice (Abidjan), `ville_Abidjan=1` et les autres à 0. Aucune ville n'est "supérieure" à une autre — c'est parfait pour des variables nominales.

### 6.4 Pourquoi ne PAS utiliser Label Encoding sur des variables nominales ?

```python
# ❌ MAUVAIS : Label Encoding sur des villes (nominales)
villes_encode = {"Abidjan": 0, "Dakar": 1, "Accra": 2}
# → Le modèle croirait que Accra (2) > Dakar (1) > Abidjan (0)
# → Il inventerait un ORDRE qui n'existe pas ! Cela fausse le modèle.

# ✅ BON : One-Hot Encoding — aucune hiérarchie inventée
```

### 6.5 Tableau récapitulatif de l'encodage

| Situation | Méthode | Fonction Pandas |
|-----------|---------|------------------|
| Variable **ordinale** (avec ordre) | Label Encoding | `.map()` ou `pd.Categorical` |
| Variable **nominale** (sans ordre) | One-Hot Encoding | `pd.get_dummies()` |
| Variable **binaire** (2 valeurs) | Mapping 0/1 | `.map({"Oui": 1, "Non": 0})` |

---

## 7. Exploratory Data Analysis (EDA) with Pandas

### 📖 Qu'est-ce que l'EDA ?

L'**Analyse Exploratoire des Données** (EDA) est l'approche qui consiste à **résumer, visualiser et découvrir des tendances** dans les données à l'aide de statistiques et de graphiques. C'est la synthèse de tout ce chapitre.

> On travaille ici directement sur le vrai jeu de données `bootcamp_500.csv` (chargé en section 2), idéalement après un premier nettoyage des valeurs impossibles.

### 7.1 EDA univariée — Analyser une variable à la fois

```python
# Variable numérique : statistiques + distribution
print(df["note_sql"].describe())

# Variable catégorielle : fréquences
print(df["niveau"].value_counts())
```

```python
import matplotlib.pyplot as plt

# Histogramme d'une variable numérique (500 lignes → distribution lisible !)
df["note_sql"].hist(bins=20)
plt.title("Distribution des notes SQL")
plt.xlabel("Note")
plt.ylabel("Fréquence")
plt.show()

# Diagramme en barres d'une variable catégorielle
df["niveau"].value_counts().plot(kind="bar")
plt.title("Nombre d'étudiants par niveau")
plt.show()
```

> 💡 Avec 510 lignes, l'histogramme révèle une **vraie forme de distribution** (ici, les notes SQL suivent grossièrement une courbe en cloche) — ce qui serait impossible à voir sur 7 lignes.

### 7.2 EDA bivariée — Relations entre deux variables

```python
# Corrélation entre deux variables numériques
print(df[["heures_etude", "note_sql"]].corr())

# Moyenne d'une variable numérique par catégorie (groupby)
print(df.groupby("niveau")["note_sql"].mean())

# Tableau croisé (crosstab)
print(pd.crosstab(df["niveau"], df["ville"]))
```

```python
# Nuage de points : relation heures d'étude / note SQL
df.plot(kind="scatter", x="heures_etude", y="note_sql", alpha=0.5)
plt.title("Relation heures d'étude / note SQL")
plt.show()
```

> 💡 Sur le nuage de points de 510 étudiants, on **voit clairement** la tendance : plus les heures d'étude augmentent, plus les notes montent — une relation invisible sur un petit échantillon.

### 7.3 La matrice de corrélation

La corrélation mesure **à quel point deux variables évoluent ensemble** (de -1 à +1).

```python
# Matrice de corrélation sur toutes les colonnes numériques
df_num = df[["age", "heures_etude", "note_sql", "note_python", "salaire_stage"]]
correlation = df_num.corr()
print(correlation.round(2))
```

**Résultat sur `bootcamp_500.csv` (après nettoyage des âges aberrants) :**
```
               heures_etude  note_sql  note_python   age  salaire_stage
heures_etude           1.00      0.79         0.78 -0.01           0.06
note_sql               0.79      1.00         0.84 -0.02           0.02
note_python            0.78      0.84         1.00 -0.00           0.05
age                   -0.01     -0.02        -0.00  1.00          -0.03
salaire_stage          0.06      0.02         0.05 -0.03           1.00
```

**Interprétation des coefficients de corrélation :**
```
+1.0  → corrélation positive parfaite (les deux augmentent ensemble)
+0.7  → forte corrélation positive
 0.0  → aucune corrélation
-0.7  → forte corrélation négative (l'une monte, l'autre descend)
-1.0  → corrélation négative parfaite
```

> 💡 **Lecture de notre matrice** :
> - `heures_etude` ↔ `note_sql` = **0.79** → forte corrélation : plus on étudie, meilleure est la note (logique !)
> - `note_sql` ↔ `note_python` = **0.84** → très forte : un bon étudiant l'est dans les deux matières
> - `age` ↔ notes = **~0.00** → aucune corrélation : l'âge n'a aucun lien avec les résultats
> - `salaire_stage` ↔ notes = **~0.00** → aucune corrélation ici

> ⚠️ **Corrélation ≠ Causalité !** Deux variables corrélées n'impliquent pas que l'une cause l'autre. C'est l'un des pièges les plus importants en Data Science.

### 7.4 Le workflow EDA complet

```
WORKFLOW EDA
│
├── 1. Vue d'ensemble    → shape, info(), describe()
├── 2. Valeurs manquantes → isna().sum()
├── 3. Distributions      → histogrammes, value_counts()
├── 4. Outliers           → boxplot, IQR
├── 5. Anomalies          → valeurs impossibles, incohérences
├── 6. Relations          → corr(), groupby, scatter plots
└── 7. Synthèse           → documenter les découvertes et décisions
```

---

## 8. Conclusion

### 📌 Récapitulatif du chapitre

```
DATA EXPLORATION WITH PANDAS
│
├── Analyse initiale (IDA)
│   └── shape, head(), info(), describe(), value_counts()
│
├── Valeurs manquantes
│   ├── Détecter  → isna().sum()
│   └── Traiter   → dropna(), fillna(moyenne/médiane/mode)
│
├── Outliers (valeurs aberrantes)
│   ├── Détecter  → boxplot, méthode IQR, Z-score
│   └── Traiter   → supprimer, plafonner (clip), conserver
│
├── Anomalies
│   └── Casse, espaces, valeurs impossibles, doublons cachés
│
├── Encodage
│   ├── Ordinal  → Label Encoding (.map)
│   └── Nominal  → One-Hot Encoding (get_dummies)
│
└── EDA
    ├── Univariée   → une variable (histogramme, value_counts)
    ├── Bivariée    → deux variables (corr, scatter, groupby)
    └── Corrélation → corr() (attention : ≠ causalité)
```

### 🔑 Points clés à retenir

1. L'exploration **précède** l'analyse et la modélisation — on comprend avant d'agir.
2. `df.info()` et `df.describe()` sont les **premiers réflexes** face à un nouveau jeu de données.
3. Pour imputer, la **médiane** est plus robuste que la moyenne en présence d'outliers.
4. Les **outliers** se détectent avec le boxplot, la méthode IQR ou le Z-score — mais il faut toujours **investiguer** avant de supprimer.
5. **Label Encoding** pour les variables ordinales (avec ordre), **One-Hot Encoding** pour les nominales (sans ordre).
6. La **corrélation** révèle des relations, mais **corrélation ≠ causalité**.

### 🗺️ Ce qui vient ensuite

Vous maîtrisez maintenant tout le cycle de préparation des données : collecte (scraping/fichiers), nettoyage, exploration et pré-traitement. La prochaine étape logique est la **visualisation avancée** (Matplotlib/Seaborn) puis le **Machine Learning** avec Scikit-learn — où toutes ces données soigneusement préparées serviront enfin à construire des modèles prédictifs.

---

## 9. Data Pre-processing Checkpoint — Projet

### 🎯 Objectif du projet

Réaliser un **pipeline complet de pré-traitement** sur le vrai jeu de données `bootcamp_500.csv` (510 lignes, avec tous ses problèmes), en appliquant **toutes** les compétences du chapitre : exploration, valeurs manquantes, outliers, anomalies, et encodage.

```python
import pandas as pd
import numpy as np

# ============================================
# ÉTAPE 0 : Charger le jeu de données brut (510 lignes)
# ============================================
df = pd.read_csv("bootcamp_500.csv")

print("=== JEU DE DONNÉES BRUT ===")
print(df.head())
print(f"Dimensions : {df.shape}")


# ============================================
# ÉTAPE 1 : Exploration initiale
# ============================================
print("\n=== ÉTAPE 1 : EXPLORATION ===")
print("Valeurs manquantes :")
print(df.isna().sum())
print("\nStatistiques numériques :")
print(df.describe().round(2))


# ============================================
# ÉTAPE 2 : Corriger les anomalies (casse, espaces sur les villes)
# ============================================
print("\n=== ÉTAPE 2 : ANOMALIES ===")
print("Villes AVANT nettoyage :", df["ville"].nunique(), "valeurs uniques")
df["ville"] = df["ville"].str.strip().str.title()
print("Villes APRÈS nettoyage :", df["ville"].nunique(), "valeurs uniques")
# → le nombre de villes uniques diminue car les variantes (ABIDJAN, abidjan...) fusionnent


# ============================================
# ÉTAPE 3 : Traiter les valeurs impossibles (outliers/anomalies)
# ============================================
print("\n=== ÉTAPE 3 : VALEURS IMPOSSIBLES ===")
# Un âge doit être entre 15 et 100 pour un bootcamp
nb_ages_invalides = ((df["age"] < 15) | (df["age"] > 100)).sum()
print(f"Âges invalides détectés : {nb_ages_invalides}")
df.loc[(df["age"] < 15) | (df["age"] > 100), "age"] = np.nan

# Une note doit être entre 0 et 20
nb_notes_invalides = (df["note_sql"] > 20).sum()
print(f"Notes SQL invalides (>20) détectées : {nb_notes_invalides}")
df.loc[df["note_sql"] > 20, "note_sql"] = np.nan


# ============================================
# ÉTAPE 4 : Imputer les valeurs manquantes (médiane = robuste)
# ============================================
print("\n=== ÉTAPE 4 : IMPUTATION ===")
df["age"]         = df["age"].fillna(df["age"].median())
df["note_sql"]    = df["note_sql"].fillna(df["note_sql"].median())
df["note_python"] = df["note_python"].fillna(df["note_python"].median())
df["ville"]       = df["ville"].fillna(df["ville"].mode()[0])
print("Valeurs manquantes après imputation :", df.isna().sum().sum())


# ============================================
# ÉTAPE 5 : Supprimer les doublons
# ============================================
print("\n=== ÉTAPE 5 : DOUBLONS ===")
avant = len(df)
df = df.drop_duplicates().reset_index(drop=True)
print(f"Doublons supprimés : {avant - len(df)}")


# ============================================
# ÉTAPE 6 : Encodage des variables catégorielles
# ============================================
print("\n=== ÉTAPE 6 : ENCODAGE ===")
# niveau = ORDINAL → Label Encoding
ordre = {"Débutant": 0, "Intermédiaire": 1, "Avancé": 2}
df["niveau_encode"] = df["niveau"].map(ordre)

# ville = NOMINAL → One-Hot Encoding
df_final = pd.get_dummies(df, columns=["ville"], prefix="ville")

print(f"Nombre de colonnes finales : {len(df_final.columns)}")


# ============================================
# ÉTAPE 7 : Résultat final et sauvegarde
# ============================================
print("\n=== JEU DE DONNÉES PRÉ-TRAITÉ (prêt pour le ML) ===")
print(f"Dimensions finales : {df_final.shape}")
print(df_final.head())

df_final.to_csv("bootcamp_500_pretraite.csv", index=False, encoding="utf-8")
print("\n✅ Données pré-traitées sauvegardées dans bootcamp_500_pretraite.csv")
```

> 💡 **Résultat attendu** : après le pipeline, on passe de 510 lignes "sales" (15+25+20 valeurs manquantes, 6 âges impossibles, 3 notes > 20, 10 doublons, villes en casse incohérente) à un jeu de données **entièrement propre et numérique** — prêt pour Scikit-learn.

> 💡 **Ce projet illustre le pré-traitement complet** que subit tout jeu de données **avant** d'entraîner un modèle de Machine Learning : nettoyage des anomalies → traitement des valeurs impossibles → imputation → suppression des doublons → encodage. À la fin, toutes les colonnes sont numériques et propres — prêtes pour Scikit-learn.

---

## 10. ✅ Point de contrôle — Data Exploration

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre Data Cleaning et Data Exploration ?

<details>
<summary>👀 Voir la réponse</summary>

> Le **Data Cleaning** consiste à **corriger** les problèmes des données (supprimer doublons, remplir valeurs manquantes, convertir types). La **Data Exploration** consiste à **comprendre et diagnostiquer** les données (distributions, corrélations, anomalies) pour décider quoi corriger et comment analyser. En pratique, les deux sont entremêlés dans un cycle itératif.
</details>

---

**Q2.** Pourquoi préfère-t-on parfois imputer par la médiane plutôt que par la moyenne ?

<details>
<summary>👀 Voir la réponse</summary>

> La **médiane** est **robuste aux valeurs aberrantes** (outliers), contrairement à la moyenne qui est tirée vers le haut ou le bas par les valeurs extrêmes. Par exemple, pour des salaires où quelques personnes gagnent des millions, la médiane représente mieux le "salaire typique". En présence d'outliers, la médiane est donc un meilleur choix pour l'imputation.
</details>

---

**Q3.** Expliquez la méthode IQR pour détecter les outliers.

<details>
<summary>👀 Voir la réponse</summary>

> La méthode IQR (Interquartile Range) calcule l'écart entre le 3e quartile (Q3) et le 1er quartile (Q1) : `IQR = Q3 - Q1`. Une valeur est considérée comme outlier si elle est **inférieure à Q1 - 1.5×IQR** ou **supérieure à Q3 + 1.5×IQR**. C'est la méthode utilisée par le boxplot pour afficher les points aberrants.
</details>

---

**Q4.** Quelle est la différence entre Label Encoding et One-Hot Encoding, et quand utiliser chacun ?

<details>
<summary>👀 Voir la réponse</summary>

> Le **Label Encoding** attribue un entier à chaque catégorie (0, 1, 2...) — à utiliser pour les variables **ordinales** (avec un ordre naturel, ex : Débutant < Intermédiaire < Avancé). Le **One-Hot Encoding** crée une colonne binaire par catégorie — à utiliser pour les variables **nominales** (sans ordre, ex : villes). Utiliser Label Encoding sur des variables nominales ferait croire au modèle qu'il existe un ordre qui n'existe pas, ce qui fausserait les résultats.
</details>

---

**Q5.** Pourquoi dit-on que "corrélation n'est pas causalité" ?

<details>
<summary>👀 Voir la réponse</summary>

> Deux variables **corrélées** évoluent ensemble statistiquement, mais cela ne signifie **pas** que l'une **cause** l'autre. Il peut y avoir une troisième variable cachée qui explique les deux, ou une simple coïncidence. Par exemple, les ventes de glaces et les noyades sont corrélées (elles augmentent l'été), mais les glaces ne causent pas les noyades — c'est la chaleur qui explique les deux.
</details>

---

### 💻 Exercices pratiques

> Utilisez le fichier `bootcamp_500.csv` (510 lignes, fourni) — idéal pour voir les outils d'exploration en action sur un vrai volume de données. Le fichier `inscriptions_sales.csv` (plus petit) reste utilisable pour des tests rapides.

---

**Exercice 1 — Analyse initiale**

Chargez un jeu de données et affichez : ses dimensions, les types de chaque colonne, le nombre de valeurs manquantes par colonne, et les statistiques descriptives.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd

df = pd.read_csv("bootcamp_500.csv")

print("Dimensions :", df.shape)          # (510, 10)
print("\nTypes :\n", df.dtypes)
print("\nValeurs manquantes :\n", df.isna().sum())
print("\nStatistiques :\n", df.describe())
```
</details>

---

**Exercice 2 — Valeurs manquantes**

Pour une colonne numérique de votre jeu de données, calculez le pourcentage de valeurs manquantes, puis imputez-les par la médiane.

<details>
<summary>👀 Voir la solution</summary>

```python
# Pourcentage de manquants
pct = df["note_sql"].isna().sum() / len(df) * 100
print(f"Valeurs manquantes : {pct:.1f}%")

# Imputation par la médiane
df["note_sql"] = df["note_sql"].fillna(df["note_sql"].median())
print("Après imputation :", df["note_sql"].isna().sum())
```
</details>

---

**Exercice 3 — Détection d'outliers (IQR)**

Avec la Series `ages = pd.Series([23, 25, 22, 28, 24, 150, 26, 21])`, détectez les outliers avec la méthode IQR.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd

ages = pd.Series([23, 25, 22, 28, 24, 150, 26, 21])

Q1 = ages.quantile(0.25)
Q3 = ages.quantile(0.75)
IQR = Q3 - Q1
borne_haute = Q3 + 1.5 * IQR
borne_basse = Q1 - 1.5 * IQR

outliers = ages[(ages < borne_basse) | (ages > borne_haute)]
print(f"Bornes : [{borne_basse}, {borne_haute}]")
print("Outliers :", outliers.tolist())   # [150]
```
</details>

---

**Exercice 4 — Anomalies**

Avec `villes = pd.Series(["Abidjan", "abidjan", "  ABIDJAN  ", "Dakar", "dakar"])`, uniformisez la casse et les espaces, puis comptez les valeurs uniques.

<details>
<summary>👀 Voir la solution</summary>

```python
villes = pd.Series(["Abidjan", "abidjan", "  ABIDJAN  ", "Dakar", "dakar"])

villes_propres = villes.str.strip().str.title()
print(villes_propres.value_counts())
# Abidjan    3
# Dakar      2
```
</details>

---

**Exercice 5 — Encodage**

Vous avez `df = pd.DataFrame({"niveau": ["Débutant", "Avancé", "Intermédiaire", "Débutant"], "ville": ["Abidjan", "Dakar", "Accra", "Abidjan"]})`. Encodez `niveau` avec du Label Encoding (ordinal) et `ville` avec du One-Hot Encoding (nominal).

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "niveau": ["Débutant", "Avancé", "Intermédiaire", "Débutant"],
    "ville": ["Abidjan", "Dakar", "Accra", "Abidjan"]
})

# Label Encoding pour niveau (ordinal)
ordre = {"Débutant": 0, "Intermédiaire": 1, "Avancé": 2}
df["niveau_encode"] = df["niveau"].map(ordre)

# One-Hot Encoding pour ville (nominal)
df_final = pd.get_dummies(df, columns=["ville"])
print(df_final)
```
</details>

---

**Exercice 6 — Corrélation**

Avec le DataFrame suivant, calculez la matrice de corrélation et identifiez la paire de variables la plus fortement corrélée.
```python
df = pd.DataFrame({
    "heures_etude": [10, 6, 12, 4, 11, 7],
    "note": [16, 12, 18, 10, 17, 13],
    "age": [23, 25, 22, 28, 24, 26]
})
```

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "heures_etude": [10, 6, 12, 4, 11, 7],
    "note": [16, 12, 18, 10, 17, 13],
    "age": [23, 25, 22, 28, 24, 26]
})

correlation = df.corr()
print(correlation.round(2))
# heures_etude et note sont très fortement corrélées (~0.99)
# → plus on étudie, meilleure est la note
```
</details>

---

### 🏆 Challenge bonus — Rapport d'exploration complet sur `bootcamp_500.csv`

En repartant du **résultat nettoyé** du Python Project (`bootcamp_500_pretraite.csv`), réalisez une **analyse exploratoire complète** et répondez à ces questions métier :

1. Quelle ville compte le plus d'étudiants ?
2. Quelle est la moyenne des notes SQL par niveau (`groupby`) ? Les "Avancé" ont-ils vraiment de meilleures notes ?
3. Existe-t-il une corrélation entre `heures_etude` et `note_python` ? Quelle est sa valeur ?
4. Tracez l'histogramme des notes SQL et le boxplot de `salaire_stage`.
5. Combien d'étudiants ont une moyenne (note_sql + note_python)/2 ≥ 14 ?

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données nettoyées (issues du Python Project)
df = pd.read_csv("bootcamp_500_pretraite.csv")

# 1. Ville la plus représentée (attention : colonnes one-hot après encodage,
#    on peut aussi repartir de bootcamp_500.csv nettoyé sans encodage)
df_brut = pd.read_csv("bootcamp_500.csv")
df_brut["ville"] = df_brut["ville"].str.strip().str.title()
print("Ville la plus fréquente :", df_brut["ville"].value_counts().idxmax())

# 2. Moyenne des notes SQL par niveau
print(df_brut.groupby("niveau")["note_sql"].mean().round(2))

# 3. Corrélation heures_etude / note_python
df_valide = df_brut[(df_brut["note_python"].notna()) & (df_brut["note_sql"] <= 20)]
print("Corrélation :", df_valide["heures_etude"].corr(df_valide["note_python"]).round(2))

# 4. Visualisations
df_valide["note_sql"].hist(bins=20); plt.title("Notes SQL"); plt.show()
df_valide.boxplot(column=["salaire_stage"]); plt.title("Salaires"); plt.show()

# 5. Étudiants avec moyenne >= 14
df_valide = df_valide.copy()
df_valide["moyenne"] = (df_valide["note_sql"] + df_valide["note_python"]) / 2
print("Étudiants avec moyenne >= 14 :", (df_valide["moyenne"] >= 14).sum())
```
</details>
---

*📘 Module Data Science — Data Exploration with Pandas | Bootcamp Data Science*
