# 📊 Data Visualization with Python — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : NumPy, Pandas (Cleaning, Exploration), Profiling

---

## Table des matières

1. [Introduction to Data Visualization](#1-introduction-to-data-visualization)
2. [Exploring Popular Chart Types](#2-exploring-popular-chart-types)
3. [How to Choose the Right Chart for Your Data](#3-how-to-choose-the-right-chart-for-your-data)
4. [Introduction to Matplotlib and Seaborn](#4-introduction-to-matplotlib-and-seaborn)
5. [Introduction to Plotly](#5-introduction-to-plotly)
6. [How to Choose Between Plotly, Matplotlib, and Seaborn](#6-how-to-choose-between-plotly-matplotlib-and-seaborn)
7. [Bonnes pratiques de visualisation](#7-bonnes-pratiques-de-visualisation)
8. [Conclusion](#8-conclusion)
9. [Python Project — Dashboard du Bootcamp](#9-python-project--dashboard-du-bootcamp)
10. [✅ Point de contrôle — Data Visualization](#10--point-de-contrôle--data-visualization)

---

## 1. Introduction to Data Visualization

### 📖 Qu'est-ce que la visualisation de données ?

La **visualisation de données** consiste à représenter des données sous forme **graphique** (courbes, barres, nuages de points...) pour les rendre **compréhensibles en un coup d'œil**. C'est le pont entre les chiffres bruts et la compréhension humaine.

> 💡 **Analogie** : Imaginez qu'on vous donne un tableau de 510 lignes de notes d'étudiants. En le lisant ligne par ligne, vous ne verrez rien. Mais si on transforme ce tableau en **histogramme**, vous voyez immédiatement si les notes sont bonnes, mauvaises, groupées ou dispersées. La visualisation, c'est **donner des yeux à vos données**.

### 1.1 Pourquoi visualiser ?

```
POURQUOI LA VISUALISATION EST ESSENTIELLE
│
├── 👁️  Comprendre vite     → Un graphique se lit en secondes, un tableau en minutes
├── 🔍 Détecter            → Outliers, tendances, groupes invisibles dans les chiffres
├── 📖 Raconter            → Communiquer un résultat à un public non technique
├── 🧭 Explorer            → Guider l'analyse (quelle variable creuser ?)
└── ✅ Convaincre          → Un bon graphique vaut mille tableaux Excel
```

### 1.2 Le célèbre "Quartet d'Anscombe"

Quatre jeux de données peuvent avoir **exactement les mêmes statistiques** (même moyenne, même écart type, même corrélation) mais des formes **totalement différentes** — visibles uniquement en les traçant.

```
Même moyenne, même écart type, même corrélation...
mais des réalités COMPLÈTEMENT différentes :

  Jeu 1          Jeu 2          Jeu 3          Jeu 4
  linéaire       courbe         ligne+outlier  vertical+outlier
     •              •••            •               •
   •   •         •      •        •              •
  •     •       •        •      •               •
 •       •     •          •    •                •••••
```

> 🔑 **Leçon fondamentale** : Les statistiques seules **peuvent mentir**. Toujours **visualiser** avant de conclure. C'est pourquoi la visualisation est indissociable de l'exploration de données.

### 1.3 Les visualisations que vous connaissez déjà

Vous avez déjà créé des graphiques dans les chapitres précédents !

```python
# Rappel des chapitres Exploration/Profiling
df["note_sql"].hist()              # histogramme
df.boxplot(column=["age"])          # boîte à moustaches
df.plot(kind="scatter", x=..., y=...) # nuage de points
```

Dans ce chapitre, nous allons **maîtriser** ces outils et en découvrir de nouveaux, plus puissants et plus beaux.

### 1.4 Le jeu de données du chapitre

Nous utilisons `bootcamp_500.csv` (510 lignes), déjà connu des chapitres précédents. Chargeons-le et nettoyons-le rapidement :

```python
import pandas as pd
import numpy as np

# Charger et nettoyer (compétences des chapitres précédents)
df = pd.read_csv("bootcamp_500.csv")
df["ville"] = df["ville"].str.strip().str.title()
df.loc[(df["age"] < 15) | (df["age"] > 100), "age"] = np.nan
df.loc[df["note_sql"] > 20, "note_sql"] = np.nan
for col in ["age", "note_sql", "note_python"]:
    df[col] = df[col].fillna(df[col].median())
df["ville"] = df["ville"].fillna(df["ville"].mode()[0])
df = df.drop_duplicates().reset_index(drop=True)

print(df.shape)   # (500, 10)
```

> 💡 On travaille toujours sur des données **propres** — d'où l'importance des chapitres précédents. Un beau graphique sur des données sales reste trompeur !

---

## 2. Exploring Popular Chart Types

### 📖 Les grandes familles de graphiques

Chaque type de graphique répond à une **question** précise. Voici les plus courants.

### 2.1 Vue d'ensemble

```
TYPES DE GRAPHIQUES ET LEUR USAGE
│
├── 📊 Histogramme       → Distribution d'UNE variable numérique
├── 📈 Courbe (line)     → Évolution dans le TEMPS
├── 📊 Barres (bar)      → Comparer des CATÉGORIES
├── 🥧 Camembert (pie)   → Proportions d'un TOUT (à éviter souvent !)
├── ⚫ Nuage (scatter)   → Relation entre DEUX variables numériques
├── 📦 Boîte (boxplot)   → Distribution + outliers, comparaison de groupes
├── 🌡️  Heatmap          → Matrice de valeurs (corrélations, densité)
└── 🎻 Violon (violin)   → Distribution détaillée par groupe
```

### 2.2 Histogramme — Distribution d'une variable

Montre **comment les valeurs se répartissent** (groupées, étalées, symétriques...).

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["note_sql"], bins=20, color="#3498db", edgecolor="white")
plt.title("Distribution des notes SQL")
plt.xlabel("Note SQL")
plt.ylabel("Nombre d'étudiants")
plt.show()
```

> **Question répondue** : "Comment sont réparties les notes ? La plupart des étudiants ont-ils de bonnes ou mauvaises notes ?"

### 2.3 Diagramme en barres — Comparer des catégories

```python
# Nombre d'étudiants par ville
comptage = df["ville"].value_counts()

plt.figure(figsize=(10, 5))
comptage.plot(kind="bar", color="#2ecc71")
plt.title("Nombre d'étudiants par ville")
plt.xlabel("Ville")
plt.ylabel("Nombre d'étudiants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

> **Question répondue** : "Quelle ville a le plus d'étudiants ?"

### 2.4 Nuage de points — Relation entre deux variables

```python
plt.figure(figsize=(8, 5))
plt.scatter(df["heures_etude"], df["note_sql"], alpha=0.5, color="#e74c3c")
plt.title("Relation heures d'étude / note SQL")
plt.xlabel("Heures d'étude par semaine")
plt.ylabel("Note SQL")
plt.show()
```

> **Question répondue** : "Est-ce que plus on étudie, meilleures sont les notes ?" (Réponse : oui, tendance montante nette !)

### 2.5 Boxplot — Distribution et outliers

```python
plt.figure(figsize=(8, 5))
df.boxplot(column="note_sql", by="niveau")
plt.title("Notes SQL par niveau")
plt.suptitle("")  # supprime le titre automatique
plt.xlabel("Niveau")
plt.ylabel("Note SQL")
plt.show()
```

> **Question répondue** : "Les étudiants 'Avancé' ont-ils vraiment de meilleures notes ? Y a-t-il des outliers par groupe ?"

### 2.6 Courbe (line chart) — Évolution

La courbe est idéale pour les **séries temporelles**. Notre dataset n'a pas de dimension temporelle, mais voici le principe :

```python
# Exemple : évolution simulée de la moyenne sur plusieurs promotions
promotions = ["2021", "2022", "2023", "2024", "2025"]
moyennes = [12.5, 13.2, 13.8, 14.1, 14.6]

plt.figure(figsize=(8, 5))
plt.plot(promotions, moyennes, marker="o", color="#9b59b6", linewidth=2)
plt.title("Évolution de la moyenne par promotion")
plt.xlabel("Promotion")
plt.ylabel("Moyenne générale")
plt.grid(True, alpha=0.3)
plt.show()
```

> **Question répondue** : "Comment la moyenne évolue-t-elle au fil des années ?"

### 2.7 Camembert (pie chart) — Proportions

```python
proportions = df["niveau"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(proportions, labels=proportions.index, autopct="%1.1f%%",
        colors=["#3498db", "#2ecc71", "#e74c3c"])
plt.title("Répartition des niveaux")
plt.show()
```

> ⚠️ **Attention aux camemberts !** Ils sont difficiles à lire dès qu'il y a plus de 3-4 catégories, et l'œil humain compare mal les angles. **Un diagramme en barres est presque toujours préférable.**

### 2.8 Heatmap — Matrice de valeurs

```python
import seaborn as sns

# Matrice de corrélation visualisée
correlation = df[["age", "heures_etude", "note_sql", "note_python", "salaire_stage"]].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()
```

> **Question répondue** : "Quelles variables sont liées entre elles ?" (Les cases foncées révèlent les fortes corrélations comme note_sql ↔ note_python.)

---

## 3. How to Choose the Right Chart for Your Data

### 📖 Le bon graphique pour la bonne question

Choisir le graphique dépend de **ce que vous voulez montrer** et du **type de vos variables**.

### 3.1 L'arbre de décision

```
QUELLE EST VOTRE QUESTION ?
│
├── "Comment se répartit UNE variable ?"
│   ├── numérique   → HISTOGRAMME ou BOXPLOT
│   └── catégorielle → DIAGRAMME EN BARRES
│
├── "Comparer des CATÉGORIES ?"
│   → DIAGRAMME EN BARRES
│
├── "Relation entre DEUX variables numériques ?"
│   → NUAGE DE POINTS (scatter)
│
├── "Évolution dans le TEMPS ?"
│   → COURBE (line chart)
│
├── "Proportions d'un TOUT ?"
│   → BARRES (ou camembert si ≤ 3 catégories)
│
├── "Distribution par GROUPE ?"
│   → BOXPLOT ou VIOLIN PLOT
│
└── "Relations entre PLUSIEURS variables ?"
    → HEATMAP ou PAIRPLOT
```

### 3.2 Tableau de correspondance question → graphique

| Question | Type de variables | Graphique recommandé |
|----------|---------------------|------------------------|
| Distribution d'une variable | 1 numérique | Histogramme, Boxplot |
| Fréquence d'une catégorie | 1 catégorielle | Barres |
| Comparer des groupes | 1 catég. + 1 numér. | Barres, Boxplot |
| Corrélation | 2 numériques | Nuage de points |
| Évolution temporelle | temps + numérique | Courbe |
| Proportions | 1 catégorielle | Barres (ou camembert) |
| Corrélations multiples | plusieurs numér. | Heatmap |
| Vue d'ensemble des relations | plusieurs numér. | Pairplot |

### 3.3 Les erreurs à éviter

```
❌ ERREURS COURANTES                    ✅ BONNE PRATIQUE
─────────────────────────               ─────────────────────────
Camembert avec 10 catégories            → Diagramme en barres
Courbe pour des catégories              → Barres (la courbe = temps)
Axes tronqués (ne commencent pas à 0)   → Axes honnêtes
Trop de couleurs sans signification     → Couleurs sobres et utiles
Pas de titre ni de labels                → Toujours titrer et étiqueter
3D inutile qui déforme la lecture       → 2D clair
```

---

## 4. Introduction to Matplotlib and Seaborn

### 📖 Les deux bibliothèques fondamentales

**Matplotlib** est la bibliothèque de visualisation **historique et fondamentale** de Python — puissante mais parfois verbeuse. **Seaborn** est construite **par-dessus** Matplotlib pour produire de **beaux graphiques statistiques** avec moins de code.

```
RELATION MATPLOTLIB / SEABORN
│
Matplotlib   → moteur de base, contrôle total, verbeux
   │
   ▼
Seaborn      → couche au-dessus, graphiques statistiques élégants,
               intégration directe avec Pandas, moins de code
```

> 💡 **Analogie** : Matplotlib est comme cuisiner **à partir d'ingrédients bruts** — contrôle total mais plus de travail. Seaborn est comme un **kit de préparation** — plus rapide, plus joli par défaut, mais construit sur les mêmes ingrédients (Matplotlib en dessous).

### 4.1 Matplotlib — Les bases

```python
import matplotlib.pyplot as plt

# Structure de base d'un graphique Matplotlib
plt.figure(figsize=(8, 5))        # créer la figure (taille en pouces)
plt.plot([1, 2, 3], [4, 5, 6])    # tracer les données
plt.title("Mon titre")             # titre
plt.xlabel("Axe X")                # étiquette axe X
plt.ylabel("Axe Y")                # étiquette axe Y
plt.legend(["Ma courbe"])          # légende
plt.grid(True, alpha=0.3)          # grille
plt.show()                          # afficher
```

### 4.2 Matplotlib — Anatomie d'une figure

```
        Titre de la figure
   ┌─────────────────────────────┐
 A │                        •     │
 x │                   •          │
 e │              •               │  ← zone de tracé (Axes)
   │         •                    │
 Y │    •                         │
   └─────────────────────────────┘
        Axe X (xlabel)
```

### 4.3 Matplotlib — Plusieurs graphiques (subplots)

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))   # 1 ligne, 2 colonnes

# Premier graphique (à gauche)
axes[0].hist(df["note_sql"], bins=20, color="#3498db")
axes[0].set_title("Distribution note SQL")
axes[0].set_xlabel("Note")

# Deuxième graphique (à droite)
axes[1].scatter(df["heures_etude"], df["note_sql"], alpha=0.5, color="#e74c3c")
axes[1].set_title("Heures d'étude vs note")
axes[1].set_xlabel("Heures")

plt.tight_layout()
plt.show()
```

### 4.4 Seaborn — Plus beau, moins de code

```python
import seaborn as sns

# Seaborn applique un style élégant par défaut
sns.set_theme(style="whitegrid")

# Histogramme avec courbe de densité — en UNE ligne !
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="note_sql", kde=True, color="#3498db")
plt.title("Distribution des notes SQL")
plt.show()
```

### 4.5 Seaborn — Graphiques statistiques puissants

```python
# Boxplot par catégorie — comparaison instantanée
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="niveau", y="note_sql",
            order=["Débutant", "Intermédiaire", "Avancé"])
plt.title("Notes SQL par niveau")
plt.show()
```

```python
# Nuage de points avec couleur par catégorie + droite de régression
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="heures_etude", y="note_sql", hue="niveau", alpha=0.6)
plt.title("Heures d'étude vs note SQL, par niveau")
plt.show()

# Avec droite de tendance automatique
sns.lmplot(data=df, x="heures_etude", y="note_sql", height=5, aspect=1.5)
plt.title("Tendance : heures d'étude → note SQL")
plt.show()
```

```python
# Violin plot — distribution détaillée par groupe
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x="niveau", y="note_python",
               order=["Débutant", "Intermédiaire", "Avancé"])
plt.title("Distribution des notes Python par niveau")
plt.show()
```

```python
# Heatmap de corrélation (très courant en Data Science)
plt.figure(figsize=(8, 6))
corr = df[["age", "heures_etude", "note_sql", "note_python", "salaire_stage"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()
```

```python
# Pairplot — TOUTES les relations entre variables numériques d'un coup
sns.pairplot(df[["heures_etude", "note_sql", "note_python", "niveau"]], hue="niveau")
plt.show()
```

> 🔑 Le **pairplot** est un outil d'exploration extrêmement puissant : il trace en une commande **toutes les paires de variables** + les distributions sur la diagonale. Idéal en début d'analyse.

### 4.6 Tableau des fonctions Seaborn essentielles

| Fonction Seaborn | Type de graphique | Usage |
|--------------------|---------------------|-------|
| `sns.histplot()` | Histogramme | Distribution d'une variable |
| `sns.boxplot()` | Boîte à moustaches | Distribution + outliers par groupe |
| `sns.violinplot()` | Violon | Distribution détaillée par groupe |
| `sns.scatterplot()` | Nuage de points | Relation entre 2 variables |
| `sns.lmplot()` | Nuage + régression | Relation avec tendance |
| `sns.barplot()` | Barres | Comparer des moyennes par catégorie |
| `sns.countplot()` | Barres de comptage | Fréquence d'une catégorie |
| `sns.heatmap()` | Carte de chaleur | Matrice (corrélations) |
| `sns.pairplot()` | Grille de nuages | Toutes les relations d'un coup |

---

## 5. Introduction to Plotly

### 📖 Des graphiques interactifs

**Plotly** est une bibliothèque qui génère des graphiques **interactifs** : on peut **survoler** les points pour voir leurs valeurs, **zoomer**, **filtrer**, et même créer des **dashboards** dynamiques. Idéal pour l'exploration et les présentations web.

> 💡 **Analogie** : Matplotlib/Seaborn produisent des **photos** (images figées). Plotly produit des **vidéos interactives** — le lecteur peut manipuler le graphique lui-même (survoler, zoomer, masquer des séries).

### 5.1 Installation et import

```python
!pip install plotly

import plotly.express as px   # px = interface simple et rapide de Plotly
```

### 5.2 Plotly Express — Graphiques en une ligne

```python
import plotly.express as px

# Nuage de points interactif (survolez les points !)
fig = px.scatter(
    df,
    x="heures_etude",
    y="note_sql",
    color="niveau",
    hover_data=["prenom", "ville"],   # infos au survol
    title="Heures d'étude vs Note SQL (interactif)"
)
fig.show()
```

> 💡 Dans le graphique généré, **passez la souris** sur un point : vous verrez le prénom, la ville, les heures et la note de cet étudiant précis. Impossible avec Matplotlib !

### 5.3 Autres graphiques Plotly courants

```python
# Histogramme interactif
fig = px.histogram(df, x="note_sql", nbins=20, color="niveau",
                   title="Distribution des notes SQL par niveau")
fig.show()

# Diagramme en barres
comptage = df["ville"].value_counts().reset_index()
comptage.columns = ["ville", "nombre"]
fig = px.bar(comptage, x="ville", y="nombre",
             title="Étudiants par ville", color="nombre")
fig.show()

# Boxplot interactif
fig = px.box(df, x="niveau", y="note_python",
             title="Notes Python par niveau")
fig.show()

# Camembert
fig = px.pie(df, names="niveau", title="Répartition des niveaux")
fig.show()
```

### 5.4 Graphiques avancés Plotly

```python
# Scatter matrix (équivalent du pairplot, mais interactif)
fig = px.scatter_matrix(
    df,
    dimensions=["heures_etude", "note_sql", "note_python"],
    color="niveau",
    title="Matrice de nuages interactive"
)
fig.show()

# Graphique 3D
fig = px.scatter_3d(
    df,
    x="heures_etude", y="note_sql", z="note_python",
    color="niveau",
    title="Vue 3D : heures, note SQL, note Python"
)
fig.show()
```

### 5.5 Exporter un graphique Plotly

```python
# Sauvegarder en HTML interactif (partageable)
fig.write_html("graphique_interactif.html")

# Sauvegarder en image statique (nécessite : pip install kaleido)
fig.write_image("graphique.png")
```

---

## 6. How to Choose Between Plotly, Matplotlib, and Seaborn

### 📖 Trois outils, trois usages

Chaque bibliothèque a ses forces. Le choix dépend du **contexte** et de l'**objectif**.

### 6.1 Tableau comparatif

| Critère | Matplotlib | Seaborn | Plotly |
|---------|------------|---------|--------|
| **Facilité** | ⭐⭐ (verbeux) | ⭐⭐⭐⭐ (concis) | ⭐⭐⭐⭐ (concis) |
| **Beauté par défaut** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Interactivité** | ❌ Non | ❌ Non | ✅ Oui |
| **Contrôle fin** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Graphiques statistiques** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Rapports/publications** | ✅ Excellent | ✅ Excellent | ⭐⭐ |
| **Dashboards web** | ❌ | ❌ | ✅ Excellent |
| **Construit sur** | — | Matplotlib | — |

### 6.2 Quand utiliser quoi ?

```
GUIDE DE CHOIX
│
├── 📊 Exploration rapide et graphiques statistiques
│   → SEABORN (concis, beau, parfait pour l'EDA)
│
├── 🎯 Contrôle total, personnalisation poussée, publication scientifique
│   → MATPLOTLIB (le moteur de base, tout est ajustable)
│
├── 🖱️  Graphiques interactifs, présentation web, exploration dynamique
│   → PLOTLY (survol, zoom, dashboards)
│
└── 💡 En pratique : on combine souvent Seaborn (rapide) + Matplotlib
      (ajustements fins), et Plotly pour les livrables interactifs
```

### 6.3 Le même graphique dans les trois bibliothèques

```python
# ===== MATPLOTLIB =====
import matplotlib.pyplot as plt
plt.scatter(df["heures_etude"], df["note_sql"], alpha=0.5)
plt.title("Matplotlib"); plt.xlabel("Heures"); plt.ylabel("Note SQL")
plt.show()

# ===== SEABORN =====
import seaborn as sns
sns.scatterplot(data=df, x="heures_etude", y="note_sql", hue="niveau")
plt.title("Seaborn")
plt.show()

# ===== PLOTLY =====
import plotly.express as px
fig = px.scatter(df, x="heures_etude", y="note_sql", color="niveau", title="Plotly")
fig.show()
```

> 🔑 Même donnée, trois rendus : Matplotlib (basique), Seaborn (élégant + couleurs par groupe faciles), Plotly (interactif). Maîtriser les trois vous rend polyvalent.

---

## 7. Bonnes pratiques de visualisation

### 7.1 Les règles d'or d'un bon graphique

```
✅ UN BON GRAPHIQUE...
│
├── 📌 A un TITRE clair qui explique ce qu'on voit
├── 🏷️  A des AXES ÉTIQUETÉS (avec unités si pertinent)
├── 📏 A des axes HONNÊTES (commençant à 0 pour les barres)
├── 🎨 Utilise la couleur avec PARCIMONIE et un but précis
├── 🔍 Est LISIBLE (police assez grande, pas surchargé)
├── 📖 Raconte UNE histoire (un message principal)
└── ♿ Reste ACCESSIBLE (palettes adaptées au daltonisme)
```

### 7.2 Personnaliser proprement

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")   # style propre par défaut

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="ville", y="note_sql", ax=ax,
            estimator="mean", errorbar=None, palette="viridis")

ax.set_title("Note SQL moyenne par ville", fontsize=14, fontweight="bold")
ax.set_xlabel("Ville", fontsize=12)
ax.set_ylabel("Note SQL moyenne", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("note_par_ville.png", dpi=150, bbox_inches="tight")  # export haute qualité
plt.show()
```

### 7.3 Les palettes de couleurs

```
CHOISIR LA BONNE PALETTE
│
├── Séquentielle (valeurs ordonnées : faible → fort)
│   → "Blues", "viridis", "YlOrRd"
│
├── Divergente (écart autour d'un centre : -/0/+)
│   → "coolwarm", "RdBu"  (idéal pour les corrélations)
│
└── Qualitative (catégories distinctes, sans ordre)
    → "Set2", "tab10", "pastel"
```

> 💡 **Astuce accessibilité** : la palette `viridis` est lisible même par les personnes daltoniennes et en impression noir et blanc. C'est un excellent choix par défaut.

---

## 8. Conclusion

### 📌 Récapitulatif du chapitre

```
DATA VISUALIZATION WITH PYTHON
│
├── Pourquoi visualiser ?
│   └── Comprendre, détecter, raconter (Quartet d'Anscombe : les stats mentent)
│
├── Types de graphiques
│   ├── Histogramme  → distribution
│   ├── Barres        → comparer des catégories
│   ├── Nuage         → relation entre 2 variables
│   ├── Boxplot/Violin→ distribution par groupe
│   ├── Courbe         → évolution temporelle
│   └── Heatmap        → corrélations
│
├── Choisir le bon graphique
│   └── Selon la QUESTION et le TYPE de variables
│
├── Les 3 bibliothèques
│   ├── Matplotlib → moteur de base, contrôle total
│   ├── Seaborn    → statistiques élégantes, concis (sur Matplotlib)
│   └── Plotly     → interactif, dashboards web
│
└── Bonnes pratiques
    └── Titre, axes étiquetés, axes honnêtes, couleurs utiles, accessibilité
```

### 🔑 Points clés à retenir

1. **Toujours visualiser** : les statistiques seules peuvent masquer la réalité (Quartet d'Anscombe).
2. Le **choix du graphique** dépend de la question posée et du type de variables.
3. **Matplotlib** = contrôle total ; **Seaborn** = beau et concis pour les stats ; **Plotly** = interactif.
4. **Seaborn est construit sur Matplotlib** — on combine souvent les deux.
5. Un bon graphique a **toujours** un titre, des axes étiquetés et des couleurs utiles.
6. Éviter les **camemberts** à plus de 3-4 catégories et les **axes tronqués** (trompeurs).

### 🗺️ Ce qui vient ensuite

Vous disposez maintenant de tout l'arsenal pour **explorer, nettoyer, diagnostiquer ET visualiser** vos données. La dernière grande étape du parcours est le **Machine Learning** avec Scikit-learn — où toutes ces compétences convergent pour construire des modèles prédictifs, dont les résultats devront eux aussi être... visualisés !

---

## 9. Python Project — Dashboard du Bootcamp

### 🎯 Objectif du projet

Construire un **tableau de bord visuel complet** de la promotion du bootcamp, combinant plusieurs graphiques pour raconter l'histoire des données `bootcamp_500.csv`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# ============================================
# ÉTAPE 1 : Charger et nettoyer les données
# ============================================
df = pd.read_csv("bootcamp_500.csv")
df["ville"] = df["ville"].str.strip().str.title()
df.loc[(df["age"] < 15) | (df["age"] > 100), "age"] = np.nan
df.loc[df["note_sql"] > 20, "note_sql"] = np.nan
for col in ["age", "note_sql", "note_python"]:
    df[col] = df[col].fillna(df[col].median())
df["ville"] = df["ville"].fillna(df["ville"].mode()[0])
df = df.drop_duplicates().reset_index(drop=True)
df["moyenne"] = (df["note_sql"] + df["note_python"]) / 2

# ============================================
# ÉTAPE 2 : Construire un dashboard 2x2
# ============================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("📊 Dashboard du Bootcamp Data Science", fontsize=18, fontweight="bold")

# Graphique 1 : Distribution des moyennes (histogramme)
sns.histplot(data=df, x="moyenne", bins=20, kde=True, ax=axes[0, 0], color="#3498db")
axes[0, 0].set_title("Distribution des moyennes")
axes[0, 0].set_xlabel("Moyenne générale")

# Graphique 2 : Étudiants par ville (barres)
comptage = df["ville"].value_counts()
sns.barplot(x=comptage.values, y=comptage.index, ax=axes[0, 1], palette="viridis")
axes[0, 1].set_title("Nombre d'étudiants par ville")
axes[0, 1].set_xlabel("Nombre d'étudiants")

# Graphique 3 : Heures d'étude vs moyenne (nuage de points)
sns.scatterplot(data=df, x="heures_etude", y="moyenne", hue="niveau",
                alpha=0.6, ax=axes[1, 0])
axes[1, 0].set_title("Relation heures d'étude / moyenne")
axes[1, 0].set_xlabel("Heures d'étude par semaine")

# Graphique 4 : Notes par niveau (boxplot)
sns.boxplot(data=df, x="niveau", y="moyenne",
            order=["Débutant", "Intermédiaire", "Avancé"], ax=axes[1, 1])
axes[1, 1].set_title("Moyenne par niveau")

plt.tight_layout()
plt.savefig("dashboard_bootcamp.png", dpi=150, bbox_inches="tight")
plt.show()

print("✅ Dashboard généré et sauvegardé dans dashboard_bootcamp.png")

# ============================================
# ÉTAPE 3 : Une visualisation interactive avec Plotly (bonus)
# ============================================
import plotly.express as px

fig_interactif = px.scatter(
    df, x="heures_etude", y="moyenne", color="niveau",
    size="salaire_stage", hover_data=["prenom", "ville"],
    title="Dashboard interactif — Heures d'étude vs Moyenne"
)
fig_interactif.write_html("dashboard_interactif.html")
print("✅ Dashboard interactif sauvegardé dans dashboard_interactif.html")
```

> 💡 **Ce projet illustre le rôle final de la visualisation** : après avoir collecté, nettoyé et exploré les données, on les **synthétise en un dashboard** qui raconte une histoire claire — l'aboutissement de tout le travail de préparation.

---

## 10. ✅ Point de contrôle — Data Visualization

### 📝 Questions théoriques

**Q1.** Que nous enseigne le "Quartet d'Anscombe" sur l'importance de la visualisation ?

<details>
<summary>👀 Voir la réponse</summary>

> Le Quartet d'Anscombe montre que quatre jeux de données peuvent avoir des **statistiques identiques** (moyenne, écart type, corrélation) tout en ayant des **formes complètement différentes**, visibles uniquement en les traçant. La leçon : les statistiques seules peuvent être trompeuses, il faut **toujours visualiser** ses données avant de conclure.
</details>

---

**Q2.** Quel graphique choisir pour montrer la relation entre deux variables numériques ?

<details>
<summary>👀 Voir la réponse</summary>

> Le **nuage de points** (scatter plot). Il place chaque observation selon ses deux valeurs et révèle visuellement s'il existe une tendance (corrélation positive/négative) ou aucune relation. On peut y ajouter une droite de régression (`sns.lmplot`) pour confirmer la tendance.
</details>

---

**Q3.** Quelle est la relation entre Matplotlib et Seaborn ?

<details>
<summary>👀 Voir la réponse</summary>

> Seaborn est **construit par-dessus Matplotlib**. Seaborn fournit une interface plus simple et des graphiques statistiques plus élégants par défaut, mais utilise Matplotlib comme moteur en dessous. On peut donc mélanger les deux : créer un graphique avec Seaborn puis l'ajuster finement avec des commandes Matplotlib.
</details>

---

**Q4.** Dans quel cas privilégier Plotly plutôt que Matplotlib/Seaborn ?

<details>
<summary>👀 Voir la réponse</summary>

> On privilégie **Plotly** quand on a besoin d'**interactivité** : survol pour voir les valeurs exactes, zoom, filtrage dynamique, ou création de **dashboards web**. Matplotlib/Seaborn produisent des images statiques, idéales pour des rapports ou publications, tandis que Plotly excelle pour l'exploration dynamique et les présentations interactives.
</details>

---

**Q5.** Pourquoi déconseille-t-on souvent le camembert (pie chart) ?

<details>
<summary>👀 Voir la réponse</summary>

> Le camembert devient **difficile à lire dès qu'il y a plus de 3-4 catégories**, car l'œil humain compare mal les **angles** et les **surfaces**. Un diagramme en barres, où l'on compare des **longueurs** (plus faciles à évaluer), est presque toujours plus lisible et précis pour représenter des proportions ou des comparaisons.
</details>

---

### 💻 Exercices pratiques

> Utilisez `bootcamp_500.csv` (nettoyé au préalable comme montré en section 1.4).

---

**Exercice 1 — Histogramme**

Tracez l'histogramme de la colonne `note_python` avec 20 intervalles (bins), un titre et des axes étiquetés.

<details>
<summary>👀 Voir la solution</summary>

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["note_python"], bins=20, color="#2ecc71", edgecolor="white")
plt.title("Distribution des notes Python")
plt.xlabel("Note Python")
plt.ylabel("Nombre d'étudiants")
plt.show()
```
</details>

---

**Exercice 2 — Diagramme en barres**

Affichez le nombre d'étudiants par niveau sous forme de diagramme en barres avec Seaborn (`countplot`).

<details>
<summary>👀 Voir la solution</summary>

```python
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="niveau", order=["Débutant", "Intermédiaire", "Avancé"])
plt.title("Nombre d'étudiants par niveau")
plt.show()
```
</details>

---

**Exercice 3 — Nuage de points**

Avec Seaborn, tracez `note_sql` en fonction de `note_python`, coloré par `niveau`. Que constatez-vous ?

<details>
<summary>👀 Voir la solution</summary>

```python
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="note_sql", y="note_python", hue="niveau", alpha=0.6)
plt.title("Note SQL vs Note Python")
plt.show()
# Constat : forte corrélation positive — un bon étudiant l'est dans les deux matières
```
</details>

---

**Exercice 4 — Boxplot comparatif**

Comparez la distribution de `salaire_stage` selon le `niveau` avec un boxplot Seaborn.

<details>
<summary>👀 Voir la solution</summary>

```python
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="niveau", y="salaire_stage",
            order=["Débutant", "Intermédiaire", "Avancé"])
plt.title("Salaire de stage par niveau")
plt.show()
```
</details>

---

**Exercice 5 — Heatmap de corrélation**

Créez une heatmap de corrélation entre `age`, `heures_etude`, `note_sql`, `note_python` et `salaire_stage`.

<details>
<summary>👀 Voir la solution</summary>

```python
import seaborn as sns

corr = df[["age", "heures_etude", "note_sql", "note_python", "salaire_stage"]].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()
```
</details>

---

**Exercice 6 — Plotly interactif**

Créez un nuage de points interactif avec Plotly : `heures_etude` vs `moyenne` (à calculer), coloré par `ville`, avec le prénom au survol.

<details>
<summary>👀 Voir la solution</summary>

```python
import plotly.express as px

df["moyenne"] = (df["note_sql"] + df["note_python"]) / 2

fig = px.scatter(
    df, x="heures_etude", y="moyenne", color="ville",
    hover_data=["prenom"],
    title="Heures d'étude vs Moyenne (interactif)"
)
fig.show()
```
</details>

---

### 🏆 Challenge bonus — Raconter une histoire avec les données

En utilisant `bootcamp_500.csv`, créez une **série de 3 à 4 graphiques** qui répondent à cette question métier :

> **"Quels sont les facteurs associés à la réussite des étudiants (moyenne élevée) ?"**

Votre analyse visuelle devrait explorer :
1. La distribution des moyennes (qui réussit ?)
2. Le lien entre heures d'étude et moyenne (l'effort paie-t-il ?)
3. La différence de réussite entre niveaux ou entre villes
4. La corrélation entre les différentes variables

Terminez par un **court paragraphe** (3-5 lignes) résumant vos conclusions, appuyées par vos graphiques.

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Charger et nettoyer
df = pd.read_csv("bootcamp_500.csv")
df["ville"] = df["ville"].str.strip().str.title()
df.loc[(df["age"]<15)|(df["age"]>100), "age"] = np.nan
df.loc[df["note_sql"]>20, "note_sql"] = np.nan
for c in ["age","note_sql","note_python"]: df[c]=df[c].fillna(df[c].median())
df = df.drop_duplicates().reset_index(drop=True)
df["moyenne"] = (df["note_sql"] + df["note_python"]) / 2

fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# 1. Distribution des moyennes
sns.histplot(df["moyenne"], bins=20, kde=True, ax=axes[0,0], color="#3498db")
axes[0,0].set_title("1. Qui réussit ? (distribution des moyennes)")

# 2. Heures d'étude vs moyenne
sns.regplot(data=df, x="heures_etude", y="moyenne", ax=axes[0,1],
            scatter_kws={"alpha":0.4})
axes[0,1].set_title("2. L'effort paie-t-il ?")

# 3. Moyenne par niveau
sns.boxplot(data=df, x="niveau", y="moyenne",
            order=["Débutant","Intermédiaire","Avancé"], ax=axes[1,0])
axes[1,0].set_title("3. Réussite par niveau")

# 4. Corrélations
corr = df[["heures_etude","note_sql","note_python","moyenne"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f", ax=axes[1,1])
axes[1,1].set_title("4. Corrélations")

plt.tight_layout()
plt.show()

print('''
CONCLUSIONS :
- Les moyennes suivent une distribution en cloche centrée autour de 9-10/20.
- Il existe une forte corrélation positive (~0.8) entre les heures d'étude
  et la moyenne : l'effort est clairement associé à la réussite.
- Les étudiants de niveau "Avancé" ont des moyennes légèrement supérieures,
  mais l'écart est modéré.
- note_sql et note_python sont très corrélées : les compétences se transfèrent.
''')
```
</details>

---

*📘 Module Data Science — Data Visualization with Python | Bootcamp Data Science*
