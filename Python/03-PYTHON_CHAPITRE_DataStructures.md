# 🗂️ Data Structures in Python — Cours Bootcamp Data Science

> **Chapitre 3** | Prérequis : Chapitre 1 (Introduction) + Chapitre 2 (Bases)

---

## Table des matières

1. [Vue d'ensemble des structures de données](#1-vue-densemble-des-structures-de-données)
2. [List — Les listes](#2-list--les-listes)
3. [List Manipulation — Manipuler les listes](#3-list-manipulation--manipuler-les-listes)
4. [Dictionary — Les dictionnaires](#4-dictionary--les-dictionnaires)
5. [Dictionary Manipulation — Manipuler les dictionnaires](#5-dictionary-manipulation--manipuler-les-dictionnaires)
6. [Sets — Les ensembles](#6-sets--les-ensembles)
7. [Tuple — Les tuples](#7-tuple--les-tuples)
8. [Nested Structures — Structures imbriquées](#8-nested-structures--structures-imbriquées)
9. [Choisir la bonne structure](#9-choisir-la-bonne-structure)
10. [Conclusion](#10-conclusion)
11. [✅ Point de contrôle — Data Structures](#11--point-de-contrôle--data-structures)

---

## 1. Vue d'ensemble des structures de données

### 📖 Qu'est-ce qu'une structure de données ?

Une **structure de données** est une façon organisée de **stocker et regrouper plusieurs valeurs** dans une seule variable. Plutôt que de créer 30 variables pour 30 étudiants, on les regroupe dans une seule structure.

> 💡 **Analogie** : Imaginez que vous devez ranger des documents.
> - Une **liste** → un **classeur avec des pages numérotées** (ordre garanti)
> - Un **dictionnaire** → un **répertoire avec des étiquettes** (clé → valeur)
> - Un **ensemble** → un **sac de billes uniques** (pas de doublons)
> - Un **tuple** → une **archive scellée** (immuable, ne peut pas être modifiée)

### 1.1 Les 4 structures fondamentales

```
STRUCTURES DE DONNÉES PYTHON
│
├── list   [ ]   → Ordonnée, modifiable, doublons autorisés
├── dict   { }   → Paires clé:valeur, modifiable
├── set    { }   → Non ordonnée, unique, modifiable
└── tuple  ( )   → Ordonnée, NON modifiable (immuable)
```

### 1.2 Tableau comparatif

| Propriété | `list` | `dict` | `set` | `tuple` |
|-----------|--------|--------|-------|---------|
| **Syntaxe** | `[...]` | `{clé: val}` | `{...}` | `(...)` |
| **Ordonnée** | ✅ Oui | ✅ Oui (Python 3.7+) | ❌ Non | ✅ Oui |
| **Modifiable** | ✅ Oui | ✅ Oui | ✅ Oui | ❌ Non |
| **Doublons** | ✅ Oui | ❌ Clés uniques | ❌ Non | ✅ Oui |
| **Accès** | Par indice `[0]` | Par clé `["nom"]` | Itération | Par indice `[0]` |
| **Usage typique** | Collection ordonnée | Données structurées | Valeurs uniques | Données fixes |

---

## 2. List — Les listes

### 📖 Définition

Une **liste** est une collection **ordonnée** et **modifiable** d'éléments. C'est la structure de données la plus utilisée en Python.

> 💡 **Analogie** : Une liste Python, c'est comme une **liste de courses** : vous pouvez ajouter des articles, en retirer, les réorganiser, et accéder à chaque article par sa position.

### 2.1 Créer une liste

```python
# Liste vide
liste_vide = []
liste_vide2 = list()

# Liste de nombres
notes = [14, 16, 12, 18, 15]

# Liste de chaînes
etudiants = ["Alice", "Bob", "Claire", "David"]

# Liste mixte (différents types)
profil = ["Alice", 23, 15.75, True]

# Liste de listes (imbriquée)
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(notes)      # [14, 16, 12, 18, 15]
print(type(notes))# <class 'list'>
print(len(notes)) # 5
```

### 2.2 Accéder aux éléments — Indexation

```python
fruits = ["mangue", "papaye", "ananas", "banane", "orange"]
#           0          1         2         3         4
#          -5         -4        -3        -2        -1

# Accès par indice positif
print(fruits[0])   # mangue  (premier)
print(fruits[2])   # ananas
print(fruits[4])   # orange  (dernier)

# Accès par indice négatif (depuis la fin)
print(fruits[-1])  # orange  (dernier)
print(fruits[-2])  # banane
print(fruits[-5])  # mangue  (premier)
```

### 2.3 Slicing — Extraire une sous-liste

```python
notes = [14, 16, 12, 18, 15, 10, 19]
#         0   1   2   3   4   5   6

print(notes[1:4])    # [16, 12, 18]  (indices 1, 2, 3)
print(notes[:3])     # [14, 16, 12]  (du début jusqu'à 3 exclu)
print(notes[3:])     # [18, 15, 10, 19] (de 3 jusqu'à la fin)
print(notes[::2])    # [14, 12, 15, 19] (un sur deux)
print(notes[::-1])   # [19, 10, 15, 18, 12, 16, 14] (inversée)
```

### 2.4 Parcourir une liste

```python
etudiants = ["Alice", "Bob", "Claire"]

# Boucle for simple
for etudiant in etudiants:
    print(f"Bonjour {etudiant} !")

# Avec enumerate (indice + valeur)
for i, etudiant in enumerate(etudiants):
    print(f"{i+1}. {etudiant}")
# 1. Alice
# 2. Bob
# 3. Claire

# List comprehension (façon pythonique rapide)
majuscules = [e.upper() for e in etudiants]
print(majuscules)  # ['ALICE', 'BOB', 'CLAIRE']
```

---

## 3. List Manipulation — Manipuler les listes

### 3.1 Ajouter des éléments

```python
courses = ["riz", "huile", "sucre"]

# .append() — ajouter à la FIN
courses.append("sel")
print(courses)  # ['riz', 'huile', 'sucre', 'sel']

# .insert(indice, valeur) — insérer à une POSITION précise
courses.insert(1, "tomates")
print(courses)  # ['riz', 'tomates', 'huile', 'sucre', 'sel']

# .extend() — fusionner avec une autre liste
nouveaux = ["poivre", "cube maggi"]
courses.extend(nouveaux)
print(courses)  # ['riz', 'tomates', 'huile', 'sucre', 'sel', 'poivre', 'cube maggi']
```

### 3.2 Supprimer des éléments

```python
notes = [14, 16, 12, 14, 18, 12]

# .remove(valeur) — supprime la PREMIÈRE occurrence
notes.remove(14)
print(notes)  # [16, 12, 14, 18, 12]

# .pop(indice) — supprime et RETOURNE l'élément à l'indice donné
dernier = notes.pop()    # sans indice → supprime le dernier
print(dernier)  # 12
print(notes)    # [16, 12, 14, 18]

element = notes.pop(1)   # supprime l'indice 1
print(element)  # 12
print(notes)    # [16, 14, 18]

# del — supprimer par indice ou slice
del notes[0]
print(notes)    # [14, 18]

# .clear() — vider toute la liste
notes.clear()
print(notes)    # []
```

### 3.3 Modifier des éléments

```python
etudiants = ["Alice", "Bob", "Claire"]

# Modifier par indice
etudiants[1] = "Bobby"
print(etudiants)  # ['Alice', 'Bobby', 'Claire']

# Modifier un slice
etudiants[0:2] = ["Anna", "Bruno"]
print(etudiants)  # ['Anna', 'Bruno', 'Claire']
```

### 3.4 Trier une liste

```python
notes = [14, 18, 12, 16, 10, 15]

# .sort() — trier EN PLACE (modifie la liste originale)
notes.sort()
print(notes)              # [10, 12, 14, 15, 16, 18]

notes.sort(reverse=True)
print(notes)              # [18, 16, 15, 14, 12, 10]

# sorted() — retourne une NOUVELLE liste triée
original = [14, 18, 12, 16]
nouvelle = sorted(original)
print(original)  # [14, 18, 12, 16]  ← inchangé
print(nouvelle)  # [12, 14, 16, 18]  ← nouvelle liste

# Trier des chaînes (ordre alphabétique)
noms = ["Charlie", "Alice", "Bob"]
noms.sort()
print(noms)  # ['Alice', 'Bob', 'Charlie']
```

### 3.5 Méthodes utiles

```python
notes = [14, 16, 12, 18, 14, 15]

print(notes.count(14))   # 2   — nombre d'occurrences de 14
print(notes.index(18))   # 3   — indice de la première occurrence de 18
print(min(notes))        # 12  — valeur minimale
print(max(notes))        # 18  — valeur maximale
print(sum(notes))        # 89  — somme de tous les éléments
print(sum(notes)/len(notes))  # 14.83 — moyenne

notes.reverse()          # inverser la liste EN PLACE
print(notes)             # [15, 14, 18, 12, 16, 14]

# Vérifier l'appartenance
print(18 in notes)       # True
print(20 in notes)       # False
print(20 not in notes)   # True
```

### 3.6 List Comprehension — La syntaxe élégante

```python
# Syntaxe : [expression for element in iterable if condition]

# Carrés de 1 à 10
carres = [x**2 for x in range(1, 11)]
print(carres)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Notes supérieures à 14
notes = [14, 16, 12, 18, 10, 15]
bonnes_notes = [n for n in notes if n > 14]
print(bonnes_notes)  # [16, 18, 15]

# Transformer une liste
noms = ["alice", "bob", "claire"]
noms_maj = [n.capitalize() for n in noms]
print(noms_maj)  # ['Alice', 'Bob', 'Claire']
```

### 3.7 Tableau récapitulatif des méthodes de liste

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `.append(x)` | Ajouter à la fin | `lst.append(5)` |
| `.insert(i, x)` | Insérer à la position i | `lst.insert(0, 5)` |
| `.extend(lst2)` | Fusionner deux listes | `lst.extend([6, 7])` |
| `.remove(x)` | Supprimer première occurrence | `lst.remove(5)` |
| `.pop(i)` | Supprimer et retourner à l'indice i | `lst.pop(0)` |
| `.sort()` | Trier en place | `lst.sort()` |
| `.reverse()` | Inverser en place | `lst.reverse()` |
| `.count(x)` | Compter les occurrences | `lst.count(5)` |
| `.index(x)` | Trouver l'indice | `lst.index(5)` |
| `.clear()` | Vider la liste | `lst.clear()` |
| `len(lst)` | Longueur | `len(lst)` |
| `x in lst` | Vérifier appartenance | `5 in lst` |

---

## 4. Dictionary — Les dictionnaires

### 📖 Définition

Un **dictionnaire** est une collection de paires **clé : valeur**. Chaque valeur est accessible via sa clé (comme un dictionnaire réel : le mot est la clé, la définition est la valeur).

> 💡 **Analogie** : Un dictionnaire Python, c'est comme un **annuaire téléphonique**. Vous cherchez un nom (clé) et vous trouvez le numéro (valeur). Vous n'avez pas besoin de parcourir tout l'annuaire — vous accédez directement à l'information via le nom.

### 4.1 Créer un dictionnaire

```python
# Dictionnaire vide
vide = {}
vide2 = dict()

# Dictionnaire d'un étudiant
etudiant = {
    "nom"     : "Alice Dupont",
    "age"     : 23,
    "note"    : 16.5,
    "actif"   : True,
    "cours"   : ["SQL", "Python", "ML"]
}

print(etudiant)
print(type(etudiant))  # <class 'dict'>
print(len(etudiant))   # 5 (nombre de paires clé:valeur)
```

### 4.2 Accéder aux valeurs

```python
etudiant = {
    "nom"  : "Alice",
    "age"  : 23,
    "ville": "Abidjan"
}

# Accès par clé (avec [])
print(etudiant["nom"])    # Alice
print(etudiant["age"])    # 23

# Accès avec .get() — plus sûr (pas d'erreur si la clé n'existe pas)
print(etudiant.get("ville"))        # Abidjan
print(etudiant.get("email"))        # None  (pas d'erreur !)
print(etudiant.get("email", "N/A")) # N/A   (valeur par défaut)

# ❌ Accès direct à une clé inexistante → erreur
# print(etudiant["email"])  # KeyError: 'email'
```

### 4.3 Parcourir un dictionnaire

```python
etudiant = {"nom": "Alice", "age": 23, "note": 16.5}

# Parcourir les clés (par défaut)
for cle in etudiant:
    print(cle)                        # nom, age, note

# Parcourir les valeurs
for valeur in etudiant.values():
    print(valeur)                     # Alice, 23, 16.5

# Parcourir les paires clé:valeur
for cle, valeur in etudiant.items():
    print(f"{cle} → {valeur}")
# nom → Alice
# age → 23
# note → 16.5
```

---

## 5. Dictionary Manipulation — Manipuler les dictionnaires

### 5.1 Ajouter et modifier des entrées

```python
etudiant = {"nom": "Alice", "age": 23}

# Ajouter une nouvelle clé
etudiant["email"] = "alice@email.com"
print(etudiant)
# {'nom': 'Alice', 'age': 23, 'email': 'alice@email.com'}

# Modifier une valeur existante
etudiant["age"] = 24
print(etudiant["age"])  # 24

# .update() — ajouter/modifier plusieurs clés à la fois
etudiant.update({
    "ville" : "Abidjan",
    "note"  : 17.5
})
print(etudiant)
```

### 5.2 Supprimer des entrées

```python
etudiant = {
    "nom"  : "Alice",
    "age"  : 23,
    "email": "alice@email.com",
    "ville": "Abidjan"
}

# del — supprimer une clé
del etudiant["ville"]
print(etudiant)

# .pop(clé) — supprimer et retourner la valeur
age = etudiant.pop("age")
print(f"Âge supprimé : {age}")   # 23
print(etudiant)

# .pop avec valeur par défaut (évite l'erreur si clé absente)
val = etudiant.pop("telephone", "Non renseigné")
print(val)  # Non renseigné

# .clear() — vider le dictionnaire
etudiant.clear()
print(etudiant)  # {}
```

### 5.3 Méthodes essentielles

```python
catalogue = {
    "Python": 45000,
    "SQL"   : 30000,
    "ML"    : 60000,
    "Stats" : 35000
}

# Obtenir toutes les clés
print(catalogue.keys())    # dict_keys(['Python', 'SQL', 'ML', 'Stats'])

# Obtenir toutes les valeurs
print(catalogue.values())  # dict_values([45000, 30000, 60000, 35000])

# Obtenir toutes les paires
print(catalogue.items())

# Vérifier l'existence d'une clé
print("Python" in catalogue)   # True
print("Java"   in catalogue)   # False

# Copier un dictionnaire
copie = catalogue.copy()
```

### 5.4 Dict Comprehension

```python
# Créer un dictionnaire avec une compréhension
carres = {x: x**2 for x in range(1, 6)}
print(carres)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrer un dictionnaire
catalogue = {"Python": 45000, "SQL": 30000, "ML": 60000, "Stats": 35000}
cours_chers = {k: v for k, v in catalogue.items() if v >= 40000}
print(cours_chers)  # {'Python': 45000, 'ML': 60000}

# Inverser clés et valeurs
inverse = {v: k for k, v in catalogue.items()}
print(inverse)  # {45000: 'Python', 30000: 'SQL', ...}
```

### 5.5 Tableau récapitulatif des méthodes de dictionnaire

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `d[clé]` | Accéder à une valeur | `d["nom"]` |
| `.get(clé, défaut)` | Accès sécurisé | `d.get("nom", "N/A")` |
| `.keys()` | Obtenir les clés | `d.keys()` |
| `.values()` | Obtenir les valeurs | `d.values()` |
| `.items()` | Obtenir paires clé:valeur | `d.items()` |
| `.update(d2)` | Fusionner/modifier | `d.update({"age": 25})` |
| `.pop(clé)` | Supprimer et retourner | `d.pop("age")` |
| `.copy()` | Copier | `d.copy()` |
| `.clear()` | Vider | `d.clear()` |
| `clé in d` | Vérifier existence | `"nom" in d` |

---

## 6. Sets — Les ensembles

### 📖 Définition

Un **set** (ensemble) est une collection **non ordonnée** d'éléments **uniques**. Il est inspiré de la notion mathématique d'ensemble — chaque valeur n'y apparaît qu'une seule fois.

> 💡 **Analogie** : Un set, c'est comme une **boîte de timbres de collection** — vous ne gardez qu'un seul exemplaire de chaque timbre. Si vous essayez d'en ajouter un en double, il est automatiquement ignoré.

### 6.1 Créer un set

```python
# Set vide (ATTENTION : {} crée un dict, pas un set !)
set_vide = set()

# Set de valeurs
langages = {"Python", "SQL", "R", "Python", "SQL"}
print(langages)  # {'Python', 'SQL', 'R'} — doublons supprimés !

# Créer un set depuis une liste (pour supprimer les doublons)
notes = [14, 16, 14, 18, 16, 12, 14]
notes_uniques = set(notes)
print(notes_uniques)  # {12, 14, 16, 18}

print(type(langages))  # <class 'set'>
print(len(langages))   # 3
```

### 6.2 Ajouter et supprimer

```python
langages = {"Python", "SQL", "R"}

# .add() — ajouter un élément
langages.add("Julia")
print(langages)  # {'Python', 'SQL', 'R', 'Julia'}

# Ajouter un doublon → ignoré silencieusement
langages.add("Python")
print(langages)  # Toujours {'Python', 'SQL', 'R', 'Julia'}

# .remove() — supprimer (erreur si absent)
langages.remove("R")
print(langages)

# .discard() — supprimer sans erreur si absent
langages.discard("Java")  # Pas d'erreur même si "Java" n'existe pas
```

### 6.3 Opérations ensemblistes

C'est là que les sets deviennent très puissants — opérations mathématiques directement disponibles.

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union — tous les éléments des deux sets
print(A | B)            # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))       # Même résultat

# Intersection — éléments communs aux deux
print(A & B)            # {4, 5}
print(A.intersection(B))

# Différence — éléments dans A mais pas dans B
print(A - B)            # {1, 2, 3}
print(A.difference(B))

# Différence symétrique — éléments dans l'un OU l'autre, mais pas les deux
print(A ^ B)                    # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))
```

**Visualisation :**
```
A = {1, 2, 3, 4, 5}      B = {4, 5, 6, 7, 8}

    ┌────────────────────────────────┐
    │  A              │      B       │
    │  {1, 2, 3}   {4, 5}  {6, 7, 8}│
    │  (A - B)    (A ∩ B)   (B - A) │
    └────────────────────────────────┘

A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8}
A ∩ B = {4, 5}
A - B = {1, 2, 3}
B - A = {6, 7, 8}
```

### 6.4 Cas d'usage typique — Supprimer les doublons

```python
# Supprimer les doublons d'une liste en passant par un set
villes = ["Abidjan", "Dakar", "Abidjan", "Accra", "Dakar", "Lagos"]
villes_uniques = list(set(villes))
print(villes_uniques)  # ['Dakar', 'Lagos', 'Abidjan', 'Accra'] (ordre aléatoire)

# Comparer deux listes
inscrits_sql    = {"Alice", "Bob", "Claire", "David"}
inscrits_python = {"Bob", "David", "Emma", "Fatou"}

# Qui suit les deux cours ?
print(inscrits_sql & inscrits_python)   # {'Bob', 'David'}

# Qui suit au moins un cours ?
print(inscrits_sql | inscrits_python)   # Tout le monde

# Qui suit SQL mais pas Python ?
print(inscrits_sql - inscrits_python)   # {'Alice', 'Claire'}
```

---

## 7. Tuple — Les tuples

### 📖 Définition

Un **tuple** est une collection **ordonnée** et **immuable** (non modifiable). Une fois créé, un tuple ne peut plus être modifié — on ne peut ni ajouter, ni supprimer, ni changer ses éléments.

> 💡 **Analogie** : Un tuple, c'est comme une **date de naissance gravée sur un document officiel**. Une fois inscrite, elle ne peut plus changer. C'est son caractère permanent et fiable qui le rend utile.

### 7.1 Créer un tuple

```python
# Avec parenthèses
coordonnees = (48.8566, 2.3522)    # Latitude, longitude de Paris
rgb_rouge   = (255, 0, 0)          # Couleur rouge en RGB
jours       = ("Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim")

# Sans parenthèses (Python détecte le tuple grâce aux virgules)
point = 3, 5
print(point)       # (3, 5)
print(type(point)) # <class 'tuple'>

# Tuple d'un seul élément (virgule obligatoire !)
singleton = (42,)         # ✅ Tuple
pas_tuple  = (42)         # ❌ Juste un entier entre parenthèses
print(type(singleton))    # <class 'tuple'>
print(type(pas_tuple))    # <class 'int'>
```

### 7.2 Accéder aux éléments

```python
couleurs = ("rouge", "vert", "bleu", "jaune")

# Comme une liste — indexation et slicing
print(couleurs[0])      # rouge
print(couleurs[-1])     # jaune
print(couleurs[1:3])    # ('vert', 'bleu')

# Longueur
print(len(couleurs))    # 4

# Appartenance
print("vert" in couleurs)   # True
print("orange" in couleurs) # False
```

### 7.3 Immuabilité — Le tuple ne peut pas être modifié

```python
point = (3, 5)

# ❌ Tentative de modification → TypeError
# point[0] = 10       # TypeError: 'tuple' object does not support item assignment
# point.append(7)     # AttributeError: 'tuple' object has no attribute 'append'

# ✅ On peut créer un NOUVEAU tuple
nouveau_point = point + (7,)
print(nouveau_point)  # (3, 5, 7)
```

### 7.4 Déballage de tuple (Tuple Unpacking)

```python
# Assigner les valeurs d'un tuple à des variables séparées
coordonnees = (5.345, -4.008)   # Abidjan
latitude, longitude = coordonnees
print(f"Latitude  : {latitude}")   # 5.345
print(f"Longitude : {longitude}")  # -4.008

# Retourner plusieurs valeurs depuis une fonction
def min_max(liste):
    return min(liste), max(liste)   # Retourne un tuple

notes = [14, 18, 12, 16, 10]
minimum, maximum = min_max(notes)
print(f"Min : {minimum}, Max : {maximum}")  # Min : 10, Max : 18

# Ignorer certaines valeurs avec _
premier, _, troisieme = (10, 20, 30)
print(premier)   # 10
print(troisieme) # 30
```

### 7.5 Quand utiliser un tuple plutôt qu'une liste ?

```python
# ✅ Tuple — données qui ne doivent PAS changer
COULEURS_RVB = {
    "rouge" : (255, 0, 0),
    "vert"  : (0, 255, 0),
    "bleu"  : (0, 0, 255)
}

JOURS_SEMAINE = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi")
COORDONNEES_ABIDJAN = (5.345, -4.008)

# ✅ Liste — données qui peuvent changer
etudiants = ["Alice", "Bob"]  # On ajoutera des étudiants
etudiants.append("Claire")
```

---

## 8. Nested Structures — Structures imbriquées

Les structures de données peuvent être **imbriquées** les unes dans les autres pour représenter des données complexes.

### 8.1 Liste de dictionnaires

Le cas le plus courant en Data Science — représente un **tableau de données** :

```python
# Chaque dictionnaire = une ligne du tableau
etudiants = [
    {"nom": "Alice",  "age": 23, "note": 16.5, "ville": "Abidjan"},
    {"nom": "Bob",    "age": 25, "note": 14.0, "ville": "Dakar"},
    {"nom": "Claire", "age": 22, "note": 18.0, "ville": "Accra"},
    {"nom": "David",  "age": 28, "note": 12.5, "ville": "Lagos"},
]

# Accéder à un étudiant
print(etudiants[0])              # Toute la ligne Alice
print(etudiants[0]["nom"])       # Alice
print(etudiants[2]["note"])      # 18.0

# Parcourir tous les étudiants
for e in etudiants:
    print(f"{e['nom']} ({e['ville']}) — note : {e['note']}/20")

# Calculer la moyenne des notes
notes  = [e["note"] for e in etudiants]
moyenne = sum(notes) / len(notes)
print(f"\nMoyenne : {moyenne}")  # 15.25

# Filtrer les étudiants avec note >= 15
bons = [e["nom"] for e in etudiants if e["note"] >= 15]
print(f"Notes ≥ 15 : {bons}")   # ['Alice', 'Claire']
```

### 8.2 Dictionnaire de listes

```python
# Données groupées par catégorie
resultats_par_cours = {
    "SQL"   : [14, 16, 12, 18, 15],
    "Python": [16, 18, 14, 20, 17],
    "ML"    : [12, 14, 10, 16, 13]
}

# Accéder aux notes d'un cours
print(resultats_par_cours["Python"])      # [16, 18, 14, 20, 17]
print(resultats_par_cours["SQL"][2])      # 12

# Calculer la moyenne de chaque cours
for cours, notes in resultats_par_cours.items():
    moy = sum(notes) / len(notes)
    print(f"{cours} — Moyenne : {moy:.1f}/20")
```

### 8.3 Matrice avec liste de listes

```python
# Matrice 3x3 (similaire au checkpoint Maths !)
D = [
    [4,  8,  12],
    [6,  10, 15],
    [5,  7,  9],
    [3,  6,  9]
]

# Accéder à un élément [ligne][colonne]
print(D[0][0])   # 4   (ligne 0, colonne 0)
print(D[1][2])   # 15  (ligne 1, colonne 2)

# Afficher la matrice proprement
for i, ligne in enumerate(D):
    print(f"Région {i+1} : {ligne}")

# Calculer la somme de chaque colonne (produit A, B, C)
nb_colonnes = len(D[0])
for j in range(nb_colonnes):
    total = sum(D[i][j] for i in range(len(D)))
    print(f"Colonne {j} — Total : {total}")
```

---

## 9. Choisir la bonne structure

### 9.1 Guide de décision

```
Je veux stocker des données...
│
├── dans un ORDRE précis et les MODIFIER ?
│       → list [ ]
│
├── avec des ÉTIQUETTES (clé:valeur) ?
│       → dict { }
│
├── en évitant les DOUBLONS ?
│       → set { }
│
└── qui NE DOIVENT PAS CHANGER ?
        → tuple ( )
```

### 9.2 Exemples de cas d'usage

| Situation | Structure recommandée | Exemple |
|-----------|-----------------------|---------|
| Liste de notes d'étudiants | `list` | `[14, 16, 18, 12]` |
| Fiche d'un étudiant | `dict` | `{"nom": "Alice", "age": 23}` |
| Tags d'un article (uniques) | `set` | `{"python", "data", "ia"}` |
| Coordonnées GPS | `tuple` | `(5.345, -4.008)` |
| Tableau de données | `list` de `dict` | `[{"nom": "Alice", "note": 16}]` |
| Notes par cours | `dict` de `list` | `{"SQL": [14, 16], "Python": [18]}` |
| Jours de la semaine | `tuple` | `("Lun", "Mar", ...)` |

### 9.3 Conversion entre structures

```python
# list → set (supprimer les doublons)
liste  = [1, 2, 2, 3, 3, 4]
en_set = set(liste)
print(en_set)   # {1, 2, 3, 4}

# set → list (pour retrouver l'indexation)
en_liste = list(en_set)
print(en_liste) # [1, 2, 3, 4]

# list → tuple (rendre immuable)
en_tuple = tuple(liste)
print(en_tuple) # (1, 2, 2, 3, 3, 4)

# tuple → list (rendre modifiable)
t = (10, 20, 30)
l = list(t)
l.append(40)
print(l)  # [10, 20, 30, 40]

# dict → list de clés / de valeurs
d = {"a": 1, "b": 2, "c": 3}
print(list(d.keys()))    # ['a', 'b', 'c']
print(list(d.values()))  # [1, 2, 3]
print(list(d.items()))   # [('a', 1), ('b', 2), ('c', 3)]
```

---

## 10. Conclusion

### 📌 Récapitulatif du chapitre

```
DATA STRUCTURES IN PYTHON
│
├── list [ ]
│   ├── Ordonnée, modifiable, doublons autorisés
│   ├── Accès par indice [0], slicing [1:3]
│   └── Méthodes : append, insert, remove, pop, sort, reverse
│
├── dict { }
│   ├── Paires clé:valeur, ordonnée (Python 3.7+), modifiable
│   ├── Accès par clé ["nom"] ou .get("nom")
│   └── Méthodes : keys, values, items, update, pop
│
├── set { }
│   ├── Non ordonnée, unique, modifiable
│   ├── Opérations : union |, intersection &, différence -
│   └── Idéal pour supprimer des doublons
│
└── tuple ( )
    ├── Ordonnée, IMMUABLE
    ├── Accès par indice, déballage (unpacking)
    └── Idéal pour des données constantes
```

### 🔑 Points clés à retenir

1. **`list`** pour les collections ordonnées et modifiables — la plus polyvalente.
2. **`dict`** pour les données avec des étiquettes (clé:valeur) — clé d'accès rapide.
3. **`set`** pour garantir l'unicité et faire des opérations ensemblistes.
4. **`tuple`** pour les données constantes et fiables — plus rapide qu'une liste.
5. Les **structures imbriquées** (`list` de `dict`, `dict` de `list`) sont la base des tableaux de données — fondement de Pandas en Data Science.
6. La **list comprehension** est la façon pythonique de créer/filtrer des listes en une ligne.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons les **fonctions Python** : comment créer des fonctions réutilisables (`def`), les paramètres, les valeurs de retour, les fonctions lambda et les notions de portée des variables — des outils indispensables pour structurer votre code de Data Science.

---

## 11. ✅ Point de contrôle — Data Structures

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre une `list` et un `tuple` ?

<details>
<summary>👀 Voir la réponse</summary>

> Une `list` est **modifiable** (on peut ajouter, supprimer, modifier des éléments) et se définit avec `[]`. Un `tuple` est **immuable** (ses éléments ne peuvent pas changer après création) et se définit avec `()`. On utilise un tuple pour des données qui ne doivent pas changer (coordonnées GPS, jours de la semaine), et une liste pour des collections dynamiques.
</details>

---

**Q2.** Pourquoi utilise-t-on `set()` pour créer un ensemble vide plutôt que `{}` ?

<details>
<summary>👀 Voir la réponse</summary>

> `{}` crée un **dictionnaire vide** en Python, pas un ensemble. Pour créer un ensemble vide, il faut obligatoirement utiliser `set()`. C'est un piège classique : `type({})` retourne `<class 'dict'>`, tandis que `type(set())` retourne `<class 'set'>`.
</details>

---

**Q3.** Quelle est la différence entre `.remove()` et `.discard()` dans un set ?

<details>
<summary>👀 Voir la réponse</summary>

> `.remove(x)` supprime l'élément `x` mais lève une erreur `KeyError` si `x` n'existe pas dans le set. `.discard(x)` supprime `x` **sans générer d'erreur** si `x` est absent. En pratique, `.discard()` est plus sûr quand on n'est pas certain que l'élément existe.
</details>

---

**Q4.** Quelle est la différence entre `d["clé"]` et `d.get("clé")` pour un dictionnaire ?

<details>
<summary>👀 Voir la réponse</summary>

> `d["clé"]` lève une `KeyError` si la clé n'existe pas dans le dictionnaire. `d.get("clé")` retourne `None` (ou une valeur par défaut que l'on peut spécifier : `d.get("clé", "valeur_défaut")`). `get()` est préférable quand on n'est pas certain que la clé existe.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Listes**

Créez une liste `notes` contenant : `[12, 18, 15, 9, 14, 16, 11, 18]`

a) Affichez la première et la dernière note.
b) Affichez les 3 premières notes.
c) Triez la liste par ordre décroissant.
d) Calculez la moyenne.
e) Affichez uniquement les notes supérieures à 13.

<details>
<summary>👀 Voir la solution</summary>

```python
notes = [12, 18, 15, 9, 14, 16, 11, 18]

# a)
print(notes[0], notes[-1])        # 12  18

# b)
print(notes[:3])                  # [12, 18, 15]

# c)
notes.sort(reverse=True)
print(notes)                      # [18, 18, 16, 15, 14, 12, 11, 9]

# d)
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne:.2f}") # 14.13

# e)
sup_13 = [n for n in notes if n > 13]
print(sup_13)                     # [18, 18, 16, 15, 14]
```
</details>

---

**Exercice 2 — Dictionnaires**

Créez un dictionnaire représentant un étudiant avec les clés : `nom`, `age`, `ville`, `note`.

a) Affichez la note de l'étudiant.
b) Ajoutez une clé `email`.
c) Modifiez l'âge.
d) Affichez toutes les paires clé:valeur avec une boucle.
e) Vérifiez si la clé `"telephone"` existe dans le dictionnaire.

<details>
<summary>👀 Voir la solution</summary>

```python
etudiant = {
    "nom"  : "Fatou Diallo",
    "age"  : 22,
    "ville": "Abidjan",
    "note" : 17.5
}

# a)
print(etudiant["note"])           # 17.5

# b)
etudiant["email"] = "fatou@email.com"

# c)
etudiant["age"] = 23

# d)
for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")

# e)
print("telephone" in etudiant)    # False
```
</details>

---

**Exercice 3 — Sets**

a) Créez un set avec les valeurs `[1, 2, 3, 2, 4, 1, 5]` et affichez-le.
b) Soient A = `{1, 2, 3, 4, 5}` et B = `{4, 5, 6, 7}`. Calculez : union, intersection, différence A-B.
c) Supprimez les doublons de la liste `villes = ["Abidjan", "Dakar", "Abidjan", "Accra", "Dakar"]`.

<details>
<summary>👀 Voir la solution</summary>

```python
# a)
s = set([1, 2, 3, 2, 4, 1, 5])
print(s)   # {1, 2, 3, 4, 5}

# b)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A | B)   # {1, 2, 3, 4, 5, 6, 7}
print(A & B)   # {4, 5}
print(A - B)   # {1, 2, 3}

# c)
villes = ["Abidjan", "Dakar", "Abidjan", "Accra", "Dakar"]
villes_uniques = list(set(villes))
print(villes_uniques)
```
</details>

---

**Exercice 4 — Tuples**

a) Créez un tuple `rgb_vert = (0, 255, 0)` et affichez chaque composante avec le déballage.
b) Essayez de modifier la première valeur du tuple. Que se passe-t-il ?
c) Créez une liste de tuples `[(nom, note)]` pour 3 étudiants et affichez-les avec une boucle.

<details>
<summary>👀 Voir la solution</summary>

```python
# a)
rgb_vert = (0, 255, 0)
r, g, b = rgb_vert
print(f"Rouge: {r}, Vert: {g}, Bleu: {b}")

# b)
# rgb_vert[0] = 10  → TypeError: 'tuple' object does not support item assignment

# c)
etudiants = [("Alice", 16), ("Bob", 14), ("Claire", 18)]
for nom, note in etudiants:
    print(f"{nom} : {note}/20")
```
</details>

---

**Exercice 5 — Structure imbriquée**

Créez une liste de dictionnaires pour 4 étudiants (nom, note, ville).

a) Affichez le nom de l'étudiant avec la meilleure note.
b) Calculez la moyenne des notes.
c) Filtrez et affichez uniquement les étudiants avec une note ≥ 15.

<details>
<summary>👀 Voir la solution</summary>

```python
etudiants = [
    {"nom": "Alice",  "note": 16.5, "ville": "Abidjan"},
    {"nom": "Bob",    "note": 13.0, "ville": "Dakar"},
    {"nom": "Claire", "note": 18.5, "ville": "Accra"},
    {"nom": "David",  "note": 14.0, "ville": "Lagos"},
]

# a)
meilleur = max(etudiants, key=lambda e: e["note"])
print(f"Meilleur : {meilleur['nom']} ({meilleur['note']})")

# b)
notes   = [e["note"] for e in etudiants]
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne:.2f}")

# c)
bons = [e for e in etudiants if e["note"] >= 15]
for e in bons:
    print(f"{e['nom']} — {e['note']}/20")
```
</details>

---

### 🏆 Challenge bonus

Vous gérez les données d'un **bootcamp data science** avec les informations suivantes :

```python
bootcamp = {
    "nom"      : "DataTech Bootcamp",
    "ville"    : "Abidjan",
    "modules"  : ["SQL", "Python", "Machine Learning", "Visualisation"],
    "etudiants": [
        {"nom": "Fatou",   "note_sql": 16, "note_python": 18},
        {"nom": "Kofi",    "note_sql": 14, "note_python": 15},
        {"nom": "Aminata", "note_sql": 18, "note_python": 17},
        {"nom": "Moussa",  "note_sql": 12, "note_python": 13},
    ]
}
```

Écrivez un programme qui :
1. Affiche le nombre de modules et d'étudiants
2. Calcule la moyenne SQL et la moyenne Python de toute la promotion
3. Affiche l'étudiant avec la meilleure moyenne générale (SQL + Python) / 2
4. Crée un nouveau dictionnaire `resultats` avec pour chaque étudiant son nom et sa moyenne générale

<details>
<summary>👀 Voir la solution</summary>

```python
bootcamp = {
    "nom"      : "DataTech Bootcamp",
    "ville"    : "Abidjan",
    "modules"  : ["SQL", "Python", "Machine Learning", "Visualisation"],
    "etudiants": [
        {"nom": "Fatou",   "note_sql": 16, "note_python": 18},
        {"nom": "Kofi",    "note_sql": 14, "note_python": 15},
        {"nom": "Aminata", "note_sql": 18, "note_python": 17},
        {"nom": "Moussa",  "note_sql": 12, "note_python": 13},
    ]
}

etudiants = bootcamp["etudiants"]

# 1. Nombre de modules et d'étudiants
print(f"Modules   : {len(bootcamp['modules'])}")
print(f"Étudiants : {len(etudiants)}")

# 2. Moyennes SQL et Python de la promotion
moy_sql    = sum(e["note_sql"]    for e in etudiants) / len(etudiants)
moy_python = sum(e["note_python"] for e in etudiants) / len(etudiants)
print(f"Moyenne SQL    : {moy_sql:.1f}")
print(f"Moyenne Python : {moy_python:.1f}")

# 3. Meilleur étudiant
meilleur = max(etudiants,
    key=lambda e: (e["note_sql"] + e["note_python"]) / 2)
moy_meilleur = (meilleur["note_sql"] + meilleur["note_python"]) / 2
print(f"Meilleur : {meilleur['nom']} — moyenne {moy_meilleur:.1f}/20")

# 4. Dictionnaire des résultats
resultats = {
    e["nom"]: round((e["note_sql"] + e["note_python"]) / 2, 1)
    for e in etudiants
}
print(resultats)
# {'Fatou': 17.0, 'Kofi': 14.5, 'Aminata': 17.5, 'Moussa': 12.5}
```
</details>

---

*📘 Fin du Chapitre 3 — Data Structures in Python | Bootcamp Data Science*
