# 📁 File Handling — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : Module Python Pur (Chapitres 1 à 5) + NumPy + Web Scraping

---

## Table des matières

1. [Introduction to Files](#1-introduction-to-files)
2. [Understanding Files, Objects, Reading, and Parsing](#2-understanding-files-objects-reading-and-parsing)
3. [Understanding Data Types](#3-understanding-data-types)
4. [Distinguishing Text Files from Flat Files](#4-distinguishing-text-files-from-flat-files)
5. [I/O Operations with NumPy](#5-io-operations-with-numpy)
6. [Conclusion](#6-conclusion)
7. [Python Project — Gestionnaire de notes du Bootcamp](#7-python-project--gestionnaire-de-notes-du-bootcamp)
8. [✅ Point de contrôle — File Handling](#8--point-de-contrôle--file-handling)

---

## 1. Introduction to Files

### 📖 Pourquoi manipuler des fichiers ?

Jusqu'ici, toutes les données de vos programmes (variables, listes, DataFrames scrapés) **disparaissent** dès que le programme s'arrête ou que vous fermez le notebook. Pour **conserver des données de façon permanente**, les partager, ou les faire persister d'une session à l'autre, il faut les écrire dans des **fichiers** sur le disque.

> 💡 **Analogie** : Une variable Python, c'est comme écrire sur un **tableau blanc** — dès que vous quittez la salle (fin du programme), tout est effacé. Un fichier, c'est comme écrire dans un **cahier** — il reste là, sur l'étagère (le disque dur), prêt à être relu des mois plus tard, même après avoir éteint l'ordinateur.

### 1.1 RAM vs Disque — Le concept clé

```
MÉMOIRE VIVE (RAM)                        DISQUE (Stockage permanent)
─────────────────────                     ─────────────────────────────
Variables, listes, DataFrames             Fichiers .txt, .csv, .json, .npy
    │                                          │
    ▼                                          ▼
⚡ Très rapide                              🐢 Plus lent (mais permanent)
❌ Volatile (effacée à la fermeture)        ✅ Persiste après fermeture
    du programme                                du programme
```

> 🔑 **En Data Science, le cycle est presque toujours** : lire des données depuis un fichier (ou le web, comme au chapitre précédent) → les charger en mémoire (RAM) pour les analyser → écrire les résultats dans un nouveau fichier pour les conserver.

### 1.2 Chemins d'accès (Paths)

Pour manipuler un fichier, il faut d'abord savoir **où il se trouve** — son **chemin d'accès**.

```python
# Chemin RELATIF — par rapport au dossier où s'exécute le programme
chemin_relatif = "donnees/etudiants.csv"

# Chemin ABSOLU — l'adresse complète depuis la racine du système
chemin_absolu_linux   = "/home/utilisateur/bootcamp/donnees/etudiants.csv"
chemin_absolu_windows = "C:\\Users\\utilisateur\\bootcamp\\donnees\\etudiants.csv"
```

| Type de chemin | Description | Avantage |
|-----------------|-------------|----------|
| **Relatif** | Par rapport au dossier courant | Portable entre machines/collaborateurs |
| **Absolu** | Adresse complète depuis la racine | Sans ambiguïté, mais dépend de la machine |

```python
import os

# Connaître le dossier de travail actuel
print(os.getcwd())

# Vérifier si un fichier existe avant de le manipuler
print(os.path.exists("donnees/etudiants.csv"))

# Lister les fichiers d'un dossier
print(os.listdir("."))
```

### 1.3 Extensions de fichiers courantes en Data Science

| Extension | Type de fichier | Usage typique |
|-----------|-------------------|----------------|
| `.txt` | Texte brut | Notes, logs, texte libre |
| `.csv` | Valeurs séparées par virgules | Données tabulaires simples |
| `.tsv` | Valeurs séparées par tabulations | Alternative au CSV |
| `.json` | JavaScript Object Notation | Données structurées/hiérarchiques (APIs) |
| `.npy` / `.npz` | Format binaire NumPy | Tableaux NumPy (rapide, compact) |
| `.xlsx` | Excel | Tableurs avec plusieurs feuilles |
| `.parquet` | Format binaire colonne | Big Data, très performant |

---

## 2. Understanding Files, Objects, Reading, and Parsing

### 2.1 Ouvrir un fichier — la fonction `open()`

En Python, on ouvre un fichier avec `open()`, qui retourne un **objet fichier** (rappelez-vous le chapitre OOP : cet objet possède ses propres attributs et méthodes).

```python
fichier = open("notes.txt", "r")   # "r" = mode lecture (read)
contenu = fichier.read()
print(contenu)
fichier.close()   # ⚠️ Ne JAMAIS oublier de fermer le fichier !
```

### 2.2 Les modes d'ouverture

| Mode | Signification | Comportement |
|------|-----------------|---------------|
| `"r"` | Read (lecture) | Erreur si le fichier n'existe pas |
| `"w"` | Write (écriture) | Crée le fichier, **écrase** le contenu existant |
| `"a"` | Append (ajout) | Ajoute à la fin du fichier existant (le crée si absent) |
| `"x"` | Exclusive creation | Erreur si le fichier existe déjà |
| `"r+"` | Lecture + écriture | Le fichier doit déjà exister |
| `"rb"` / `"wb"` | Mode binaire | Pour images, fichiers non textuels |

```python
# Écriture (écrase tout contenu existant)
fichier = open("notes.txt", "w")
fichier.write("Alice : 16\n")
fichier.write("Bob : 14\n")
fichier.close()

# Ajout (ne supprime pas le contenu existant)
fichier = open("notes.txt", "a")
fichier.write("Claire : 18\n")
fichier.close()
```

### 2.3 ⚠️ Pourquoi fermer un fichier avec `.close()` ?

```
FICHIER OUVERT MAIS NON FERMÉ
│
├── 🔒 Verrouillage      → D'autres programmes ne peuvent pas l'utiliser
├── 💾 Données non écrites → Le buffer n'est pas forcé sur le disque
├── 🐛 Fuite de ressources → Le système garde le fichier "occupé"
└── ❌ Résultats imprévisibles → Surtout en cas de plantage du programme
```

### 2.4 La bonne pratique — `with` (context manager)

> 🔑 **Règle d'or professionnelle** : Utilisez **toujours** `with open(...) as f:` plutôt que `open()` / `.close()` séparément. Le fichier se ferme **automatiquement**, même en cas d'erreur dans le bloc.

```python
# ✅ Bonne pratique — fermeture automatique garantie
with open("notes.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
# Ici, le fichier est DÉJÀ fermé automatiquement, même si une erreur survient

# ❌ À éviter — risque d'oublier .close(), ou de ne jamais l'atteindre si erreur
fichier = open("notes.txt", "r")
contenu = fichier.read()
# ... si une erreur survient ici, fichier.close() n'est jamais exécuté !
fichier.close()
```

```
AVEC open()/.close()               AVEC with ... as f:
─────────────────────              ─────────────────────
f = open(...)                      with open(...) as f:
resultat = f.read()                     resultat = f.read()
# risque d'oubli de close()        # fermeture AUTOMATIQUE
f.close()                          # même si une erreur survient
```

### 2.5 Méthodes de lecture

```python
with open("notes.txt", "r") as f:
    # .read() — tout le contenu en UNE seule chaîne de caractères
    contenu_complet = f.read()
    print(contenu_complet)

with open("notes.txt", "r") as f:
    # .readline() — UNE seule ligne à chaque appel
    premiere_ligne = f.readline()
    deuxieme_ligne = f.readline()
    print(premiere_ligne)

with open("notes.txt", "r") as f:
    # .readlines() — TOUTES les lignes sous forme de LISTE
    toutes_les_lignes = f.readlines()
    print(toutes_les_lignes)
    # ['Alice : 16\n', 'Bob : 14\n', 'Claire : 18\n']

with open("notes.txt", "r") as f:
    # Itérer directement sur le fichier (façon la plus "pythonique")
    for ligne in f:
        print(ligne.strip())   # .strip() supprime le \n final
```

### 2.6 Parsing — Transformer du texte brut en données structurées

**Parser**, c'est **analyser et découper** un texte brut pour en extraire des données exploitables — l'étape indispensable entre "un fichier plein de texte" et "des données utilisables dans votre programme".

```python
# Contenu du fichier notes.txt :
# Alice,16
# Bob,14
# Claire,18

etudiants = []

with open("notes.txt", "r") as f:
    for ligne in f:
        ligne = ligne.strip()             # supprimer le retour à la ligne
        nom, note = ligne.split(",")      # PARSING : découper sur la virgule
        etudiants.append({
            "nom"  : nom,
            "note" : float(note)          # conversion : texte → nombre
        })

print(etudiants)
# [{'nom': 'Alice', 'note': 16.0}, {'nom': 'Bob', 'note': 14.0}, {'nom': 'Claire', 'note': 18.0}]
```

> 💡 Vous reconnaissez cette logique ? C'est exactement ce que vous avez fait au chapitre **Web Scraping** en extrayant du texte HTML — parser, c'est toujours la même démarche : **texte brut → découpage → structure exploitable**.

---

## 3. Understanding Data Types

### 📖 Piège n°1 du File Handling : TOUT est du texte !

> 🚨 **Règle absolue à retenir** : Quel que soit le contenu apparent d'un fichier texte (nombres, dates, booléens), Python le lit **toujours** comme une **chaîne de caractères (`str`)**. Il faut **convertir explicitement** vers le bon type.

```python
with open("notes.txt", "r") as f:
    ligne = f.readline().strip()   # "Alice,16"
    nom, note = ligne.split(",")

print(type(note))     # <class 'str'>  ← "16", PAS 16 !
print(note + 4)        # ❌ TypeError : impossible d'additionner str + int

# ✅ Conversion nécessaire
note_numerique = float(note)
print(type(note_numerique))   # <class 'float'>
print(note_numerique + 4)      # 20.0 ✅
```

### 3.1 Tableau des conversions courantes

| Donnée lue (str) | Fonction de conversion | Résultat |
|--------------------|--------------------------|----------|
| `"16"` | `int("16")` | `16` |
| `"16.5"` | `float("16.5")` | `16.5` |
| `"True"` | `"True" == "True"` (pas `bool()` !) | `True` |
| `"2024-01-15"` | `datetime.strptime(...)` | objet date |
| `"14,16,18"` | `.split(",")` puis conversion | liste de nombres |

> ⚠️ **Piège classique** : `bool("False")` retourne `True` ! En effet, `bool()` sur une chaîne **non vide** retourne toujours `True`, peu importe son contenu. Il faut comparer explicitement : `valeur == "True"`.

```python
# ❌ Piège
print(bool("False"))    # True !! (car la chaîne "False" n'est pas vide)

# ✅ Bonne pratique
texte = "False"
valeur_bool = (texte == "True")
print(valeur_bool)      # False ✅
```

### 3.2 Gérer les erreurs de conversion

```python
valeurs_brutes = ["14", "16", "abc", "18", ""]

valeurs_propres = []
for v in valeurs_brutes:
    try:
        valeurs_propres.append(float(v))
    except ValueError:
        print(f"⚠️ Valeur ignorée (non convertible) : '{v}'")
        valeurs_propres.append(None)   # ou une valeur par défaut

print(valeurs_propres)   # [14.0, 16.0, None, 18.0, None]
```

### 3.3 Types de fichiers : Texte vs Binaire

```
FICHIERS TEXTE                          FICHIERS BINAIRES
────────────────────                    ────────────────────
.txt, .csv, .json, .html                .jpg, .png, .npy, .xlsx, .mp3
    │                                        │
    ▼                                        ▼
Lisibles par un humain                  Illisibles directement
(ouvrir avec un éditeur de texte)       (nécessitent un logiciel/librairie
                                          spécifique pour être interprétés)
    │                                        │
    ▼                                        ▼
Mode "r" / "w"                          Mode "rb" / "wb" (binary)
Encodage à préciser (utf-8)             Pas d'encodage texte
```

```python
# Toujours préciser l'encodage pour les fichiers texte (gère les accents, é, à, ç...)
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# Fichier binaire (ex : une image)
with open("photo.jpg", "rb") as f:
    donnees_binaires = f.read()
    print(type(donnees_binaires))   # <class 'bytes'>
```

---

## 4. Distinguishing Text Files from Flat Files

### 📖 Deux grandes familles de fichiers texte

Bien que les deux soient des "fichiers texte" lisibles par un humain, il existe une distinction importante en Data Science entre **fichiers texte libres** et **fichiers plats (flat files)**.

### 4.1 Fichiers texte (non structurés)

Un **fichier texte libre** (`.txt`) contient du texte **sans structure imposée** — comme un article, un roman, des logs.

```
notes_de_cours.txt
────────────────────────────────────────
Aujourd'hui nous avons vu le File Handling.
Les points clés à retenir :
- toujours fermer les fichiers
- utiliser with pour la sécurité
- convertir les types après lecture
```

### 4.2 Fichiers plats (Flat Files) — Données tabulaires

Un **fichier plat** organise les données en **lignes et colonnes**, avec un **délimiteur** cohérent (virgule, tabulation...) — c'est le format `.csv` que vous connaissez déjà de Pandas/du web scraping.

```
etudiants.csv
────────────────────────────────
nom,age,ville,note
Alice,23,Abidjan,16.5
Bob,25,Dakar,14.0
Claire,22,Accra,18.0
```

> 💡 **Analogie** : Un fichier texte libre est comme une **lettre manuscrite** — le contenu est libre, sans structure fixe. Un fichier plat (CSV) est comme un **tableau Excel imprimé en texte** — chaque ligne est un enregistrement, chaque colonne a un sens précis, séparé par des virgules.

### 4.3 Pourquoi "plat" (flat) ?

```
FICHIER PLAT (flat) — structure à 2 dimensions SEULEMENT
┌──────────┬─────┬──────────┬───────┐
│   nom    │ age │  ville   │ note  │
├──────────┼─────┼──────────┼───────┤
│ Alice    │ 23  │ Abidjan  │ 16.5  │
│ Bob      │ 25  │ Dakar    │ 14.0  │
└──────────┴─────┴──────────┴───────┘
→ Lignes × Colonnes. Pas de hiérarchie, pas d'imbrication.

FICHIER STRUCTURÉ (ex: JSON) — peut avoir plusieurs niveaux
{
  "etudiant": "Alice",
  "cours": [
      {"nom": "SQL", "note": 16},
      {"nom": "Python", "note": 18}
  ]
}
→ Imbrication possible (un étudiant a une LISTE de cours)
```

| Caractéristique | Fichier texte libre | Fichier plat (CSV/TSV) | Fichier structuré (JSON) |
|-------------------|------------------------|---------------------------|------------------------------|
| Structure | Aucune | Lignes/colonnes (2D) | Hiérarchique (imbriqué) |
| Délimiteur | Aucun | Virgule, tabulation... | Accolades, crochets |
| Usage typique | Texte libre, logs | Données tabulaires | APIs, configurations |
| Lecture Python | `open()` | `open()` + `.split()` ou `csv` | module `json` |

### 4.4 Lire un fichier plat "à la main"

```python
with open("etudiants.csv", "r", encoding="utf-8") as f:
    lignes = f.readlines()

entetes = lignes[0].strip().split(",")     # ['nom', 'age', 'ville', 'note']
print("Colonnes :", entetes)

donnees = []
for ligne in lignes[1:]:                    # on saute la ligne d'en-tête
    valeurs = ligne.strip().split(",")
    enregistrement = dict(zip(entetes, valeurs))
    donnees.append(enregistrement)

print(donnees)
```

### 4.5 Le module `csv` — Plus robuste que `.split(",")`

> ⚠️ **Piège** : découper "à la main" avec `.split(",")` échoue si une valeur contient elle-même une virgule (ex : `"Abidjan, Cocody"`). Le module `csv` gère ces cas correctement.

```python
import csv

with open("etudiants.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    entetes = next(lecteur)          # première ligne = en-têtes
    for ligne in lecteur:
        print(ligne)                  # chaque ligne = une LISTE

# DictReader — encore plus pratique : chaque ligne devient un DICTIONNAIRE
with open("etudiants.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne["nom"], "-", ligne["note"])
```

### 4.6 Écrire un fichier CSV avec le module `csv`

```python
import csv

donnees = [
    {"nom": "Fatou",  "age": 22, "ville": "Abidjan", "note": 17.5},
    {"nom": "Kofi",   "age": 24, "ville": "Accra",   "note": 15.0},
]

with open("resultats.csv", "w", encoding="utf-8", newline="") as f:
    champs = ["nom", "age", "ville", "note"]
    ecrivain = csv.DictWriter(f, fieldnames=champs)
    ecrivain.writeheader()          # écrit la ligne d'en-tête
    ecrivain.writerows(donnees)     # écrit toutes les lignes
```

---

## 5. I/O Operations with NumPy

NumPy propose ses propres fonctions optimisées pour lire et écrire des **données numériques**, particulièrement utiles pour des grands volumes de données.

### 5.1 `np.loadtxt()` — Chargement simple

```python
import numpy as np

# Fichier notes_numpy.txt :
# 14 16 18
# 12 15 17
# 10 20 19

donnees = np.loadtxt("notes_numpy.txt")
print(donnees)
print(donnees.shape)   # (3, 3)
```

```python
# Avec un délimiteur spécifique (ex : virgules) et en sautant l'en-tête
donnees_csv = np.loadtxt("notes.csv", delimiter=",", skiprows=1)
print(donnees_csv)
```

> ⚠️ `np.loadtxt()` exige que **toutes** les valeurs soient numériques et qu'il n'y ait **aucune valeur manquante** — sinon il lève une erreur.

### 5.2 `np.genfromtxt()` — Plus robuste (valeurs manquantes)

```python
# Gère les valeurs manquantes (NaN) et les en-têtes nommés
donnees = np.genfromtxt(
    "notes_avec_trous.csv",
    delimiter=",",
    skip_header=1,
    filling_values=np.nan    # remplace les valeurs manquantes par NaN
)
print(donnees)

# Avec noms de colonnes (dtype=None détecte automatiquement les types)
donnees_nommees = np.genfromtxt(
    "etudiants_numeriques.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)
print(donnees_nommees["note"])   # accès par nom de colonne
```

### 5.3 `np.savetxt()` — Écrire un tableau NumPy dans un fichier texte

```python
notes = np.array([[14, 16, 18], [12, 15, 17], [10, 20, 19]])

np.savetxt("notes_sauvegardees.txt", notes, fmt="%d")            # entiers
np.savetxt("notes_sauvegardees.csv", notes, delimiter=",", fmt="%.2f")  # CSV, 2 décimales
```

### 5.4 Format binaire natif — `.npy` et `.npz`

Pour un usage **purement Python/NumPy** (pas besoin d'ouvrir le fichier dans Excel), le format binaire `.npy` est **beaucoup plus rapide** et conserve **exactement** le type et la forme du tableau.

```python
notes = np.array([[14, 16, 18], [12, 15, 17]])

# Sauvegarder UN tableau au format binaire NumPy
np.save("notes.npy", notes)

# Recharger — la forme et le dtype sont préservés à l'identique
notes_rechargees = np.load("notes.npy")
print(notes_rechargees)
print(np.array_equal(notes, notes_rechargees))   # True

# Sauvegarder PLUSIEURS tableaux dans un seul fichier compressé
ages   = np.array([23, 25, 22])
notes2 = np.array([16.5, 14.0, 18.0])
np.savez("etudiants.npz", ages=ages, notes=notes2)

# Recharger
donnees = np.load("etudiants.npz")
print(donnees["ages"])
print(donnees["notes"])
```

### 5.5 Comparatif des méthodes d'I/O NumPy

| Fonction | Usage | Avantage | Limite |
|----------|-------|----------|--------|
| `np.loadtxt()` | Charger un fichier texte numérique | Simple | Pas de valeurs manquantes |
| `np.genfromtxt()` | Charger avec valeurs manquantes/en-têtes | Robuste | Plus lent |
| `np.savetxt()` | Écrire un tableau en texte lisible | Lisible par Excel | Fichier plus volumineux |
| `np.save()` / `np.load()` | Format binaire `.npy` | Très rapide, préserve le dtype | Illisible hors NumPy |
| `np.savez()` | Plusieurs tableaux, un seul fichier | Pratique, compressible | Format spécifique NumPy |

---

## 6. Conclusion

### 📌 Récapitulatif du chapitre

```
FILE HANDLING
│
├── Introduction
│   ├── RAM (volatile) vs Disque (permanent)
│   └── Chemins relatifs vs absolus
│
├── Manipulation de fichiers
│   ├── open(chemin, mode)         → "r", "w", "a", "rb"...
│   ├── with open(...) as f:       → fermeture AUTOMATIQUE (bonne pratique)
│   ├── .read() / .readline() / .readlines()
│   └── Parsing                    → texte brut → structure exploitable
│
├── Types de données
│   ├── ⚠️ Tout est lu comme str    → conversion int()/float() nécessaire
│   └── Fichiers texte vs binaires  → mode "r" vs "rb"
│
├── Text Files vs Flat Files
│   ├── Texte libre                 → pas de structure (.txt)
│   ├── Fichier plat                → lignes/colonnes 2D (.csv)
│   └── module csv                  → csv.reader, csv.DictReader/Writer
│
└── I/O avec NumPy
    ├── np.loadtxt() / np.genfromtxt()  → charger des tableaux numériques
    ├── np.savetxt()                     → écrire en texte lisible
    └── np.save() / np.load() (.npy)     → format binaire rapide
```

### 🔑 Points clés à retenir

1. Les **fichiers** permettent de conserver des données **au-delà** de l'exécution d'un programme.
2. **`with open(...) as f:`** est la méthode recommandée — fermeture garantie, même en cas d'erreur.
3. **Tout ce qui est lu depuis un fichier texte est une chaîne de caractères** — convertissez toujours explicitement.
4. Un **fichier plat** (CSV) organise les données en 2D (lignes/colonnes) ; un fichier structuré (JSON) peut être imbriqué.
5. Le module `csv` est plus robuste que `.split(",")` pour parser des fichiers plats.
6. Pour des données **purement numériques**, `np.loadtxt()`/`np.genfromtxt()` (texte) ou `np.save()`/`np.load()` (binaire, plus rapide) sont préférables à une lecture manuelle.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons **Pandas** en profondeur — la bibliothèque qui **automatise** presque tout ce que vous venez d'apprendre manuellement (`pd.read_csv()`, `pd.read_json()`, `df.to_csv()`...) tout en offrant des outils bien plus puissants pour nettoyer, filtrer et analyser vos données.

---

## 7. Python Project — Gestionnaire de notes du Bootcamp

### 🎯 Objectif du projet

Construire un **mini-système complet** qui :
1. **Écrit** un fichier CSV brut avec les inscriptions d'étudiants
2. **Lit et parse** ce fichier
3. **Convertit** les types de données correctement
4. **Calcule des statistiques** avec NumPy
5. **Génère un rapport** texte
6. **Sauvegarde** les résultats en formats CSV et binaire NumPy (`.npy`)

Ce projet regroupe **toutes les notions** de ce chapitre dans un pipeline réaliste, comme vous en construirez tout au long de votre carrière en Data Science.

```python
import csv
import numpy as np

# ============================================
# ÉTAPE 1 : Créer le fichier source (simulation d'inscriptions)
# ============================================
def creer_fichier_inscriptions(chemin):
    """Écrit un fichier CSV brut avec les inscriptions des étudiants."""
    inscriptions = [
        ["nom", "age", "ville", "note_sql", "note_python"],
        ["Fatou Diallo",  "23", "Abidjan", "16", "18"],
        ["Kofi Asante",   "25", "Accra",   "14", "15"],
        ["Awa Traore",    "22", "Dakar",   "18", "17"],
        ["Moussa Keita",  "28", "Bamako",  "12", "13"],
        ["Aminata Sow",   "24", "Abidjan", "17", "19"],
    ]

    with open(chemin, "w", encoding="utf-8", newline="") as f:
        ecrivain = csv.writer(f)
        ecrivain.writerows(inscriptions)

    print(f"✅ Fichier créé : {chemin}")


# ============================================
# ÉTAPE 2 : Lire et parser le fichier
# ============================================
def lire_inscriptions(chemin):
    """Lit le fichier CSV et retourne une liste de dictionnaires typés."""
    etudiants = []

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            etudiants.append({
                "nom"         : ligne["nom"],
                "age"         : int(ligne["age"]),           # conversion str → int
                "ville"       : ligne["ville"],
                "note_sql"    : float(ligne["note_sql"]),    # conversion str → float
                "note_python" : float(ligne["note_python"])
            })

    print(f"✅ {len(etudiants)} étudiants chargés depuis {chemin}")
    return etudiants


# ============================================
# ÉTAPE 3 : Analyser avec NumPy
# ============================================
def analyser_notes(etudiants):
    """Utilise NumPy pour calculer des statistiques sur les notes."""
    notes_sql    = np.array([e["note_sql"] for e in etudiants])
    notes_python = np.array([e["note_python"] for e in etudiants])

    stats = {
        "moyenne_sql"    : notes_sql.mean(),
        "moyenne_python" : notes_python.mean(),
        "meilleure_sql"  : notes_sql.max(),
        "meilleure_python": notes_python.max(),
        "ecart_type_sql" : notes_sql.std(),
        "ecart_type_python": notes_python.std(),
    }

    return stats, notes_sql, notes_python


# ============================================
# ÉTAPE 4 : Générer un rapport texte
# ============================================
def generer_rapport(etudiants, stats, chemin_rapport):
    """Écrit un rapport lisible dans un fichier texte."""
    with open(chemin_rapport, "w", encoding="utf-8") as f:
        f.write("=== RAPPORT DU BOOTCAMP DATA SCIENCE ===\n\n")
        f.write(f"Nombre d'étudiants : {len(etudiants)}\n\n")

        f.write("--- Statistiques SQL ---\n")
        f.write(f"Moyenne    : {stats['moyenne_sql']:.2f}\n")
        f.write(f"Meilleure  : {stats['meilleure_sql']:.2f}\n")
        f.write(f"Écart type : {stats['ecart_type_sql']:.2f}\n\n")

        f.write("--- Statistiques Python ---\n")
        f.write(f"Moyenne    : {stats['moyenne_python']:.2f}\n")
        f.write(f"Meilleure  : {stats['meilleure_python']:.2f}\n")
        f.write(f"Écart type : {stats['ecart_type_python']:.2f}\n\n")

        f.write("--- Détail par étudiant ---\n")
        for e in etudiants:
            moyenne_perso = (e["note_sql"] + e["note_python"]) / 2
            f.write(f"{e['nom']:20} ({e['ville']:10}) — Moyenne : {moyenne_perso:.1f}/20\n")

    print(f"✅ Rapport généré : {chemin_rapport}")


# ============================================
# ÉTAPE 5 : Sauvegarder en formats CSV et NumPy binaire
# ============================================
def sauvegarder_resultats(etudiants, notes_sql, notes_python):
    """Sauvegarde les résultats en CSV (lisible) et .npy (rapide)."""
    # CSV enrichi avec la moyenne calculée
    with open("resultats_finaux.csv", "w", encoding="utf-8", newline="") as f:
        champs = ["nom", "ville", "note_sql", "note_python", "moyenne"]
        ecrivain = csv.DictWriter(f, fieldnames=champs)
        ecrivain.writeheader()
        for e in etudiants:
            ecrivain.writerow({
                "nom"        : e["nom"],
                "ville"      : e["ville"],
                "note_sql"   : e["note_sql"],
                "note_python": e["note_python"],
                "moyenne"    : round((e["note_sql"] + e["note_python"]) / 2, 1)
            })

    # Sauvegarde binaire NumPy (rapide à recharger pour analyse future)
    np.savez("notes_brutes.npz", sql=notes_sql, python=notes_python)

    print("✅ Résultats sauvegardés : resultats_finaux.csv + notes_brutes.npz")


# ============================================
# EXÉCUTION DU PIPELINE COMPLET
# ============================================
if __name__ == "__main__":
    FICHIER_SOURCE  = "inscriptions.csv"
    FICHIER_RAPPORT = "rapport_bootcamp.txt"

    creer_fichier_inscriptions(FICHIER_SOURCE)
    etudiants = lire_inscriptions(FICHIER_SOURCE)
    stats, notes_sql, notes_python = analyser_notes(etudiants)
    generer_rapport(etudiants, stats, FICHIER_RAPPORT)
    sauvegarder_resultats(etudiants, notes_sql, notes_python)

    print("\n🎉 Pipeline terminé avec succès !")
```

### 🔍 Vérifier le résultat

```python
# Relire et afficher le rapport généré
with open("rapport_bootcamp.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Recharger les données binaires sauvegardées
donnees_rechargees = np.load("notes_brutes.npz")
print("Notes SQL rechargées :", donnees_rechargees["sql"])
```

> 💡 **Ce projet illustre le cycle complet d'un Data Scientist** : collecte (ici simulée, mais ce serait le résultat d'un scraping ou d'une base de données) → lecture/parsing → nettoyage/typage → analyse → rapport → sauvegarde pour réutilisation future. Vous retrouverez exactement ce schéma, en plus automatisé, avec Pandas au prochain chapitre.

---

## 8. ✅ Point de contrôle — File Handling

### 📝 Questions théoriques

**Q1.** Pourquoi préfère-t-on `with open(...) as f:` plutôt que `open()` suivi de `.close()` ?

<details>
<summary>👀 Voir la réponse</summary>

> `with` garantit la **fermeture automatique** du fichier dès la sortie du bloc, **même si une erreur survient** pendant la lecture/écriture. Avec `open()`/`.close()` manuels, une exception avant l'appel à `.close()` laisserait le fichier ouvert, ce qui peut causer des fuites de ressources ou des données non enregistrées.
</details>

---

**Q2.** Pourquoi `bool("False")` retourne-t-il `True` en Python ?

<details>
<summary>👀 Voir la réponse</summary>

> `bool()` appliqué à une chaîne de caractères retourne `True` pour **toute chaîne non vide**, peu importe son contenu textuel. `"False"` est une chaîne de 5 caractères, donc non vide → `True`. Pour convertir correctement, il faut comparer explicitement : `texte == "True"`.
</details>

---

**Q3.** Quelle est la différence fondamentale entre un fichier texte libre (.txt) et un fichier plat (.csv) ?

<details>
<summary>👀 Voir la réponse</summary>

> Un fichier texte libre ne suit **aucune structure imposée** (texte libre, comme un article). Un fichier plat organise les données en **lignes et colonnes** (structure 2D), avec un délimiteur cohérent (virgule, tabulation), représentant des enregistrements tabulaires.
</details>

---

**Q4.** Pourquoi utiliser le module `csv` plutôt que `.split(",")` pour parser un fichier CSV ?

<details>
<summary>👀 Voir la réponse</summary>

> `.split(",")` échoue si une valeur contient elle-même une virgule (ex : une adresse `"Abidjan, Cocody"` entre guillemets dans le CSV). Le module `csv` comprend les règles d'échappement du format CSV (guillemets, virgules internes) et parse correctement ces cas particuliers.
</details>

---

**Q5.** Quand privilégier `np.save()`/`.npy` plutôt que `np.savetxt()` ?

<details>
<summary>👀 Voir la réponse</summary>

> `np.save()` (format `.npy`) est préférable quand les données seront **uniquement réutilisées avec NumPy/Python** : il est plus **rapide** à écrire/lire et préserve **exactement** le type et la forme du tableau. `np.savetxt()` est préférable quand le fichier doit rester **lisible par un humain** ou ouvrable dans Excel/un éditeur de texte.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Écriture et lecture simples**

Écrivez un fichier `villes.txt` contenant une ville par ligne (`Abidjan`, `Dakar`, `Accra`, `Lomé`), puis relisez-le et affichez chaque ville en majuscules.

<details>
<summary>👀 Voir la solution</summary>

```python
villes = ["Abidjan", "Dakar", "Accra", "Lomé"]

with open("villes.txt", "w", encoding="utf-8") as f:
    for ville in villes:
        f.write(ville + "\n")

with open("villes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip().upper())
```
</details>

---

**Exercice 2 — Parsing et conversion**

Créez un fichier `temperatures.txt` avec le contenu `"22,25,19,30,18"` (une seule ligne). Lisez-le, transformez-le en liste de nombres flottants, et calculez la moyenne.

<details>
<summary>👀 Voir la solution</summary>

```python
with open("temperatures.txt", "w", encoding="utf-8") as f:
    f.write("22,25,19,30,18")

with open("temperatures.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

temperatures = [float(t) for t in contenu.split(",")]
moyenne = sum(temperatures) / len(temperatures)
print(f"Températures : {temperatures}")
print(f"Moyenne : {moyenne:.2f}")
```
</details>

---

**Exercice 3 — Module csv**

Créez un fichier `produits.csv` avec les colonnes `nom,prix,stock` et 3 produits de votre choix, en utilisant `csv.DictWriter`. Relisez-le avec `csv.DictReader` et affichez le produit le plus cher.

<details>
<summary>👀 Voir la solution</summary>

```python
import csv

produits = [
    {"nom": "Ordinateur", "prix": "850000", "stock": "10"},
    {"nom": "Souris",     "prix": "15000",  "stock": "50"},
    {"nom": "Clavier",    "prix": "25000",  "stock": "30"},
]

with open("produits.csv", "w", encoding="utf-8", newline="") as f:
    ecrivain = csv.DictWriter(f, fieldnames=["nom", "prix", "stock"])
    ecrivain.writeheader()
    ecrivain.writerows(produits)

with open("produits.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    produits_lus = list(lecteur)

plus_cher = max(produits_lus, key=lambda p: float(p["prix"]))
print(f"Produit le plus cher : {plus_cher['nom']} ({plus_cher['prix']} FCFA)")
```
</details>

---

**Exercice 4 — I/O NumPy**

Créez un tableau NumPy 3x3 de votre choix, sauvegardez-le en `.npy`, puis rechargez-le et vérifiez avec `np.array_equal()` que les données sont identiques.

<details>
<summary>👀 Voir la solution</summary>

```python
import numpy as np

original = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.save("matrice.npy", original)

recharge = np.load("matrice.npy")
print(recharge)
print("Identiques :", np.array_equal(original, recharge))
```
</details>

---

**Exercice 5 — Gestion d'erreur de conversion**

Vous avez la liste `valeurs = ["12", "15", "erreur", "20", ""]`. Écrivez un code qui convertit chaque valeur en `float`, et remplace par `None` celles qui ne peuvent pas être converties (sans faire planter le programme).

<details>
<summary>👀 Voir la solution</summary>

```python
valeurs = ["12", "15", "erreur", "20", ""]
resultat = []

for v in valeurs:
    try:
        resultat.append(float(v))
    except ValueError:
        resultat.append(None)

print(resultat)   # [12.0, 15.0, None, 20.0, None]
```
</details>

---

### 🏆 Challenge bonus — Fusionner scraping et file handling

Reprenez les données météo scrapées au chapitre précédent (ou simulez-les avec une liste de dictionnaires `{"periode": ..., "temperature": ...}`). Écrivez un pipeline complet qui :

1. Sauvegarde les données scrapées dans un fichier `meteo_brute.csv`
2. Relit ce fichier depuis le disque
3. Convertit les températures en valeurs numériques
4. Utilise NumPy pour calculer min, max, moyenne
5. Écrit un rapport texte `rapport_meteo.txt` avec ces statistiques
6. Sauvegarde le tableau NumPy des températures en `.npy` pour archivage

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import csv
import numpy as np

# Simulation de données scrapées (chapitre précédent)
donnees_scrapees = [
    {"periode": "Overnight", "temperature": "58"},
    {"periode": "Wednesday", "temperature": "72"},
    {"periode": "Thursday",  "temperature": "72"},
    {"periode": "Friday",    "temperature": "73"},
]

# 1. Sauvegarder
with open("meteo_brute.csv", "w", encoding="utf-8", newline="") as f:
    ecrivain = csv.DictWriter(f, fieldnames=["periode", "temperature"])
    ecrivain.writeheader()
    ecrivain.writerows(donnees_scrapees)

# 2-3. Relire et convertir
temperatures = []
with open("meteo_brute.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        temperatures.append(float(ligne["temperature"]))

# 4. Statistiques NumPy
temp_array = np.array(temperatures)
stats = {
    "min"    : temp_array.min(),
    "max"    : temp_array.max(),
    "moyenne": temp_array.mean()
}

# 5. Rapport
with open("rapport_meteo.txt", "w", encoding="utf-8") as f:
    f.write("=== RAPPORT MÉTÉO ===\n")
    f.write(f"Température minimale : {stats['min']}°F\n")
    f.write(f"Température maximale : {stats['max']}°F\n")
    f.write(f"Température moyenne  : {stats['moyenne']:.1f}°F\n")

# 6. Archivage binaire
np.save("temperatures_archive.npy", temp_array)

print("✅ Pipeline complet terminé !")
with open("rapport_meteo.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
</details>

---

*📘 Module Data Science — File Handling | Bootcamp Data Science*
