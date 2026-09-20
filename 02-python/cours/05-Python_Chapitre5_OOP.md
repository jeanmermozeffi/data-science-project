# 🏛️ Object Oriented Programming (OOP) — Cours Bootcamp Data Science

> **Chapitre 5** | Prérequis : Chapitres 1 à 4 (Introduction, Bases, Data Structures, Fonctions)

---

## Table des matières

1. [Fundamentals of OOP — Fondamentaux](#1-fundamentals-of-oop--fondamentaux-de-la-poo)
2. [Build Your First Class — Créer sa première classe](#2-build-your-first-class--créer-sa-première-classe)
3. [Details — Approfondissement](#3-details--approfondissement)
4. [Principles of OOP — Les 4 piliers](#4-principles-of-object-oriented-programming--les-4-piliers)
5. [Creating a Bank Account — Exemple complet](#5-creating-a-bank-account--exemple-complet)
6. [OOP One to One — Relations entre classes](#6-oop-one-to-one--relations-entre-classes)
7. [Conclusion](#7-conclusion)
8. [✅ Point de contrôle — OOP](#8--point-de-contrôle--oop)

---

## 1. Fundamentals of OOP — Fondamentaux de la POO

### 📖 Qu'est-ce que la Programmation Orientée Objet ?

La **Programmation Orientée Objet** (POO, ou OOP en anglais) est un **paradigme de programmation** qui organise le code autour d'**objets**, plutôt qu'autour de fonctions et de logique pure (programmation procédurale, vue aux chapitres précédents).

> 💡 **Analogie** : Jusqu'ici, vous avez utilisé des fonctions et des dictionnaires séparément pour représenter un étudiant (`{"nom": "Alice", "note": 16}` + une fonction `evaluer_note()`). La POO permet de **fusionner les données ET les comportements** en un seul concept : un **objet**. C'est comme construire un moule (la **classe**) pour fabriquer des objets qui possèdent à la fois des caractéristiques (attributs) et des capacités (méthodes).

### 1.1 Objet vs Classe

```
CLASSE = le moule / le plan          OBJET = ce qui est fabriqué avec le moule
─────────────────────────           ─────────────────────────────────────────
class Etudiant:                     alice = Etudiant("Alice", 23)
    (définit la STRUCTURE)          bob   = Etudiant("Bob", 25)
                                     (des INSTANCES concrètes)
```

> 💡 **Analogie** : La classe `Voiture` est comme le **plan d'architecte** d'un modèle de voiture. Chaque voiture réellement construite à partir de ce plan (une Toyota rouge, une Toyota bleue) est un **objet** (aussi appelé **instance**). Toutes partagent la même structure (4 roues, un moteur), mais chacune a ses propres valeurs (couleur, kilométrage).

### 1.2 Vocabulaire essentiel

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Classe** | Le modèle / plan qui définit une structure | `class Etudiant:` |
| **Objet / Instance** | Un exemplaire concret créé à partir d'une classe | `alice = Etudiant(...)` |
| **Attribut** | Une donnée / caractéristique de l'objet | `alice.nom`, `alice.age` |
| **Méthode** | Une fonction définie dans une classe (un comportement) | `alice.calculer_moyenne()` |
| **Constructeur** | Méthode spéciale exécutée à la création de l'objet | `__init__()` |
| **`self`** | Référence à l'instance elle-même dans une méthode | `self.nom` |

### 1.3 Pourquoi utiliser la POO ?

```
SANS POO (procédural)                   AVEC POO (orienté objet)
──────────────────────                  ──────────────────────────
etudiant1 = {"nom": "Alice", "note": 16}  class Etudiant:
etudiant2 = {"nom": "Bob",   "note": 12}      def __init__(self, nom, note):
                                                    self.nom = nom
def evaluer(etudiant):                             self.note = note
    if etudiant["note"] >= 10:
        return "Admis"                        def evaluer(self):
    return "Ajourné"                               if self.note >= 10:
                                                        return "Admis"
print(evaluer(etudiant1))                          return "Ajourné"

→ Données et logique séparées         alice = Etudiant("Alice", 16)
→ Facile de faire des erreurs         print(alice.evaluer())
  (oublier un champ, mauvaise clé)
                                       → Données et comportements
                                         regroupés, structure garantie
```

### 1.4 Domaines d'application en Data Science

```
LA POO EST PARTOUT EN DATA SCIENCE
│
├── 🔵 Scikit-learn   → chaque modèle ML est une classe (LinearRegression(), KMeans()...)
├── 🔵 Pandas          → DataFrame et Series sont des classes
├── 🔵 TensorFlow/Keras → les réseaux de neurones sont construits avec des classes
└── 🔵 Vos projets     → structurer un pipeline de données, un scraper, une API...
```

---

## 2. Build Your First Class — Créer sa première classe

### 📖 Syntaxe de base

```python
class NomDeLaClasse:
    def __init__(self, param1, param2):
        self.attribut1 = param1
        self.attribut2 = param2

    def une_methode(self):
        # logique utilisant self.attribut1, self.attribut2
        pass
```

> 🔑 **Convention Python (PEP 8)** : le nom d'une classe s'écrit en **PascalCase** (première lettre de chaque mot en majuscule) : `Etudiant`, `CompteBancaire`, `VoitureElectrique`.

### 2.1 Votre première classe

```python
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom  = nom
        self.age  = age
        self.note = note

# Créer des OBJETS (instances) à partir de la classe
alice = Etudiant("Alice", 23, 16.5)
bob   = Etudiant("Bob", 25, 12.0)

# Accéder aux attributs avec la notation pointée
print(alice.nom)    # Alice
print(alice.age)    # 23
print(bob.note)     # 12.0
```

### 2.2 Comprendre `__init__` et `self`

```
alice = Etudiant("Alice", 23, 16.5)
                    │       │    │
                    ▼       ▼    ▼
def __init__(self, nom,   age, note):
                │    │      │    │
                │    └──────┴────┴──► deviennent des ATTRIBUTS
                │                     via self.nom, self.age, self.note
                │
                └─► représente l'objet EN COURS DE CRÉATION (alice)
```

- **`__init__`** est le **constructeur** : une méthode spéciale automatiquement appelée quand on crée un nouvel objet.
- **`self`** représente **l'instance elle-même**. C'est toujours le **premier paramètre** de chaque méthode d'une classe — Python le fournit automatiquement, vous n'avez jamais besoin de le passer explicitement lors de l'appel.

```python
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom  = nom    # self.nom = attribut de CET objet précis
        self.age  = age
        self.note = note

alice = Etudiant("Alice", 23, 16.5)
bob   = Etudiant("Bob", 25, 12.0)

# self.nom d'alice ≠ self.nom de bob → chaque objet a SES PROPRES données
print(alice.nom, bob.nom)   # Alice Bob
```

### 2.3 Ajouter des méthodes (comportements)

```python
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom  = nom
        self.age  = age
        self.note = note

    def est_admis(self):
        """Retourne True si l'étudiant a la moyenne."""
        return self.note >= 10

    def afficher_profil(self):
        """Affiche les informations de l'étudiant."""
        statut = "Admis ✅" if self.est_admis() else "Ajourné ❌"
        print(f"{self.nom} ({self.age} ans) — Note : {self.note}/20 — {statut}")

alice = Etudiant("Alice", 23, 16.5)
bob   = Etudiant("Bob", 25, 8.0)

alice.afficher_profil()   # Alice (23 ans) — Note : 16.5/20 — Admis ✅
bob.afficher_profil()     # Bob (25 ans) — Note : 8.0/20 — Ajourné ❌

print(alice.est_admis())  # True
print(bob.est_admis())    # False
```

> 💡 Remarquez que dans `afficher_profil()`, on appelle `self.est_admis()` — **une méthode peut en appeler une autre** via `self`.

---

## 3. Details — Approfondissement

### 3.1 Attributs d'instance vs attributs de classe

```python
class Etudiant:
    # Attribut de CLASSE — partagé par TOUS les objets
    ecole = "Bootcamp Data Science Abidjan"

    def __init__(self, nom, note):
        # Attributs d'INSTANCE — propres à chaque objet
        self.nom  = nom
        self.note = note

alice = Etudiant("Alice", 16)
bob   = Etudiant("Bob", 14)

# Les attributs d'instance sont différents
print(alice.nom, bob.nom)      # Alice Bob

# L'attribut de classe est partagé (identique pour tous)
print(alice.ecole)             # Bootcamp Data Science Abidjan
print(bob.ecole)                # Bootcamp Data Science Abidjan
print(Etudiant.ecole)           # Accès direct via la classe
```

```
VISUALISATION
─────────────
class Etudiant:
    ecole = "Bootcamp..."    ← 1 SEULE copie, partagée par TOUS les objets

    alice.nom  = "Alice"     ← copie PROPRE à alice
    bob.nom    = "Bob"       ← copie PROPRE à bob
```

### 3.2 Compteur d'instances — Cas d'usage des attributs de classe

```python
class Etudiant:
    nombre_total = 0   # attribut de classe : compte tous les étudiants créés

    def __init__(self, nom):
        self.nom = nom
        Etudiant.nombre_total += 1   # incrémenté à chaque nouvelle instance

alice = Etudiant("Alice")
bob   = Etudiant("Bob")
claire = Etudiant("Claire")

print(f"Nombre d'étudiants créés : {Etudiant.nombre_total}")  # 3
```

### 3.3 Méthodes spéciales (dunder methods)

Les méthodes entourées de doubles underscores (`__methode__`) sont des **méthodes spéciales** que Python appelle automatiquement dans certaines situations.

```python
class Etudiant:
    def __init__(self, nom, note):
        self.nom  = nom
        self.note = note

    def __str__(self):
        """Définit ce qui s'affiche avec print(objet)."""
        return f"Étudiant({self.nom}, {self.note}/20)"

    def __eq__(self, autre):
        """Définit le comportement de l'opérateur ==."""
        return self.note == autre.note

alice = Etudiant("Alice", 16)
bob   = Etudiant("Bob", 16)

print(alice)              # Étudiant(Alice, 16/20)  ← grâce à __str__
print(alice == bob)       # True                    ← grâce à __eq__ (mêmes notes)
```

### 3.4 Attributs "privés" — Encapsulation légère

Python n'a pas de vrais attributs privés comme Java, mais utilise une **convention** avec des underscores.

```python
class CompteBancaire:
    def __init__(self, solde_initial):
        self._solde = solde_initial   # underscore = "usage interne" (convention)
        self.__code_secret = "1234"   # double underscore = plus fortement protégé

compte = CompteBancaire(1000)
print(compte._solde)          # 1000 — accessible mais déconseillé
# print(compte.__code_secret) # ❌ AttributeError (name mangling)
```

| Convention | Signification | Accessibilité |
|------------|----------------|----------------|
| `nom` | Public | Librement accessible |
| `_nom` | Protégé (convention) | Accessible mais "usage interne" |
| `__nom` | Privé (name mangling) | Très difficile d'accès depuis l'extérieur |

### 3.5 Méthodes avec paramètres supplémentaires

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} FCFA effectué. Nouveau solde : {self.solde}")

    def retirer(self, montant):
        if montant > self.solde:
            print("❌ Solde insuffisant")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} FCFA effectué. Nouveau solde : {self.solde}")

compte = CompteBancaire("Alice", 5000)
compte.deposer(2000)     # Dépôt de 2000 FCFA effectué. Nouveau solde : 7000
compte.retirer(1500)     # Retrait de 1500 FCFA effectué. Nouveau solde : 5500
compte.retirer(10000)    # ❌ Solde insuffisant
```

---

## 4. Principles of Object-Oriented Programming — Les 4 piliers

La POO repose sur **4 grands principes fondamentaux**, souvent résumés par l'acronyme **PEHA** (Polymorphisme, Encapsulation, Héritage, Abstraction).

```
LES 4 PILIERS DE LA POO
│
├── 🔒 Encapsulation    → Regrouper données + méthodes, cacher les détails internes
├── 👪 Héritage         → Une classe hérite des attributs/méthodes d'une autre
├── 🎭 Polymorphisme    → Une même méthode se comporte différemment selon l'objet
└── 🎨 Abstraction      → Cacher la complexité, exposer seulement l'essentiel
```

### 4.1 Encapsulation

L'**encapsulation** consiste à **regrouper les données et les méthodes** qui les manipulent dans une seule unité (la classe), tout en **protégeant l'accès direct** aux données sensibles.

```python
class CompteBancaire:
    def __init__(self, solde_initial):
        self.__solde = solde_initial   # attribut privé

    def consulter_solde(self):
        """Accès contrôlé au solde (lecture seule)."""
        return self.__solde

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("❌ Montant invalide")

compte = CompteBancaire(1000)
print(compte.consulter_solde())   # 1000 — accès via une méthode contrôlée
compte.deposer(500)
print(compte.consulter_solde())   # 1500

# On NE PEUT PAS modifier directement le solde depuis l'extérieur
# compte.__solde = 1000000   # Ne fonctionne pas comme prévu (name mangling)
```

> 💡 **Pourquoi c'est utile ?** L'encapsulation empêche de modifier accidentellement des données critiques (comme un solde bancaire) sans passer par une logique de validation.

### 4.2 Héritage

L'**héritage** permet à une classe (dite **classe fille** ou **sous-classe**) de **réutiliser les attributs et méthodes** d'une autre classe (dite **classe mère** ou **classe parente**), tout en pouvant les étendre ou les modifier.

> 💡 **Analogie** : Un `EtudiantBootcamp` est un cas particulier d'`Etudiant` — il possède tout ce qu'un étudiant possède (nom, âge), plus des caractéristiques propres (module suivi).

```python
# Classe MÈRE (parente)
class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

# Classe FILLE (hérite de Etudiant)
class EtudiantBootcamp(Etudiant):
    def __init__(self, nom, age, module):
        super().__init__(nom, age)   # appelle le constructeur de la classe mère
        self.module = module

    def se_presenter(self):
        # redéfinit (override) la méthode de la classe mère
        super().se_presenter()       # réutilise la version parente
        print(f"Je suis en formation {self.module} au bootcamp.")

alice = EtudiantBootcamp("Alice", 23, "Data Science")
alice.se_presenter()
# Je m'appelle Alice et j'ai 23 ans.
# Je suis en formation Data Science au bootcamp.
```

**Visualisation de l'héritage :**
```
              ┌───────────────┐
              │   Etudiant    │      ← Classe MÈRE
              │  nom, age     │
              │  se_presenter │
              └───────┬───────┘
                       │ hérite de
                       ▼
              ┌────────────────────┐
              │ EtudiantBootcamp   │  ← Classe FILLE
              │ + module           │     (hérite de nom, age)
              │ se_presenter()     │     (redéfinit la méthode)
              │   [override]       │
              └────────────────────┘
```

```python
# super() permet d'accéder aux méthodes de la classe parente
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def parler(self):
        print(f"{self.nom} fait un bruit.")

class Chien(Animal):
    def parler(self):
        print(f"{self.nom} aboie : Wouf !")

class Chat(Animal):
    def parler(self):
        print(f"{self.nom} miaule : Miaou !")

animaux = [Chien("Rex"), Chat("Minou"), Animal("Créature")]
for animal in animaux:
    animal.parler()
# Rex aboie : Wouf !
# Minou miaule : Miaou !
# Créature fait un bruit.
```

### 4.3 Polymorphisme

Le **polymorphisme** ("plusieurs formes") signifie qu'une **même méthode** peut avoir des **comportements différents** selon la classe de l'objet qui l'appelle. L'exemple ci-dessus (`Chien`, `Chat`, `Animal` ayant chacun leur propre `parler()`) est justement un exemple de polymorphisme.

```python
class Forme:
    def aire(self):
        return 0   # valeur par défaut

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur  = largeur
    def aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return 3.14159 * self.rayon ** 2

# Polymorphisme : même méthode .aire(), comportements différents
formes = [Rectangle(5, 3), Cercle(4), Rectangle(2, 2)]

for forme in formes:
    print(f"{type(forme).__name__} — Aire : {forme.aire():.2f}")
# Rectangle — Aire : 15.00
# Cercle — Aire : 50.27
# Rectangle — Aire : 4.00
```

> 💡 **Pourquoi c'est puissant ?** On peut traiter des objets de classes différentes de **manière uniforme** (une boucle unique appelant `.aire()`), sans se soucier du type exact de chaque objet.

### 4.4 Abstraction

L'**abstraction** consiste à **cacher la complexité interne** d'un objet et à n'exposer que ce qui est nécessaire à l'utilisateur.

```python
class ModeleMachineLearning:
    def __init__(self, donnees):
        self.donnees = donnees
        self.__poids = None   # détails internes cachés

    def entrainer(self):
        # Toute la complexité mathématique est CACHÉE ici
        print("Entraînement en cours... (logique complexe cachée)")
        self.__poids = [0.5, 0.3, 0.2]   # simplifié pour l'exemple
        print("✅ Modèle entraîné !")

    def predire(self, nouvelle_donnee):
        # L'utilisateur n'a pas besoin de savoir COMMENT la prédiction est calculée
        print(f"Prédiction pour {nouvelle_donnee} : résultat calculé")

modele = ModeleMachineLearning(donnees=[1, 2, 3, 4, 5])
modele.entrainer()          # L'utilisateur appelle juste .entrainer()
modele.predire(10)          # ... sans connaître les calculs internes
```

> 💡 **Analogie** : Quand vous conduisez une voiture, vous utilisez le volant et les pédales (**interface simple**) sans avoir besoin de comprendre le fonctionnement du moteur (**complexité cachée**). C'est exactement ce que fait `scikit-learn` : `modele.fit(X, y)` cache des calculs mathématiques complexes derrière une interface simple.

### 4.5 Tableau récapitulatif des 4 piliers

| Principe | Ce qu'il fait | Mot-clé Python |
|----------|----------------|-----------------|
| **Encapsulation** | Protège les données, regroupe données + comportements | `_attribut`, `__attribut` |
| **Héritage** | Réutilise le code d'une classe parente | `class Fille(Mere):`, `super()` |
| **Polymorphisme** | Une méthode se comporte différemment selon l'objet | Redéfinition de méthodes |
| **Abstraction** | Cache la complexité, expose une interface simple | Méthodes publiques vs privées |

---

## 5. Creating a Bank Account — Exemple complet

Construisons ensemble une classe `CompteBancaire` complète, illustrant tous les concepts vus jusqu'ici.

### 5.1 Version de base

```python
class CompteBancaire:
    """Représente un compte bancaire simple."""

    banque = "Banque Bootcamp Data Science"   # attribut de classe
    nombre_comptes = 0                         # compteur global

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self._solde    = solde_initial          # protégé (convention)
        self.historique = []                    # liste des opérations

        CompteBancaire.nombre_comptes += 1
        self._enregistrer("Ouverture du compte", solde_initial)

    def _enregistrer(self, operation, montant):
        """Méthode interne pour tracer les opérations."""
        self.historique.append(f"{operation} : {montant} FCFA")

    def deposer(self, montant):
        if montant <= 0:
            print("❌ Le montant doit être positif")
            return
        self._solde += montant
        self._enregistrer("Dépôt", montant)
        print(f"✅ Dépôt de {montant} FCFA. Nouveau solde : {self._solde} FCFA")

    def retirer(self, montant):
        if montant <= 0:
            print("❌ Le montant doit être positif")
            return
        if montant > self._solde:
            print(f"❌ Solde insuffisant (solde actuel : {self._solde} FCFA)")
            return
        self._solde -= montant
        self._enregistrer("Retrait", montant)
        print(f"✅ Retrait de {montant} FCFA. Nouveau solde : {self._solde} FCFA")

    def consulter_solde(self):
        return self._solde

    def afficher_historique(self):
        print(f"\n--- Historique de {self.titulaire} ---")
        for operation in self.historique:
            print(f"  • {operation}")

    def __str__(self):
        return f"Compte de {self.titulaire} — Solde : {self._solde} FCFA"
```

### 5.2 Utiliser la classe

```python
# Créer des comptes
compte_alice = CompteBancaire("Alice", 10000)
compte_bob   = CompteBancaire("Bob")   # solde_initial=0 par défaut

# Effectuer des opérations
compte_alice.deposer(5000)
compte_alice.retirer(3000)
compte_alice.retirer(50000)   # échoue : solde insuffisant

compte_bob.deposer(2000)

# Afficher les informations
print(compte_alice)              # Compte de Alice — Solde : 12000 FCFA
compte_alice.afficher_historique()

print(f"\nNombre total de comptes créés : {CompteBancaire.nombre_comptes}")
```

**Résultat attendu :**
```
✅ Dépôt de 5000 FCFA. Nouveau solde : 15000 FCFA
✅ Retrait de 3000 FCFA. Nouveau solde : 12000 FCFA
❌ Solde insuffisant (solde actuel : 12000 FCFA)
✅ Dépôt de 2000 FCFA. Nouveau solde : 2000 FCFA
Compte de Alice — Solde : 12000 FCFA

--- Historique de Alice ---
  • Ouverture du compte : 10000 FCFA
  • Dépôt : 5000 FCFA
  • Retrait : 3000 FCFA

Nombre total de comptes créés : 2
```

### 5.3 Étendre avec l'héritage — CompteEpargne

```python
class CompteEpargne(CompteBancaire):
    """Compte bancaire avec taux d'intérêt (hérite de CompteBancaire)."""

    def __init__(self, titulaire, solde_initial=0, taux_interet=0.03):
        super().__init__(titulaire, solde_initial)   # réutilise le constructeur parent
        self.taux_interet = taux_interet

    def appliquer_interets(self):
        """Ajoute les intérêts annuels au solde (méthode propre à CompteEpargne)."""
        interets = self._solde * self.taux_interet
        self._solde += interets
        self._enregistrer("Intérêts appliqués", round(interets, 2))
        print(f"💰 Intérêts de {interets:.2f} FCFA appliqués. Nouveau solde : {self._solde:.2f} FCFA")

# Utilisation
epargne = CompteEpargne("Claire", 100000, taux_interet=0.05)
epargne.deposer(20000)          # méthode héritée de CompteBancaire
epargne.appliquer_interets()    # méthode propre à CompteEpargne
print(epargne)                  # __str__ hérité de CompteBancaire
```

---

## 6. OOP One to One — Relations entre classes

### 📖 Définition

Une relation **« un à un » (one-to-one)** existe quand **un objet d'une classe est associé à exactement un objet d'une autre classe**. C'est ce qu'on appelle la **composition** (ou **association**) en POO : une classe "contient" un objet d'une autre classe comme attribut.

> 💡 **Analogie** : Un `Etudiant` possède **une seule** `CarteEtudiant`. Une `Personne` a **une seule** `AdresseDomicile`. Ce n'est pas de l'héritage (l'étudiant n'*est* pas une carte), c'est de la **composition** (l'étudiant *possède* une carte).

### 6.1 Héritage vs Composition — Ne pas confondre

```
HÉRITAGE ("EST UN")                    COMPOSITION ("A UN")
─────────────────────                  ─────────────────────
class Animal: ...                      class Moteur: ...
class Chien(Animal): ...               class Voiture:
                                            def __init__(self):
Un Chien EST UN Animal                         self.moteur = Moteur()

                                        Une Voiture A UN Moteur
```

### 6.2 Exemple — Relation one-to-one Etudiant ↔ CarteEtudiant

```python
class CarteEtudiant:
    """Une carte étudiant appartient à UN SEUL étudiant."""

    def __init__(self, numero, date_expiration):
        self.numero = numero
        self.date_expiration = date_expiration

    def __str__(self):
        return f"Carte n°{self.numero} (expire le {self.date_expiration})"


class Etudiant:
    """Un étudiant possède UNE SEULE carte étudiant (relation one-to-one)."""

    def __init__(self, nom, numero_carte, date_expiration):
        self.nom = nom
        # Composition : Etudiant CONTIENT un objet CarteEtudiant
        self.carte = CarteEtudiant(numero_carte, date_expiration)

    def afficher_infos(self):
        print(f"{self.nom} — {self.carte}")


alice = Etudiant("Alice", "BC2024-001", "31/12/2025")
alice.afficher_infos()          # Alice — Carte n°BC2024-001 (expire le 31/12/2025)

# Accès à l'objet imbriqué via la notation pointée
print(alice.carte.numero)       # BC2024-001
print(alice.carte.date_expiration)  # 31/12/2025
```

**Visualisation de la relation one-to-one :**
```
┌─────────────────┐        possède         ┌────────────────────┐
│    Etudiant      │ ─────────1────1──────► │   CarteEtudiant    │
│  - nom            │                        │  - numero          │
│  - carte ─────────┼───────────────────────►│  - date_expiration │
└─────────────────┘                        └────────────────────┘

Un Etudiant a EXACTEMENT une CarteEtudiant
Une CarteEtudiant appartient à EXACTEMENT un Etudiant
```

### 6.3 Exemple — CompteBancaire ↔ Titulaire (relation one-to-one)

```python
class Personne:
    """Représente une personne (titulaire potentiel d'un compte)."""

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} ({self.email})"


class CompteBancaire:
    """Chaque compte appartient à EXACTEMENT une personne."""

    def __init__(self, titulaire: Personne, solde=0):
        self.titulaire = titulaire   # relation one-to-one : 1 compte → 1 titulaire
        self.solde = solde

    def afficher_details(self):
        print(f"Compte de {self.titulaire} — Solde : {self.solde} FCFA")


# Créer la personne D'ABORD
alice = Personne("Alice Dupont", "alice@email.com")

# Puis créer le compte en lui associant la personne
compte = CompteBancaire(titulaire=alice, solde=15000)

compte.afficher_details()          # Compte de Alice Dupont (alice@email.com) — Solde : 15000 FCFA
print(compte.titulaire.email)      # alice@email.com — accès à l'objet imbriqué
```

### 6.4 Pourquoi la composition (one-to-one) plutôt que tout mettre dans une seule classe ?

```python
# ❌ MOINS BON : tout entassé dans une seule classe
class CompteBancaireMonolithique:
    def __init__(self, nom_titulaire, email_titulaire, solde):
        self.nom_titulaire   = nom_titulaire
        self.email_titulaire = email_titulaire
        self.solde           = solde
    # Si demain on doit gérer aussi le téléphone, l'adresse...
    # → il faut modifier CETTE classe à chaque fois

# ✅ MEILLEUR : classes séparées avec composition
class Personne:
    def __init__(self, nom, email, telephone=None):
        self.nom = nom
        self.email = email
        self.telephone = telephone

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire   # réutilise la classe Personne
        self.solde = solde

# La classe Personne peut être réutilisée ailleurs :
# un Etudiant, un Client, un Employe... peuvent tous être des Personne
```

> 🔑 **Principe de conception** : Séparer les responsabilités en classes distinctes, puis les **relier** par composition, rend le code plus **modulaire**, plus **réutilisable** et plus **facile à maintenir** que d'entasser tous les attributs dans une seule grosse classe.

---

## 7. Conclusion

### 📌 Récapitulatif du chapitre

```
OBJECT ORIENTED PROGRAMMING (OOP)
│
├── Fondamentaux
│   ├── Classe = plan/moule    → class NomClasse:
│   └── Objet = instance créée → objet = NomClasse(...)
│
├── Créer une classe
│   ├── __init__(self, ...)    → constructeur
│   ├── self                    → référence à l'instance
│   ├── self.attribut           → donnée propre à l'objet
│   └── def methode(self):      → comportement de l'objet
│
├── Détails
│   ├── Attribut de classe      → partagé par tous les objets
│   ├── Attribut d'instance     → propre à chaque objet
│   ├── Méthodes spéciales      → __str__, __eq__...
│   └── _protégé / __privé      → convention d'encapsulation
│
├── Les 4 piliers
│   ├── Encapsulation  → protéger et regrouper données + comportements
│   ├── Héritage       → class Fille(Mere): + super()
│   ├── Polymorphisme  → même méthode, comportements différents
│   └── Abstraction    → cacher la complexité, exposer l'essentiel
│
└── Relations entre classes
    └── One-to-one (composition) → une classe CONTIENT un objet d'une autre
        (à distinguer de l'héritage : "A UN" vs "EST UN")
```

### 🔑 Points clés à retenir

1. Une **classe** est un plan ; un **objet** (instance) est ce qu'on construit à partir de ce plan.
2. **`__init__`** est le constructeur, appelé automatiquement à la création d'un objet.
3. **`self`** représente toujours l'instance courante — premier paramètre de chaque méthode.
4. Les **4 piliers** (Encapsulation, Héritage, Polymorphisme, Abstraction) structurent toute la logique orientée objet.
5. **Héritage** = "EST UN" (`class Fille(Mere)`) ; **Composition (one-to-one)** = "A UN" (un attribut qui est un objet d'une autre classe).
6. La POO est **omniprésente** dans les bibliothèques de Data Science (Scikit-learn, Pandas, TensorFlow) — comprendre les classes permet de mieux utiliser (et déboguer) ces outils.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons **NumPy**, la bibliothèque fondamentale du calcul numérique en Python — tableaux multidimensionnels (`ndarray`), opérations vectorisées et algèbre linéaire, qui s'appuient eux-mêmes largement sur les principes de la POO que vous venez d'apprendre.

---

## 8. ✅ Point de contrôle — OOP

### 📝 Questions théoriques

**Q1.** Quelle est la différence entre une classe et un objet ?

<details>
<summary>👀 Voir la réponse</summary>

> Une **classe** est le **plan/modèle** qui définit la structure (attributs) et les comportements (méthodes) d'un type d'objet. Un **objet** (ou instance) est un **exemplaire concret** créé à partir de cette classe, avec ses propres valeurs d'attributs. Exemple : `class Etudiant:` est la classe ; `alice = Etudiant("Alice", 23)` crée un objet.
</details>

---

**Q2.** À quoi sert `self` dans une méthode de classe ?

<details>
<summary>👀 Voir la réponse</summary>

> `self` représente **l'instance elle-même** sur laquelle la méthode est appelée. Il permet d'accéder et de modifier les attributs propres à cet objet précis (`self.nom`, `self.solde`...). C'est toujours le premier paramètre d'une méthode, et Python le fournit automatiquement lors de l'appel (`alice.methode()` équivaut à `Etudiant.methode(alice)`).
</details>

---

**Q3.** Quelle est la différence entre un attribut de classe et un attribut d'instance ?

<details>
<summary>👀 Voir la réponse</summary>

> Un **attribut de classe** est défini directement dans la classe (hors de `__init__`) et est **partagé par tous les objets** de cette classe (une seule copie en mémoire). Un **attribut d'instance** est défini avec `self.attribut = ...` dans `__init__` (ou une autre méthode) et est **propre à chaque objet** (chaque instance a sa propre copie).
</details>

---

**Q4.** Expliquez la différence entre héritage et composition avec un exemple pour chacun.

<details>
<summary>👀 Voir la réponse</summary>

> L'**héritage** exprime une relation "EST UN" : une classe fille hérite des attributs/méthodes d'une classe mère (`class Chien(Animal):` — un Chien EST UN Animal). La **composition** exprime une relation "A UN" : une classe contient un objet d'une autre classe comme attribut (`class Voiture: self.moteur = Moteur()` — une Voiture A UN Moteur). Le choix dépend de la nature de la relation entre les concepts modélisés.
</details>

---

**Q5.** Que fait `super()` dans une classe fille ?

<details>
<summary>👀 Voir la réponse</summary>

> `super()` permet d'appeler une méthode de la **classe parente** depuis la classe fille — le plus souvent `super().__init__(...)` pour réutiliser le constructeur du parent sans le réécrire entièrement. Cela évite la duplication de code et garantit que l'initialisation de la classe mère est correctement effectuée.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Première classe**

Créez une classe `Livre` avec les attributs `titre`, `auteur`, `annee`. Ajoutez une méthode `afficher()` qui affiche `"Titre (Auteur, Année)"`.

<details>
<summary>👀 Voir la solution</summary>

```python
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre  = titre
        self.auteur = auteur
        self.annee  = annee

    def afficher(self):
        print(f"{self.titre} ({self.auteur}, {self.annee})")

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre1.afficher()   # Le Petit Prince (Antoine de Saint-Exupéry, 1943)
```
</details>

---

**Exercice 2 — Attributs de classe**

Modifiez la classe `Livre` pour ajouter un attribut de classe `bibliotheque = "Bibliothèque du Bootcamp"` et un compteur `nombre_livres` incrémenté à chaque création.

<details>
<summary>👀 Voir la solution</summary>

```python
class Livre:
    bibliotheque = "Bibliothèque du Bootcamp"
    nombre_livres = 0

    def __init__(self, titre, auteur, annee):
        self.titre  = titre
        self.auteur = auteur
        self.annee  = annee
        Livre.nombre_livres += 1

livre1 = Livre("Le Petit Prince", "Saint-Exupéry", 1943)
livre2 = Livre("1984", "George Orwell", 1949)

print(Livre.bibliotheque)      # Bibliothèque du Bootcamp
print(Livre.nombre_livres)     # 2
```
</details>

---

**Exercice 3 — Héritage**

Créez une classe `Vehicule` avec `marque` et `vitesse_max`, et une méthode `decrire()`. Créez une classe `Voiture(Vehicule)` qui ajoute un attribut `nb_portes` et redéfinit `decrire()` pour inclure cette information (en réutilisant `super()`).

<details>
<summary>👀 Voir la solution</summary>

```python
class Vehicule:
    def __init__(self, marque, vitesse_max):
        self.marque = marque
        self.vitesse_max = vitesse_max

    def decrire(self):
        print(f"{self.marque} — Vitesse max : {self.vitesse_max} km/h")

class Voiture(Vehicule):
    def __init__(self, marque, vitesse_max, nb_portes):
        super().__init__(marque, vitesse_max)
        self.nb_portes = nb_portes

    def decrire(self):
        super().decrire()
        print(f"Nombre de portes : {self.nb_portes}")

voiture = Voiture("Toyota", 180, 4)
voiture.decrire()
# Toyota — Vitesse max : 180 km/h
# Nombre de portes : 4
```
</details>

---

**Exercice 4 — Polymorphisme**

Créez une classe `Employe` avec une méthode `calculer_salaire()` retournant `0`. Créez deux classes filles `EmployeFixe` (salaire fixe) et `EmployeCommission` (salaire = ventes × taux de commission), chacune redéfinissant `calculer_salaire()`. Parcourez une liste des deux types et affichez chaque salaire.

<details>
<summary>👀 Voir la solution</summary>

```python
class Employe:
    def __init__(self, nom):
        self.nom = nom
    def calculer_salaire(self):
        return 0

class EmployeFixe(Employe):
    def __init__(self, nom, salaire_fixe):
        super().__init__(nom)
        self.salaire_fixe = salaire_fixe
    def calculer_salaire(self):
        return self.salaire_fixe

class EmployeCommission(Employe):
    def __init__(self, nom, ventes, taux):
        super().__init__(nom)
        self.ventes = ventes
        self.taux = taux
    def calculer_salaire(self):
        return self.ventes * self.taux

employes = [
    EmployeFixe("Alice", 250000),
    EmployeCommission("Bob", 1000000, 0.05)
]

for e in employes:
    print(f"{e.nom} : {e.calculer_salaire()} FCFA")
# Alice : 250000 FCFA
# Bob : 50000.0 FCFA
```
</details>

---

**Exercice 5 — Relation One-to-One**

Créez une classe `Adresse` (rue, ville) et une classe `Personne` (nom, adresse) où chaque `Personne` possède **une seule** `Adresse` (composition). Affichez le nom et la ville de la personne.

<details>
<summary>👀 Voir la solution</summary>

```python
class Adresse:
    def __init__(self, rue, ville):
        self.rue = rue
        self.ville = ville

    def __str__(self):
        return f"{self.rue}, {self.ville}"

class Personne:
    def __init__(self, nom, rue, ville):
        self.nom = nom
        self.adresse = Adresse(rue, ville)   # composition (one-to-one)

    def afficher(self):
        print(f"{self.nom} habite à {self.adresse}")

p = Personne("Fatou", "Rue des Jardins", "Abidjan")
p.afficher()                  # Fatou habite à Rue des Jardins, Abidjan
print(p.adresse.ville)        # Abidjan
```
</details>

---

### 🏆 Challenge bonus — Système de gestion de bootcamp

Concevez un mini-système avec les classes suivantes :

1. `Personne` — attributs `nom`, `email`
2. `Formateur(Personne)` — hérite de `Personne`, ajoute `specialite`
3. `Etudiant(Personne)` — hérite de `Personne`, ajoute `notes` (liste), avec une méthode `moyenne()`
4. `Cours` — attributs `titre`, `formateur` (relation one-to-one avec `Formateur`), et une liste `etudiants_inscrits`, avec une méthode `inscrire(etudiant)` et `afficher_moyenne_classe()`

Testez votre système en créant un formateur, deux étudiants avec leurs notes, un cours, et affichez la moyenne de la classe.

<details>
<summary>👀 Voir une piste de solution</summary>

```python
class Personne:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

class Formateur(Personne):
    def __init__(self, nom, email, specialite):
        super().__init__(nom, email)
        self.specialite = specialite

class Etudiant(Personne):
    def __init__(self, nom, email):
        super().__init__(nom, email)
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def moyenne(self):
        return sum(self.notes) / len(self.notes) if self.notes else 0

class Cours:
    def __init__(self, titre, formateur):
        self.titre = titre
        self.formateur = formateur       # relation one-to-one
        self.etudiants_inscrits = []

    def inscrire(self, etudiant):
        self.etudiants_inscrits.append(etudiant)
        print(f"{etudiant.nom} inscrit(e) au cours {self.titre}")

    def afficher_moyenne_classe(self):
        if not self.etudiants_inscrits:
            print("Aucun étudiant inscrit")
            return
        moyennes = [e.moyenne() for e in self.etudiants_inscrits]
        moyenne_classe = sum(moyennes) / len(moyennes)
        print(f"Moyenne de la classe pour {self.titre} : {moyenne_classe:.2f}/20")


# Utilisation
formateur = Formateur("Jean Konan", "jean.konan@bootcamp.ci", "Machine Learning")

alice = Etudiant("Alice", "alice@email.com")
alice.ajouter_note(16)
alice.ajouter_note(18)

bob = Etudiant("Bob", "bob@email.com")
bob.ajouter_note(12)
bob.ajouter_note(14)

cours_ml = Cours("Machine Learning Avancé", formateur)
cours_ml.inscrire(alice)
cours_ml.inscrire(bob)

cours_ml.afficher_moyenne_classe()
# Moyenne de la classe pour Machine Learning Avancé : 15.00/20
```
</details>

---

*📘 Fin du Chapitre 5 — Object Oriented Programming | Bootcamp Data Science*
