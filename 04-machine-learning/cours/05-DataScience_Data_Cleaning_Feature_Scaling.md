# 🧹 Nettoyage des Données & Mise à l'Échelle — Cours Bootcamp Data Science

> **Module Data Science — Preprocessing** | Prérequis : Pandas, cours "Train/Test Split & Validation Croisée"

---

## Table des matières

### Partie I — Le Nettoyage des Données (Data Cleaning)
1. [Pourquoi nettoyer ? « Garbage in, garbage out »](#1-pourquoi-nettoyer--garbage-in-garbage-out)
2. [Naviguer parmi les problèmes de qualité des données](#2-naviguer-parmi-les-problèmes-de-qualité-des-données)
3. [Les tâches courantes de nettoyage](#3-les-tâches-courantes-de-nettoyage)
   - 3.1 [Gérer les valeurs manquantes](#31-gérer-les-valeurs-manquantes)
   - 3.2 [Supprimer les doublons](#32-supprimer-les-doublons)
   - 3.3 [Corriger les inexactitudes](#33-corriger-les-inexactitudes)
   - 3.4 [Standardiser les formats](#34-standardiser-les-formats)
   - 3.5 [Traiter les valeurs aberrantes (outliers)](#35-traiter-les-valeurs-aberrantes-outliers)
4. [Les étapes d'un nettoyage méthodique](#4-les-étapes-dun-nettoyage-méthodique)
5. [Outils et techniques](#5-outils-et-techniques)
6. [Les défis du nettoyage de données](#6-les-défis-du-nettoyage-de-données)
7. [Bonnes pratiques d'assurance qualité](#7-bonnes-pratiques-dassurance-qualité)

### Partie II — La Mise à l'Échelle des Variables (Feature Scaling)
8. [Pourquoi mettre à l'échelle ? (Why use Feature Scaling ?)](#8-pourquoi-mettre-à-léchelle--why-use-feature-scaling-)
9. [Absolute Maximum Scaling](#9-absolute-maximum-scaling)
10. [Min-Max Scaling](#10-min-max-scaling)
11. [Normalisation (Normalization)](#11-normalisation-normalization)
12. [Standardisation (Standardization)](#12-standardisation-standardization)
13. [RobustScaler et le cas des outliers](#13-robustscaler-et-le-cas-des-outliers)
14. [Quel scaler pour quel algorithme ?](#14-quel-scaler-pour-quel-algorithme-)

### Partie III — Aspects complémentaires (indispensables)
15. [Encodage des variables catégorielles](#15-encodage-des-variables-catégorielles)
16. [Fuite de données : le fit uniquement sur le train](#16-fuite-de-données--le-fit-uniquement-sur-le-train)
17. [Tout automatiser proprement : Pipeline & ColumnTransformer](#17-tout-automatiser-proprement--pipeline--columntransformer)

### Partie IV — Synthèse
18. [Conclusion](#18-conclusion)
19. [✅ Point de contrôle — Preprocessing](#19--point-de-contrôle--preprocessing)

---

# PARTIE I — LE NETTOYAGE DES DONNÉES (DATA CLEANING)

## 1. Pourquoi nettoyer ? « Garbage in, garbage out »

### 📖 L'idée

Dans un vrai projet, les données arrivent **sales** : trous, doublons, fautes de frappe, formats incohérents, valeurs impossibles. Le **nettoyage** (*data cleaning*) consiste à les rendre **fiables** avant toute analyse ou modélisation.

> 💡 **Analogie du cuisinier** : un grand chef avec des ingrédients avariés fera un mauvais plat. En data science, le modèle est le chef, les données sont les ingrédients. **Aucun algorithme, aussi puissant soit-il, ne compense des données pourries.**

> 🔑 **La loi fondamentale** : *Garbage in, garbage out* — des données pourries en entrée donnent des résultats pourris en sortie. En pratique, un data scientist passe **60 à 80 %** de son temps à préparer et nettoyer les données.

### 1.1 Ce que le nettoyage garantit

| Dimension de qualité | Question posée | Exemple de défaut |
|----------------------|----------------|-------------------|
| **Complétude** | Manque-t-il des valeurs ? | Salaire vide pour 12 % des lignes |
| **Exactitude** | Les valeurs sont-elles justes ? | Âge = 250 ans |
| **Cohérence** | Les formats concordent-ils ? | Dates en `JJ/MM/AAAA` et `AAAA-MM-JJ` mélangées |
| **Unicité** | Y a-t-il des doublons ? | Même client enregistré 3 fois |
| **Validité** | Les valeurs respectent-elles les règles ? | Email sans `@` |

---

## 2. Naviguer parmi les problèmes de qualité des données

### 📖 Reconnaître les défauts avant de corriger

Avant de nettoyer, il faut **diagnostiquer**. Voici la carte des problèmes qu'on rencontre le plus souvent.

```
PROBLÈMES DE QUALITÉ DES DONNÉES
│
├── 🕳️  VALEURS MANQUANTES     → cases vides, NaN, "N/A", -999, ""
├── 👯  DOUBLONS               → lignes identiques ou quasi-identiques
├── ❌  INEXACTITUDES           → âge=250, prix négatif, faute de frappe
├── 🔀  FORMATS INCOHÉRENTS     → "Abidjan"/"abidjan"/"ABJ", dates mélangées
├── 📊  OUTLIERS                → valeurs extrêmes (vraies ou erronées)
├── 🏷️  TYPES INCORRECTS        → nombre stocké en texte ("1 200")
└── 🧩  ERREURS STRUCTURELLES   → colonnes mal nommées, unités mélangées
```

> ⚠️ **Attention à l'interprétation** : un défaut de qualité **fausse silencieusement** les conclusions. Une moyenne calculée sur des données incohérentes est fausse — mais rien ne le signale. Le nettoyage protège la **validité de l'interprétation**.

### 2.1 Premier réflexe : le diagnostic en Pandas

```python
import pandas as pd
df = pd.read_csv("fiche_employes.csv")

df.info()                 # types + valeurs non nulles par colonne
df.describe()             # stats : repérer min/max aberrants
df.isna().sum()           # nombre de manquants par colonne
df.duplicated().sum()     # nombre de doublons
df.nunique()              # nb de valeurs uniques (repère les catégories)
for col in df.select_dtypes("object"):
    print(col, df[col].unique()[:10])   # repérer les incohérences de format
```

---

## 3. Les tâches courantes de nettoyage

### 3.1 Gérer les valeurs manquantes

#### 📖 Le problème

Une valeur manquante (`NaN`) casse les calculs et fait planter la plupart des modèles. Trois stratégies :

```
VALEURS MANQUANTES : QUE FAIRE ?
│
├── 1️⃣  SUPPRIMER
│      ├── la ligne   → si peu de lignes concernées
│      └── la colonne → si la colonne est vide à > 50-60 %
│
├── 2️⃣  IMPUTER (remplacer par une estimation)
│      ├── numérique  → moyenne / médiane
│      ├── catégoriel → mode (valeur la plus fréquente)
│      └── avancé     → KNNImputer, régression, "manquant" comme catégorie
│
└── 3️⃣  SIGNALER
       └── créer un indicateur "était_manquant" (parfois informatif !)
```

```python
# Diagnostic
df.isna().mean().sort_values(ascending=False)   # % de manquants par colonne

# 1. Supprimer
df = df.dropna(subset=["Salary"])          # lignes sans salaire
df = df.dropna(axis=1, thresh=len(df)*0.5) # colonnes vides à > 50 %

# 2. Imputer
df["Salary"] = df["Salary"].fillna(df["Salary"].median())   # médiane (robuste)
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])  # mode

# 2 bis. Imputation scikit-learn (recommandé pour le ML → compatible Pipeline)
from sklearn.impute import SimpleImputer, KNNImputer
imp = SimpleImputer(strategy="median")     # ou "mean", "most_frequent", "constant"
```

> 🔑 **Médiane plutôt que moyenne** : la médiane **résiste aux outliers**. Si un salaire est saisi à 99 000 000 par erreur, la moyenne explose, pas la médiane. **Réflexe : imputer les numériques par la médiane.**

> 💡 **MCAR / MAR / MNAR** : les données peuvent manquer *complètement au hasard* (MCAR), *au hasard conditionnellement* (MAR), ou *non au hasard* (MNAR — la valeur manquante dépend de la valeur elle-même, ex. les hauts revenus refusent de le déclarer). Dans ce dernier cas, imputer naïvement **biaise** l'analyse — mieux vaut ajouter un indicateur « manquant ».

### 3.2 Supprimer les doublons

```python
df.duplicated().sum()                       # combien de doublons exacts ?
df = df.drop_duplicates()                    # supprime les lignes identiques

# Doublons sur une clé métier (même email = même personne)
df = df.drop_duplicates(subset=["Email"], keep="first")
```

> ⚠️ **Doublons « flous »** : « Jean Dupont » et « jean  dupont » (espace, casse) ne sont pas des doublons exacts. Il faut d'abord **standardiser** (§3.4) avant de dédupliquer, sinon `drop_duplicates` les rate.

### 3.3 Corriger les inexactitudes

Valeurs impossibles, incohérentes ou fautes de frappe.

```python
# Valeurs hors bornes → règles métier
df.loc[df["Age"] > 100, "Age"] = pd.NA        # âge impossible → manquant
df.loc[df["Salary"] < 0, "Salary"] = pd.NA    # salaire négatif → manquant

# Types incorrects : nombre stocké en texte "1 200 €"
df["Salary"] = (df["Salary"].astype(str)
                .str.replace(r"[^\d.]", "", regex=True)   # ne garder que chiffres
                .replace("", pd.NA).astype(float))

# Fautes de frappe / valeurs proches → mapping
df["Department"] = df["Department"].replace({"Finence": "Finance", "RH ": "RH"})
```

### 3.4 Standardiser les formats

Uniformiser casse, espaces, dates, catégories.

```python
# Texte : minuscules + suppression des espaces superflus
df["Ville"] = df["Ville"].str.strip().str.lower()

# Catégories équivalentes → forme canonique
df["Ville"] = df["Ville"].replace({"abj": "abidjan", "abidjan ": "abidjan"})

# Dates : tout convertir en datetime (formats mélangés gérés)
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# Nettoyer les colonnes elles-mêmes (typo "Fist Name", espaces)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

> 🔑 **Ordre malin** : standardiser **avant** de dédupliquer et de grouper. Sinon `"Abidjan"` et `"abidjan"` comptent comme deux villes différentes.

### 3.5 Traiter les valeurs aberrantes (outliers)

#### 📖 Un outlier n'est pas toujours une erreur

Une valeur extrême peut être **une erreur** (âge = 250) **ou une vraie observation rare** (salaire d'un PDG). **Ne jamais supprimer aveuglément** : d'abord comprendre.

**Détecter** — deux méthodes classiques :

```python
# Méthode IQR (écart interquartile) — robuste
Q1, Q3 = df["Salary"].quantile([0.25, 0.75])
IQR = Q3 - Q1
borne_bas, borne_haut = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = df[(df["Salary"] < borne_bas) | (df["Salary"] > borne_haut)]

# Méthode Z-score (suppose une distribution ~normale)
from scipy import stats
z = stats.zscore(df["Salary"].dropna())
# |z| > 3 → outlier
```

```
DÉTECTION PAR IQR (boîte à moustaches)
                  Q1        médiane      Q3
        ┌─────────┬────────────┬─────────┐
   ○    │         │            │         │    ○   ○
outlier └─────────┴────────────┴─────────┘  outliers
   ↑                                          ↑
 < Q1 - 1.5×IQR                        > Q3 + 1.5×IQR
```

**Traiter** :

| Méthode | Quand | Comment |
|---------|-------|---------|
| **Supprimer** | Erreur avérée | `df = df[~outlier_mask]` |
| **Capping / Winsorisation** | Vraie valeur mais extrême | ramener à la borne (`clip`) |
| **Transformer** | Distribution très étalée | `np.log1p(x)` |
| **Garder** | Outlier informatif (fraude !) | ne rien faire |

```python
df["Salary"] = df["Salary"].clip(borne_bas, borne_haut)   # capping
```

> 🔑 **Le contexte décide.** En détection de fraude, les outliers sont **exactement** ce qu'on cherche — les supprimer serait une faute. Toujours se demander : *« cette valeur extrême est-elle une erreur ou un signal ? »*

---

## 4. Les étapes d'un nettoyage méthodique

Un nettoyage se fait dans un **ordre logique**, pas au hasard.

```
WORKFLOW DE NETTOYAGE (ordre recommandé)
│
1️⃣  ÉVALUER la qualité      → info(), describe(), isna(), duplicated()
        │
2️⃣  SUPPRIMER l'inutile     → colonnes hors sujet, identifiants, colonnes vides
        │
3️⃣  CORRIGER la structure   → noms de colonnes, types, unités, formats
        │
4️⃣  DÉDUPLIQUER             → drop_duplicates (après standardisation)
        │
5️⃣  GÉRER les manquants     → supprimer / imputer / signaler
        │
6️⃣  TRAITER les outliers    → détecter puis décider (garder/capper/supprimer)
        │
7️⃣  NORMALISER / METTRE     → mise à l'échelle (Partie II) — souvent DANS le pipeline ML
    À L'ÉCHELLE
```

### 4.1 Assess Data Quality (évaluer)
Mesurer l'ampleur des problèmes **avant** d'agir : combien de manquants, de doublons, quelles colonnes aberrantes. On ne corrige pas ce qu'on n'a pas quantifié.

### 4.2 Remove Irrelevant Data (supprimer l'inutile)
Retirer les colonnes qui n'apportent rien au problème (identifiants techniques, colonnes constantes, données hors périmètre). Moins de bruit = meilleur modèle.

### 4.3 Fix Structural Errors (corriger la structure)
Noms de colonnes incohérents (`"Fist Name"`), types mal lus (nombres en texte), unités mélangées (€ et FCFA), catégories dupliquées par la casse.

### 4.4 Handle Missing Data (gérer les manquants)
Appliquer la stratégie de §3.1 : supprimer, imputer (médiane/mode/KNN) ou signaler.

### 4.5 Normalize Data (normaliser)
Mettre les variables sur une échelle comparable — c'est le pont vers la **Partie II** (feature scaling). Dans un projet ML, cette étape se fait **dans un Pipeline** pour éviter la fuite de données (§16).

---

## 5. Outils et techniques

### 5.1 Les outils

| Outil | Usage |
|-------|-------|
| **Pandas** | Le couteau suisse du nettoyage en Python |
| **NumPy** | Opérations numériques, gestion des NaN |
| **scikit-learn** | `SimpleImputer`, `KNNImputer`, scalers, encoders (compatibles Pipeline) |
| **ydata-profiling** (ex pandas-profiling) | Rapport de qualité automatique (voir cours 03 data-science) |
| **Expressions régulières (`re`)** | Nettoyage fin de texte |

### 5.2 Techniques Pandas essentielles

```python
df.info(); df.describe(include="all")     # diagnostic
df.isna().sum(); df.duplicated().sum()    # manquants & doublons
df.drop_duplicates(); df.dropna(); df.fillna()   # correction
df["col"].str.strip().str.lower()         # texte
df["col"].astype(...)                     # types
pd.to_datetime(df["col"], errors="coerce")# dates
df["col"].replace({...}); df["col"].map({...})   # remappage
df["col"].clip(bas, haut)                 # capping outliers
df["col"].quantile([.25,.75])             # IQR
```

---

## 6. Les défis du nettoyage de données

| Défi | Pourquoi c'est difficile |
|------|--------------------------|
| **Volume** | Des millions de lignes → nettoyage manuel impossible, il faut automatiser |
| **Décisions subjectives** | Imputer ou supprimer ? Le choix influence les résultats — aucune règle absolue |
| **Risque de biais** | Imputer par la moyenne réduit artificiellement la variance et peut biaiser |
| **Outliers ambigus** | Erreur ou signal ? Sans connaissance métier, impossible de trancher |
| **Reproductibilité** | Un nettoyage « à la main » n'est pas reproductible → tout scripter |
| **Fuite de données** | Nettoyer/scaler avant le split contamine l'évaluation (§16) |

---

## 7. Bonnes pratiques d'assurance qualité

> ✅ **Les 8 règles d'or du nettoyage**

1. **Toujours garder les données brutes intactes.** On travaille sur une **copie** (`df_clean = df.copy()`), jamais sur l'original.
2. **Tout scripter, jamais à la main.** Un notebook reproductible > Excel manuel.
3. **Documenter chaque décision.** Pourquoi la médiane ? Pourquoi supprimer telle colonne ? Le futur vous (et vos collègues) remercieront.
4. **Diagnostiquer avant de corriger.** Quantifier l'ampleur d'un problème avant de le traiter.
5. **Comprendre le métier.** Un âge de 0 est-il un bébé, une erreur, ou un « non renseigné » ?
6. **Vérifier après chaque étape.** Re-`isna()`, re-`describe()` pour confirmer l'effet.
7. **Ne jamais scaler/imputer sur l'ensemble complet en ML.** Fit sur le train uniquement (§16).
8. **Automatiser via un Pipeline** pour garantir cohérence train/production (§17).

---

# PARTIE II — LA MISE À L'ÉCHELLE DES VARIABLES (FEATURE SCALING)

## 8. Pourquoi mettre à l'échelle ? (Why use Feature Scaling ?)

### 📖 Le problème des échelles différentes

Les variables ont souvent des **unités et amplitudes très différentes** : un âge (20–70) et un revenu (200 000–5 000 000). De nombreux algorithmes calculent des **distances** ou des **poids** : la variable aux **grands nombres écrase** les autres.

```
SANS mise à l'échelle : le revenu DOMINE tout
  âge      : [20 .......... 70]          (amplitude 50)
  revenu   : [200000 ...... 5000000]     (amplitude 4 800 000)
  → distance ≈ uniquement pilotée par le revenu, l'âge devient invisible

AVEC mise à l'échelle : chaque variable pèse équitablement
  âge      : [0 ............ 1]
  revenu   : [0 ............ 1]
  → les deux contribuent de façon comparable ✅
```

### 8.1 Quels algorithmes en ont besoin ?

| Sensible à l'échelle ? | Algorithmes | Pourquoi |
|------------------------|-------------|----------|
| ✅ **OUI, indispensable** | KNN, K-Means, SVM, PCA, régression logistique/linéaire régularisée (Ridge/Lasso), réseaux de neurones | Basés sur **distances** ou **descente de gradient** |
| ❌ **NON, inutile** | Arbres de décision, Random Forest, Gradient Boosting (XGBoost…) | Basés sur des **seuils** (`x > valeur`), insensibles à l'échelle |

> 🔑 **La règle** : dès qu'un algorithme calcule des **distances** (KNN, K-Means, SVM) ou fait de la **descente de gradient** (régression, réseaux), la mise à l'échelle est **obligatoire**. Les modèles à base d'**arbres** n'en ont pas besoin.

> 💡 **Bonus** : la mise à l'échelle **accélère la convergence** de la descente de gradient (les courbes de niveau deviennent « rondes »), donc l'entraînement est plus rapide et plus stable.

---

## 9. Absolute Maximum Scaling

### 📖 Définition

Diviser chaque valeur par la **valeur absolue maximale** de sa colonne. Ramène les données dans **[-1, 1]**.

$$x_{\text{scaled}} = \frac{x}{\max(|x|)}$$

```python
import numpy as np
X_scaled = X / np.abs(X).max()
# ou
from sklearn.preprocessing import MaxAbsScaler
X_scaled = MaxAbsScaler().fit_transform(X)
```

### 🎯 Points clés
- ✅ **Préserve la sparsité** (les zéros restent zéros) → utile pour les **matrices creuses** (texte/TF-IDF).
- ⚠️ **Très sensible aux outliers** : un seul maximum extrême écrase tout le reste vers 0.
- Rarement le premier choix hors données creuses.

---

## 10. Min-Max Scaling

### 📖 Définition

Ramène chaque variable dans un intervalle fixe, typiquement **[0, 1]**.

$$x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()               # feature_range=(0, 1) par défaut
X_scaled = scaler.fit_transform(X)
```

### 🎯 Points clés
- ✅ Bornes **connues et fixes** [0, 1] → parfait pour les **réseaux de neurones** (entrées bornées) et le traitement d'images.
- ✅ Préserve la **forme** de la distribution.
- ⚠️ **Sensible aux outliers** : un maximum extrême comprime toutes les autres valeurs vers 0.

---

## 11. Normalisation (Normalization)

### 📖 Attention : deux sens du mot « normalisation »

> ⚠️ **Confusion fréquente !** Le terme « normalisation » désigne souvent, au sens large, **la mise à l'échelle en [0,1] (Min-Max)**. Mais dans scikit-learn, `Normalizer` a un sens **précis et différent** : il normalise **chaque ligne** (chaque observation) pour que son **vecteur ait une norme de 1**, pas chaque colonne.

$$x_{\text{scaled}} = \frac{x}{\|x\|} \quad (\text{par LIGNE, pas par colonne})$$

```python
from sklearn.preprocessing import Normalizer
X_scaled = Normalizer(norm="l2").fit_transform(X)   # chaque LIGNE → norme 1
```

### 🎯 Points clés
- Agit **par observation** (ligne), pas par variable (colonne) — contrairement à tous les autres scalers.
- ✅ Utile quand seule la **direction** du vecteur compte, pas sa magnitude : **similarité de textes** (TF-IDF + cosinus), certains systèmes de recommandation.
- ❌ **Ce n'est PAS** l'outil pour « mettre les colonnes à la même échelle » — pour cela, utilisez Min-Max ou la standardisation.

> 🔑 **À retenir** : *Min-Max / Standardisation = par colonne (variable)* ; *`Normalizer` = par ligne (observation)*. Ne pas confondre.

---

## 12. Standardisation (Standardization)

### 📖 Définition

Centrer sur une **moyenne de 0** et réduire à un **écart-type de 1** (score Z). C'est **le scaler le plus utilisé**.

$$x_{\text{scaled}} = \frac{x - \mu}{\sigma}$$

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)     # moyenne ≈ 0, écart-type ≈ 1
```

### 🎯 Points clés
- ✅ **Pas de bornes fixes** (les valeurs peuvent dépasser ±3) → **moins sensible** aux outliers que Min-Max.
- ✅ Idéal quand les données sont **~gaussiennes** ; **exigé par PCA, SVM, régression logistique, Ridge/Lasso**.
- ✅ Le **choix par défaut** dans la plupart des cas ML.

### 📊 Min-Max vs Standardisation

| Critère | Min-Max Scaling | Standardisation |
|---------|-----------------|-----------------|
| Résultat | Borné [0, 1] | Moyenne 0, écart-type 1 (non borné) |
| Sensibilité aux outliers | **Forte** | Modérée |
| Distribution attendue | Quelconque | Idéalement ~normale |
| Usage typique | Réseaux de neurones, images | ⭐ Cas général ML (SVM, PCA, régression) |

---

## 13. RobustScaler et le cas des outliers

### 📖 Quand les outliers gâchent tout

Min-Max et Standardisation utilisent min/max/moyenne/écart-type — **tous sensibles aux valeurs extrêmes**. Le **`RobustScaler`** utilise la **médiane** et l'**IQR** (écart interquartile), donc **résiste aux outliers**.

$$x_{\text{scaled}} = \frac{x - \text{médiane}}{Q_3 - Q_1}$$

```python
from sklearn.preprocessing import RobustScaler
X_scaled = RobustScaler().fit_transform(X)
```

> 🔑 **Réflexe** : si vos données contiennent des outliers que vous ne pouvez/voulez pas retirer, préférez le **RobustScaler** à Min-Max ou StandardScaler.

---

## 14. Quel scaler pour quel algorithme ?

```
CHOISIR SON SCALER
│
├── Modèle à base d'ARBRES (RF, GBM, XGBoost)
│        → AUCUN scaling nécessaire ✅
│
├── Données ~normales, cas général (SVM, PCA, régression, KNN)
│        → StandardScaler ⭐ (le défaut)
│
├── Réseau de neurones, images, bornes fixes voulues
│        → MinMaxScaler [0, 1]
│
├── Beaucoup d'OUTLIERS non supprimables
│        → RobustScaler (médiane + IQR)
│
├── Matrices CREUSES (texte, TF-IDF)
│        → MaxAbsScaler (préserve les zéros)
│
└── Similarité de DIRECTION par observation (texte, reco)
         → Normalizer (par ligne)
```

### 🔬 Pourquoi ce lien entre scaler et algorithme ?

- **KNN / K-Means** : calculent des **distances euclidiennes** → une variable non mise à l'échelle domine la distance. Scaling **obligatoire** (Standard ou Min-Max).
- **SVM (noyau RBF)** : le noyau dépend des distances → **StandardScaler** quasi obligatoire.
- **PCA** : cherche les directions de **variance maximale** → sans standardisation, la variable de plus grande amplitude capte artificiellement toute la variance.
- **Régression régularisée (Ridge/Lasso)** : la pénalité s'applique aux coefficients → il faut des variables à la **même échelle** pour pénaliser équitablement.
- **Arbres** : découpent par **seuils** (`revenu > 300 000`) ; multiplier une variable par 1000 ne change **rien** aux seuils relatifs → scaling inutile.

---

# PARTIE III — ASPECTS COMPLÉMENTAIRES (INDISPENSABLES)

## 15. Encodage des variables catégorielles

### 📖 Le problème

Les modèles ne mangent que des **nombres**. Une colonne `type_contrat` = {CDI, CDD, Intérim} doit être **encodée**.

| Technique | Quand | Comment |
|-----------|-------|---------|
| **One-Hot Encoding** | Catégories **sans ordre** (nominal) : ville, contrat | Une colonne 0/1 par catégorie |
| **Ordinal / Label Encoding** | Catégories **ordonnées** : « Faible < Moyen < Élevé » | Un entier par niveau |

```python
# One-Hot (nominal) — pas d'ordre inventé
import pandas as pd
df = pd.get_dummies(df, columns=["type_contrat", "ville"], drop_first=True)

# scikit-learn (compatible Pipeline)
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

# Ordinal (ordre explicite)
oe = OrdinalEncoder(categories=[["Faible", "Moyen", "Élevé"]])
```

> ⚠️ **Piège classique** : encoder une variable nominale (sans ordre) avec un Label Encoder (0,1,2) fait croire au modèle que « ville 2 > ville 1 ». **Nominal → One-Hot ; ordinal → Ordinal.**

---

## 16. Fuite de données : le fit uniquement sur le train

### 📖 La règle d'or du preprocessing en ML

> 🔑 **Tout ce qui APPREND des données (scaler, imputer, encoder) doit être `fit` sur le TRAIN uniquement, puis `transform` appliqué au test.** Sinon, des informations du test « fuitent » dans l'entraînement → score artificiellement bon, puis effondrement en production.

```python
# ❌ MAUVAIS — fuite : le scaler voit tout, y compris le test
X_scaled = StandardScaler().fit_transform(X)
X_train, X_test = train_test_split(X_scaled, ...)

# ✅ BON — fit sur train, transform sur test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)   # apprend μ, σ sur le TRAIN
X_test_s  = scaler.transform(X_test)        # APPLIQUE les μ, σ du train
```

> 💡 C'est le même principe que pour l'imputation : la **médiane d'imputation** se calcule sur le train seul. La solution robuste qui garantit tout cela : le **Pipeline** (§17).

---

## 17. Tout automatiser proprement : Pipeline & ColumnTransformer

### 📖 Le bon outil : un seul objet qui fait tout

Un projet réel mélange colonnes numériques et catégorielles, chacune avec son traitement. Le **`ColumnTransformer`** applique le bon preprocessing à chaque type de colonne, et le **`Pipeline`** enchaîne preprocessing + modèle en **un seul objet** — **anti-fuite par construction**.

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

num = ["age", "revenu_mensuel", "montant_demande"]
cat = ["type_contrat", "situation_familiale", "historique_credit"]

# Traitement des numériques : imputer (médiane) puis standardiser
pipe_num = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler",  StandardScaler()),
])

# Traitement des catégorielles : imputer (mode) puis one-hot
pipe_cat = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot",  OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer([
    ("num", pipe_num, num),
    ("cat", pipe_cat, cat),
])

# Pipeline complet : preprocessing + modèle
model = Pipeline([
    ("prep", preprocess),
    ("clf",  LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)          # tout est fit sur le train, zéro fuite
print(model.score(X_test, y_test))   # transform automatique du test
```

> 🔑 **C'est LA façon professionnelle** de faire du preprocessing. Un seul `fit`, aucune fuite, et le même objet sert en production. Compatible directement avec `cross_val_score` et `GridSearchCV` (cours 03).

---

# PARTIE IV — SYNTHÈSE

## 18. Conclusion

### 🎓 Ce qu'il faut absolument retenir

1. **Garbage in, garbage out.** La qualité du modèle est plafonnée par la qualité des données. Le nettoyage n'est pas une corvée annexe : c'est **60–80 %** du travail réel.

2. **Nettoyer, c'est méthodique** : évaluer → supprimer l'inutile → corriger la structure → dédupliquer → gérer les manquants → traiter les outliers → mettre à l'échelle. Dans cet **ordre**.

3. **Les manquants** : supprimer, imputer (médiane pour les numériques, mode pour les catégories) ou signaler. Pas de solution unique — le **contexte** décide.

4. **Les outliers** ne sont pas toujours des erreurs. Détecter (IQR, Z-score), **comprendre**, puis décider (garder / capper / supprimer).

5. **La mise à l'échelle** est **obligatoire** pour les algorithmes à distances (KNN, K-Means, SVM) et à gradient (régression, réseaux), **inutile** pour les arbres.

6. **Le bon scaler** : StandardScaler par défaut ; MinMax pour bornes fixes/réseaux ; RobustScaler si outliers ; MaxAbs/Normalizer pour cas spéciaux (texte).

7. **Ne jamais scaler/imputer avant le split** : `fit` sur le train uniquement. La parade professionnelle est le **Pipeline + ColumnTransformer** — anti-fuite, reproductible, prêt pour la production.

### 🧭 Le mémo en une image

```
┌────────────────────────────────────────────────────────────────┐
│  NETTOYAGE : évaluer → nettoyer (manquants/doublons/outliers/   │
│              formats) → toujours sur une COPIE, tout scripté     │
│                                                                  │
│  SCALING   : distances/gradient → OUI (Standard ⭐, MinMax,      │
│              Robust) ;  arbres → NON                             │
│                                                                  │
│  CATÉGORIES: nominal → One-Hot ;  ordinal → Ordinal              │
│                                                                  │
│  RÈGLE D'OR: fit sur le TRAIN uniquement → Pipeline anti-fuite   │
└────────────────────────────────────────────────────────────────┘
```

> 🔑 **En une phrase** : *le preprocessing transforme des données brutes en données fiables et comparables — c'est le socle invisible sur lequel repose la réussite de tout modèle.*

---

## 19. ✅ Point de contrôle — Preprocessing

### 🧠 Questions de compréhension

<details>
<summary><b>1. Que signifie « Garbage in, garbage out » ?</b></summary>

Des données de mauvaise qualité en entrée produisent des résultats de mauvaise qualité en sortie, quel que soit l'algorithme. D'où l'importance capitale du nettoyage.
</details>

<details>
<summary><b>2. Pour imputer une variable numérique, pourquoi préférer la médiane à la moyenne ?</b></summary>

La médiane est **robuste aux outliers** : une valeur aberrante (ex. salaire saisi à 99 000 000) fait exploser la moyenne mais n'affecte quasiment pas la médiane. L'imputation reste ainsi représentative.
</details>

<details>
<summary><b>3. Pourquoi standardiser AVANT de dédupliquer ?</b></summary>

Parce que « Abidjan », « abidjan » et « abidjan  » ne sont pas des doublons exacts pour `drop_duplicates`. En standardisant d'abord (casse, espaces), ces variantes deviennent identiques et la déduplication fonctionne.
</details>

<details>
<summary><b>4. Un outlier doit-il toujours être supprimé ?</b></summary>

Non. Il peut être une **vraie observation rare** (salaire d'un dirigeant) ou même le **signal recherché** (fraude). On détecte, on comprend le contexte, puis on décide : garder, capper, transformer ou supprimer.
</details>

<details>
<summary><b>5. Quels types d'algorithmes ont besoin de mise à l'échelle, et lesquels non ?</b></summary>

**Besoin** : ceux basés sur les distances (KNN, K-Means, SVM) ou le gradient (régression, réseaux, PCA, Ridge/Lasso). **Pas besoin** : les modèles à base d'arbres (Decision Tree, Random Forest, Gradient Boosting), qui découpent par seuils.
</details>

<details>
<summary><b>6. Différence entre MinMaxScaler et StandardScaler ?</b></summary>

**MinMax** ramène dans un intervalle borné [0,1] (sensible aux outliers). **Standard** centre sur moyenne 0 / écart-type 1, non borné et plus robuste aux extrêmes. Standard est le choix par défaut ; MinMax pour les réseaux/images.
</details>

<details>
<summary><b>7. Dans scikit-learn, que fait exactement le <code>Normalizer</code> ?</b></summary>

Il normalise **chaque ligne** (observation) pour lui donner une norme de 1 — pas chaque colonne. Il sert quand seule la **direction** du vecteur compte (similarité de textes). Ce n'est **pas** l'outil pour mettre les colonnes à la même échelle.
</details>

<details>
<summary><b>8. Pourquoi ne faut-il pas scaler AVANT le train/test split ?</b></summary>

Parce que le scaler calculerait ses paramètres (μ, σ, min, max) sur **toutes** les données, test compris : c'est une **fuite de données** qui gonfle le score. Il faut `fit` sur le train seul, puis `transform` le test — idéalement via un **Pipeline**.
</details>

<details>
<summary><b>9. Comment encoder une variable nominale vs ordinale ?</b></summary>

**Nominale** (sans ordre : ville, contrat) → **One-Hot Encoding** (une colonne 0/1 par catégorie). **Ordinale** (ordre : Faible<Moyen<Élevé) → **Ordinal Encoding** (entiers respectant l'ordre). Encoder du nominal en 0/1/2 inventerait un faux ordre.
</details>

<details>
<summary><b>10. À quoi sert le duo Pipeline + ColumnTransformer ?</b></summary>

À appliquer le bon preprocessing à chaque type de colonne (numérique/catégoriel) et à enchaîner preprocessing + modèle en un seul objet. Il **évite la fuite de données par construction** (tout est fit sur le train), rend le code reproductible et prêt pour la production.
</details>

### 🛠️ Exercice pratique

Voir le **Checkpoint 8 — Focus Preprocessing** ([`06-DataScience_Checkpoint8_Preprocessing.md`](06-DataScience_Checkpoint8_Preprocessing.md)) : nettoyage complet de `fiche_employes.csv` puis pipeline de preprocessing sur `demandes_credit.csv`.

---

*📘 Module Data Science — Nettoyage des Données & Mise à l'Échelle | Bootcamp Data Science*
