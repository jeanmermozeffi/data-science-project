# ⚙️ Fonctions Python — Cours Bootcamp Data Science

> **Chapitre 4** | Prérequis : Chapitres 1, 2, 3 (Introduction, Bases, Data Structures)

---

## Table des matières

1. [Qu'est-ce qu'une fonction ?](#1-quest-ce-quune-fonction-)
2. [Créer une fonction](#2-créer-une-fonction)
3. [Arguments des fonctions Python](#3-arguments-des-fonctions-python)
4. [Fonctions à plusieurs paramètres](#4-fonctions-à-plusieurs-paramètres)
5. [Arguments par défaut](#5-arguments-par-défaut)
6. [L'instruction de retour (return)](#6-linstruction-de-retour-return)
7. [\*args et \*\*kwargs](#7-args-et-kwargs--paramètres-flexibles)
8. [Portée des variables (Scope)](#8-portée-des-variables-scope)
9. [Fonction Lambda](#9-fonction-lambda)
10. [Fonction Map](#10-fonction-map)
11. [Filter et Reduce](#11-filter-et-reduce)
12. [Fonctions et Data Science](#12-fonctions-et-data-science)
13. [Conclusion](#13-conclusion)
14. [✅ Point de contrôle — Fonctions Python](#14--point-de-contrôle--fonctions-python)

---

## 1. Qu'est-ce qu'une fonction ?

### 📖 Définition

Une **fonction** est un **bloc de code réutilisable** qui exécute une tâche précise. On lui donne un nom, on peut lui fournir des données en entrée (paramètres), et elle peut renvoyer un résultat en sortie.

> 💡 **Analogie** : Une fonction, c'est comme une **machine à café**. Vous lui donnez de l'eau et du café moulu (les **entrées**), elle exécute un processus interne (le **code**), et elle vous rend une tasse de café (la **sortie**). Vous n'avez pas besoin de refaire le processus manuellement à chaque fois — vous appuyez juste sur le bouton.

### 🎯 Pourquoi utiliser des fonctions ?

```
SANS FONCTION (répétitif)              AVEC FONCTION (réutilisable)
──────────────────────────             ─────────────────────────────
moyenne1 = (14+16+12)/3                def moyenne(notes):
print(moyenne1)                            return sum(notes) / len(notes)

moyenne2 = (18+15+10)/3                print(moyenne([14, 16, 12]))
print(moyenne2)                        print(moyenne([18, 15, 10]))
                                        print(moyenne([9, 20, 14]))
moyenne3 = (9+20+14)/3
print(moyenne3)                        → Code écrit UNE FOIS,
                                          réutilisé autant de fois que voulu
→ Code dupliqué, difficile à
  maintenir et source d'erreurs
```

### 🔑 Les avantages des fonctions

```
AVANTAGES DES FONCTIONS
│
├── ♻️  Réutilisabilité   → Écrire une fois, utiliser partout
├── 📖 Lisibilité         → Le code est organisé et plus clair
├── 🐛 Facilité de débogage → Isoler et tester chaque partie séparément
├── 🧩 Modularité         → Découper un gros problème en petites tâches
└── 🔧 Maintenabilité     → Corriger une erreur à un seul endroit
```

### 🔟 Fonctions déjà rencontrées

Vous utilisez déjà des fonctions depuis le chapitre 2 sans le savoir !

```python
print("Bonjour")     # print() est une fonction native
len([1, 2, 3])        # len() est une fonction native
sum([1, 2, 3])         # sum() est une fonction native
type(42)               # type() est une fonction native
```

> Dans ce chapitre, vous allez apprendre à créer **vos propres fonctions**.

---

## 2. Créer une fonction

### 📖 Syntaxe de base

```python
def nom_fonction(paramètres):
    """Docstring : description de la fonction (optionnel mais recommandé)"""
    # corps de la fonction
    instructions
    return résultat  # optionnel
```

> 🔑 **`def`** (define) démarre la déclaration d'une fonction. N'oubliez pas les **deux points `:`** et l'**indentation** du corps de la fonction.

### 2.1 Une fonction simple sans paramètre

```python
def dire_bonjour():
    print("Bonjour, bienvenue au bootcamp Data Science !")

# Appeler (exécuter) la fonction
dire_bonjour()
# Affiche : Bonjour, bienvenue au bootcamp Data Science !

dire_bonjour()  # On peut l'appeler autant de fois que voulu
dire_bonjour()
```

### 2.2 Une fonction avec un paramètre

```python
def saluer(prenom):
    print(f"Bonjour, {prenom} !")

saluer("Alice")   # Bonjour, Alice !
saluer("Kofi")    # Bonjour, Kofi !
saluer("Fatou")   # Bonjour, Fatou !
```

### 2.3 Anatomie d'une fonction

```
def       calculer_carre     (   nombre   )     :
 │              │                   │            │
 mot-clé    nom de la          paramètre     deux-points
"def"       fonction           (entrée)      obligatoires
                                                    │
    ┌───────────────────────────────────────────────┘
    ▼
    """Calcule le carré d'un nombre."""    ← docstring (documentation)
    resultat = nombre ** 2                  ← corps (indenté)
    return resultat                         ← valeur de sortie
```

```python
def calculer_carre(nombre):
    """Calcule le carré d'un nombre."""
    resultat = nombre ** 2
    return resultat

print(calculer_carre(5))    # 25
print(calculer_carre(10))   # 100
```

### 2.4 La docstring — Documenter sa fonction

```python
def moyenne(notes):
    """
    Calcule la moyenne d'une liste de notes.

    Paramètre :
        notes (list) : liste de nombres

    Retourne :
        float : la moyenne des notes
    """
    return sum(notes) / len(notes)

# Consulter la documentation d'une fonction
print(moyenne.__doc__)
help(moyenne)
```

---

## 3. Arguments des fonctions Python

### 📖 Paramètre vs Argument

> ⚠️ Ces deux mots sont souvent confondus, mais il y a une nuance :
> - **Paramètre** : le nom utilisé dans la **définition** de la fonction
> - **Argument** : la **valeur réelle** transmise lors de l'**appel** de la fonction

```python
def saluer(prenom):     # "prenom" est un PARAMÈTRE
    print(f"Bonjour, {prenom} !")

saluer("Alice")          # "Alice" est un ARGUMENT
```

### 3.1 Passer un argument

```python
def afficher_note(note):
    print(f"Votre note est : {note}/20")

afficher_note(16)      # Votre note est : 16/20
afficher_note(9)       # Votre note est : 9/20

# On peut aussi passer une variable comme argument
ma_note = 18
afficher_note(ma_note)  # Votre note est : 18/20
```

### 3.2 Arguments positionnels

Par défaut, les arguments sont associés aux paramètres **selon leur position** (ordre).

```python
def presenter(nom, age, ville):
    print(f"{nom}, {age} ans, habite à {ville}")

presenter("Alice", 23, "Abidjan")
# Alice, 23 ans, habite à Abidjan
# → "Alice" va au 1er paramètre (nom)
# → 23 va au 2ème paramètre (age)
# → "Abidjan" va au 3ème paramètre (ville)
```

### 3.3 Arguments nommés (keyword arguments)

On peut préciser **explicitement** à quel paramètre correspond chaque valeur — l'ordre n'a alors plus d'importance.

```python
def presenter(nom, age, ville):
    print(f"{nom}, {age} ans, habite à {ville}")

# Arguments nommés — l'ordre ne compte plus
presenter(ville="Dakar", nom="Bob", age=25)
# Bob, 25 ans, habite à Dakar

# On peut mélanger positionnels et nommés
# (les positionnels doivent toujours venir en premier)
presenter("Claire", ville="Accra", age=22)
# Claire, 22 ans, habite à Accra
```

---

## 4. Fonctions à plusieurs paramètres

### 4.1 Exemple — Calcul d'une moyenne pondérée

```python
def moyenne_ponderee(note_examen, note_projet, note_partiel):
    """Calcule une moyenne pondérée : 50% examen, 30% projet, 20% partiel."""
    total = (note_examen * 0.5) + (note_projet * 0.3) + (note_partiel * 0.2)
    return total

resultat = moyenne_ponderee(16, 18, 14)
print(f"Moyenne pondérée : {resultat}")   # 16.2
```

### 4.2 Exemple — Calcul du prix TTC

```python
def prix_ttc(prix_ht, taux_tva, remise=0):
    """Calcule le prix TTC après application de la TVA et d'une remise."""
    prix_apres_remise = prix_ht - (prix_ht * remise)
    ttc = prix_apres_remise * (1 + taux_tva)
    return round(ttc, 2)

print(prix_ttc(10000, 0.18))            # 11800.0 (sans remise)
print(prix_ttc(10000, 0.18, 0.10))      # 10620.0 (avec 10% de remise)
```

### 4.3 Fonction avec logique conditionnelle

```python
def evaluer_note(nom, note):
    """Retourne un message d'évaluation selon la note."""
    if note >= 16:
        mention = "Très bien 🏆"
    elif note >= 14:
        mention = "Bien 👍"
    elif note >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant ❌"

    return f"{nom} : {note}/20 — {mention}"

print(evaluer_note("Alice", 17))   # Alice : 17/20 — Très bien 🏆
print(evaluer_note("Bob", 8))      # Bob : 8/20 — Insuffisant ❌
```

---

## 5. Arguments par défaut

### 📖 Définition

Un **argument par défaut** fournit une valeur automatique si l'appelant ne la spécifie pas. Cela rend certains paramètres **optionnels**.

### Syntaxe

```python
def nom_fonction(param1, param2=valeur_par_defaut):
    # corps
```

### 5.1 Exemple simple

```python
def saluer(prenom, message="Bienvenue au bootcamp !"):
    print(f"Bonjour {prenom}, {message}")

saluer("Alice")                          # utilise la valeur par défaut
# Bonjour Alice, Bienvenue au bootcamp !

saluer("Bob", "Bon retour parmi nous !")  # remplace la valeur par défaut
# Bonjour Bob, Bon retour parmi nous !
```

### 5.2 Plusieurs arguments par défaut

```python
def creer_profil(nom, age=18, ville="Abidjan", actif=True):
    print(f"{nom}, {age} ans, {ville}, actif: {actif}")

creer_profil("Alice")
# Alice, 18 ans, Abidjan, actif: True

creer_profil("Bob", 25)
# Bob, 25 ans, Abidjan, actif: True

creer_profil("Claire", 22, "Dakar")
# Claire, 22 ans, Dakar, actif: True

creer_profil("David", ville="Lagos", actif=False)
# David, 18 ans, Lagos, actif: False
```

### 5.3 ⚠️ Règle importante — Ordre des paramètres

> Les paramètres **sans valeur par défaut** doivent toujours précéder les paramètres **avec valeur par défaut**.

```python
# ❌ Incorrect
def fonction(a=5, b):     # SyntaxError !
    pass

# ✅ Correct
def fonction(b, a=5):
    pass
```

---

## 6. L'instruction de retour (return)

### 📖 Définition

L'instruction `return` permet à une fonction de **renvoyer une valeur** à l'endroit où elle a été appelée. Sans `return`, une fonction retourne `None` par défaut.

### 6.1 Fonction avec return vs sans return

```python
# Sans return — affiche seulement, ne renvoie rien d'utilisable
def afficher_carre(n):
    print(n ** 2)

resultat = afficher_carre(5)   # Affiche : 25
print(resultat)                 # None ← rien n'est retourné !

# Avec return — renvoie une valeur utilisable
def calculer_carre(n):
    return n ** 2

resultat = calculer_carre(5)
print(resultat)                 # 25
print(resultat + 10)            # 35 ← on peut réutiliser la valeur
```

### 6.2 `return` arrête immédiatement la fonction

```python
def verifier_age(age):
    if age < 0:
        return "Âge invalide"   # ← la fonction s'arrête ici si True
    if age < 18:
        return "Mineur"
    return "Majeur"              # ← atteint seulement si les 2 précédents sont False

print(verifier_age(-5))   # Âge invalide
print(verifier_age(15))   # Mineur
print(verifier_age(25))   # Majeur
```

### 6.3 Retourner plusieurs valeurs (tuple)

```python
def statistiques(notes):
    """Retourne plusieurs statistiques en une seule fois."""
    minimum = min(notes)
    maximum = max(notes)
    moyenne = sum(notes) / len(notes)
    return minimum, maximum, moyenne     # retourne un tuple

notes = [14, 18, 12, 16, 10]
mini, maxi, moy = statistiques(notes)     # déballage du tuple

print(f"Min : {mini}, Max : {maxi}, Moyenne : {moy:.2f}")
# Min : 10, Max : 18, Moyenne : 14.00
```

### 6.4 Fonctions imbriquées (une fonction qui en appelle une autre)

```python
def carre(n):
    return n ** 2

def somme_des_carres(liste):
    total = 0
    for n in liste:
        total += carre(n)      # appelle la fonction carre()
    return total

print(somme_des_carres([1, 2, 3, 4]))  # 1+4+9+16 = 30
```

---

## 7. \*args et \*\*kwargs — Paramètres flexibles

### 📖 Définition

Parfois, on ne connaît pas à l'avance le **nombre d'arguments** qu'une fonction va recevoir. Python propose deux outils pour gérer cela :
- **`*args`** : accepte un nombre variable d'arguments **positionnels**
- **`**kwargs`** : accepte un nombre variable d'arguments **nommés**

### 7.1 \*args — Arguments positionnels illimités

```python
def somme(*args):
    """Additionne un nombre quelconque de valeurs."""
    print(f"args reçus : {args} (type: {type(args)})")
    return sum(args)

print(somme(1, 2))              # args reçus : (1, 2)         → 3
print(somme(1, 2, 3, 4, 5))     # args reçus : (1, 2, 3, 4, 5) → 15
print(somme())                  # args reçus : ()              → 0
```

> 💡 `*args` regroupe tous les arguments positionnels dans un **tuple**.

### 7.2 \*\*kwargs — Arguments nommés illimités

```python
def creer_profil(**kwargs):
    """Crée un profil avec un nombre quelconque de champs."""
    print(f"kwargs reçus : {kwargs} (type: {type(kwargs)})")
    for cle, valeur in kwargs.items():
        print(f"  {cle} : {valeur}")

creer_profil(nom="Alice", age=23, ville="Abidjan")
# kwargs reçus : {'nom': 'Alice', 'age': 23, 'ville': 'Abidjan'}
#   nom : Alice
#   age : 23
#   ville : Abidjan
```

> 💡 `**kwargs` regroupe tous les arguments nommés dans un **dictionnaire**.

### 7.3 Combiner tous les types de paramètres

```python
def fonction_complete(param1, param2=10, *args, **kwargs):
    print(f"param1 : {param1}")
    print(f"param2 : {param2}")
    print(f"args   : {args}")
    print(f"kwargs : {kwargs}")

fonction_complete(1, 2, 3, 4, 5, nom="Alice", age=23)
# param1 : 1
# param2 : 2
# args   : (3, 4, 5)
# kwargs : {'nom': 'Alice', 'age': 23}
```

### 7.4 Cas d'usage — Fonction de statistiques flexible

```python
def statistiques_flexibles(*nombres):
    """Calcule des statistiques sur un nombre variable de valeurs."""
    if not nombres:
        return "Aucune donnée fournie"
    return {
        "somme"   : sum(nombres),
        "moyenne" : sum(nombres) / len(nombres),
        "min"     : min(nombres),
        "max"     : max(nombres)
    }

print(statistiques_flexibles(14, 16, 18))
print(statistiques_flexibles(10, 20, 30, 40, 50))
```

---

## 8. Portée des variables (Scope)

### 📖 Définition

La **portée** (scope) détermine où une variable est **visible et accessible** dans le code. Une variable créée à l'intérieur d'une fonction n'existe **que dans cette fonction**.

### 8.1 Variables locales vs globales

```python
x = 10   # variable GLOBALE (accessible partout)

def ma_fonction():
    y = 5   # variable LOCALE (accessible seulement dans la fonction)
    print(f"À l'intérieur : x = {x}, y = {y}")

ma_fonction()          # À l'intérieur : x = 10, y = 5
print(x)                # 10 ✅ (x est global)
# print(y)              # ❌ NameError: name 'y' is not defined
```

### 8.2 Modifier une variable globale (mot-clé `global`)

```python
compteur = 0

def incrementer():
    global compteur      # indique qu'on veut modifier la variable GLOBALE
    compteur += 1

incrementer()
incrementer()
incrementer()
print(compteur)   # 3
```

> ⚠️ **Bonne pratique** : Évitez d'abuser de `global`. Préférez utiliser `return` pour renvoyer les valeurs modifiées — c'est plus prévisible et plus facile à déboguer.

### 8.3 Visualisation de la portée

```
┌─────────────────────────────────────────┐
│  PORTÉE GLOBALE                         │
│  x = 10                                 │
│                                          │
│  ┌────────────────────────────────┐    │
│  │  PORTÉE LOCALE (ma_fonction)   │    │
│  │  y = 5                          │    │
│  │  → peut LIRE x (globale)        │    │
│  │  → y n'existe que dans ce bloc  │    │
│  └────────────────────────────────┘    │
│                                          │
└─────────────────────────────────────────┘
```

---

## 9. Fonction Lambda

### 📖 Définition

Une **fonction lambda** (ou fonction anonyme) est une fonction **courte, sans nom**, définie en **une seule ligne**. Elle est utile pour des opérations simples et ponctuelles.

> 💡 **Analogie** : Si une fonction classique (`def`) est comme un plat cuisiné avec une recette complète, une lambda est comme un **snack rapide** — pratique pour un usage ponctuel, sans préparation complexe.

### Syntaxe

```python
lambda paramètres: expression
```

### 9.1 Comparaison def vs lambda

```python
# Fonction classique
def carre(x):
    return x ** 2

# Équivalent en lambda
carre_lambda = lambda x: x ** 2

print(carre(5))         # 25
print(carre_lambda(5))  # 25
```

### 9.2 Lambda avec plusieurs paramètres

```python
addition = lambda a, b: a + b
print(addition(3, 5))   # 8

moyenne = lambda a, b, c: (a + b + c) / 3
print(moyenne(14, 16, 18))   # 16.0

est_pair = lambda n: n % 2 == 0
print(est_pair(4))   # True
print(est_pair(7))   # False
```

### 9.3 Quand utiliser lambda ?

```python
# ✅ Cas d'usage typique : trier une liste selon un critère
etudiants = [
    {"nom": "Alice",  "note": 16},
    {"nom": "Bob",    "note": 12},
    {"nom": "Claire", "note": 18}
]

# Trier par note (lambda extrait la clé de tri)
etudiants_tries = sorted(etudiants, key=lambda e: e["note"])
print(etudiants_tries)

# Trier par note décroissante
etudiants_tries_desc = sorted(etudiants, key=lambda e: e["note"], reverse=True)
for e in etudiants_tries_desc:
    print(f"{e['nom']} : {e['note']}")
```

> 🔑 **Règle générale** : Utilisez `lambda` pour des fonctions **très courtes et ponctuelles** (souvent en argument d'une autre fonction). Pour des fonctions plus complexes ou réutilisées souvent, préférez `def` — c'est plus lisible.

---

## 10. Fonction Map

### 📖 Définition

`map()` **applique une fonction à chaque élément** d'une séquence (liste, tuple...) et retourne un nouvel itérable avec les résultats.

> 💡 **Analogie** : `map()` est comme une **chaîne de production en usine** — chaque élément qui passe sur le tapis roulant subit **la même transformation**.

### Syntaxe

```python
map(fonction, iterable)
```

### 10.1 Exemple simple

```python
notes = [14, 16, 12, 18, 10]

# Avec une fonction lambda
notes_sur_10 = list(map(lambda n: n / 2, notes))
print(notes_sur_10)   # [7.0, 8.0, 6.0, 9.0, 5.0]

# Avec une fonction classique
def convertir_en_pourcentage(note):
    return (note / 20) * 100

pourcentages = list(map(convertir_en_pourcentage, notes))
print(pourcentages)   # [70.0, 80.0, 60.0, 90.0, 50.0]
```

### 10.2 map() vs list comprehension

Les deux approches sont équivalentes, mais la **list comprehension** est souvent préférée en Python moderne pour sa lisibilité.

```python
notes = [14, 16, 12, 18]

# Avec map()
resultat_map = list(map(lambda n: n * 2, notes))

# Avec list comprehension (équivalent, souvent plus lisible)
resultat_comprehension = [n * 2 for n in notes]

print(resultat_map)            # [28, 32, 24, 36]
print(resultat_comprehension)  # [28, 32, 24, 36]
```

### 10.3 map() sur plusieurs listes

```python
prix       = [1000, 2500, 500]
quantites  = [3, 2, 10]

# Calculer le total pour chaque paire (prix, quantité)
totaux = list(map(lambda p, q: p * q, prix, quantites))
print(totaux)   # [3000, 5000, 5000]
```

---

## 11. Filter et Reduce

### 📖 filter() — Filtrer selon une condition

`filter()` garde **uniquement les éléments** pour lesquels la fonction retourne `True`.

```python
notes = [8, 14, 16, 9, 18, 11, 20]

# Garder seulement les notes >= 10
notes_admises = list(filter(lambda n: n >= 10, notes))
print(notes_admises)   # [14, 16, 18, 11, 20]

# Équivalent en list comprehension
notes_admises2 = [n for n in notes if n >= 10]
print(notes_admises2)  # [14, 16, 18, 11, 20]
```

### 📖 reduce() — Réduire à une seule valeur

`reduce()` applique une fonction de façon **cumulative** pour réduire une séquence à une seule valeur. Il faut l'importer depuis le module `functools`.

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

# Calculer le produit de tous les nombres
produit = reduce(lambda a, b: a * b, nombres)
print(produit)   # 120  (1×2×3×4×5)

# Trouver le maximum "manuellement" avec reduce
maximum = reduce(lambda a, b: a if a > b else b, nombres)
print(maximum)   # 5
```

**Visualisation du fonctionnement de reduce :**
```
nombres = [1, 2, 3, 4, 5]

Étape 1 : reduce(1, 2) = 1 * 2 = 2
Étape 2 : reduce(2, 3) = 2 * 3 = 6
Étape 3 : reduce(6, 4) = 6 * 4 = 24
Étape 4 : reduce(24, 5) = 24 * 5 = 120

Résultat final : 120
```

### 📊 Comparaison map / filter / reduce

| Fonction | Rôle | Retourne |
|----------|------|----------|
| `map()` | Transformer chaque élément | Même nombre d'éléments |
| `filter()` | Sélectionner des éléments | Nombre d'éléments ≤ original |
| `reduce()` | Combiner en une seule valeur | Une seule valeur |

```python
from functools import reduce

notes = [8, 14, 16, 9, 18, 11, 20]

# Pipeline complet : filtrer puis transformer puis agréger
notes_admises   = list(filter(lambda n: n >= 10, notes))          # [14,16,18,11,20]
notes_sur_100   = list(map(lambda n: n * 5, notes_admises))       # [70,80,90,55,100]
total           = reduce(lambda a, b: a + b, notes_sur_100)        # 395

print(f"Notes admises  : {notes_admises}")
print(f"Sur 100        : {notes_sur_100}")
print(f"Total          : {total}")
```

---

## 12. Fonctions et Data Science

Les fonctions sont **omniprésentes** en Data Science. Voici quelques applications concrètes.

### 12.1 Fonction de nettoyage de données

```python
def nettoyer_texte(texte):
    """Nettoie une chaîne de texte : minuscules + espaces supprimés."""
    return texte.strip().lower()

noms_bruts = ["  Alice  ", "BOB", " Claire"]
noms_propres = list(map(nettoyer_texte, noms_bruts))
print(noms_propres)   # ['alice', 'bob', 'claire']
```

### 12.2 Fonction de normalisation (utile pour le Machine Learning)

```python
def normaliser(valeur, minimum, maximum):
    """Normalise une valeur entre 0 et 1 (min-max scaling)."""
    return (valeur - minimum) / (maximum - minimum)

notes = [8, 12, 15, 18, 20]
mini, maxi = min(notes), max(notes)

notes_normalisees = [round(normaliser(n, mini, maxi), 2) for n in notes]
print(notes_normalisees)   # [0.0, 0.33, 0.58, 0.83, 1.0]
```

### 12.3 Fonction de calcul statistique réutilisable

```python
def resume_statistique(donnees):
    """Retourne un résumé statistique complet d'une liste de nombres."""
    n = len(donnees)
    moyenne = sum(donnees) / n
    variance = sum((x - moyenne) ** 2 for x in donnees) / n
    ecart_type = variance ** 0.5

    return {
        "n"          : n,
        "moyenne"    : round(moyenne, 2),
        "min"        : min(donnees),
        "max"        : max(donnees),
        "variance"   : round(variance, 2),
        "ecart_type" : round(ecart_type, 2)
    }

ventes = [4500, 7800, 11200, 6300, 9100]
print(resume_statistique(ventes))
```

### 12.4 Pipeline de traitement de données avec fonctions

```python
def charger_donnees():
    """Simule le chargement de données brutes."""
    return [
        {"nom": " alice ", "note": 16.234},
        {"nom": "BOB",     "note": 12.876},
        {"nom": " Claire", "note": 18.512}
    ]

def nettoyer_donnees(donnees):
    """Nettoie les noms et arrondit les notes."""
    for d in donnees:
        d["nom"]  = d["nom"].strip().title()
        d["note"] = round(d["note"], 1)
    return donnees

def filtrer_admis(donnees):
    """Garde uniquement les étudiants avec note >= 14."""
    return [d for d in donnees if d["note"] >= 14]

# Pipeline complet : charger → nettoyer → filtrer
donnees = charger_donnees()
donnees = nettoyer_donnees(donnees)
admis   = filtrer_admis(donnees)

for etudiant in admis:
    print(etudiant)
# {'nom': 'Alice', 'note': 16.2}
# {'nom': 'Claire', 'note': 18.5}
```

> 💡 Ce style de **pipeline de fonctions** (charger → nettoyer → transformer → analyser) est exactement la structure que vous retrouverez avec **Pandas** dans les prochains modules du bootcamp.

### 12.5 Fonctions récursives (bonus)

Une fonction **récursive** s'appelle elle-même jusqu'à atteindre une condition d'arrêt.

```python
def factorielle(n):
    """Calcule n! = n × (n-1) × ... × 1"""
    if n <= 1:              # condition d'arrêt (cas de base)
        return 1
    return n * factorielle(n - 1)   # appel récursif

print(factorielle(5))   # 120  (5×4×3×2×1)

def fibonacci(n):
    """Retourne le n-ième terme de la suite de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13
```

---

## 13. Conclusion

### 📌 Récapitulatif du chapitre

```
FONCTIONS PYTHON
│
├── def nom(param):          → Créer une fonction
│       return valeur            renvoie un résultat
│
├── Arguments
│   ├── Positionnels          → selon l'ordre
│   ├── Nommés (keyword)      → nom=valeur
│   ├── Par défaut            → param=valeur_defaut
│   ├── *args                 → arguments positionnels illimités (tuple)
│   └── **kwargs               → arguments nommés illimités (dict)
│
├── Portée (scope)
│   ├── Variable locale        → existe dans la fonction seulement
│   └── Variable globale       → accessible partout, global pour modifier
│
├── lambda param: expr        → fonction courte, anonyme, une ligne
│
├── map(fonction, iterable)   → transforme chaque élément
├── filter(fonction, iterable)→ sélectionne des éléments
└── reduce(fonction, iterable)→ réduit à une seule valeur
```

### 🔑 Points clés à retenir

1. Une fonction se définit avec `def`, s'exécute avec `nom_fonction()`.
2. **`return`** renvoie une valeur ; sans lui, la fonction retourne `None`.
3. Les **arguments par défaut** doivent toujours venir après les arguments obligatoires.
4. `*args` capture les arguments positionnels en trop dans un **tuple** ; `**kwargs` capture les arguments nommés dans un **dict**.
5. Une variable définie **dans** une fonction (locale) n'existe pas en dehors.
6. `lambda` est utile pour des fonctions **courtes et ponctuelles**, souvent en argument d'une autre fonction (`sorted`, `map`, `filter`).
7. `map()`, `filter()`, `reduce()` sont la base de nombreux **pipelines de traitement de données**.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons les **bibliothèques Python pour la Data Science** : **NumPy** pour le calcul numérique et les tableaux multidimensionnels, première étape vers la manipulation de données à grande échelle avec **Pandas**.

---

## 14. ✅ Point de contrôle — Fonctions Python

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre un paramètre et un argument ?

<details>
<summary>👀 Voir la réponse</summary>

> Un **paramètre** est le nom utilisé dans la **définition** de la fonction (`def saluer(prenom):`). Un **argument** est la **valeur réelle** transmise lors de l'**appel** de la fonction (`saluer("Alice")` → `"Alice"` est l'argument).
</details>

---

**Q2.** Que se passe-t-il si une fonction n'a pas d'instruction `return` ?

<details>
<summary>👀 Voir la réponse</summary>

> La fonction retourne automatiquement `None`. Elle peut toujours exécuter des instructions comme `print()`, mais aucune valeur utilisable n'est renvoyée à l'appelant.
</details>

---

**Q3.** Quelle est la différence entre `*args` et `**kwargs` ?

<details>
<summary>👀 Voir la réponse</summary>

> `*args` capture un nombre variable d'**arguments positionnels** et les regroupe dans un **tuple**. `**kwargs` capture un nombre variable d'**arguments nommés** (clé=valeur) et les regroupe dans un **dictionnaire**.
</details>

---

**Q4.** Pourquoi et quand utiliser une fonction `lambda` plutôt qu'une fonction `def` ?

<details>
<summary>👀 Voir la réponse</summary>

> On utilise `lambda` pour des fonctions **très courtes, à usage ponctuel**, souvent passées comme argument à une autre fonction (`sorted()`, `map()`, `filter()`). Pour des fonctions plus complexes, réutilisées à plusieurs endroits, ou nécessitant plusieurs lignes de logique, `def` est préférable car plus lisible et documentable (docstring).
</details>

---

**Q5.** Quelle est la différence entre une variable locale et une variable globale ?

<details>
<summary>👀 Voir la réponse</summary>

> Une variable **locale** est créée à l'intérieur d'une fonction et n'existe que pendant l'exécution de cette fonction — elle est inaccessible en dehors. Une variable **globale** est définie en dehors de toute fonction et est accessible partout dans le programme (en lecture directement ; en écriture, il faut le mot-clé `global` à l'intérieur d'une fonction).
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Fonction simple**

Créez une fonction `est_majeur(age)` qui retourne `True` si l'âge est ≥ 18, sinon `False`.

<details>
<summary>👀 Voir la solution</summary>

```python
def est_majeur(age):
    return age >= 18

print(est_majeur(20))  # True
print(est_majeur(15))  # False
```
</details>

---

**Exercice 2 — Arguments par défaut**

Créez une fonction `calculer_prix(prix, tva=0.18)` qui retourne le prix TTC. Testez-la avec et sans préciser le taux de TVA.

<details>
<summary>👀 Voir la solution</summary>

```python
def calculer_prix(prix, tva=0.18):
    return round(prix * (1 + tva), 2)

print(calculer_prix(10000))        # 11800.0 (TVA par défaut)
print(calculer_prix(10000, 0.20))  # 12000.0 (TVA personnalisée)
```
</details>

---

**Exercice 3 — Retour multiple**

Créez une fonction `analyser_notes(notes)` qui retourne un tuple `(moyenne, minimum, maximum)`.

<details>
<summary>👀 Voir la solution</summary>

```python
def analyser_notes(notes):
    moyenne = sum(notes) / len(notes)
    return moyenne, min(notes), max(notes)

moy, mini, maxi = analyser_notes([14, 16, 12, 18, 10])
print(f"Moyenne : {moy}, Min : {mini}, Max : {maxi}")
```
</details>

---

**Exercice 4 — Lambda et tri**

Vous avez une liste de dictionnaires représentant des produits :
```python
produits = [
    {"nom": "Ordinateur", "prix": 850000},
    {"nom": "Souris",     "prix": 15000},
    {"nom": "Clavier",    "prix": 25000}
]
```
Triez cette liste par prix croissant en utilisant `sorted()` et une fonction `lambda`.

<details>
<summary>👀 Voir la solution</summary>

```python
produits = [
    {"nom": "Ordinateur", "prix": 850000},
    {"nom": "Souris",     "prix": 15000},
    {"nom": "Clavier",    "prix": 25000}
]

produits_tries = sorted(produits, key=lambda p: p["prix"])
for p in produits_tries:
    print(f"{p['nom']} : {p['prix']} FCFA")
```
</details>

---

**Exercice 5 — Map et Filter**

Avec la liste `temperatures = [22, 35, 18, 40, 25, 15, 30]` :
a) Utilisez `filter()` pour garder les températures ≥ 25
b) Utilisez `map()` pour convertir toutes les températures de Celsius en Fahrenheit (`F = C × 9/5 + 32`)

<details>
<summary>👀 Voir la solution</summary>

```python
temperatures = [22, 35, 18, 40, 25, 15, 30]

# a)
chaudes = list(filter(lambda t: t >= 25, temperatures))
print(chaudes)  # [35, 40, 25, 30]

# b)
fahrenheit = list(map(lambda c: c * 9/5 + 32, temperatures))
print(fahrenheit)  # [71.6, 95.0, 64.4, 104.0, 77.0, 59.0, 86.0]
```
</details>

---

**Exercice 6 — \*args**

Créez une fonction `produit(*nombres)` qui retourne le produit de tous les nombres fournis (utilisez une boucle, pas `reduce`).

<details>
<summary>👀 Voir la solution</summary>

```python
def produit(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

print(produit(2, 3, 4))     # 24
print(produit(5, 5))        # 25
print(produit(1, 2, 3, 4, 5)) # 120
```
</details>

---

### 🏆 Challenge bonus — Pipeline de traitement

Vous recevez des données brutes de ventes d'un bootcamp de data science. Créez un pipeline de fonctions qui :

1. `charger_ventes()` : retourne une liste de dictionnaires `{"produit": ..., "quantite": ..., "prix_unitaire": ...}`
2. `calculer_totaux(ventes)` : ajoute une clé `"total"` à chaque vente (`quantite × prix_unitaire`)
3. `filtrer_grosses_ventes(ventes, seuil)` : garde seulement les ventes avec `total >= seuil`
4. `chiffre_affaires_total(ventes)` : utilise `reduce` pour calculer le CA total

```python
ventes_brutes = [
    {"produit": "Formation SQL",    "quantite": 15, "prix_unitaire": 25000},
    {"produit": "Formation Python", "quantite": 20, "prix_unitaire": 35000},
    {"produit": "Formation ML",     "quantite": 8,  "prix_unitaire": 50000},
]
```

<details>
<summary>👀 Voir la solution</summary>

```python
from functools import reduce

def charger_ventes():
    return [
        {"produit": "Formation SQL",    "quantite": 15, "prix_unitaire": 25000},
        {"produit": "Formation Python", "quantite": 20, "prix_unitaire": 35000},
        {"produit": "Formation ML",     "quantite": 8,  "prix_unitaire": 50000},
    ]

def calculer_totaux(ventes):
    for v in ventes:
        v["total"] = v["quantite"] * v["prix_unitaire"]
    return ventes

def filtrer_grosses_ventes(ventes, seuil):
    return [v for v in ventes if v["total"] >= seuil]

def chiffre_affaires_total(ventes):
    return reduce(lambda acc, v: acc + v["total"], ventes, 0)

# Pipeline complet
ventes = charger_ventes()
ventes = calculer_totaux(ventes)
grosses_ventes = filtrer_grosses_ventes(ventes, 400000)
ca_total = chiffre_affaires_total(ventes)

print("--- Toutes les ventes ---")
for v in ventes:
    print(v)

print("\n--- Grosses ventes (≥ 400 000) ---")
for v in grosses_ventes:
    print(v)

print(f"\nChiffre d'affaires total : {ca_total} FCFA")
```
</details>

---

*📘 Fin du Chapitre 4 — Fonctions Python | Bootcamp Data Science*
