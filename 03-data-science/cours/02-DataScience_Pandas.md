# 🐼 Data Cleaning and Transformation with Pandas — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : NumPy, File Handling, Web Scraping

---

## Table des matières

1. [Introduction to Pandas — Vue d'ensemble](#1-introduction-to-pandas--vue-densemble)
2. [Introduction to Pandas Series](#2-introduction-to-pandas-series)
3. [Introduction to Pandas DataFrames](#3-introduction-to-pandas-dataframes)
4. [Charger et explorer un jeu de données](#4-charger-et-explorer-un-jeu-de-données)
5. [DataFrame Selection — Sélection de base](#5-dataframe-selection--sélection-de-base)
6. [DataFrame Filtering and Selection using iloc and loc](#6-dataframe-filtering-and-selection-using-iloc-and-loc)
7. [Data Cleaning — Nettoyage des données](#7-data-cleaning--nettoyage-des-données)
8. [Data Transformation — Transformer les données](#8-data-transformation--transformer-les-données)
9. [Regroupement et agrégation (GroupBy)](#9-regroupement-et-agrégation-groupby)
10. [Fusionner des DataFrames](#10-fusionner-des-dataframes)
11. [Conclusion](#11-conclusion)
12. [Python Project — Nettoyer un jeu de données réel](#12-python-project--nettoyer-un-jeu-de-données-réel)
13. [✅ Point de contrôle — Pandas](#13--point-de-contrôle--pandas)

---

## 1. Introduction to Pandas — Vue d'ensemble

### 📖 Qu'est-ce que Pandas ?

**Pandas** est la bibliothèque Python **incontournable** pour manipuler, nettoyer et analyser des données tabulaires (lignes et colonnes) — l'équivalent d'un **Excel surpuissant piloté par du code**.

> 💡 **Analogie** : Si NumPy est une **calculatrice scientifique industrielle** (chapitre précédent), Pandas est le **tableur intelligent** construit par-dessus — il ajoute des **étiquettes** (noms de colonnes, index) et des outils de **nettoyage/analyse** aux tableaux numériques de NumPy.

### 1.1 Pandas est construit SUR NumPy

```
ÉCOSYSTÈME DATA SCIENCE PYTHON
│
NumPy          → tableaux numériques bruts, calcul rapide
   │
   ▼
Pandas         → tableaux ÉTIQUETÉS (noms de colonnes, index),
                  nettoyage, filtrage, agrégation
   │
   ▼
Matplotlib/Seaborn → visualiser les données Pandas
Scikit-learn        → entraîner des modèles à partir de DataFrames
```

### 1.2 Pourquoi Pandas est essentiel en Data Science ?

```
CE QUE PANDAS PERMET DE FAIRE
│
├── 📂 Charger des données   → CSV, Excel, JSON, SQL, HTML (rappel : chapitre File Handling)
├── 🧹 Nettoyer               → valeurs manquantes, doublons, types incorrects
├── 🔍 Filtrer / Sélectionner → cibler exactement les lignes/colonnes voulues
├── 🔄 Transformer            → créer des colonnes, appliquer des calculs
├── 📊 Agréger                → moyennes, sommes, comptages par groupe
└── 💾 Exporter               → sauvegarder les résultats nettoyés
```

> 🔑 En pratique, un Data Scientist passe **60 à 80% de son temps** à nettoyer et préparer les données avant même de commencer une analyse ou un modèle de Machine Learning. Pandas est l'outil central de ce travail.

### 1.3 Installation et import

```python
# Installation (une seule fois)
!pip install pandas

# Import — convention universelle : alias "pd"
import pandas as pd
import numpy as np   # souvent utilisé conjointement

print(pd.__version__)
```

### 1.4 Les deux structures fondamentales de Pandas

```
PANDAS
│
├── Series      → tableau 1D ÉTIQUETÉ (comme une seule colonne)
│
└── DataFrame   → tableau 2D ÉTIQUETÉ (lignes × colonnes,
                   comme une feuille Excel complète)
```

---

## 2. Introduction to Pandas Series

### 📖 Définition

Une **Series** est un tableau **unidimensionnel étiqueté** — comme une colonne unique d'un tableur, où chaque valeur possède une **étiquette (index)**.

> 💡 **Analogie** : Une Series, c'est comme une **liste de casiers postaux numérotés** — chaque casier (valeur) a un numéro ou un nom (l'index) qui permet de le retrouver directement, plutôt que de compter depuis le début à chaque fois.

### 2.1 Créer une Series

```python
import pandas as pd

# Depuis une liste — index numérique automatique (0, 1, 2...)
notes = pd.Series([14, 16, 12, 18, 15])
print(notes)
```

**Résultat :**
```
0    14
1    16
2    12
3    18
4    15
dtype: int64
```

```python
# Avec un index PERSONNALISÉ
notes_etudiants = pd.Series(
    [14, 16, 12, 18, 15],
    index=["Alice", "Bob", "Claire", "David", "Emma"]
)
print(notes_etudiants)
```

**Résultat :**
```
Alice     14
Bob       16
Claire    12
David     18
Emma      15
dtype: int64
```

```python
# Depuis un dictionnaire — les clés deviennent automatiquement l'index
ventes = pd.Series({"Lundi": 4500, "Mardi": 7800, "Mercredi": 11200})
print(ventes)
```

### 2.2 Anatomie d'une Series

```python
notes_etudiants = pd.Series([14, 16, 12], index=["Alice", "Bob", "Claire"])

print(notes_etudiants.values)   # [14 16 12]  → un tableau NumPy !
print(notes_etudiants.index)    # Index(['Alice', 'Bob', 'Claire'])
print(notes_etudiants.dtype)    # int64
print(notes_etudiants.shape)    # (3,)
print(notes_etudiants.name)     # None (peut être nommé)
```

```
VISUALISATION D'UNE SERIES
┌─────────┬────────┐
│  INDEX  │ VALEUR │
├─────────┼────────┤
│  Alice  │   14   │
│  Bob    │   16   │
│  Claire │   12   │
└─────────┴────────┘
   ↑           ↑
étiquettes   données NumPy
(comme des   (accessible via
 clés dict)   .values)
```

### 2.3 Accéder aux éléments d'une Series

```python
notes_etudiants = pd.Series([14, 16, 12, 18], index=["Alice", "Bob", "Claire", "David"])

# Par label (nom)
print(notes_etudiants["Alice"])     # 14
print(notes_etudiants.loc["Bob"])   # 16 (voir section 6 pour .loc)

# Par position (comme une liste)
print(notes_etudiants[0])            # 14
print(notes_etudiants.iloc[1])       # 16 (voir section 6 pour .iloc)

# Slicing
print(notes_etudiants[1:3])
```

### 2.4 Opérations vectorisées sur une Series (héritées de NumPy)

```python
notes = pd.Series([14, 16, 12, 18, 10])

print(notes + 2)          # ajouté à chaque élément
print(notes * 5)          # conversion sur 100
print(notes.mean())       # 14.0
print(notes.max())        # 18
print(notes[notes >= 14]) # filtrage booléen — comme avec NumPy !
```

> 🔑 Vous reconnaissez cette syntaxe ? **Une Series se comporte exactement comme un tableau NumPy**, avec en plus des étiquettes. Toutes les compétences du chapitre NumPy (indexation booléenne, opérations vectorisées, broadcasting) fonctionnent directement sur les Series.

---

## 3. Introduction to Pandas DataFrames

### 📖 Définition

Un **DataFrame** est une structure **bidimensionnelle étiquetée** — un tableau complet avec des lignes et des colonnes, où **chaque colonne est en réalité une Series**.

> 💡 **Analogie** : Si une Series est **une seule colonne** d'un tableur Excel, un DataFrame est **la feuille Excel complète** — plusieurs colonnes, chacune pouvant avoir son propre type de données (texte, nombre, date...), toutes alignées sur le même index de lignes.

### 3.1 Un DataFrame = un assemblage de Series

```
DataFrame "etudiants"
┌────────┬────────┬─────┬──────────┬───────┐
│ index  │  nom   │ age │  ville   │ note  │
├────────┼────────┼─────┼──────────┼───────┤
│   0    │ Alice  │ 23  │ Abidjan  │ 16.5  │
│   1    │ Bob    │ 25  │ Dakar    │ 14.0  │
│   2    │ Claire │ 22  │ Accra    │ 18.0  │
└────────┴────────┴─────┴──────────┴───────┘
            ↑        ↑       ↑         ↑
         Series    Series  Series    Series
         "nom"     "age"   "ville"   "note"

→ Un DataFrame est un DICTIONNAIRE de Series, alignées sur le même index
```

### 3.2 Créer un DataFrame

```python
import pandas as pd

# Depuis un dictionnaire de listes (méthode la plus courante)
donnees = {
    "nom"   : ["Alice", "Bob", "Claire", "David"],
    "age"   : [23, 25, 22, 28],
    "ville" : ["Abidjan", "Dakar", "Accra", "Lagos"],
    "note"  : [16.5, 14.0, 18.0, 12.5]
}

df = pd.DataFrame(donnees)
print(df)
```

**Résultat :**
```
      nom  age    ville  note
0   Alice   23  Abidjan  16.5
1     Bob   25    Dakar  14.0
2  Claire   22    Accra  18.0
3   David   28    Lagos  12.5
```

```python
# Depuis une LISTE DE DICTIONNAIRES (une ligne = un dictionnaire)
donnees_lignes = [
    {"nom": "Alice", "age": 23, "note": 16.5},
    {"nom": "Bob",   "age": 25, "note": 14.0},
    {"nom": "Claire","age": 22, "note": 18.0},
]
df2 = pd.DataFrame(donnees_lignes)
print(df2)
```

```python
# Depuis un tableau NumPy (avec noms de colonnes explicites)
import numpy as np
tableau = np.array([[4, 8, 12], [6, 10, 15], [5, 7, 9]])
df3 = pd.DataFrame(tableau, columns=["Produit_A", "Produit_B", "Produit_C"])
print(df3)
```

> 💡 Vous reconnaissez ce tableau ? C'est exactement la **matrice D du checkpoint Maths** — maintenant avec des **noms de colonnes lisibles** grâce à Pandas !

### 3.3 Anatomie d'un DataFrame

```python
df = pd.DataFrame({
    "nom"  : ["Alice", "Bob", "Claire"],
    "age"  : [23, 25, 22],
    "note" : [16.5, 14.0, 18.0]
})

print(df.shape)      # (3, 3) → 3 lignes, 3 colonnes
print(df.columns)    # Index(['nom', 'age', 'note'])
print(df.index)      # RangeIndex(start=0, stop=3, step=1)
print(df.dtypes)     # le type de CHAQUE colonne
print(df.values)     # les données brutes en tableau NumPy 2D
```

**`df.dtypes` — un point essentiel :**
```
nom       object     ← texte (chaînes de caractères)
age        int64     ← entiers
note      float64    ← décimaux
dtype: object
```

> 🔑 Contrairement à un tableau NumPy (un seul type pour tout le tableau), **chaque colonne d'un DataFrame peut avoir son propre type** — c'est ce qui rend Pandas si adapté aux données réelles (mélange de texte, nombres, dates...).

---

## 4. Charger et explorer un jeu de données

### 4.1 Lire des fichiers — Rappel du chapitre File Handling

Pandas **automatise** presque tout ce que vous avez appris à faire manuellement avec `open()` et le module `csv` !

```python
# Lire un CSV (le plus courant)
df = pd.read_csv("etudiants.csv")

# Lire un fichier Excel
df_excel = pd.read_excel("donnees.xlsx", sheet_name="Feuille1")

# Lire un fichier JSON
df_json = pd.read_json("donnees.json")

# Lire directement un tableau HTML (rappel du chapitre Web Scraping !)
tableaux = pd.read_html("https://www.example.com/tableau")
```

```
CE QUE PANDAS REMPLACE (du chapitre File Handling)
│
open() + csv.DictReader + boucle manuelle + conversion de types
                        │
                        ▼
              pd.read_csv("fichier.csv")   ← UNE seule ligne !
```

### 4.2 Options utiles de `read_csv()`

```python
df = pd.read_csv(
    "etudiants.csv",
    sep=",",              # délimiteur (par défaut virgule)
    encoding="utf-8",      # encodage (gère les accents)
    index_col=0,           # utiliser la première colonne comme index
    na_values=["N/A", ""], # valeurs à considérer comme manquantes
    dtype={"age": int}     # forcer le type d'une colonne
)
```

### 4.3 Explorer un DataFrame — Les premiers réflexes

```python
df = pd.DataFrame({
    "nom"   : ["Alice", "Bob", "Claire", "David", "Emma"],
    "age"   : [23, 25, 22, 28, 24],
    "ville" : ["Abidjan", "Dakar", "Accra", "Lagos", "Abidjan"],
    "note"  : [16.5, 14.0, 18.0, 12.5, 17.0]
})

df.head()        # les 5 PREMIÈRES lignes (par défaut)
df.head(2)        # les 2 premières lignes

df.tail(3)         # les 3 DERNIÈRES lignes

df.info()          # résumé : colonnes, types, valeurs non nulles, mémoire

df.describe()       # statistiques descriptives (moyenne, min, max, quartiles...)

df.shape             # (5, 4) → dimensions

df.columns            # liste des noms de colonnes

df.nunique()           # nombre de valeurs uniques par colonne
```

**`df.describe()` — très utile pour un premier diagnostic :**
```
             age       note
count   5.000000   5.000000
mean   24.400000  15.600000
std     2.302173   2.257761
min    22.000000  12.500000
25%    23.000000  14.000000
50%    24.000000  16.500000
75%    25.000000  17.000000
max    28.000000  18.000000
```

> 🔑 **Réflexe professionnel** : après tout chargement de données, exécutez systématiquement `df.head()`, `df.info()` et `df.describe()` — c'est le **diagnostic de base** avant toute analyse.

---

## 5. DataFrame Selection — Sélection de base

### 5.1 Sélectionner une colonne

```python
df = pd.DataFrame({
    "nom"   : ["Alice", "Bob", "Claire"],
    "age"   : [23, 25, 22],
    "note"  : [16.5, 14.0, 18.0]
})

# Une seule colonne → retourne une Series
print(df["nom"])
print(type(df["nom"]))   # <class 'pandas.core.series.Series'>

# Notation alternative (fonctionne SEULEMENT si le nom n'a pas d'espace)
print(df.nom)
```

### 5.2 Sélectionner plusieurs colonnes

```python
# Plusieurs colonnes → utiliser une LISTE de noms → retourne un DataFrame
sous_df = df[["nom", "note"]]
print(sous_df)
print(type(sous_df))    # <class 'pandas.core.frame.DataFrame'>
```

> ⚠️ **Piège fréquent** : `df["nom"]` (une chaîne) retourne une **Series**. `df[["nom"]]` (une liste avec un seul élément) retourne un **DataFrame** à une seule colonne. Ce n'est pas la même chose !

```python
print(type(df["nom"]))     # Series
print(type(df[["nom"]]))   # DataFrame
```

### 5.3 Sélectionner des lignes par slicing

```python
# Slicing de lignes (comme une liste Python)
print(df[0:2])     # les 2 premières lignes (lignes 0 et 1)
```

### 5.4 Créer une nouvelle colonne

```python
df["moyenne_pondere"] = df["note"] * 1.0   # nouvelle colonne à partir d'une existante
df["est_majeur"] = df["age"] >= 18          # colonne booléenne calculée
print(df)
```

---

## 6. DataFrame Filtering and Selection using iloc and loc

### 📖 Pourquoi deux méthodes différentes ?

C'est **LA notion la plus importante** de ce chapitre : Pandas propose deux façons distinctes de sélectionner des lignes/colonnes, selon que vous raisonnez en **positions** (comme une liste) ou en **étiquettes** (labels).

```
.loc[]                              .iloc[]
─────────────────────               ─────────────────────
Sélection par LABEL (étiquette)     Sélection par POSITION (index numérique)
"loc" = "location" (par nom)        "iloc" = "integer location"

df.loc["Alice"]                     df.iloc[0]
→ la ligne dont l'INDEX = "Alice"   → la ligne à la POSITION 0
```

> 💡 **Analogie** : Imaginez une étagère de livres.
> - **`.loc`** cherche un livre par son **titre inscrit sur la tranche** ("Donne-moi le livre intitulé *Python*").
> - **`.iloc`** cherche un livre par sa **position physique** sur l'étagère ("Donne-moi le 3ème livre en partant de la gauche").

### 6.1 `.loc[]` — Sélection par label

```python
df = pd.DataFrame({
    "age"   : [23, 25, 22, 28],
    "ville" : ["Abidjan", "Dakar", "Accra", "Lagos"],
    "note"  : [16.5, 14.0, 18.0, 12.5]
}, index=["Alice", "Bob", "Claire", "David"])

# Une ligne par son label
print(df.loc["Alice"])

# Plusieurs lignes
print(df.loc[["Alice", "Claire"]])

# Ligne(s) + colonne(s) précises
print(df.loc["Alice", "note"])              # 16.5
print(df.loc[["Alice", "Bob"], ["age", "note"]])

# Toutes les lignes, colonnes précises
print(df.loc[:, ["nom", "note"]] if "nom" in df.columns else df.loc[:, ["age", "note"]])

# Slicing avec .loc — ⚠️ la borne de FIN est INCLUSE (contrairement à Python classique !)
print(df.loc["Alice":"Claire"])   # Alice, Bob, ET Claire incluses
```

### 6.2 `.iloc[]` — Sélection par position

```python
# Reprenons le même DataFrame (index = noms des étudiants)

# Une ligne par sa position
print(df.iloc[0])          # première ligne (Alice), quel que soit son label

# Plusieurs lignes par position
print(df.iloc[[0, 2]])      # 1ère et 3ème lignes

# Ligne(s) + colonne(s) par position
print(df.iloc[0, 1])         # ligne 0, colonne 1 → "Abidjan"
print(df.iloc[0:2, 0:2])      # 2 premières lignes, 2 premières colonnes

# Slicing avec .iloc — la borne de FIN est EXCLUE (comme les listes Python classiques)
print(df.iloc[0:2])            # lignes 0 et 1 SEULEMENT (pas la ligne 2)
```

### 6.3 Tableau comparatif `.loc` vs `.iloc`

| | `.loc[]` | `.iloc[]` |
|-|----------|-----------|
| Type de sélection | Par **label** (étiquette) | Par **position** (entier) |
| Borne de fin en slicing | **Incluse** | **Exclue** |
| Exemple ligne | `df.loc["Alice"]` | `df.iloc[0]` |
| Exemple slicing | `df.loc["Alice":"Claire"]` | `df.iloc[0:3]` |
| Fonctionne avec des booléens | ✅ Oui | ❌ Non directement |

### 6.4 Filtrage avec des conditions booléennes (le plus utilisé au quotidien !)

```python
df = pd.DataFrame({
    "nom"   : ["Alice", "Bob", "Claire", "David", "Emma"],
    "age"   : [23, 25, 22, 28, 24],
    "ville" : ["Abidjan", "Dakar", "Accra", "Lagos", "Abidjan"],
    "note"  : [16.5, 14.0, 18.0, 12.5, 17.0]
})

# Filtrer les étudiants avec note >= 15
bons_etudiants = df[df["note"] >= 15]
print(bons_etudiants)

# Équivalent explicite avec .loc (plus lisible pour les débutants)
bons_etudiants2 = df.loc[df["note"] >= 15]

# Combiner plusieurs conditions : & (et), | (ou) — TOUJOURS entre parenthèses !
resultat = df[(df["note"] >= 15) & (df["ville"] == "Abidjan")]
print(resultat)

# Sélectionner des colonnes précises EN MÊME TEMPS que le filtre (avec .loc)
resultat2 = df.loc[df["note"] >= 15, ["nom", "note"]]
print(resultat2)
```

### 6.5 `.at[]` et `.iat[]` — Accès rapide à UNE seule valeur

```python
# Pour accéder à UNE SEULE valeur précise, .at/.iat sont plus rapides que .loc/.iloc
print(df.at[0, "nom"])     # équivalent à df.loc[0, "nom"], mais plus rapide
print(df.iat[0, 0])         # équivalent à df.iloc[0, 0]
```

---

## 7. Data Cleaning — Nettoyage des données

### 📖 Pourquoi nettoyer les données ?

Les données réelles (scrapées du web, exportées de bases de données, saisies manuellement) sont **rarement propres** : valeurs manquantes, doublons, types incorrects, espaces superflus... Le nettoyage est **l'étape la plus longue** — mais aussi la plus **critique** — de tout projet Data Science.

> 🔑 **"Garbage in, garbage out"** : un modèle entraîné sur des données sales produira des résultats peu fiables, peu importe sa sophistication.

### 7.1 Détecter les valeurs manquantes

```python
df = pd.DataFrame({
    "nom"  : ["Alice", "Bob", None, "David"],
    "age"  : [23, None, 22, 28],
    "note" : [16.5, 14.0, 18.0, None]
})

print(df.isna())          # tableau de True/False (True = valeur manquante)
print(df.isna().sum())    # nombre de valeurs manquantes PAR COLONNE

# Pourcentage de valeurs manquantes
print((df.isna().sum() / len(df)) * 100)
```

**Résultat de `.isna().sum()` :**
```
nom     1
age     1
note    1
dtype: int64
```

### 7.2 Supprimer les valeurs manquantes

```python
# Supprimer les LIGNES contenant au moins une valeur manquante
df_sans_na = df.dropna()

# Supprimer seulement si TOUTE la ligne est vide
df_sans_na2 = df.dropna(how="all")

# Supprimer les lignes où une colonne PRÉCISE est manquante
df_sans_na3 = df.dropna(subset=["note"])

# Supprimer les COLONNES contenant des valeurs manquantes
df_sans_colonnes_na = df.dropna(axis=1)
```

### 7.3 Remplacer les valeurs manquantes

```python
# Remplacer par une valeur fixe
df["note"] = df["note"].fillna(0)

# Remplacer par la MOYENNE de la colonne (technique courante)
df["age"] = df["age"].fillna(df["age"].mean())

# Remplacer par la valeur précédente/suivante (utile pour des séries temporelles)
df["note"] = df["note"].fillna(method="ffill")   # forward fill
df["note"] = df["note"].fillna(method="bfill")   # backward fill
```

| Stratégie | Quand l'utiliser |
|-----------|-------------------|
| `dropna()` | Peu de valeurs manquantes, perte de données acceptable |
| `fillna(valeur_fixe)` | Une valeur par défaut a du sens (ex : 0 pour un stock) |
| `fillna(moyenne)` | Variable numérique continue, distribution raisonnable |
| `fillna(method="ffill")` | Données ordonnées dans le temps (séries temporelles) |

### 7.4 Détecter et supprimer les doublons

```python
df = pd.DataFrame({
    "nom" : ["Alice", "Bob", "Alice", "Claire"],
    "age" : [23, 25, 23, 22]
})

print(df.duplicated())          # True là où la ligne est un doublon EXACT
print(df.duplicated().sum())     # nombre total de doublons

df_sans_doublons = df.drop_duplicates()
print(df_sans_doublons)

# Doublons basés sur UNE colonne seulement
df_sans_doublons_nom = df.drop_duplicates(subset=["nom"])
```

### 7.5 Corriger les types de données

```python
df = pd.DataFrame({
    "age"  : ["23", "25", "22"],        # texte au lieu de nombre !
    "date" : ["2024-01-15", "2024-02-20", "2024-03-10"]
})

print(df.dtypes)   # age: object (texte), date: object

# Convertir en numérique
df["age"] = pd.to_numeric(df["age"])
# ou : df["age"] = df["age"].astype(int)

# Convertir en date
df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)   # age: int64, date: datetime64
```

```python
# Gérer les erreurs de conversion (valeurs non convertibles)
donnees_sales = pd.Series(["12", "15", "erreur", "20"])
donnees_propres = pd.to_numeric(donnees_sales, errors="coerce")
print(donnees_propres)   # 'erreur' devient NaN au lieu de planter le programme
```

### 7.6 Nettoyer du texte avec `.str`

```python
df = pd.DataFrame({
    "nom" : ["  alice  ", "BOB", "Claire ", " david"]
})

df["nom_propre"] = df["nom"].str.strip()       # supprimer les espaces
df["nom_propre"] = df["nom_propre"].str.title() # Première lettre en majuscule

print(df)
```

| Méthode `.str` | Description |
|------------------|--------------|
| `.str.strip()` | Supprime les espaces en début/fin |
| `.str.lower()` / `.str.upper()` | Minuscules / majuscules |
| `.str.title()` | Première lettre de chaque mot en majuscule |
| `.str.replace(a, b)` | Remplacer du texte |
| `.str.contains(texte)` | Vérifier si une sous-chaîne est présente |
| `.str.split(sep)` | Découper une chaîne |
| `.str.len()` | Longueur de chaque chaîne |

### 7.7 Renommer des colonnes

```python
df = df.rename(columns={"nom": "nom_complet", "age": "age_annees"})

# Ou remplacer TOUS les noms de colonnes d'un coup
df.columns = ["nouvelle_col1", "nouvelle_col2"]
```

---

## 8. Data Transformation — Transformer les données

### 8.1 Créer des colonnes calculées

```python
df = pd.DataFrame({
    "nom"        : ["Alice", "Bob", "Claire"],
    "note_sql"   : [16, 14, 18],
    "note_python": [18, 15, 17]
})

# Nouvelle colonne = calcul entre colonnes existantes
df["moyenne"] = (df["note_sql"] + df["note_python"]) / 2
print(df)
```

### 8.2 `.apply()` — Appliquer une fonction personnalisée

```python
def attribuer_mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"

df["mention"] = df["moyenne"].apply(attribuer_mention)
print(df)

# Avec une fonction lambda (rappel du chapitre Fonctions !)
df["moyenne_arrondie"] = df["moyenne"].apply(lambda x: round(x))
```

### 8.3 `.map()` — Remplacer des valeurs via un dictionnaire

```python
statuts = {"Abidjan": "CI", "Dakar": "SN", "Accra": "GH"}

df_villes = pd.DataFrame({"ville": ["Abidjan", "Dakar", "Accra"]})
df_villes["code_pays"] = df_villes["ville"].map(statuts)
print(df_villes)
```

### 8.4 Trier les données

```python
# Trier par une colonne (croissant par défaut)
df_trie = df.sort_values("moyenne")

# Trier décroissant
df_trie_desc = df.sort_values("moyenne", ascending=False)

# Trier par plusieurs colonnes
df_trie_multi = df.sort_values(["ville", "moyenne"], ascending=[True, False])

# Trier par l'index
df_trie_index = df.sort_index()
```

### 8.5 `pd.cut()` — Regrouper des valeurs en catégories (binning)

```python
notes = pd.DataFrame({"note": [8, 12, 15, 18, 20, 6, 14]})

notes["categorie"] = pd.cut(
    notes["note"],
    bins=[0, 10, 14, 16, 20],
    labels=["Insuffisant", "Passable", "Bien", "Très bien"]
)
print(notes)
```

### 8.6 Remplacer des valeurs précises

```python
df["ville"] = df["ville"].replace({"Abidjan": "Abidjan, CI", "Dakar": "Dakar, SN"})
```

---

## 9. Regroupement et agrégation (GroupBy)

### 📖 Le concept `groupby` — Regrouper puis résumer

`groupby()` reproduit la logique du `GROUP BY` que vous avez déjà appris en **SQL** ! C'est l'outil le plus puissant de Pandas pour résumer des données par catégorie.

```
SPLIT-APPLY-COMBINE (le principe du groupby)
│
1. SPLIT   → diviser les données en groupes (ex: par ville)
2. APPLY   → appliquer une fonction à chaque groupe (ex: moyenne)
3. COMBINE → recombiner les résultats en un nouveau tableau
```

```python
df = pd.DataFrame({
    "ville" : ["Abidjan", "Dakar", "Abidjan", "Accra", "Dakar"],
    "note"  : [16, 14, 18, 12, 15]
})

# Moyenne des notes PAR ville
moyenne_par_ville = df.groupby("ville")["note"].mean()
print(moyenne_par_ville)
```

**Résultat :**
```
ville
Abidjan    17.0
Accra      12.0
Dakar      14.5
Name: note, dtype: float64
```

```python
# Plusieurs agrégations à la fois
resume = df.groupby("ville")["note"].agg(["mean", "min", "max", "count"])
print(resume)

# Regrouper par plusieurs colonnes
df2 = pd.DataFrame({
    "ville": ["Abidjan", "Abidjan", "Dakar", "Dakar"],
    "cours": ["SQL", "Python", "SQL", "Python"],
    "note" : [16, 18, 14, 15]
})
resume2 = df2.groupby(["ville", "cours"])["note"].mean()
print(resume2)
```

### 9.1 `value_counts()` — Compter les occurrences

```python
villes = pd.Series(["Abidjan", "Dakar", "Abidjan", "Accra", "Abidjan"])
print(villes.value_counts())
```

**Résultat :**
```
Abidjan    3
Dakar      1
Accra      1
Name: count, dtype: int64
```

---

## 10. Fusionner des DataFrames

### 📖 `pd.concat()` — Empiler des DataFrames

```python
df_promo1 = pd.DataFrame({"nom": ["Alice", "Bob"], "note": [16, 14]})
df_promo2 = pd.DataFrame({"nom": ["Claire", "David"], "note": [18, 12]})

# Empiler verticalement (ajouter des lignes)
df_toutes_promos = pd.concat([df_promo1, df_promo2], ignore_index=True)
print(df_toutes_promos)
```

### 10.1 `pd.merge()` — Fusionner comme une jointure SQL

```python
etudiants = pd.DataFrame({
    "id_etudiant": [1, 2, 3],
    "nom": ["Alice", "Bob", "Claire"]
})

notes = pd.DataFrame({
    "id_etudiant": [1, 2, 3],
    "note": [16, 14, 18]
})

# Équivalent d'un INNER JOIN en SQL !
fusion = pd.merge(etudiants, notes, on="id_etudiant")
print(fusion)
```

> 💡 Vous reconnaissez ce concept ? C'est **exactement** le `JOIN` du chapitre DQL en SQL — Pandas utilise le même principe pour combiner des tableaux liés par une clé commune.

```python
# Types de jointures (comme en SQL)
pd.merge(etudiants, notes, on="id_etudiant", how="inner")   # intersection
pd.merge(etudiants, notes, on="id_etudiant", how="left")    # tout etudiants
pd.merge(etudiants, notes, on="id_etudiant", how="right")   # tout notes
pd.merge(etudiants, notes, on="id_etudiant", how="outer")   # tout des deux
```

---

## 11. Conclusion

### 📌 Récapitulatif du chapitre

```
PANDAS — DATA CLEANING & TRANSFORMATION
│
├── Structures de base
│   ├── Series      → tableau 1D étiqueté (une colonne)
│   └── DataFrame   → tableau 2D étiqueté (lignes × colonnes)
│
├── Charger et explorer
│   ├── pd.read_csv() / read_excel() / read_json() / read_html()
│   └── .head() / .info() / .describe() / .shape
│
├── Sélection
│   ├── df["col"] / df[["col1","col2"]]
│   ├── .loc[]   → par LABEL (borne fin incluse)
│   └── .iloc[]  → par POSITION (borne fin exclue)
│
├── Nettoyage (Data Cleaning)
│   ├── isna() / dropna() / fillna()          → valeurs manquantes
│   ├── duplicated() / drop_duplicates()       → doublons
│   ├── astype() / to_numeric() / to_datetime()→ types
│   └── .str.strip()/.lower()/.replace()       → texte
│
├── Transformation
│   ├── Nouvelles colonnes calculées
│   ├── .apply() / .map()
│   ├── sort_values()
│   └── pd.cut()  → catégorisation
│
├── Agrégation
│   └── groupby() → SPLIT → APPLY → COMBINE (comme SQL GROUP BY)
│
└── Fusion
    ├── pd.concat()  → empiler
    └── pd.merge()   → jointure (comme SQL JOIN)
```

### 🔑 Points clés à retenir

1. **Series** = 1 colonne étiquetée ; **DataFrame** = plusieurs Series alignées sur le même index.
2. **`.loc`** sélectionne par label (borne incluse) ; **`.iloc`** sélectionne par position (borne exclue).
3. Le nettoyage (`isna()`, `dropna()`, `fillna()`, `drop_duplicates()`) est **l'étape la plus critique** avant toute analyse.
4. **`.apply()`** applique une fonction personnalisée ; **`.map()`** remplace des valeurs via un dictionnaire.
5. **`groupby()`** reproduit exactement la logique du `GROUP BY` SQL : diviser → agréger → recombiner.
6. **`pd.merge()`** reproduit les `JOIN` SQL pour combiner des tableaux liés par une clé commune.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons la **visualisation de données** avec **Matplotlib** et **Seaborn** — transformer vos DataFrames nettoyés en graphiques clairs et percutants (histogrammes, nuages de points, boîtes à moustaches...), l'étape qui précède directement le Machine Learning.

---

## 12. Python Project — Nettoyer un jeu de données réel

### 🎯 Objectif du projet

Reprendre le fichier `inscriptions.csv` du chapitre **File Handling**, mais cette fois **volontairement rendu "sale"** (valeurs manquantes, doublons, espaces, types incorrects) — comme un vrai jeu de données du monde réel — et le nettoyer entièrement avec Pandas.

```python
import pandas as pd
import numpy as np

# ============================================
# ÉTAPE 1 : Créer un jeu de données "sale" (simulation réaliste)
# ============================================
donnees_sales = {
    "nom"         : ["  Fatou Diallo", "Kofi Asante", "Awa Traore", "Kofi Asante", "  Aminata Sow  ", None],
    "age"         : ["23", "25", "22", "25", "24", "26"],
    "ville"       : ["Abidjan", "accra", "Dakar", "accra", "ABIDJAN", "Bamako"],
    "note_sql"    : [16, 14, 18, 14, None, 15],
    "note_python" : [18, 15, 17, 15, 19, None],
}

df_brut = pd.DataFrame(donnees_sales)
print("=== DONNÉES BRUTES (sales) ===")
print(df_brut)
print(f"\nDimensions : {df_brut.shape}")


# ============================================
# ÉTAPE 2 : Diagnostic
# ============================================
print("\n=== DIAGNOSTIC ===")
print("Valeurs manquantes par colonne :")
print(df_brut.isna().sum())
print(f"\nDoublons détectés : {df_brut.duplicated(subset=['nom']).sum()}")
print(f"\nTypes de données :\n{df_brut.dtypes}")


# ============================================
# ÉTAPE 3 : Nettoyage
# ============================================
df_propre = df_brut.copy()

# 3.1 Nettoyer les espaces et supprimer les lignes sans nom
df_propre["nom"] = df_propre["nom"].str.strip()
df_propre = df_propre.dropna(subset=["nom"])

# 3.2 Uniformiser la casse des villes
df_propre["ville"] = df_propre["ville"].str.title()

# 3.3 Convertir l'âge en entier
df_propre["age"] = df_propre["age"].astype(int)

# 3.4 Remplacer les notes manquantes par la moyenne de leur colonne
df_propre["note_sql"] = df_propre["note_sql"].fillna(df_propre["note_sql"].mean())
df_propre["note_python"] = df_propre["note_python"].fillna(df_propre["note_python"].mean())

# 3.5 Supprimer les doublons (garder la première occurrence)
df_propre = df_propre.drop_duplicates(subset=["nom"], keep="first")

# 3.6 Réinitialiser l'index après suppression de lignes
df_propre = df_propre.reset_index(drop=True)

print("\n=== DONNÉES NETTOYÉES ===")
print(df_propre)


# ============================================
# ÉTAPE 4 : Transformation
# ============================================
df_propre["moyenne"] = ((df_propre["note_sql"] + df_propre["note_python"]) / 2).round(2)

def attribuer_mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 10:
        return "Passable"
    return "Insuffisant"

df_propre["mention"] = df_propre["moyenne"].apply(attribuer_mention)

print("\n=== DONNÉES TRANSFORMÉES ===")
print(df_propre)


# ============================================
# ÉTAPE 5 : Analyse par groupe
# ============================================
print("\n=== MOYENNE PAR VILLE ===")
print(df_propre.groupby("ville")["moyenne"].mean().round(2))

print("\n=== RÉPARTITION DES MENTIONS ===")
print(df_propre["mention"].value_counts())


# ============================================
# ÉTAPE 6 : Sauvegarder le résultat nettoyé
# ============================================
df_propre.to_csv("inscriptions_nettoyees.csv", index=False, encoding="utf-8")
print("\n✅ Données nettoyées sauvegardées dans inscriptions_nettoyees.csv")
```

> 💡 **Ce projet illustre le cycle complet de nettoyage** que vous rencontrerez sur **chaque nouveau jeu de données** de votre carrière : diagnostiquer → nettoyer → transformer → analyser → sauvegarder.

---

## 13. ✅ Point de contrôle — Pandas

### 📝 Questions théoriques

**Q1.** Quelle est la différence fondamentale entre une Series et un DataFrame ?

<details>
<summary>👀 Voir la réponse</summary>

> Une **Series** est un tableau **unidimensionnel étiqueté** (une seule colonne avec un index). Un **DataFrame** est une structure **bidimensionnelle** (lignes × colonnes), où **chaque colonne est en réalité une Series** — toutes alignées sur le même index.
</details>

---

**Q2.** Quelle est la différence entre `.loc[]` et `.iloc[]`, notamment concernant le slicing ?

<details>
<summary>👀 Voir la réponse</summary>

> `.loc[]` sélectionne par **label** (étiquette/nom de l'index ou de la colonne) ; en slicing, la **borne de fin est incluse**. `.iloc[]` sélectionne par **position entière** (comme une liste Python) ; en slicing, la **borne de fin est exclue**, comme pour les listes Python classiques.
</details>

---

**Q3.** Quelle est la différence entre `df["nom"]` et `df[["nom"]]` ?

<details>
<summary>👀 Voir la réponse</summary>

> `df["nom"]` (une chaîne de caractères) retourne une **Series**. `df[["nom"]]` (une liste contenant un seul élément) retourne un **DataFrame** à une seule colonne. Le type de retour dépend de si l'on passe une chaîne ou une liste.
</details>

---

**Q4.** Citez trois stratégies pour gérer les valeurs manquantes dans un DataFrame, et quand les utiliser.

<details>
<summary>👀 Voir la réponse</summary>

> `dropna()` supprime les lignes/colonnes concernées — utile quand peu de données sont manquantes et que leur perte est acceptable. `fillna(valeur)` remplace par une valeur fixe — utile quand une valeur par défaut a du sens métier. `fillna(df["col"].mean())` remplace par la moyenne — utile pour des variables numériques continues sans valeur par défaut évidente.
</details>

---

**Q5.** En quoi `groupby()` en Pandas ressemble-t-il à `GROUP BY` en SQL ?

<details>
<summary>👀 Voir la réponse</summary>

> Les deux suivent la même logique **"diviser puis résumer"** : regrouper les lignes selon une ou plusieurs colonnes (comme les catégories d'un `GROUP BY`), puis appliquer une fonction d'agrégation (moyenne, somme, comptage) à chaque groupe pour produire un résultat résumé.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Créer et explorer**

Créez un DataFrame avec les colonnes `produit`, `prix`, `stock` pour 5 produits de votre choix. Affichez `.head()`, `.info()` et `.describe()`.

<details>
<summary>👀 Voir la solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "produit": ["Ordinateur", "Souris", "Clavier", "Écran", "Casque"],
    "prix"   : [850000, 15000, 25000, 180000, 45000],
    "stock"  : [10, 50, 30, 8, 20]
})

print(df.head())
print(df.info())
print(df.describe())
```
</details>

---

**Exercice 2 — loc et iloc**

Avec le DataFrame de l'exercice 1, utilisez `.loc` pour afficher le prix du produit à l'index 2, puis `.iloc` pour afficher les 3 premières lignes et les 2 premières colonnes.

<details>
<summary>👀 Voir la solution</summary>

```python
print(df.loc[2, "prix"])
print(df.iloc[0:3, 0:2])
```
</details>

---

**Exercice 3 — Filtrage**

Filtrez les produits dont le stock est inférieur à 15 ET le prix supérieur à 20000.

<details>
<summary>👀 Voir la solution</summary>

```python
resultat = df[(df["stock"] < 15) & (df["prix"] > 20000)]
print(resultat)
```
</details>

---

**Exercice 4 — Nettoyage**

Avec `df = pd.DataFrame({"nom": ["  Alice", "BOB ", None, "claire"], "note": [16, None, 14, 18]})`, nettoyez les espaces et la casse des noms, supprimez les lignes sans nom, et remplacez les notes manquantes par la moyenne.

<details>
<summary>👀 Voir la solution</summary>

```python
df = pd.DataFrame({
    "nom": ["  Alice", "BOB ", None, "claire"],
    "note": [16, None, 14, 18]
})

df["nom"] = df["nom"].str.strip().str.title()
df = df.dropna(subset=["nom"])
df["note"] = df["note"].fillna(df["note"].mean())
print(df)
```
</details>

---

**Exercice 5 — Transformation et groupby**

Avec le DataFrame des étudiants (nom, ville, note), créez une colonne `mention` (Très bien ≥16, Bien ≥14, sinon Passable), puis affichez la moyenne des notes par ville.

<details>
<summary>👀 Voir la solution</summary>

```python
df = pd.DataFrame({
    "nom": ["Alice", "Bob", "Claire", "David"],
    "ville": ["Abidjan", "Dakar", "Abidjan", "Dakar"],
    "note": [16, 12, 18, 15]
})

df["mention"] = df["note"].apply(
    lambda n: "Très bien" if n >= 16 else ("Bien" if n >= 14 else "Passable")
)
print(df)

print(df.groupby("ville")["note"].mean())
```
</details>

---

**Exercice 6 — Merge**

Fusionnez ces deux DataFrames sur `id` :
```python
etudiants = pd.DataFrame({"id": [1, 2, 3], "nom": ["Alice", "Bob", "Claire"]})
villes    = pd.DataFrame({"id": [1, 2, 3], "ville": ["Abidjan", "Dakar", "Accra"]})
```

<details>
<summary>👀 Voir la solution</summary>

```python
etudiants = pd.DataFrame({"id": [1, 2, 3], "nom": ["Alice", "Bob", "Claire"]})
villes    = pd.DataFrame({"id": [1, 2, 3], "ville": ["Abidjan", "Dakar", "Accra"]})

fusion = pd.merge(etudiants, villes, on="id")
print(fusion)
```
</details>

---

### 🏆 Challenge bonus — Pipeline complet BRVM

En reprenant les données scrapées de la **BRVM** (chapitre Web Scraping) — ou en simulant un petit tableau `symbole, cours_cloture, variation` :

1. Chargez les données dans un DataFrame
2. Nettoyez la colonne `variation` (supprimer le `%`, convertir en nombre)
3. Filtrez les titres avec une variation positive
4. Triez par variation décroissante
5. Calculez la variation moyenne du marché
6. Créez une colonne `tendance` ("Hausse" / "Baisse" / "Stable") avec `.apply()`
7. Sauvegardez le résultat nettoyé en CSV

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd

donnees_brvm = pd.DataFrame({
    "symbole": ["SICC", "SAFC", "BOAC", "STBC", "LNBB"],
    "cours_cloture": [8730, 5090, 12295, 23000, 4015],
    "variation": ["7,45%", "5,82%", "3,28%", "-7,26%", "-5,42%"]
})

# 2. Nettoyer la variation
donnees_brvm["variation_num"] = (
    donnees_brvm["variation"]
    .str.replace("%", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# 3. Filtrer les hausses
hausses = donnees_brvm[donnees_brvm["variation_num"] > 0]
print("Titres en hausse :\n", hausses)

# 4. Trier par variation décroissante
donnees_triees = donnees_brvm.sort_values("variation_num", ascending=False)
print("\nTrié par variation :\n", donnees_triees)

# 5. Variation moyenne du marché
print(f"\nVariation moyenne : {donnees_brvm['variation_num'].mean():.2f}%")

# 6. Colonne tendance
def tendance(v):
    if v > 0.5:
        return "Hausse"
    elif v < -0.5:
        return "Baisse"
    return "Stable"

donnees_brvm["tendance"] = donnees_brvm["variation_num"].apply(tendance)
print("\n", donnees_brvm)

# 7. Sauvegarder
donnees_brvm.to_csv("brvm_nettoye.csv", index=False, encoding="utf-8")
print("\n✅ Sauvegardé dans brvm_nettoye.csv")
```
</details>

---

*📘 Module Data Science — Data Cleaning and Transformation with Pandas | Bootcamp Data Science*
