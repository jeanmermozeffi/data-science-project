# 🐍 Introduction to Python — Cours Bootcamp Data Science

> **Chapitre 1** | Nouveau module : Python pour la Data Science

---

## Table des matières

1. [Qu'est-ce que Python ?](#1-quest-ce-que-python-)
2. [Python vs Autres langages](#2-python-vs-autres-langages--comparaison-de-la-syntaxe)
3. [Caractéristiques de Python](#3-caractéristiques-de-python)
4. [Applications Python](#4-applications-python)
5. [Google Colab](#5-google-colab)
6. [Conclusion](#6-conclusion)
7. [✅ Point de contrôle — Introduction à Python](#7--point-de-contrôle--introduction-à-python)

---

## 1. Qu'est-ce que Python ?

### 🔍 Définition

**Python** est un **langage de programmation interprété, généraliste et open source**, créé par **Guido van Rossum** et publié pour la première fois en **1991**. Son nom s'inspire non pas du serpent, mais de l'émission comique britannique *Monty Python's Flying Circus* — ce qui reflète bien la philosophie fun et accessible du langage.

> 💡 **Analogie** : Si les langages de programmation étaient des outils, Python serait un **couteau suisse**. Il n'est pas forcément le meilleur dans chaque domaine spécifique, mais il est **polyvalent, facile à prendre en main** et capable de faire presque tout — du développement web à l'intelligence artificielle.

### 🏛️ Un peu d'histoire

| Année | Événement |
|-------|-----------|
| 1989 | Guido van Rossum commence à développer Python pendant les fêtes de Noël |
| 1991 | Publication de Python 0.9.0 (première version) |
| 2000 | Python 2.0 — introduction de la gestion mémoire automatique |
| 2008 | Python 3.0 — réécriture majeure (non rétrocompatible) |
| 2020 | Fin du support officiel de Python 2 |
| Aujourd'hui | Python est le **langage n°1 mondial** selon les indices TIOBE et IEEE |

### 🎯 La philosophie Python — Le Zen de Python

Python repose sur une philosophie bien précise, résumée dans le célèbre **Zen de Python** (PEP 20). Ses principes fondateurs :

```python
import this  # Taper cette commande dans Python pour afficher le Zen complet
```

Les principes clés :

```
✦ Beautiful is better than ugly.
  → Un code beau vaut mieux qu'un code laid.

✦ Simple is better than complex.
  → La simplicité prime sur la complexité.

✦ Readability counts.
  → La lisibilité du code est essentielle.

✦ There should be one obvious way to do it.
  → Il doit y avoir une façon évidente de faire les choses.
```

> 💡 Ces principes expliquent pourquoi Python est si populaire pour l'enseignement et la recherche : il **ressemble presque à du pseudocode lisible**.

---

## 2. Python vs Autres langages — Comparaison de la syntaxe

Voyons comment Python se compare aux autres langages populaires sur une tâche simple : **afficher "Bonjour, Monde !" et calculer la somme de 1 à 5**.

### 2.1 Afficher un message

```
┌───────────────┬──────────────────────────────────────────────┐
│   Langage     │           Code                               │
├───────────────┼──────────────────────────────────────────────┤
│ Python        │ print("Bonjour, Monde !")                    │
├───────────────┼──────────────────────────────────────────────┤
│ Java          │ public class Main {                          │
│               │   public static void main(String[] args) {   │
│               │     System.out.println("Bonjour, Monde !"); │
│               │   }                                          │
│               │ }                                            │
├───────────────┼──────────────────────────────────────────────┤
│ C             │ #include <stdio.h>                           │
│               │ int main() {                                 │
│               │   printf("Bonjour, Monde !\n");              │
│               │   return 0;                                  │
│               │ }                                            │
├───────────────┼──────────────────────────────────────────────┤
│ JavaScript    │ console.log("Bonjour, Monde !");              │
└───────────────┴──────────────────────────────────────────────┘
```

### 2.2 Calculer la somme de 1 à 5

**Python :**
```python
nombres = [1, 2, 3, 4, 5]
total = sum(nombres)
print(total)  # Affiche : 15
```

**Java :**
```java
int[] nombres = {1, 2, 3, 4, 5};
int total = 0;
for (int n : nombres) {
    total += n;
}
System.out.println(total);
```

**C :**
```c
int nombres[] = {1, 2, 3, 4, 5};
int total = 0;
for (int i = 0; i < 5; i++) {
    total += nombres[i];
}
printf("%d\n", total);
```

### 2.3 Tableau comparatif global

| Critère | Python | Java | C/C++ | JavaScript | R |
|---------|--------|------|-------|------------|---|
| **Facilité d'apprentissage** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Lisibilité** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Vitesse d'exécution** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Data Science / ML** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **Développement web** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| **Écosystème bibliothèques** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

> 🎯 **Conclusion** : Pour la Data Science, Python est le choix n°1 mondial. Son seul point faible par rapport à C ou Java est la **vitesse d'exécution brute** — mais les bibliothèques Python comme NumPy sont optimisées en C en coulisses, ce qui compense largement.

---

## 3. Caractéristiques de Python

### 3.1 Vue d'ensemble

```
PYTHON
│
├── 🟢 Interprété        → Exécution ligne par ligne, sans compilation
├── 🟢 Langage de haut niveau → Proche du langage humain
├── 🟢 Typage dynamique  → Pas besoin de déclarer les types
├── 🟢 Multi-paradigme   → Orienté objet, fonctionnel, impératif
├── 🟢 Open Source       → Gratuit et libre
├── 🟢 Multi-plateforme  → Windows, Mac, Linux, cloud
└── 🟢 Grande communauté → Des millions de bibliothèques disponibles
```

### 3.2 Interprété vs Compilé

```
LANGAGE COMPILÉ (C, Java)          LANGAGE INTERPRÉTÉ (Python)
───────────────────────            ────────────────────────────
Code source                        Code source
    ↓                                  ↓
Compilation (étape séparée)        Interpréteur (ligne par ligne)
    ↓                                  ↓
Fichier exécutable                 Résultat immédiat
    ↓
Exécution

→ Plus rapide à l'exécution        → Plus rapide à développer
→ Erreurs détectées avant run      → Erreurs détectées à l'exécution
```

### 3.3 Typage dynamique

En Python, vous n'avez **pas besoin de déclarer le type** d'une variable. Python le détermine automatiquement.

```python
# Python — typage dynamique
x = 10          # Python sait que x est un entier
x = "Bonjour"   # x devient maintenant une chaîne — pas d'erreur !
x = 3.14        # x devient un flottant

# Java — typage statique (pour comparaison)
# int x = 10;
# x = "Bonjour";  ← ERREUR de compilation en Java !
```

### 3.4 Indentation obligatoire

En Python, l'**indentation (décalage)** n'est pas juste une convention de style — elle fait partie de la **syntaxe du langage**. Elle remplace les accolades `{}` des autres langages.

```python
# ✅ Indentation correcte
if 5 > 3:
    print("5 est plus grand que 3")   # Indenté → appartient au if
    print("Ceci aussi")               # Toujours dans le if
print("Ceci est en dehors du if")     # Pas indenté → hors du if

# ❌ Indentation incorrecte → Erreur !
if 5 > 3:
print("Erreur !")   # IndentationError : expected an indented block
```

### 3.5 Syntaxe claire et lisible

```python
# Python ressemble à de l'anglais lisible

# Vérifier si un nombre est pair
nombre = 8
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")

# Créer une liste et l'itérer
fruits = ["mangue", "papaye", "banane"]
for fruit in fruits:
    print(f"J'aime les {fruit}s")
```

### 3.6 Multi-paradigme

Python supporte plusieurs **styles de programmation** :

```python
# 1. IMPÉRATIF (séquentiel, étape par étape)
total = 0
for i in range(1, 6):
    total += i
print(total)  # 15

# 2. FONCTIONNEL (fonctions comme objets)
total = sum(range(1, 6))
print(total)  # 15

# 3. ORIENTÉ OBJET (classes et objets)
class Etudiant:
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note

    def mention(self):
        if self.note >= 16:
            return "Très bien"
        elif self.note >= 14:
            return "Bien"
        else:
            return "Assez bien"

alice = Etudiant("Alice", 17)
print(f"{alice.nom} : {alice.mention()}")  # Alice : Très bien
```

---

## 4. Applications Python

Python est utilisé dans des domaines extrêmement variés. Voici les principaux, avec les bibliothèques associées.

### 4.1 Data Science & Analyse de données 📊

C'est **le domaine principal** de notre bootcamp.

```python
import pandas as pd
import numpy as np

# Créer un DataFrame (tableau de données)
data = {
    'Produit': ['A', 'B', 'C'],
    'Ventes':  [4500, 7800, 11200]
}
df = pd.DataFrame(data)
print(df)
print(f"\nVentes moyennes : {df['Ventes'].mean()}")
```

**Bibliothèques clés :**

| Bibliothèque | Rôle |
|-------------|------|
| `NumPy` | Calcul numérique, matrices, algèbre linéaire |
| `Pandas` | Manipulation et analyse de données tabulaires |
| `Matplotlib` | Visualisation de données (graphiques) |
| `Seaborn` | Visualisation statistique avancée |
| `SciPy` | Calcul scientifique et statistiques |

### 4.2 Machine Learning & Intelligence Artificielle 🤖

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Exemple simple de régression linéaire
X = np.array([[1], [2], [3], [4], [5]])  # Heures d'étude
y = np.array([2, 4, 5, 4, 5])            # Notes

modele = LinearRegression()
modele.fit(X, y)
prediction = modele.predict([[6]])
print(f"Prédiction pour 6 heures : {prediction[0]:.2f}")
```

**Bibliothèques clés :**

| Bibliothèque | Rôle |
|-------------|------|
| `Scikit-learn` | Machine Learning (classification, régression, clustering) |
| `TensorFlow` | Deep Learning (Google) |
| `PyTorch` | Deep Learning (Meta) |
| `Keras` | Interface simplifiée pour le Deep Learning |
| `XGBoost` | Algorithmes de boosting (compétitions Kaggle) |

### 4.3 Visualisation de données 📈

```python
import matplotlib.pyplot as plt

produits = ['A', 'B', 'C']
ventes   = [4500, 7800, 11200]

plt.bar(produits, ventes, color=['#3498db', '#2ecc71', '#e74c3c'])
plt.title('Ventes par produit')
plt.xlabel('Produit')
plt.ylabel('Quantité vendue')
plt.show()
```

### 4.4 Développement Web 🌐

```python
# Avec Flask (framework léger)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def accueil():
    return "Bienvenue sur mon API Data Science !"

# Avec Django (framework complet)
# → Utilisé par Instagram, Pinterest, Disqus
```

**Bibliothèques clés :**

| Bibliothèque | Rôle |
|-------------|------|
| `Flask` | Framework web léger, idéal pour les APIs |
| `Django` | Framework web complet et robuste |
| `FastAPI` | APIs haute performance (très populaire en ML) |

### 4.5 Automatisation & Scripting 🤖

```python
import os

# Lister tous les fichiers CSV dans un dossier
dossier = "./data"
for fichier in os.listdir(dossier):
    if fichier.endswith(".csv"):
        print(f"Fichier trouvé : {fichier}")
```

### 4.6 Vue d'ensemble des domaines

```
                    PYTHON
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Data Science    Web Dev     Automatisation
   & IA / ML       & APIs      & Scripting
   (NumPy,         (Flask,     (os, sys,
   Pandas,         Django,     selenium,
   Sklearn,        FastAPI)    requests)
   TensorFlow)
        │
        ▼
  Finance quantitative, NLP,
  Computer Vision, IoT, Jeux...
```

---

## 5. Google Colab

### 🔍 Qu'est-ce que Google Colab ?

**Google Colaboratory** (Colab) est un **environnement de développement Python gratuit** basé sur le navigateur, hébergé par Google. Il permet d'écrire et d'exécuter du code Python directement depuis votre navigateur, **sans aucune installation**.

> 💡 **Analogie** : Google Colab est à Python ce que Google Docs est à Word — vous travaillez directement dans le navigateur, vos fichiers sont sauvegardés dans Google Drive, et vous pouvez **collaborer en temps réel**.

**Accès :** [https://colab.research.google.com](https://colab.research.google.com)

### 5.1 Pourquoi utiliser Google Colab ?

```
AVANTAGES DE GOOGLE COLAB
│
├── ✅ Gratuit          → Aucun abonnement requis
├── ✅ Zéro installation → Fonctionne dans le navigateur
├── ✅ GPU/TPU gratuits  → Accélération pour le Machine Learning
├── ✅ Bibliothèques pré-installées → NumPy, Pandas, TensorFlow...
├── ✅ Sauvegarde auto   → Intégré à Google Drive
├── ✅ Partage facile    → Comme un Google Docs
└── ✅ Format Notebook   → Code + texte + graphiques dans un seul fichier
```

### 5.2 L'interface de Google Colab

```
┌────────────────────────────────────────────────────────────┐
│  📓 Mon_Notebook.ipynb                    🔗 Partager      │
├────────────────────────────────────────────────────────────┤
│  + Code  |  + Texte         ▶ Exécuter tout                │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  [Cellule Texte - Markdown]                                │
│  # Mon premier notebook                                    │
│  Voici une analyse de données avec Python.                 │
│                                                            │
├────────────────────────────────────────────────────────────┤
│  [Cellule Code]                                            │
│  ▶ │ print("Bonjour depuis Colab !")                       │
│    │                                                       │
│    │ Bonjour depuis Colab !          ← Résultat            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 5.3 Les deux types de cellules

#### Cellule Code
```python
# Ceci est une cellule de CODE
# Appuyez sur ▶ ou Shift+Enter pour exécuter

x = 10
y = 20
print(f"La somme est : {x + y}")
# Résultat : La somme est : 30
```

#### Cellule Texte (Markdown)
```markdown
# Titre principal
## Sous-titre

Voici mon **analyse** de données en Python.
- Point 1
- Point 2

Une formule mathématique : $\bar{x} = \frac{\sum x_i}{n}$
```

### 5.4 Raccourcis clavier essentiels

| Raccourci | Action |
|-----------|--------|
| `Shift + Enter` | Exécuter la cellule et passer à la suivante |
| `Ctrl + Enter` | Exécuter la cellule sans avancer |
| `Ctrl + M + B` | Insérer une cellule en dessous |
| `Ctrl + M + A` | Insérer une cellule au dessus |
| `Ctrl + M + D` | Supprimer la cellule courante |
| `Ctrl + M + M` | Convertir en cellule Texte |
| `Ctrl + M + Y` | Convertir en cellule Code |

### 5.5 Installer une bibliothèque dans Colab

```python
# Installer une bibliothèque non disponible par défaut
!pip install seaborn

# Vérifier la version d'une bibliothèque
import pandas as pd
print(pd.__version__)
```

### 5.6 Connecter Google Drive

```python
# Monter Google Drive pour accéder à vos fichiers
from google.colab import drive
drive.mount('/content/drive')

# Accéder à un fichier CSV dans Drive
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data/mon_fichier.csv')
print(df.head())
```

### 5.7 Activer le GPU gratuit

Pour les calculs de Machine Learning intensifs :
```
Menu → Exécution → Modifier le type d'exécution → GPU
```

```python
# Vérifier que le GPU est disponible
import tensorflow as tf
print("GPU disponible :", tf.config.list_physical_devices('GPU'))
```

### 5.8 Premier notebook — Mise en pratique

Voici votre **premier notebook complet** à créer dans Google Colab :

```python
# ============================================
# 🐍 Mon premier notebook Python
# ============================================

# Cellule 1 : Variables et types de données
nom = "Data Scientist"
age = 25
note = 18.5
est_etudiant = True

print(f"Nom    : {nom}")
print(f"Âge    : {age}")
print(f"Note   : {note}")
print(f"Étudiant : {est_etudiant}")

# Cellule 2 : Opérations de base
a = 10
b = 3
print(f"Addition       : {a + b}")
print(f"Soustraction   : {a - b}")
print(f"Multiplication : {a * b}")
print(f"Division       : {a / b:.2f}")
print(f"Puissance      : {a ** b}")
print(f"Modulo         : {a % b}")

# Cellule 3 : Première bibliothèque
import numpy as np

tableau = np.array([4, 8, 12, 6, 10, 15, 5, 7, 9])
print(f"\nTableau    : {tableau}")
print(f"Moyenne    : {tableau.mean():.2f}")
print(f"Écart type : {tableau.std():.2f}")
print(f"Maximum    : {tableau.max()}")
print(f"Minimum    : {tableau.min()}")
```

---

## 6. Conclusion

### 📌 Récapitulatif du chapitre

```
INTRODUCTION À PYTHON
│
├── Qu'est-ce que Python ?
│   └── Langage interprété, open source, créé en 1991
│       Philosophie : lisibilité et simplicité
│
├── Python vs autres langages
│   └── Syntaxe la plus concise et lisible
│       Champion incontesté de la Data Science
│
├── Caractéristiques clés
│   └── Interprété, dynamique, multi-paradigme,
│       indentation obligatoire, open source
│
├── Applications
│   └── Data Science, ML/IA, Web, Automatisation,
│       Finance, NLP, Computer Vision...
│
└── Google Colab
    └── Environnement gratuit dans le navigateur
        Notebooks = code + texte + visualisations
        GPU gratuit pour le Machine Learning
```

### 🔑 Points clés à retenir

1. Python est le **langage n°1 en Data Science** grâce à son écosystème de bibliothèques.
2. Sa syntaxe est **proche du langage naturel** — idéale pour apprendre et collaborer.
3. L'**indentation** est obligatoire en Python — elle structure le code.
4. Le **typage dynamique** simplifie l'écriture du code (pas de déclaration de type).
5. **Google Colab** est l'outil idéal pour commencer : gratuit, sans installation, avec GPU.
6. Un **notebook** combine code, résultats et documentation dans un seul fichier.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous plongerons dans les **fondamentaux de Python** : les types de données (`int`, `float`, `str`, `bool`), les structures de données (`list`, `dict`, `tuple`, `set`), les structures de contrôle (`if/else`, boucles `for` et `while`) et les fonctions.

---

## 7. ✅ Point de contrôle — Introduction à Python

### 📝 Questions théoriques

**Q1.** Qui a créé Python et en quelle année a-t-il été publié ?

<details>
<summary>👀 Voir la réponse</summary>

> Python a été créé par **Guido van Rossum** et publié pour la première fois en **1991**. Il s'inspire du nom de l'émission *Monty Python's Flying Circus*, pas du serpent.
</details>

---

**Q2.** Quelle est la différence entre un langage interprété et un langage compilé ? Donnez un exemple de chaque.

<details>
<summary>👀 Voir la réponse</summary>

> Un **langage compilé** (ex : C, Java) transforme le code source en fichier exécutable avant l'exécution — plus rapide à l'exécution mais nécessite une étape de compilation. Un **langage interprété** (ex : Python) exécute le code ligne par ligne directement — plus lent mais plus flexible et rapide à développer.
</details>

---

**Q3.** Que signifie le "typage dynamique" en Python ? Donnez un exemple.

<details>
<summary>👀 Voir la réponse</summary>

> Le typage dynamique signifie qu'on **n'a pas besoin de déclarer le type** d'une variable — Python le détermine automatiquement selon la valeur assignée.
> ```python
> x = 10        # x est un entier
> x = "Bonjour" # x devient une chaîne — pas d'erreur !
> x = 3.14      # x devient un flottant
> ```
</details>

---

**Q4.** Pourquoi l'indentation est-elle importante en Python ?

<details>
<summary>👀 Voir la réponse</summary>

> En Python, l'indentation **fait partie de la syntaxe** — elle n'est pas optionnelle. Elle délimite les blocs de code (if, for, fonctions, classes) et remplace les accolades `{}` des autres langages. Une mauvaise indentation provoque une `IndentationError`.
</details>

---

**Q5.** Citez 3 avantages de Google Colab pour un étudiant en Data Science.

<details>
<summary>👀 Voir la réponse</summary>

> 1. **Gratuit et sans installation** : accessible directement depuis le navigateur.
> 2. **Bibliothèques pré-installées** : NumPy, Pandas, Scikit-learn, TensorFlow sont disponibles immédiatement.
> 3. **GPU gratuit** : permet d'entraîner des modèles de Machine Learning sans matériel coûteux.
> (Bonus : sauvegarde automatique dans Google Drive, partage facile comme un Google Docs.)
</details>

---

### 💻 Exercices pratiques

> Réalisez ces exercices dans **Google Colab**.

---

**Exercice 1 — Prise en main de Colab**

Créez un nouveau notebook Google Colab et :
a) Ajoutez une cellule Texte avec votre nom et le titre "Mon premier notebook Python"
b) Ajoutez une cellule Code qui affiche `"Bonjour, Data Science !"` avec `print()`
c) Exécutez la cellule avec `Shift + Enter`

<details>
<summary>👀 Voir la solution</summary>

```python
# Cellule Code
print("Bonjour, Data Science !")
# Résultat : Bonjour, Data Science !
```
</details>

---

**Exercice 2 — Variables et opérations**

Créez des variables pour stocker les informations suivantes et affichez-les :
- Votre prénom (chaîne de caractères)
- Votre âge (entier)
- Votre note moyenne (décimal)
- Êtes-vous étudiant ? (booléen)

<details>
<summary>👀 Voir la solution</summary>

```python
prenom        = "Fatou"
age           = 23
note_moyenne  = 15.75
est_etudiant  = True

print(f"Prénom        : {prenom}")
print(f"Âge           : {age} ans")
print(f"Note moyenne  : {note_moyenne}/20")
print(f"Étudiant(e)   : {est_etudiant}")
```
</details>

---

**Exercice 3 — Opérations arithmétiques**

Calculez et affichez :
- La somme de 128 et 256
- Le produit de 15 par 7
- La division de 100 par 3 (arrondie à 2 décimales)
- 2 à la puissance 10
- Le reste de la division de 17 par 5

<details>
<summary>👀 Voir la solution</summary>

```python
print(f"Somme           : {128 + 256}")
print(f"Produit         : {15 * 7}")
print(f"Division        : {100 / 3:.2f}")
print(f"Puissance       : {2 ** 10}")
print(f"Reste (modulo)  : {17 % 5}")
```
</details>

---

**Exercice 4 — Première bibliothèque : NumPy**

Dans Google Colab, importez NumPy et créez un tableau avec les valeurs suivantes :
`[10, 20, 30, 40, 50]`

Puis affichez : la somme, la moyenne, le minimum et le maximum.

<details>
<summary>👀 Voir la solution</summary>

```python
import numpy as np

tableau = np.array([10, 20, 30, 40, 50])

print(f"Tableau  : {tableau}")
print(f"Somme    : {tableau.sum()}")
print(f"Moyenne  : {tableau.mean()}")
print(f"Minimum  : {tableau.min()}")
print(f"Maximum  : {tableau.max()}")
```
</details>

---

**Exercice 5 — Comparaison de syntaxes**

Sans exécuter le code, prédisez le résultat de ces instructions Python, puis vérifiez dans Colab :

```python
a = 5
b = 2
print(a + b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a // b)
```

<details>
<summary>👀 Voir la solution</summary>

```
7      ← addition
10     ← multiplication
2.5    ← division réelle
25     ← puissance (5²)
1      ← modulo (reste de 5/2)
2      ← division entière (floor division)
```
</details>

---

### 🏆 Challenge bonus

Recherchez et listez **5 entreprises africaines ou ivoiriennes** qui utilisent Python dans leurs projets (startups tech, fintech, agritech, etc.). Pour chacune, précisez :
- Le nom de l'entreprise
- Le domaine d'activité
- Comment Python pourrait y être utilisé (analyse de données, application web, automatisation...)

*Cet exercice vous aide à connecter Python avec le contexte local et à développer votre veille technologique.*

---

*📘 Fin du Chapitre 1 — Introduction à Python | Bootcamp Data Science*
