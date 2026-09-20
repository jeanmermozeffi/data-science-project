# 🐍 Bases de Python — Cours Bootcamp Data Science

> **Chapitre 2** | Prérequis : Chapitre 1 — Introduction à Python

---

## Table des matières

1. [Syntaxe Python — Vue d'ensemble](#1-syntaxe-python--vue-densemble)
2. [Variables et constantes](#2-variables-et-constantes)
3. [Attribution et réattribution](#3-attribution-et-réattribution-dune-valeur)
4. [Opérateurs arithmétiques](#4-opérateurs-arithmétiques-python)
5. [Opérateurs de comparaison](#5-opérateurs-de-comparaison-python)
6. [Types de données Python](#6-types-de-données-python)
7. [Chaînes de caractères](#7-chaînes-de-caractères-python)
8. [Opérations sur les chaînes](#8-opérations-sur-les-chaînes-de-caractères)
9. [Booléens Python](#9-booléens-python)
10. [Conversion de type](#10-conversion-de-type)
11. [Condition if](#11-condition-if-en-python)
12. [Condition if/else](#12-condition-ifelse)
13. [Condition if/elif/else](#13-condition-ifelifelse)
14. [Boucle For](#14-boucle-for-en-python)
15. [Boucle While](#15-boucle-while-en-python)
16. [Conclusion](#16-conclusion)
17. [✅ Point de contrôle — Bases de Python](#17--point-de-contrôle--bases-de-python)

---

## 1. Syntaxe Python — Vue d'ensemble

### 📖 Rappel des règles fondamentales

Avant de plonger dans les détails, voici les règles de base à toujours garder en tête quand on écrit du Python.

```
RÈGLES DE SYNTAXE PYTHON
│
├── 🔵 Indentation obligatoire  → remplace les { } des autres langages
├── 🔵 Sensible à la casse      → `age` ≠ `Age` ≠ `AGE`
├── 🔵 Pas de point-virgule     → chaque instruction sur sa propre ligne
├── 🔵 Commentaires avec #      → tout ce qui suit # est ignoré
└── 🔵 Pas de déclaration type  → Python détecte le type automatiquement
```

```python
# Ceci est un commentaire — Python l'ignore complètement

# ✅ Bonne syntaxe
prenom = "Alice"
print(prenom)

# ✅ Sensibilité à la casse
age = 25
Age = 30
print(age)  # Affiche 25
print(Age)  # Affiche 30 — c'est une variable DIFFÉRENTE !

# ✅ Indentation (bloc de code décalé de 4 espaces)
if age > 18:
    print("Majeur")   # ← indenté = appartient au if
print("Fin")          # ← non indenté = hors du if
```

---

## 2. Variables et constantes

### 📖 Qu'est-ce qu'une variable ?

Une **variable** est une **boîte étiquetée** qui stocke une valeur en mémoire. On lui donne un nom, et on peut lire ou modifier son contenu à tout moment.

> 💡 **Analogie** : Une variable, c'est comme une boîte de rangement avec une étiquette. Vous écrivez "âge" sur l'étiquette, et vous mettez le chiffre 25 à l'intérieur. Plus tard, vous pouvez ouvrir la boîte, lire la valeur ou la remplacer.

### 2.1 Créer une variable

```python
# Syntaxe : nom_variable = valeur
prenom  = "Alice"
age     = 25
note    = 17.5
actif   = True
```

### 2.2 Règles de nommage des variables

| Règle | ✅ Correct | ❌ Incorrect |
|-------|-----------|-------------|
| Commence par une lettre ou `_` | `nom`, `_age` | `1nom`, `@email` |
| Lettres, chiffres, underscores | `note_finale`, `etudiant2` | `note-finale`, `etudiant 2` |
| Sensible à la casse | `age` ≠ `Age` | — |
| Pas de mot réservé Python | `valeur` | `if`, `for`, `class` |

```python
# ✅ Noms valides
nom_etudiant  = "Kofi"
age2          = 22
_score        = 18.5
noteFinale    = 16      # style camelCase (peu usité en Python)
note_finale   = 16      # style snake_case (recommandé en Python ✅)

# ❌ Noms invalides
# 2note = 10       → commence par un chiffre
# note-finale = 10 → tiret interdit
# if = 5           → mot réservé Python
```

> 💡 **Convention Python (PEP 8)** : Utilisez le **snake_case** pour les variables (mots séparés par des underscores) : `nom_etudiant`, `note_finale`, `age_moyen`.

### 2.3 Constantes

Python n'a pas de mot-clé `const` comme d'autres langages. Par **convention**, une constante est une variable écrite entièrement en **MAJUSCULES** — c'est un signal aux autres développeurs de ne pas la modifier.

```python
# Constantes (convention MAJUSCULES)
PI              = 3.14159
TVA             = 0.18        # Taux de TVA en Côte d'Ivoire (18%)
NB_MAX_ETUDIANTS = 30
ANNEE_CREATION  = 2024

# Ces valeurs ne devraient pas changer dans le programme
rayon = 5
aire = PI * rayon ** 2
print(f"Aire du cercle : {aire:.2f}")  # Affiche : Aire du cercle : 78.54
```

---

## 3. Attribution et Réattribution d'une valeur

### 3.1 Attribution simple

```python
# Créer une variable et lui assigner une valeur
ville = "Abidjan"
print(ville)  # Abidjan
```

### 3.2 Réattribution — Changer la valeur

```python
# Réaffecter une nouvelle valeur à une variable existante
score = 10
print(score)  # 10

score = 20    # Réattribution
print(score)  # 20

score = "Excellent"  # En Python, on peut même changer le type !
print(score)         # Excellent
```

### 3.3 Attribution multiple

```python
# Assigner la même valeur à plusieurs variables
a = b = c = 0
print(a, b, c)  # 0 0 0

# Assigner des valeurs différentes sur une seule ligne
x, y, z = 10, 20, 30
print(x)  # 10
print(y)  # 20
print(z)  # 30

# Échanger deux variables (très élégant en Python !)
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5
```

### 3.4 Attribution augmentée

Ces opérateurs combinent une opération et une réattribution en une seule instruction.

```python
compteur = 0

compteur += 5    # équivaut à : compteur = compteur + 5
print(compteur)  # 5

compteur -= 2    # équivaut à : compteur = compteur - 2
print(compteur)  # 3

compteur *= 4    # équivaut à : compteur = compteur * 4
print(compteur)  # 12

compteur //= 3   # équivaut à : compteur = compteur // 3
print(compteur)  # 4
```

---

## 4. Opérateurs arithmétiques Python

### 4.1 Tableau des opérateurs

| Opérateur | Nom | Exemple | Résultat |
|-----------|-----|---------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division réelle | `5 / 2` | `2.5` |
| `//` | Division entière | `5 // 2` | `2` |
| `%` | Modulo (reste) | `5 % 2` | `1` |
| `**` | Puissance | `5 ** 2` | `25` |

### 4.2 Exemples concrets

```python
a = 17
b = 5

print(f"Addition       : {a} + {b} = {a + b}")   # 22
print(f"Soustraction   : {a} - {b} = {a - b}")   # 12
print(f"Multiplication : {a} * {b} = {a * b}")   # 85
print(f"Division réelle: {a} / {b} = {a / b}")   # 3.4
print(f"Division entière:{a} //{b} = {a // b}")  # 3
print(f"Modulo         : {a} % {b} = {a % b}")   # 2
print(f"Puissance      : {a} ** 2 = {a ** 2}")   # 289
```

### 4.3 Priorité des opérations

Python respecte les règles mathématiques classiques — **PEMDAS** (Parenthèses, Exposants, Multiplication/Division, Addition/Soustraction) :

```python
# Sans parenthèses
résultat = 2 + 3 * 4
print(résultat)  # 14 (pas 20 !) — la multiplication passe avant l'addition

# Avec parenthèses
résultat = (2 + 3) * 4
print(résultat)  # 20 ✅

# Exemple complexe
résultat = 2 ** 3 + 10 / 2 - 1
print(résultat)  # 12.0
# Calcul : (2**3) + (10/2) - 1 = 8 + 5.0 - 1 = 12.0
```

### 4.4 Application — Calcul d'une note finale

```python
# Calcul d'une note finale pondérée
note_examen  = 16
note_projet  = 18
note_partiel = 14

# Pondération : examen 50%, projet 30%, partiel 20%
note_finale = (note_examen * 0.5) + (note_projet * 0.3) + (note_partiel * 0.2)
print(f"Note finale : {note_finale}")  # 16.2
```

---

## 5. Opérateurs de comparaison Python

Les opérateurs de comparaison comparent deux valeurs et retournent **toujours** `True` ou `False`.

### 5.1 Tableau des opérateurs

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `==` | Égal à | `5 == 5` | `True` |
| `!=` | Différent de | `5 != 3` | `True` |
| `>` | Supérieur à | `5 > 3` | `True` |
| `<` | Inférieur à | `5 < 3` | `False` |
| `>=` | Supérieur ou égal | `5 >= 5` | `True` |
| `<=` | Inférieur ou égal | `3 <= 5` | `True` |

### 5.2 Exemples

```python
age = 20

print(age == 20)   # True  — age est bien égal à 20
print(age != 18)   # True  — age est différent de 18
print(age > 18)    # True  — age est supérieur à 18
print(age < 18)    # False — age n'est pas inférieur à 18
print(age >= 20)   # True  — age est supérieur ou égal à 20
print(age <= 19)   # False — age n'est pas inférieur ou égal à 19
```

### 5.3 ⚠️ `=` vs `==` — L'erreur classique

```python
# ❌ Erreur classique des débutants
age = 20      # ← ATTRIBUTION (donne une valeur)
age == 20     # ← COMPARAISON (pose une question : est-ce égal ?)

# Exemple d'erreur
if age = 20:  # SyntaxError ! On ne peut pas utiliser = dans un if
    print("Majeur")

# ✅ Correct
if age == 20:  # On compare avec ==
    print("A exactement 20 ans")
```

### 5.4 Opérateurs logiques — AND, OR, NOT

Combiner plusieurs comparaisons :

```python
age   = 22
note  = 15

# AND : les DEUX conditions doivent être vraies
print(age > 18 and note >= 14)   # True AND True  → True
print(age > 18 and note >= 18)   # True AND False → False

# OR : AU MOINS UNE condition doit être vraie
print(age > 25 or note >= 14)    # False OR True  → True
print(age > 25 or note >= 18)    # False OR False → False

# NOT : inverse la condition
print(not age > 30)              # not False → True
print(not age > 18)              # not True  → False
```

---

## 6. Types de données Python

Python dispose de plusieurs types de données fondamentaux.

### 6.1 Vue d'ensemble

```
TYPES DE DONNÉES PYTHON
│
├── int      → Entiers             : 10, -5, 0, 1000
├── float    → Décimaux            : 3.14, -0.5, 2.0
├── str      → Chaînes de texte    : "Alice", 'Bonjour'
├── bool     → Booléens            : True, False
├── list     → Listes              : [1, 2, 3]
├── tuple    → Tuples (immuables)  : (1, 2, 3)
├── dict     → Dictionnaires       : {"nom": "Alice"}
└── NoneType → Absence de valeur   : None
```

### 6.2 int — Entiers

```python
# Entiers positifs et négatifs
nb_etudiants = 30
temperature  = -5
zero         = 0

print(type(nb_etudiants))  # <class 'int'>
print(type(temperature))   # <class 'int'>

# Opérations sur les entiers
print(10 + 3)   # 13
print(10 // 3)  # 3  (division entière)
print(10 % 3)   # 1  (reste)
```

### 6.3 float — Décimaux

```python
# Nombres à virgule flottante
pi      = 3.14159
taux    = 0.18
note    = 15.75

print(type(pi))  # <class 'float'>

# Arrondir un float
print(round(3.14159, 2))  # 3.14
print(round(15.756, 1))   # 15.8
```

### 6.4 Vérifier le type — `type()`

```python
# La fonction type() révèle le type d'une variable
print(type(10))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Alice"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
```

### 6.5 None — L'absence de valeur

```python
# None représente l'absence de valeur (≠ 0, ≠ "")
resultat = None

print(resultat)         # None
print(type(resultat))   # <class 'NoneType'>

# Vérifier si une variable est None
if resultat is None:
    print("Pas encore de résultat")  # Affiche ceci
```

---

## 7. Chaînes de caractères Python

### 📖 Définition

Une **chaîne de caractères** (`str`) est une séquence de caractères entourée de guillemets simples `' '` ou doubles `" "`.

> 💡 **Analogie** : Une chaîne, c'est comme un **collier de perles** — chaque perle est un caractère, et l'ensemble forme un mot, une phrase ou un texte.

### 7.1 Créer une chaîne

```python
# Guillemets simples ou doubles — les deux fonctionnent
prenom  = 'Alice'
ville   = "Abidjan"

# Chaîne sur plusieurs lignes (triple guillemets)
message = """Bonjour,
Je m'appelle Alice
et j'habite à Abidjan."""
print(message)

# Guillemets à l'intérieur d'une chaîne
phrase1 = "J'aime Python"          # guillemet simple à l'intérieur
phrase2 = 'Il dit "Bonjour"'       # guillemet double à l'intérieur
print(phrase1)  # J'aime Python
print(phrase2)  # Il dit "Bonjour"
```

### 7.2 Indexation — Accéder à un caractère

Chaque caractère d'une chaîne a un **indice** (position), qui commence à **0**.

```
  A  l  i  c  e
  0  1  2  3  4     ← indices positifs
 -5 -4 -3 -2 -1     ← indices négatifs (depuis la fin)
```

```python
mot = "Alice"

print(mot[0])    # A  (premier caractère)
print(mot[1])    # l
print(mot[4])    # e  (dernier caractère)
print(mot[-1])   # e  (dernier, en partant de la fin)
print(mot[-2])   # c
```

### 7.3 Slicing — Extraire une sous-chaîne

```python
# Syntaxe : chaine[debut:fin:pas]
# fin est EXCLU
texte = "DataScience"
#         0123456789 10

print(texte[0:4])    # Data   (indices 0, 1, 2, 3)
print(texte[4:])     # Science (du 4ème jusqu'à la fin)
print(texte[:4])     # Data   (du début jusqu'au 4ème exclu)
print(texte[::2])    # DtSine (un caractère sur deux)
print(texte[::-1])   # ecneicSataD (chaîne inversée !)
```

### 7.4 Longueur d'une chaîne — `len()`

```python
mot = "Python"
print(len(mot))     # 6

phrase = "Bonjour tout le monde"
print(len(phrase))  # 21 (espaces comptés)
```

---

## 8. Opérations sur les chaînes de caractères

### 8.1 Concaténation — Assembler des chaînes

```python
prenom = "Alice"
nom    = "Dupont"

# Avec l'opérateur +
nom_complet = prenom + " " + nom
print(nom_complet)  # Alice Dupont

# Répétition avec *
trait = "-" * 20
print(trait)  # --------------------
```

### 8.2 F-strings — Formatage moderne (recommandé)

```python
prenom  = "Alice"
age     = 23
note    = 16.75

# F-string : préfixe f avant les guillemets
print(f"Bonjour, je m'appelle {prenom} !")
print(f"J'ai {age} ans et ma note est {note}/20.")
print(f"Ma note arrondie : {note:.1f}")   # 16.8
print(f"Mon âge dans 5 ans : {age + 5}") # 28

# Calculs directement dans le f-string
a, b = 10, 3
print(f"{a} ÷ {b} = {a/b:.2f}")  # 10 ÷ 3 = 3.33
```

### 8.3 Méthodes essentielles des chaînes

```python
texte = "  bonjour le monde  "

# Casse
print(texte.upper())         # "  BONJOUR LE MONDE  "
print(texte.lower())         # "  bonjour le monde  "
print(texte.capitalize())    # "  bonjour le monde  " (1ère lettre en maj)
print("alice dupont".title()) # "Alice Dupont"

# Nettoyage
print(texte.strip())         # "bonjour le monde"  (supprime les espaces)
print(texte.lstrip())        # "bonjour le monde  " (gauche)
print(texte.rstrip())        # "  bonjour le monde" (droite)

# Recherche
phrase = "Python est un super langage"
print(phrase.find("super"))       # 15 (indice de départ du mot)
print(phrase.count("a"))          # 3  (nombre d'occurrences)
print(phrase.startswith("Python"))# True
print(phrase.endswith("langage")) # True
print("python" in phrase)         # False (sensible à la casse)
print("Python" in phrase)         # True

# Remplacement
print(phrase.replace("super", "excellent"))
# "Python est un excellent langage"

# Division
print(phrase.split(" "))
# ['Python', 'est', 'un', 'super', 'langage']

# Jointure
mots = ["Data", "Science", "Python"]
print(" - ".join(mots))  # "Data - Science - Python"
```

### 8.4 Tableau récapitulatif des méthodes

| Méthode | Description | Exemple | Résultat |
|---------|-------------|---------|----------|
| `.upper()` | Tout en majuscules | `"alice".upper()` | `"ALICE"` |
| `.lower()` | Tout en minuscules | `"ALICE".lower()` | `"alice"` |
| `.strip()` | Supprimer espaces | `"  hi  ".strip()` | `"hi"` |
| `.replace(a, b)` | Remplacer | `"chat".replace("c","r")` | `"rhat"` |
| `.split(sep)` | Diviser | `"a,b,c".split(",")` | `["a","b","c"]` |
| `.find(s)` | Trouver position | `"Python".find("y")` | `1` |
| `.startswith(s)` | Commence par | `"Python".startswith("Py")` | `True` |
| `.count(s)` | Compter occurrences | `"banana".count("a")` | `3` |
| `len()` | Longueur | `len("Python")` | `6` |

---

## 9. Booléens Python

### 📖 Définition

Un **booléen** (`bool`) est un type de données qui ne peut prendre que **deux valeurs** : `True` (vrai) ou `False` (faux). C'est la base de toute logique conditionnelle.

> ⚠️ En Python, les booléens commencent par une **majuscule** : `True` et `False` (pas `true` ni `false`).

### 9.1 Créer un booléen

```python
est_etudiant  = True
est_diplome   = False

print(type(est_etudiant))  # <class 'bool'>
print(est_etudiant)        # True
```

### 9.2 Les valeurs "truthy" et "falsy"

En Python, certaines valeurs sont considérées comme `False` même sans être des booléens :

```python
# VALEURS FALSY (considérées comme False)
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False (chaîne vide)
print(bool(None))     # False
print(bool([]))       # False (liste vide)

# VALEURS TRUTHY (considérées comme True)
print(bool(1))        # True
print(bool(-5))       # True (tout entier non nul)
print(bool("Alice"))  # True
print(bool([1, 2]))   # True (liste non vide)
```

### 9.3 Booléens et opérateurs logiques

```python
a = True
b = False

print(a and b)   # False (les deux doivent être True)
print(a or b)    # True  (au moins un True suffit)
print(not a)     # False (inverse)
print(not b)     # True

# Table de vérité AND
print(True  and True)   # True
print(True  and False)  # False
print(False and True)   # False
print(False and False)  # False

# Table de vérité OR
print(True  or True)    # True
print(True  or False)   # True
print(False or True)    # True
print(False or False)   # False
```

---

## 10. Conversion de type

### 📖 Définition

La **conversion de type** (ou *casting*) consiste à transformer une valeur d'un type vers un autre. Python le fait parfois automatiquement (**conversion implicite**), mais vous pouvez aussi le faire manuellement (**conversion explicite**).

### 10.1 Conversion explicite — Les fonctions de conversion

| Fonction | Conversion vers | Exemple | Résultat |
|----------|-----------------|---------|----------|
| `int()` | Entier | `int("42")` | `42` |
| `float()` | Décimal | `float("3.14")` | `3.14` |
| `str()` | Chaîne | `str(100)` | `"100"` |
| `bool()` | Booléen | `bool(0)` | `False` |

### 10.2 Exemples de conversion

```python
# str → int
age_texte = "25"
age_entier = int(age_texte)
print(age_entier + 5)   # 30 ✅ (impossible avec une chaîne !)

# str → float
prix_texte = "19.99"
prix = float(prix_texte)
print(prix * 2)         # 39.98

# int / float → str
note = 16
message = "Ma note est : " + str(note)
print(message)          # Ma note est : 16

# int → float
entier = 5
decimal = float(entier)
print(decimal)          # 5.0

# float → int (attention : troncature, pas arrondi !)
nombre = 9.99
print(int(nombre))      # 9 (pas 10 ! La partie décimale est supprimée)
```

### 10.3 Conversion implicite (automatique)

```python
# Python convertit automatiquement int en float lors d'opérations mixtes
résultat = 10 + 3.5
print(résultat)        # 13.5
print(type(résultat))  # <class 'float'> — automatiquement converti !
```

### 10.4 Erreurs de conversion courantes

```python
# ❌ Impossible de convertir du texte non numérique en int
int("Alice")   # ValueError: invalid literal for int() with base 10: 'Alice'
int("12.5")    # ValueError: int() ne peut pas convertir un flottant sous forme de texte

# ✅ Il faut d'abord passer par float
int(float("12.5"))  # 12 ✅

# ❌ Concaténer str et int sans conversion
print("Âge : " + 25)  # TypeError: can only concatenate str (not "int") to str

# ✅ Convertir d'abord en str
print("Âge : " + str(25))  # Âge : 25 ✅
```

---

## 11. Condition `if` en Python

### 📖 Définition

La structure `if` permet d'**exécuter un bloc de code uniquement si une condition est vraie**. C'est la base de la prise de décision en programmation.

> 💡 **Analogie** : C'est exactement comme dans la vie réelle. "**Si** il pleut, je prends un parapluie." Si la condition (il pleut) est vraie, l'action (prendre un parapluie) est exécutée.

### Syntaxe

```python
if condition:
    # bloc de code exécuté si condition == True
    instruction1
    instruction2
```

### 11.1 Exemples

```python
# Exemple 1 — Simple
age = 20
if age >= 18:
    print("Vous êtes majeur.")  # Affiché car 20 >= 18 est True

# Exemple 2 — Plusieurs instructions dans le if
note = 16
if note >= 10:
    print("Vous êtes admis !")
    print(f"Votre note est {note}/20.")

# Exemple 3 — Condition False → rien ne s'affiche
temperature = 25
if temperature < 0:
    print("Il gèle !")  # Non affiché car 25 < 0 est False
print("Fin du programme")  # Toujours affiché
```

---

## 12. Condition `if/else`

### 📖 Définition

`if/else` permet de définir **deux chemins alternatifs** : un si la condition est vraie, un autre si elle est fausse.

### Syntaxe

```python
if condition:
    # exécuté si condition == True
else:
    # exécuté si condition == False
```

### 12.1 Exemples

```python
# Exemple 1 — Pair ou impair
nombre = 7
if nombre % 2 == 0:
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")   # Affiche ceci

# Exemple 2 — Admission
note = 8
if note >= 10:
    print("Admis ✅")
else:
    print("Ajourné ❌")  # Affiche ceci

# Exemple 3 — Mot de passe
mot_de_passe = "python2024"
saisie = "python2024"
if saisie == mot_de_passe:
    print("Connexion réussie !")
else:
    print("Mot de passe incorrect.")
```

### 12.2 `if/else` en une ligne (ternaire)

```python
# Syntaxe : valeur_si_vrai if condition else valeur_si_faux
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
print(statut)  # Majeur

# Autre exemple
note = 14
mention = "Admis" if note >= 10 else "Ajourné"
print(mention)  # Admis
```

---

## 13. Condition `if/elif/else`

### 📖 Définition

`elif` (contraction de "else if") permet de tester **plusieurs conditions successives**. Python évalue chaque condition dans l'ordre et exécute le premier bloc dont la condition est vraie.

### Syntaxe

```python
if condition1:
    # si condition1 est True
elif condition2:
    # si condition1 est False ET condition2 est True
elif condition3:
    # si condition1 et 2 sont False ET condition3 est True
else:
    # si AUCUNE condition n'est True
```

### 13.1 Exemple — Mentions scolaires

```python
note = 15.5

if note >= 16:
    print("Mention : Très bien 🏆")
elif note >= 14:
    print("Mention : Bien 👍")       # Affiche ceci (15.5 >= 14)
elif note >= 12:
    print("Mention : Assez bien")
elif note >= 10:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant ❌")
```

### 13.2 Exemple — Tranche d'âge

```python
age = 45

if age < 13:
    categorie = "Enfant"
elif age < 18:
    categorie = "Adolescent"
elif age < 30:
    categorie = "Jeune adulte"
elif age < 60:
    categorie = "Adulte"            # ← Cette branche est sélectionnée
else:
    categorie = "Senior"

print(f"Catégorie : {categorie}")   # Catégorie : Adulte
```

### 13.3 Exemple — Calculatrice simple

```python
a = 10
b = 3
operateur = "+"

if operateur == "+":
    resultat = a + b
elif operateur == "-":
    resultat = a - b
elif operateur == "*":
    resultat = a * b
elif operateur == "/":
    if b != 0:
        resultat = a / b
    else:
        resultat = "Erreur : division par zéro !"
else:
    resultat = "Opérateur inconnu"

print(f"{a} {operateur} {b} = {resultat}")  # 10 + 3 = 13
```

---

## 14. Boucle `for` en Python

### 📖 Définition

La boucle `for` permet de **répéter un bloc de code** pour chaque élément d'une séquence (liste, chaîne, intervalle de nombres...).

> 💡 **Analogie** : "**Pour chaque** étudiant dans la liste, afficher son nom." On parcourt la liste du début à la fin, un élément à la fois.

### Syntaxe

```python
for element in sequence:
    # bloc répété pour chaque élément
    instruction
```

### 14.1 Boucle for avec `range()`

`range()` génère une séquence de nombres.

```python
# range(fin) → de 0 à fin-1
for i in range(5):
    print(i)
# Affiche : 0 1 2 3 4

# range(debut, fin) → de debut à fin-1
for i in range(1, 6):
    print(i)
# Affiche : 1 2 3 4 5

# range(debut, fin, pas) → avec un incrément
for i in range(0, 11, 2):
    print(i)
# Affiche : 0 2 4 6 8 10
```

### 14.2 Boucle for sur une liste

```python
etudiants = ["Alice", "Bob", "Claire", "David"]

for etudiant in etudiants:
    print(f"Bonjour, {etudiant} !")

# Affiche :
# Bonjour, Alice !
# Bonjour, Bob !
# Bonjour, Claire !
# Bonjour, David !
```

### 14.3 Boucle for sur une chaîne

```python
mot = "Python"
for lettre in mot:
    print(lettre)
# Affiche : P y t h o n (une lettre par ligne)
```

### 14.4 `enumerate()` — Indice + valeur

```python
fruits = ["mangue", "papaye", "ananas"]

for indice, fruit in enumerate(fruits):
    print(f"{indice + 1}. {fruit}")

# Affiche :
# 1. mangue
# 2. papaye
# 3. ananas
```

### 14.5 Calculs avec une boucle for

```python
# Calcul de la somme de 1 à 10
somme = 0
for i in range(1, 11):
    somme += i
print(f"Somme de 1 à 10 : {somme}")  # 55

# Moyenne des notes
notes = [14, 16, 12, 18, 15]
total = 0
for note in notes:
    total += note
moyenne = total / len(notes)
print(f"Moyenne : {moyenne}")  # 15.0
```

### 14.6 `break` et `continue`

```python
# break — arrêter la boucle prématurément
for i in range(10):
    if i == 5:
        break           # Arrête dès que i vaut 5
    print(i)
# Affiche : 0 1 2 3 4

# continue — sauter une itération
for i in range(10):
    if i % 2 == 0:
        continue        # Saute les nombres pairs
    print(i)
# Affiche : 1 3 5 7 9
```

---

## 15. Boucle `while` en Python

### 📖 Définition

La boucle `while` répète un bloc de code **tant qu'une condition reste vraie**. Contrairement à `for` qui itère sur une séquence connue, `while` continue jusqu'à ce que la condition devienne fausse.

> 💡 **Analogie** : "**Tant que** le feu est rouge, attendre." On ne sait pas combien de temps on va attendre — on continue jusqu'à ce que la condition change.

### Syntaxe

```python
while condition:
    # bloc répété tant que condition == True
    instruction
    # ⚠️ Ne pas oublier de modifier la condition pour éviter une boucle infinie
```

### 15.1 Exemple simple

```python
compteur = 0

while compteur < 5:
    print(f"Compteur : {compteur}")
    compteur += 1     # ⚠️ INDISPENSABLE pour éviter la boucle infinie !

print("Boucle terminée !")

# Affiche :
# Compteur : 0
# Compteur : 1
# Compteur : 2
# Compteur : 3
# Compteur : 4
# Boucle terminée !
```

### 15.2 Compte à rebours

```python
decompte = 5

while decompte > 0:
    print(f"{decompte}...")
    decompte -= 1

print("🚀 Décollage !")

# Affiche : 5... 4... 3... 2... 1... 🚀 Décollage !
```

### 15.3 Validation d'une entrée utilisateur

```python
# while pour valider une saisie
note = -1  # Valeur initiale invalide pour entrer dans la boucle

while note < 0 or note > 20:
    note = float(input("Entrez une note entre 0 et 20 : "))
    if note < 0 or note > 20:
        print("Note invalide, réessayez.")

print(f"Note validée : {note}/20")
```

### 15.4 ⚠️ Boucle infinie — Le piège à éviter

```python
# ❌ DANGER — Boucle infinie (ne jamais faire ça sans condition d'arrêt)
# compteur = 0
# while compteur < 5:
#     print("Boucle")
#     # On a oublié compteur += 1 → la boucle ne s'arrête jamais !

# ✅ Toujours s'assurer que la condition finira par devenir False
compteur = 0
while compteur < 5:
    print("Boucle")
    compteur += 1    # ← Condition d'arrêt : compteur atteindra 5
```

### 15.5 `while` avec `break`

```python
# Simuler un menu interactif
print("=== Menu ===")
commande = ""

while True:             # Boucle infinie contrôlée
    commande = input("Commande (q pour quitter) : ")
    if commande == "q":
        print("Au revoir !")
        break           # Sortir de la boucle
    else:
        print(f"Vous avez tapé : {commande}")
```

### 15.6 `for` vs `while` — Quand utiliser lequel ?

| Situation | Utiliser |
|-----------|----------|
| Parcourir une liste, une chaîne, un range | `for` |
| Nombre d'itérations connu à l'avance | `for` |
| Répéter jusqu'à ce qu'une condition change | `while` |
| Nombre d'itérations inconnu à l'avance | `while` |
| Valider une saisie utilisateur | `while` |

```python
# FOR → quand on sait combien de fois on itère
for i in range(5):
    print(i)

# WHILE → quand on itère jusqu'à une condition
secret = 42
devine = 0
while devine != secret:
    devine = int(input("Devinez le nombre : "))
print("Bravo !")
```

---

## 16. Conclusion

### 📌 Récapitulatif du chapitre

```
BASES DE PYTHON
│
├── Variables & Constantes   → Boîtes étiquetées pour stocker des valeurs
│                              MAJUSCULES pour les constantes
│
├── Attribution              → =, +=, -=, *=, //=
│                              Attribution multiple : x, y = 10, 20
│
├── Opérateurs arithmétiques → +, -, *, /, //, %, **
│
├── Opérateurs de comparaison→ ==, !=, >, <, >=, <= → retournent True/False
│
├── Types de données         → int, float, str, bool, None
│                              type() pour vérifier
│
├── Chaînes (str)            → Indexation, slicing, méthodes (.upper(), etc.)
│                              F-strings pour formater
│
├── Booléens                 → True / False, and, or, not
│
├── Conversion de type       → int(), float(), str(), bool()
│
├── Conditions               → if → if/else → if/elif/else
│
└── Boucles                  → for (séquence connue)
                               while (condition variable)
                               break, continue
```

### 🔑 Points clés à retenir

1. **L'indentation** est obligatoire et fait partie de la syntaxe Python.
2. **`=` ≠ `==`** : l'un attribue, l'autre compare. Confusion classique !
3. Les **f-strings** (`f"..."`) sont la façon moderne et recommandée de formater du texte.
4. **`for`** pour les séquences connues, **`while`** pour les conditions variables.
5. Toujours s'assurer qu'une boucle `while` a une **condition d'arrêt** pour éviter les boucles infinies.
6. **`break`** arrête une boucle, **`continue`** passe à l'itération suivante.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons les **structures de données Python** : les listes (`list`), les tuples (`tuple`), les dictionnaires (`dict`) et les ensembles (`set`) — des outils essentiels pour organiser et manipuler des données en Data Science.

---

## 17. ✅ Point de contrôle — Bases de Python

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre `=` et `==` en Python ?

<details>
<summary>👀 Voir la réponse</summary>

> `=` est l'opérateur d'**attribution** — il assigne une valeur à une variable (`age = 25`). `==` est l'opérateur de **comparaison** — il vérifie si deux valeurs sont égales et retourne `True` ou `False` (`age == 25`). Utiliser `=` dans un `if` provoque une `SyntaxError`.
</details>

---

**Q2.** Que retourne `bool("")` et `bool("Alice")` ? Pourquoi ?

<details>
<summary>👀 Voir la réponse</summary>

> `bool("")` retourne `False` car une **chaîne vide** est une valeur "falsy" en Python. `bool("Alice")` retourne `True` car toute chaîne non vide est "truthy".
</details>

---

**Q3.** Quelle est la différence entre `/` et `//` en Python ?

<details>
<summary>👀 Voir la réponse</summary>

> `/` effectue une **division réelle** et retourne toujours un `float` (`7 / 2 = 3.5`). `//` effectue une **division entière** (floor division) et retourne la partie entière du résultat (`7 // 2 = 3`).
</details>

---

**Q4.** Quand utiliser une boucle `for` plutôt qu'une boucle `while` ?

<details>
<summary>👀 Voir la réponse</summary>

> On utilise `for` quand on connaît à l'avance le nombre d'itérations ou qu'on parcourt une séquence (liste, chaîne, range). On utilise `while` quand le nombre d'itérations dépend d'une condition qui peut changer de façon imprévisible (validation d'entrée, attente d'un événement).
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Variables et types**

Créez les variables suivantes et affichez leur valeur ET leur type :
- Votre nom
- Votre âge
- Votre note moyenne
- `True` si vous aimez Python

<details>
<summary>👀 Voir la solution</summary>

```python
nom         = "Kofi"
age         = 23
note_moy    = 15.5
aime_python = True

print(f"Nom : {nom} — type : {type(nom)}")
print(f"Âge : {age} — type : {type(age)}")
print(f"Note : {note_moy} — type : {type(note_moy)}")
print(f"Aime Python : {aime_python} — type : {type(aime_python)}")
```
</details>

---

**Exercice 2 — Opérateurs et f-strings**

Calculez et affichez dans une phrase lisible :
- L'aire d'un rectangle de longueur 8 et largeur 5
- L'hypoténuse d'un triangle rectangle de côtés 3 et 4 (indice : `** 0.5`)
- Le reste de la division de 2024 par 7

<details>
<summary>👀 Voir la solution</summary>

```python
longueur    = 8
largeur     = 5
cote_a      = 3
cote_b      = 4

aire        = longueur * largeur
hypotenuse  = (cote_a**2 + cote_b**2) ** 0.5
reste       = 2024 % 7

print(f"Aire du rectangle     : {aire}")
print(f"Hypoténuse            : {hypotenuse}")
print(f"Reste de 2024 ÷ 7     : {reste}")
```
</details>

---

**Exercice 3 — Chaînes de caractères**

Avec la chaîne `texte = "Bootcamp Data Science Abidjan"` :
- Affichez-la en majuscules
- Affichez uniquement les 8 premiers caractères
- Comptez le nombre de fois que la lettre 'a' apparaît
- Remplacez "Abidjan" par "Côte d'Ivoire"
- Affichez la longueur totale de la chaîne

<details>
<summary>👀 Voir la solution</summary>

```python
texte = "Bootcamp Data Science Abidjan"

print(texte.upper())
print(texte[:8])
print(texte.lower().count("a"))
print(texte.replace("Abidjan", "Côte d'Ivoire"))
print(len(texte))
```
</details>

---

**Exercice 4 — Conditions**

Écrivez un programme qui, pour une note donnée (variable `note`), affiche la mention correspondante :
- ≥ 16 → "Très bien"
- ≥ 14 → "Bien"
- ≥ 12 → "Assez bien"
- ≥ 10 → "Passable"
- < 10 → "Insuffisant"

<details>
<summary>👀 Voir la solution</summary>

```python
note = 13.5

if note >= 16:
    mention = "Très bien 🏆"
elif note >= 14:
    mention = "Bien 👍"
elif note >= 12:
    mention = "Assez bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant ❌"

print(f"Note : {note}/20 → Mention : {mention}")
```
</details>

---

**Exercice 5 — Boucles**

a) Avec une boucle `for`, affichez les multiples de 3 entre 1 et 30.

b) Avec une boucle `while`, calculez la somme des entiers de 1 à 100.

c) Avec une boucle `for` et `break`, trouvez le premier multiple de 7 supérieur à 50.

<details>
<summary>👀 Voir la solution</summary>

```python
# a) Multiples de 3
for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")
print()

# b) Somme de 1 à 100
somme = 0
i = 1
while i <= 100:
    somme += i
    i += 1
print(f"Somme de 1 à 100 : {somme}")  # 5050

# c) Premier multiple de 7 > 50
for i in range(51, 200):
    if i % 7 == 0:
        print(f"Premier multiple de 7 > 50 : {i}")  # 56
        break
```
</details>

---

### 🏆 Challenge bonus

Écrivez un programme complet qui simule un **jeu de devinette** :
1. Définissez un nombre secret (ex : `42`)
2. Utilisez une boucle `while` pour demander à l'utilisateur de deviner
3. Comptez le nombre de tentatives
4. Affichez "Trop grand" ou "Trop petit" après chaque essai
5. Quand le nombre est trouvé, affichez le nombre de tentatives

<details>
<summary>👀 Voir la solution</summary>

```python
secret      = 42
tentatives  = 0
devine      = None

print("🎯 Jeu de devinette — Trouvez le nombre entre 1 et 100 !")

while devine != secret:
    devine      = int(input("Votre proposition : "))
    tentatives  += 1

    if devine < secret:
        print("📉 Trop petit !")
    elif devine > secret:
        print("📈 Trop grand !")
    else:
        print(f"🎉 Bravo ! Vous avez trouvé {secret} en {tentatives} tentative(s) !")
```
</details>

---

*📘 Fin du Chapitre 2 — Bases de Python | Bootcamp Data Science*
