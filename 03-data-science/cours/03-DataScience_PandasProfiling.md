# 📑 Pandas Profiling (ydata-profiling) — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : Pandas (Data Cleaning + Data Exploration)

---

## Table des matières

1. [Why Pandas Profiling ? — Pourquoi le profiling ?](#1-why-pandas-profiling--pourquoi-le-profiling-)
2. [Pandas Profiling → ydata-profiling — Un point important](#2-pandas-profiling--ydata-profiling--un-point-important)
3. [Installation et mise en route](#3-installation-et-mise-en-route)
4. [Pandas Profiling in Action — Le profiling en pratique](#4-pandas-profiling-in-action--le-profiling-en-pratique)
5. [Pandas Profiling Overview — Comprendre le rapport](#5-pandas-profiling-overview--comprendre-le-rapport)
6. [Interpréter et agir sur le rapport](#6-interpréter-et-agir-sur-le-rapport)
7. [Limites et bonnes pratiques](#7-limites-et-bonnes-pratiques)
8. [Conclusion](#8-conclusion)
9. [ydata-profiling — Checkpoint 1](#9-ydata-profiling--checkpoint-1)
10. [ydata-profiling — Checkpoint 2](#10-ydata-profiling--checkpoint-2)
11. [✅ Point de contrôle — Pandas Profiling](#11--point-de-contrôle--pandas-profiling)

---

## 1. Why Pandas Profiling ? — Pourquoi le profiling ?

### 📖 Le problème que résout le profiling

Au chapitre précédent (Data Exploration), vous avez appris à explorer les données **commande par commande** : `df.info()`, `df.describe()`, `df.isna().sum()`, `df.corr()`, des histogrammes, la détection d'outliers... C'est puissant, mais **long et répétitif** pour chaque nouveau jeu de données.

Le **Pandas Profiling** génère **automatiquement** un **rapport d'exploration complet** en **une seule ligne de code** — toutes ces analyses réunies dans un document interactif.

> 💡 **Analogie** : L'exploration manuelle (chapitre précédent), c'est comme faire un **bilan de santé en allant voir chaque spécialiste séparément** (cardiologue, radiologue, laboratoire...). Le profiling, c'est comme passer un **check-up complet automatisé** qui produit un seul rapport rassemblant tous les résultats d'un coup.

### 1.1 Ce que le profiling automatise

```
CE QUE VOUS FAISIEZ À LA MAIN          CE QUE LE PROFILING FAIT AUTOMATIQUEMENT
─────────────────────────────          ─────────────────────────────────────────
df.info()                              → Vue d'ensemble (lignes, colonnes, types)
df.describe()                          → Statistiques de chaque variable
df.isna().sum()                        → Valeurs manquantes + visualisation
df.duplicated().sum()                  → Détection des doublons
df["col"].value_counts()               → Distribution de chaque catégorie
df.corr()                              → Matrice de corrélation + heatmap
histogrammes, boxplots un par un       → Graphiques de TOUTES les variables
détection manuelle d'outliers          → Alertes automatiques (skew, cardinalité...)
─────────────────────────────          ─────────────────────────────────────────
    → 30-50 lignes de code                  → 1 seule ligne de code !
```

### 1.2 Les avantages du profiling

```
POURQUOI UTILISER LE PROFILING ?
│
├── ⚡ Rapidité         → un rapport complet en quelques secondes
├── 🎯 Exhaustivité      → analyse TOUTES les colonnes automatiquement
├── 🔔 Alertes           → détecte automatiquement les problèmes (manquants, corrélations, déséquilibres)
├── 📊 Visualisations    → histogrammes, distributions, heatmaps déjà tracés
├── 🤝 Partage           → rapport HTML exportable, partageable avec l'équipe
└── 🧭 Point de départ    → idéal pour la première prise de contact avec des données
```

> 🔑 **Quand l'utiliser ?** Le profiling est parfait pour le **premier contact** avec un jeu de données inconnu — il donne une vue d'ensemble instantanée qui oriente ensuite le nettoyage et l'analyse détaillée.

---

## 2. Pandas Profiling → ydata-profiling — Un point important

### ⚠️ Un changement de nom à connaître

La bibliothèque s'appelait à l'origine **`pandas-profiling`**. Depuis 2023, elle a été **renommée `ydata-profiling`** (par l'entreprise YData qui la maintient). Le fonctionnement reste identique — seul le nom du package et de l'import ont changé.

```
AVANT (déprécié)                       MAINTENANT (à utiliser)
─────────────────────                  ─────────────────────────
pip install pandas-profiling           pip install ydata-profiling
                                        
from pandas_profiling import           from ydata_profiling import
    ProfileReport                          ProfileReport
```

> 🔑 **À retenir** : Le concept s'appelle toujours "Pandas Profiling" dans le langage courant, mais le **package moderne à installer est `ydata-profiling`**. Les anciens tutoriels utilisant `pandas_profiling` peuvent ne plus fonctionner. C'est pourquoi les checkpoints de ce chapitre utilisent le nom **ydata-profiling**.

---

## 3. Installation et mise en route

### 3.1 Installation

```python
# Dans Google Colab ou un terminal
!pip install ydata-profiling
```

> ⚠️ **Note pour Colab** : après l'installation, il faut parfois **redémarrer l'environnement d'exécution** (Menu → Exécution → Redémarrer la session) pour que la bibliothèque soit bien prise en compte.

### 3.2 Import

```python
import pandas as pd
from ydata_profiling import ProfileReport
```

### 3.3 Générer un premier rapport — en 3 lignes !

```python
import pandas as pd
from ydata_profiling import ProfileReport

# 1. Charger les données
df = pd.read_csv("etudiants.csv")

# 2. Générer le rapport
rapport = ProfileReport(df, title="Rapport d'exploration des étudiants")

# 3. Afficher le rapport (dans un notebook)
rapport
```

> 💡 En **une seule ligne** (`ProfileReport(df)`), vous obtenez ce qui demandait des dizaines de commandes au chapitre précédent !

---

## 4. Pandas Profiling in Action — Le profiling en pratique

### 4.1 Charger un jeu de données réaliste

Pour ce chapitre, nous utilisons le vrai fichier **`bootcamp_500.csv`** (510 lignes). Le profiling ne révèle sa pleine puissance que sur un **volume conséquent** de données — c'est sur des centaines de lignes que les distributions, corrélations et alertes deviennent vraiment significatives.

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Charger le jeu de données (téléchargez bootcamp_500.csv dans Colab)
df = pd.read_csv("bootcamp_500.csv")
print(df.shape)   # (510, 10)
df.head()
```

> 💡 Ce fichier contient volontairement de vrais problèmes (valeurs manquantes, outliers, doublons, anomalies de casse) — le profiling va tous les détecter automatiquement et les signaler dans ses **Alerts** !

### 4.2 Générer le rapport

```python
# Générer le rapport complet
rapport = ProfileReport(
    df,
    title="Analyse du Bootcamp Data Science",
    explorative=True    # active toutes les analyses avancées
)

# Afficher dans le notebook
rapport
```

### 4.3 Exporter le rapport en HTML

```python
# Sauvegarder le rapport en fichier HTML partageable
rapport.to_file("rapport_bootcamp.html")
print("✅ Rapport sauvegardé dans rapport_bootcamp.html")
```

> 💡 Le fichier HTML est **autonome** — vous pouvez l'ouvrir dans n'importe quel navigateur et le partager avec votre équipe, même sans Python installé.

### 4.4 Mode minimal — Pour les gros jeux de données

```python
# Pour les grands datasets, le mode minimal est plus rapide
# (désactive les analyses les plus coûteuses comme les corrélations détaillées)
rapport_rapide = ProfileReport(df, minimal=True)
rapport_rapide.to_file("rapport_rapide.html")
```

---

## 5. Pandas Profiling Overview — Comprendre le rapport

Le rapport généré est organisé en **plusieurs sections**. Voici comment le lire.

### 5.1 Structure du rapport

```
RAPPORT YDATA-PROFILING
│
├── 📋 Overview (Vue d'ensemble)
│   ├── Statistiques globales (nb lignes, colonnes, cellules manquantes)
│   ├── Types de variables (numériques, catégorielles...)
│   └── ⚠️ Alerts (alertes automatiques !)
│
├── 📊 Variables (une analyse par colonne)
│   ├── Statistiques (moyenne, min, max, quartiles...)
│   ├── Distribution (histogramme)
│   ├── Valeurs manquantes
│   └── Valeurs les plus fréquentes
│
├── 🔗 Interactions (relations entre paires de variables)
│
├── 🌡️  Correlations (matrice de corrélation / heatmap)
│
├── 🕳️  Missing values (visualisation des valeurs manquantes)
│
└── 🔁 Sample (aperçu des premières/dernières lignes)
```

### 5.2 La section Overview — Le tableau de bord

Sur notre fichier `bootcamp_500.csv`, l'Overview ressemble à ceci :

```
OVERVIEW
┌─────────────────────────────────────────────┐
│ Number of variables        : 10              │
│ Number of observations     : 510             │
│ Missing cells              : 60 (1.2%)       │
│ Duplicate rows             : 10 (2.0%)       │
│ Variable types             :                 │
│    Numeric      : 6                          │
│    Categorical  : 4                          │
└─────────────────────────────────────────────┘
```

> 🔑 En un coup d'œil : 510 observations, **60 cellules manquantes** (les colonnes ville/note_sql/note_python) et **10 lignes dupliquées** détectées automatiquement — sans écrire une seule commande !

### 5.3 Les Alerts — La fonctionnalité la plus utile ⭐

Le profiling **détecte automatiquement** les problèmes potentiels et affiche des **alertes** — c'est souvent la partie la plus précieuse du rapport.

| Type d'alerte | Signification | Action possible |
|-----------------|----------------|------------------|
| `Missing` | La colonne a des valeurs manquantes | Imputer ou supprimer |
| `High correlation` | Deux colonnes sont très corrélées | Envisager d'en supprimer une (redondance) |
| `High cardinality` | Trop de valeurs uniques (ex : identifiants) | Peut ne pas être utile pour un modèle |
| `Zeros` | Beaucoup de zéros dans la colonne | Vérifier si normal |
| `Skewed` | Distribution très asymétrique | Envisager une transformation (log) |
| `Uniform` | Valeurs uniformément réparties | Peu informatif |
| `Constant` | Une seule valeur pour toute la colonne | Inutile, à supprimer |
| `Imbalance` | Catégories déséquilibrées | Attention pour la classification |

**Alertes réellement générées sur `bootcamp_500.csv` :**
```
⚠️ note_sql has 25 (4.9%) missing values                    → Missing
⚠️ note_python has 20 (3.9%) missing values                 → Missing
⚠️ ville has 15 (2.9%) missing values                       → Missing
⚠️ note_sql is highly correlated with note_python           → High correlation
⚠️ note_python is highly correlated with note_sql           → High correlation
⚠️ id_etudiant has unique values                            → Unique / High cardinality
⚠️ Dataset has 10 (2.0%) duplicate rows                     → Duplicates
```

> 🔑 Ces alertes reproduisent **exactement** ce que vous avez détecté manuellement au chapitre précédent (valeurs manquantes, corrélation forte notes, doublons) — mais générées **automatiquement en une ligne** !

### 5.4 La section Variables — Analyse détaillée de chaque colonne

Pour **chaque colonne**, le rapport affiche automatiquement :

```
VARIABLE : note_sql (numérique)
┌──────────────────────────────────────────────┐
│ Distinct       : ~120       Mean   : 9.03     │
│ Missing        : 25 (4.9%)  Min    : 0        │
│ Distinct (%)   : ~24%       Max    : 30 (!)   │
│ Zeros          : quelques                     │
│                                               │
│ [Histogramme de la distribution en cloche]    │
│                                               │
│ Quartiles : Q1=6.3  médiane=8.8  Q3=11.6     │
└──────────────────────────────────────────────┘
```

### 5.5 La section Correlations

Le rapport génère automatiquement une **heatmap de corrélation** entre toutes les variables numériques — visuellement, plus les cases sont foncées (proches de +1 ou -1), plus les variables sont corrélées.

> 💡 C'est l'équivalent visuel et automatique de `df.corr()` du chapitre précédent, mais présenté sous forme de carte de chaleur (heatmap) facile à interpréter d'un coup d'œil.

---

## 6. Interpréter et agir sur le rapport

### 📖 Le profiling ne remplace pas la réflexion

Le profiling **diagnostique** mais **ne corrige pas** — c'est à vous, Data Scientist, d'interpréter les alertes et de décider des actions.

### 6.1 Le workflow profiling → action

```
1. GÉNÉRER le rapport         → ProfileReport(df)
        │
        ▼
2. LIRE les Alerts             → quels problèmes détectés ?
        │
        ▼
3. INVESTIGUER chaque alerte   → est-ce un vrai problème ?
        │
        ▼
4. AGIR avec Pandas            → nettoyer (chapitres précédents)
        │
        ▼
5. RE-PROFILER                 → vérifier que les problèmes sont réglés
```

### 6.2 Exemple concret — Du rapport à l'action

```python
# Le rapport signale : "note_sql has 1 missing value"
# → ACTION : imputer par la médiane
df["note_sql"] = df["note_sql"].fillna(df["note_sql"].median())

# Le rapport signale : "note_python and note_sql are highly correlated (0.85)"
# → INVESTIGUER : est-ce normal ? (oui, un bon étudiant l'est dans les deux)
# → DÉCISION : on garde les deux, la corrélation est logique et attendue

# Le rapport signale : "nom has high cardinality (100% distinct)"
# → INVESTIGUER : c'est un identifiant, normal qu'il soit unique
# → ACTION : on ne l'utilisera pas comme variable prédictive dans un modèle

# Re-générer le rapport pour vérifier
rapport_v2 = ProfileReport(df, title="Après nettoyage")
rapport_v2.to_file("rapport_v2.html")
```

### 6.3 Comparer deux jeux de données

Une fonctionnalité avancée très utile : comparer deux DataFrames (ex : avant/après nettoyage, ou données d'entraînement vs test).

```python
rapport_avant = ProfileReport(df_brut, title="Avant")
rapport_apres = ProfileReport(df_propre, title="Après")

# Comparaison côte à côte
comparaison = rapport_avant.compare(rapport_apres)
comparaison.to_file("comparaison.html")
```

---

## 7. Limites et bonnes pratiques

### 7.1 Les limites du profiling

```
⚠️ LIMITES À CONNAÎTRE
│
├── 🐌 Lenteur sur gros datasets  → très lent au-delà de ~100 000 lignes
│                                   (utiliser minimal=True ou un échantillon)
│
├── 💾 Consommation mémoire        → peut saturer la RAM sur de gros fichiers
│
├── 🤖 Ne corrige rien             → diagnostique seulement, à vous d'agir
│
├── 🎯 Pas de contexte métier      → ne sait pas qu'un "age=150" est impossible
│                                   (il le signale comme outlier, pas comme erreur)
│
└── 📊 Généraliste                 → une analyse ciblée manuelle reste parfois nécessaire
```

### 7.2 Bonnes pratiques

```python
# ✅ Sur un gros dataset, profiler un ÉCHANTILLON d'abord
echantillon = df.sample(n=5000, random_state=42)
rapport = ProfileReport(echantillon, minimal=True)

# ✅ Utiliser le profiling comme PREMIER contact, puis affiner à la main
# ✅ Toujours investiguer les alertes avec son jugement métier
# ✅ Exporter en HTML pour documenter et partager
```

### 7.3 Profiling vs Exploration manuelle — Quand utiliser quoi ?

| Situation | Approche recommandée |
|-----------|------------------------|
| Premier contact avec des données inconnues | **Profiling** (vue d'ensemble rapide) |
| Petit à moyen dataset (< 100k lignes) | **Profiling** (rapide et complet) |
| Très gros dataset (millions de lignes) | **Exploration manuelle** ciblée + échantillon |
| Analyse précise d'une variable spécifique | **Exploration manuelle** (contrôle total) |
| Documentation/partage avec l'équipe | **Profiling** (rapport HTML) |

> 🔑 **Le profiling et l'exploration manuelle sont complémentaires** : le profiling donne la vue d'ensemble rapide, l'exploration manuelle permet le contrôle fin. Un bon Data Scientist maîtrise les deux.

---

## 8. Conclusion

### 📌 Récapitulatif du chapitre

```
PANDAS PROFILING (ydata-profiling)
│
├── Pourquoi ?
│   └── Automatiser l'exploration en 1 ligne (vs 30-50 lignes manuelles)
│
├── Le bon package
│   └── ydata-profiling (ex pandas-profiling, renommé en 2023)
│
├── En pratique
│   ├── ProfileReport(df, title="...")     → générer
│   ├── rapport.to_file("rapport.html")    → exporter
│   └── minimal=True                        → mode rapide (gros datasets)
│
├── Le rapport
│   ├── Overview       → statistiques globales
│   ├── ⚠️ Alerts       → problèmes détectés automatiquement (le plus utile !)
│   ├── Variables      → analyse détaillée de chaque colonne
│   └── Correlations   → heatmap des relations
│
└── Workflow
    └── Générer → Lire les alertes → Investiguer → Agir (Pandas) → Re-profiler
```

### 🔑 Points clés à retenir

1. Le profiling **automatise** en une ligne toute l'exploration manuelle du chapitre précédent.
2. Le package moderne est **`ydata-profiling`** (l'ancien `pandas-profiling` est déprécié).
3. `ProfileReport(df)` génère le rapport ; `.to_file("...html")` l'exporte.
4. Les **Alerts** sont la partie la plus précieuse : elles détectent automatiquement les problèmes.
5. Le profiling **diagnostique mais ne corrige pas** — c'est au Data Scientist d'interpréter et d'agir.
6. Sur de gros datasets, utiliser `minimal=True` ou un **échantillon** pour éviter la lenteur.

### 🗺️ Ce qui vient ensuite

Avec le profiling, vous disposez d'un outil de diagnostic rapide qui complète toute votre boîte à outils d'exploration et de nettoyage. La prochaine étape logique est la **visualisation avancée** (Matplotlib/Seaborn) pour créer vos propres graphiques sur mesure, puis le **Machine Learning** avec Scikit-learn — où vos données soigneusement diagnostiquées et nettoyées serviront enfin à construire des modèles.

---

## 9. ydata-profiling — Checkpoint 1

### 🎯 Objectif

Générer votre **premier rapport de profiling complet** sur un jeu de données du bootcamp, et **interpréter** les résultats.

### Instructions

```python
# ============================================
# CHECKPOINT 1 : Premier rapport de profiling
# ============================================
import pandas as pd
from ydata_profiling import ProfileReport

# ÉTAPE 1 : Charger le jeu de données (510 lignes)
df = pd.read_csv("bootcamp_500.csv")

# ÉTAPE 2 : Générer le rapport
rapport = ProfileReport(df, title="Bootcamp — Checkpoint 1", explorative=True)

# ÉTAPE 3 : Afficher dans le notebook
rapport

# ÉTAPE 4 : Exporter en HTML
rapport.to_file("checkpoint1_rapport.html")
print("✅ Rapport généré : checkpoint1_rapport.html")
```

### Questions à répondre en observant le rapport

1. Combien de variables et d'observations le jeu de données contient-il ?
2. Combien de cellules manquantes sont détectées, et dans quelles colonnes ?
3. Quelles **alertes** (Alerts) le rapport affiche-t-il ?
4. Quelle est la corrélation la plus forte entre deux variables numériques ?
5. Quelle colonne a la plus haute cardinalité (le plus de valeurs uniques) ?
6. La variable `age` présente-t-elle des valeurs suspectes (regardez son min et son max) ?

<details>
<summary>👀 Voir les réponses attendues</summary>

> 1. **10 variables**, **510 observations**.
> 2. **60 cellules manquantes** au total : `note_sql` (25), `note_python` (20), `ville` (15).
> 3. Alertes attendues : `note_sql/note_python/ville have missing values`, `note_sql highly correlated with note_python`, `id_etudiant has unique values` (haute cardinalité), `Dataset has 10 duplicate rows`.
> 4. **note_sql ↔ note_python (≈ 0.84)** est la plus forte, suivie de heures_etude ↔ notes (≈ 0.79).
> 5. **id_etudiant** (identifiant unique) — également prenom/nom avec une forte cardinalité.
> 6. **Oui** : `age` a un minimum de **-5** et un maximum de **200**, des valeurs impossibles → outliers/erreurs à corriger.
> 5. **nom** — chaque étudiant a un nom unique → 100% de valeurs distinctes.
</details>

---

## 10. ydata-profiling — Checkpoint 2

### 🎯 Objectif

Utiliser le profiling comme **outil de décision** : générer un rapport, **agir** sur les problèmes détectés, puis **comparer** avant/après nettoyage.

### Instructions

```python
# ============================================
# CHECKPOINT 2 : Profiling → Action → Comparaison
# ============================================
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# ÉTAPE 1 : Charger le jeu de données "sale" (510 lignes)
df_brut = pd.read_csv("bootcamp_500.csv")

# ÉTAPE 2 : Profiler les données BRUTES pour diagnostiquer
rapport_avant = ProfileReport(df_brut, title="AVANT nettoyage")
rapport_avant.to_file("checkpoint2_avant.html")
print("✅ Rapport AVANT généré")

# ÉTAPE 3 : Nettoyer selon les problèmes détectés (compétences des chapitres précédents)
df_propre = df_brut.copy()

# 3a. Anomalies : espaces + casse sur les villes
df_propre["ville"] = df_propre["ville"].str.strip().str.title()

# 3b. Valeurs impossibles : age hors [15, 100] et note > 20 → NaN
df_propre.loc[(df_propre["age"] < 15) | (df_propre["age"] > 100), "age"] = np.nan
df_propre.loc[df_propre["note_sql"] > 20, "note_sql"] = np.nan

# 3c. Supprimer les doublons
df_propre = df_propre.drop_duplicates()

# 3d. Imputer les valeurs manquantes (médiane pour le numérique, mode pour la ville)
df_propre["age"]         = df_propre["age"].fillna(df_propre["age"].median())
df_propre["note_sql"]    = df_propre["note_sql"].fillna(df_propre["note_sql"].median())
df_propre["note_python"] = df_propre["note_python"].fillna(df_propre["note_python"].median())
df_propre["ville"]       = df_propre["ville"].fillna(df_propre["ville"].mode()[0])

df_propre = df_propre.reset_index(drop=True)

# ÉTAPE 4 : Profiler les données NETTOYÉES
rapport_apres = ProfileReport(df_propre, title="APRÈS nettoyage")
rapport_apres.to_file("checkpoint2_apres.html")
print("✅ Rapport APRÈS généré")

# ÉTAPE 5 : Comparer les deux rapports côte à côte
comparaison = rapport_avant.compare(rapport_apres)
comparaison.to_file("checkpoint2_comparaison.html")
print("✅ Comparaison générée : checkpoint2_comparaison.html")
```

### Questions à répondre

1. Dans le rapport AVANT, combien de cellules manquantes et de lignes dupliquées sont détectées ?
2. Quelle alerte le profiling affiche-t-il concernant la variable `age` (à cause des valeurs 150, 200, -5...) ?
3. Dans le rapport APRÈS, les valeurs manquantes ont-elles disparu ?
4. En comparant les deux rapports, comment la moyenne et le maximum de `age` ont-ils évolué après traitement des outliers ?
5. Pourquoi la comparaison avant/après est-elle utile dans un vrai projet ?

<details>
<summary>👀 Voir les réponses attendues</summary>

> 1. **60 cellules manquantes** (note_sql : 25, note_python : 20, ville : 15) et **10 lignes dupliquées**.
> 2. Le profiling signale `age` comme fortement **asymétrique (skewed)** avec un maximum anormalement élevé (200) et un minimum négatif (-5) — signalant des outliers/valeurs impossibles.
> 3. **Oui**, après imputation (médiane/mode) et suppression des doublons, il ne devrait plus rester de cellules manquantes.
> 4. La **moyenne de `age` chute** d'environ 31 ans (tirée par les 150/175/200) vers ~31 ans réaliste, et surtout le **maximum passe de 200 à ~44 ans** une fois les valeurs impossibles remplacées par la médiane. La distribution redevient réaliste.
> 5. La comparaison permet de **vérifier objectivement** que le nettoyage a réglé les problèmes (plus de manquants, plus d'outliers, distributions normalisées) et de **documenter** l'impact du pré-traitement pour l'équipe.
</details>

---

## 11. ✅ Point de contrôle — Pandas Profiling

### 📝 Questions théoriques

**Q1.** Quel est l'intérêt du profiling par rapport à l'exploration manuelle vue au chapitre précédent ?

<details>
<summary>👀 Voir la réponse</summary>

> Le profiling **automatise** en une seule ligne (`ProfileReport(df)`) toute l'exploration qui demandait manuellement des dizaines de commandes (`info()`, `describe()`, `isna()`, `corr()`, histogrammes...). Il analyse toutes les colonnes, génère les visualisations et détecte automatiquement les problèmes via des **alertes**. C'est idéal pour un premier contact rapide avec un jeu de données.
</details>

---

**Q2.** Quelle est la différence entre `pandas-profiling` et `ydata-profiling` ?

<details>
<summary>👀 Voir la réponse</summary>

> Il s'agit de la **même bibliothèque** : `pandas-profiling` a été **renommée `ydata-profiling`** en 2023. Le package moderne à installer est `ydata-profiling` (`pip install ydata-profiling`) et l'import est `from ydata_profiling import ProfileReport`. L'ancien nom `pandas-profiling` est déprécié.
</details>

---

**Q3.** Qu'est-ce que la section "Alerts" d'un rapport et pourquoi est-elle utile ?

<details>
<summary>👀 Voir la réponse</summary>

> Les "Alerts" sont des **avertissements automatiques** que le profiling génère pour signaler des problèmes potentiels : valeurs manquantes, fortes corrélations, haute cardinalité, distributions asymétriques, colonnes constantes, déséquilibres... C'est souvent la partie la plus précieuse du rapport car elle attire immédiatement l'attention sur ce qui mérite d'être investigué.
</details>

---

**Q4.** Le profiling corrige-t-il automatiquement les problèmes détectés ?

<details>
<summary>👀 Voir la réponse</summary>

> **Non.** Le profiling **diagnostique** seulement — il détecte et signale les problèmes, mais ne les corrige pas. C'est au Data Scientist d'**interpréter** les alertes (avec son jugement métier) et d'**agir** avec Pandas (imputer, supprimer, encoder...). Le profiling ne connaît pas le contexte métier : il signalera un `age=150` comme un outlier, mais ne saura pas que c'est une erreur impossible.
</details>

---

**Q5.** Pourquoi utilise-t-on `minimal=True` ou un échantillon sur de gros jeux de données ?

<details>
<summary>👀 Voir la réponse</summary>

> Le profiling complet peut être **très lent et gourmand en mémoire** sur de gros datasets (au-delà de ~100 000 lignes), notamment à cause du calcul des corrélations et interactions entre toutes les variables. `minimal=True` désactive les analyses les plus coûteuses, et profiler un **échantillon** (`df.sample(n=5000)`) donne un aperçu rapide sans traiter tout le jeu de données.
</details>

---

### 💻 Exercices pratiques

> Ces exercices nécessitent l'installation de `ydata-profiling` (`!pip install ydata-profiling`).

---

**Exercice 1 — Premier rapport**

Chargez le fichier `etudiants.csv` (fourni) et générez un rapport de profiling que vous exportez en HTML.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("etudiants.csv")
rapport = ProfileReport(df, title="Étudiants")
rapport.to_file("rapport_etudiants.html")
print("✅ Rapport généré")
```
</details>

---

**Exercice 2 — Mode minimal**

Générez un rapport en mode minimal (rapide) sur le fichier `produits.csv`.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("produits.csv")
rapport = ProfileReport(df, title="Produits", minimal=True)
rapport.to_file("rapport_produits_minimal.html")
```
</details>

---

**Exercice 3 — Profiling d'un échantillon**

Créez un DataFrame de 1000 lignes aléatoires (avec NumPy), puis profilez un échantillon de 100 lignes seulement.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

np.random.seed(42)
df = pd.DataFrame({
    "age"  : np.random.randint(18, 60, 1000),
    "note" : np.random.uniform(0, 20, 1000),
    "ville": np.random.choice(["Abidjan", "Dakar", "Accra"], 1000)
})

echantillon = df.sample(n=100, random_state=42)
rapport = ProfileReport(echantillon, title="Échantillon", minimal=True)
rapport.to_file("rapport_echantillon.html")
```
</details>

---

**Exercice 4 — Comparaison avant/après**

Chargez `inscriptions_sales.csv`, générez un rapport, nettoyez les données, puis générez un rapport de comparaison avant/après.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Avant
df_brut = pd.read_csv("inscriptions_sales.csv")
rapport_avant = ProfileReport(df_brut, title="Avant")

# Nettoyage
df_propre = df_brut.copy()
df_propre["nom"]   = df_propre["nom"].str.strip().str.title()
df_propre["ville"] = df_propre["ville"].str.strip().str.title()
for col in ["note_sql", "note_python"]:
    df_propre[col] = df_propre[col].fillna(df_propre[col].median())
df_propre = df_propre.dropna(subset=["nom"]).drop_duplicates(subset=["nom"])

# Après
rapport_apres = ProfileReport(df_propre, title="Après")

# Comparaison
comparaison = rapport_avant.compare(rapport_apres)
comparaison.to_file("comparaison.html")
print("✅ Comparaison générée")
```
</details>

---

### 🏆 Challenge bonus

Réalisez un **cycle complet de diagnostic-action-vérification** sur `bootcamp_500.csv` (recommandé, 510 lignes) ou `brvm_cours.csv` :

1. Générez un rapport de profiling initial
2. Listez toutes les alertes détectées
3. Pour chaque alerte, décidez d'une action (nettoyer, encoder, ignorer, investiguer)
4. Appliquez les actions avec Pandas
5. Générez un nouveau rapport et vérifiez que les problèmes sont résolus
6. Rédigez un court résumé (3-5 lignes) de ce que le profiling vous a appris sur ce jeu de données

*Cet exercice reproduit exactement le workflow réel d'un Data Scientist face à un nouveau jeu de données.*

---

*📘 Module Data Science — Pandas Profiling (ydata-profiling) | Bootcamp Data Science*
