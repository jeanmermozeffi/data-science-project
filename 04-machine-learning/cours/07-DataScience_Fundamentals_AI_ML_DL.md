# 🧠 Fondamentaux de l'IA, du ML et du Deep Learning — Cours Bootcamp Data Science

> **Module Data Science — Intelligence Artificielle** | Prérequis : cours "Algorithmes de ML", notions de NumPy

---

## Table des matières

### Partie I — Vue d'ensemble
1. [IA, ML, DL : trois cercles emboîtés](#1-ia-ml-dl--trois-cercles-emboîtés)
2. [L'Intelligence Artificielle (IA)](#2-lintelligence-artificielle-ia)
3. [Le Machine Learning (ML)](#3-le-machine-learning-ml)
4. [Le Deep Learning (DL)](#4-le-deep-learning-dl)
5. [ML vs DL : quand choisir quoi ?](#5-ml-vs-dl--quand-choisir-quoi-)

### Partie II — Le neurone artificiel
6. [Du neurone biologique au neurone artificiel](#6-du-neurone-biologique-au-neurone-artificiel)
7. [L'anatomie d'un neurone : poids, biais, somme pondérée](#7-lanatomie-dun-neurone--poids-biais-somme-pondérée)
8. [Les fonctions d'activation](#8-les-fonctions-dactivation)

### Partie III — Le réseau de neurones
9. [Empiler les neurones : les couches](#9-empiler-les-neurones--les-couches)
10. [La propagation avant (Forward Propagation)](#10-la-propagation-avant-forward-propagation)
11. [Comment un réseau apprend : loss, backprop, descente de gradient](#11-comment-un-réseau-apprend--loss-backprop-descente-de-gradient)
12. [Le vocabulaire de l'entraînement (epochs, batch, learning rate)](#12-le-vocabulaire-de-lentraînement-epochs-batch-learning-rate)

### Partie IV — Panorama et pratique
13. [Les grandes familles d'architectures (CNN, RNN, Transformers)](#13-les-grandes-familles-darchitectures-cnn-rnn-transformers)
14. [Frameworks et écosystème](#14-frameworks-et-écosystème)
15. [Forces, limites et considérations éthiques](#15-forces-limites-et-considérations-éthiques)

### Partie V — Synthèse
16. [Conclusion](#16-conclusion)
17. [✅ Point de contrôle — Fondamentaux IA/ML/DL](#17--point-de-contrôle--fondamentaux-iamldl)

---

# PARTIE I — VUE D'ENSEMBLE

## 1. IA, ML, DL : trois cercles emboîtés

### 📖 L'idée essentielle

On confond souvent **Intelligence Artificielle**, **Machine Learning** et **Deep Learning**. En réalité, ce sont **trois cercles emboîtés** : le DL est un sous-domaine du ML, lui-même un sous-domaine de l'IA.

```
┌─────────────────────────────────────────────────────────┐
│  🤖 INTELLIGENCE ARTIFICIELLE (IA)                        │
│  « Faire faire à une machine des tâches qui               │
│    demanderaient de l'intelligence à un humain »          │
│                                                           │
│   ┌───────────────────────────────────────────────────┐  │
│   │  📊 MACHINE LEARNING (ML)                          │  │
│   │  « La machine APPREND des schémas à partir de      │  │
│   │    données, sans être explicitement programmée »   │  │
│   │                                                    │  │
│   │    ┌────────────────────────────────────────────┐  │  │
│   │    │  🧠 DEEP LEARNING (DL)                      │  │  │
│   │    │  « Du ML avec des réseaux de neurones       │  │  │
│   │    │    PROFONDS (plusieurs couches) »           │  │  │
│   │    └────────────────────────────────────────────┘  │  │
│   └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
   Chronologie : IA (1950s) ⊃ ML (1980s) ⊃ DL (2010s)
```

> 🔑 **Le raccourci mental** : *Toute IA n'est pas du ML ; tout ML n'est pas du DL ; mais tout DL est du ML, et tout ML est de l'IA.*

### 1.1 Un exemple qui traverse les trois

| Approche | Comment reconnaître un chat sur une photo ? |
|----------|---------------------------------------------|
| **IA classique** (règles) | On code à la main : « si 2 oreilles pointues ET moustaches ET… » → fragile, ne marche jamais bien |
| **ML classique** | On extrait des *features* (contours, textures) puis un algo apprend à classer → mieux, mais l'humain choisit les features |
| **Deep Learning** | Le réseau **apprend lui-même** les features (des contours aux formes aux « visages de chat ») → l'état de l'art |

---

## 2. L'Intelligence Artificielle (IA)

### 📖 Définition

L'**IA** est le domaine le plus large : **toute technique** permettant à une machine de simuler l'intelligence humaine — raisonner, percevoir, décider, comprendre le langage.

### 2.1 IA symbolique vs IA connexionniste

```
DEUX GRANDES ÉCOLES D'IA
│
├── 🔣 IA SYMBOLIQUE (« Good Old-Fashioned AI »)
│     Règles écrites par des humains : systèmes experts, arbres de règles
│     Ex : moteur d'échecs à règles, système de diagnostic médical à IF/THEN
│     → transparente mais rigide, ne s'adapte pas
│
└── 🕸️ IA CONNEXIONNISTE (apprentissage)
      La machine apprend à partir de données : c'est le Machine Learning
      → flexible, s'améliore avec les données, mais « boîte noire »
```

### 2.2 IA faible vs IA forte

| Type | Définition | Réalité en 2026 |
|------|------------|-----------------|
| **IA faible (étroite)** | Excelle sur **une** tâche précise | ✅ C'est TOUTE l'IA actuelle (reco d'image, traduction, ChatGPT) |
| **IA forte (générale, AGI)** | Intelligence humaine polyvalente | ❌ N'existe pas — objet de recherche et de débat |

> ⚠️ **Idée reçue** : les IA actuelles, même impressionnantes, restent des **IA faibles** — très fortes sur leur tâche, incapables de généraliser à tout comme un humain.

---

## 3. Le Machine Learning (ML)

### 📖 Rappel (cours "Algorithmes de ML")

Le **ML** apprend des schémas **à partir de données** au lieu de suivre des règles écrites à la main.

```
PROGRAMMATION CLASSIQUE          MACHINE LEARNING
Données + Règles → Réponses      Données + Réponses → Règles (apprises)
```

### 3.1 Les trois familles de ML

| Famille | Données | Objectif | Exemples |
|---------|---------|----------|----------|
| **Supervisé** | Avec labels | Prédire (régression/classification) | Régression linéaire, arbres, KNN |
| **Non supervisé** | Sans labels | Découvrir une structure | K-Means (clustering), PCA |
| **Par renforcement** | Récompenses | Apprendre par essai-erreur | Jeux (AlphaGo), robotique |

> 💡 Le DL peut s'appliquer aux **trois** familles — ce n'est pas une 4ᵉ catégorie, mais une **technique** (les réseaux de neurones) utilisable partout.

---

## 4. Le Deep Learning (DL)

### 📖 Définition

Le **Deep Learning** est du ML fondé sur des **réseaux de neurones artificiels profonds** — c'est-à-dire comportant **plusieurs couches cachées**. Le mot « deep » (profond) désigne le **nombre de couches**.

```
RÉSEAU PEU PROFOND              RÉSEAU PROFOND (Deep)
Entrée → 1 couche → Sortie      Entrée → couche → couche → couche → ... → Sortie
                                          (plusieurs couches "cachées")
```

### 4.1 La révolution du DL : l'apprentissage des features

C'est **LA** différence clé avec le ML classique :

```
ML CLASSIQUE                        DEEP LEARNING
────────────                        ─────────────
Humain conçoit les features         Le réseau APPREND les features
   ↓                                   ↓
"contours", "textures"...           couche 1 → contours
   ↓                                 couche 2 → formes
Algo apprend à classer               couche 3 → parties d'objets
                                     couche 4 → l'objet entier
→ dépend de l'expertise humaine     → apprend la hiérarchie tout seul
```

> 🔑 **La force du DL** : il **apprend automatiquement** les représentations utiles, des plus simples (contours) aux plus abstraites (« c'est un chat »). Plus besoin d'un expert pour concevoir les features.

### 4.2 Pourquoi le DL a explosé après 2010 ?

Trois ingrédients réunis :

```
🔺 DONNÉES massives (Big Data, Internet, images labellisées)
      +
🔺 PUISSANCE de calcul (GPU, puis TPU)
      +
🔺 ALGORITHMES (backpropagation, ReLU, architectures nouvelles)
      =
💥 La révolution Deep Learning (vision, langage, IA générative)
```

---

## 5. ML vs DL : quand choisir quoi ?

### 📊 Tableau de décision

| Critère | ML classique | Deep Learning |
|---------|--------------|---------------|
| **Volume de données** | Fonctionne dès des centaines/milliers | Exige beaucoup (10 000+, souvent millions) |
| **Type de données** | Tabulaire (colonnes) | Non structuré (images, son, texte) |
| **Features** | Conçues par l'humain | Apprises par le réseau |
| **Puissance requise** | CPU suffit souvent | GPU quasi indispensable |
| **Interprétabilité** | Souvent bonne (arbres) | Faible (« boîte noire ») |
| **Temps d'entraînement** | Rapide | Long |

### 🎯 La règle pratique

```
Mes données sont-elles TABULAIRES (lignes/colonnes) ?
│
├── OUI, et volume modéré
│      → ML classique (Random Forest, Gradient Boosting) — souvent MEILLEUR et plus simple
│
└── NON : images, audio, texte, vidéo — ET beaucoup de données
       → Deep Learning
```

> 🔑 **Contre-intuitif mais crucial** : sur des **données tabulaires**, le ML classique (notamment le **Gradient Boosting**) bat encore très souvent le Deep Learning. Le DL brille sur le **non structuré** (vision, langage, son). *Le DL n'est pas « meilleur » en soi — il est meilleur pour certains problèmes.*

---

# PARTIE II — LE NEURONE ARTIFICIEL

## 6. Du neurone biologique au neurone artificiel

### 📖 L'inspiration

Le neurone artificiel s'inspire (de loin) du neurone biologique : il **reçoit des signaux**, les **combine**, et **s'active** si le total dépasse un seuil.

```
NEURONE BIOLOGIQUE                NEURONE ARTIFICIEL
─────────────────                 ──────────────────
dendrites (reçoivent)      →      entrées x₁, x₂, ... xₙ
force des synapses         →      poids w₁, w₂, ... wₙ
corps cellulaire (somme)   →      somme pondérée + biais
axone (émet si seuil)      →      fonction d'activation → sortie
```

> ⚠️ **L'analogie a ses limites** : le neurone artificiel est un **modèle mathématique très simplifié**. Le cerveau est infiniment plus complexe. On s'inspire du principe, pas du fonctionnement réel.

---

## 7. L'anatomie d'un neurone : poids, biais, somme pondérée

### 📖 Le calcul d'un neurone

Un neurone fait **deux opérations** :

```
        x₁ ──w₁──┐
        x₂ ──w₂──┤
        x₃ ──w₃──┤──►  z = (w₁x₁ + w₂x₂ + w₃x₃) + b  ──►  a = f(z)  ──► sortie
        ...      │         └──── somme pondérée ────┘      └activation┘
        xₙ ──wₙ──┘              + biais
```

**Étape 1 — Somme pondérée + biais :**

$$z = \sum_{i=1}^{n} w_i x_i + b = w_1x_1 + w_2x_2 + \dots + w_nx_n + b$$

**Étape 2 — Activation :**

$$a = f(z)$$

| Élément | Rôle | Analogie |
|---------|------|----------|
| **Entrées $x_i$** | Les données (features) | ce que le neurone « voit » |
| **Poids $w_i$** | Importance de chaque entrée | ce que le réseau **apprend** |
| **Biais $b$** | Décalage / seuil ajustable | règle la « facilité » à s'activer |
| **Activation $f$** | Introduit la non-linéarité | décide de la « force » du signal émis |

> 🔑 **Ce que le réseau apprend = les poids et les biais.** L'entraînement consiste précisément à trouver les **bonnes valeurs** de tous les $w$ et $b$.

### 7.1 En NumPy (un neurone)

```python
import numpy as np

x = np.array([0.5, 0.3, 0.2])      # entrées
w = np.array([0.4, 0.7, 0.1])      # poids (appris)
b = 0.1                             # biais

z = np.dot(w, x) + b               # somme pondérée + biais
a = 1 / (1 + np.exp(-z))           # activation sigmoïde
print(z, a)
```

---

## 8. Les fonctions d'activation

### 📖 Pourquoi une activation ?

Sans fonction d'activation **non linéaire**, empiler des neurones reviendrait à une simple **combinaison linéaire** — incapable d'apprendre des relations complexes. L'activation **casse la linéarité** et donne au réseau sa puissance.

> 🔑 **Sans non-linéarité, un réseau profond = une seule couche linéaire.** L'activation est ce qui rend le « deep » utile.

### 8.1 Les activations incontournables

```
SIGMOÏDE                    TANH                      ReLU
σ(z)=1/(1+e⁻ᶻ)              tanh(z)                   max(0, z)
     1 ┤    ___              1 ┤    ___                 ┤      /
       │   /                   │   /                    │     /
   0.5 ┤  /                  0 ┤──/──                   │    /
       │ /                     │ /                    0 ┤───/────
     0 ┤_/                  -1 ┤/                       │
       └──────                 └──────                  └──────
   sortie ∈ [0,1]          sortie ∈ [-1,1]          sortie ∈ [0,+∞[
```

| Fonction | Formule | Sortie | Usage typique |
|----------|---------|--------|---------------|
| **Sigmoïde** | $1/(1+e^{-z})$ | [0, 1] | Sortie **binaire** (probabilité) |
| **Tanh** | $\tanh(z)$ | [-1, 1] | Couches cachées (centrée en 0) |
| **ReLU** | $\max(0, z)$ | [0, +∞[ | ⭐ Défaut des couches cachées (rapide, évite le gradient qui s'évanouit) |
| **Softmax** | $e^{z_i}/\sum e^{z_j}$ | probabilités | Sortie **multiclasse** (somme = 1) |

> 🔑 **Les réflexes** : **ReLU** dans les couches cachées ; **sigmoïde** pour une sortie binaire ; **softmax** pour une sortie multiclasse.

---

# PARTIE III — LE RÉSEAU DE NEURONES

## 9. Empiler les neurones : les couches

### 📖 Structure d'un réseau

Un **réseau de neurones** organise les neurones en **couches** :

```
COUCHE          COUCHE(S)           COUCHE
D'ENTRÉE        CACHÉE(S)           DE SORTIE
                                    
  x₁ ●─────────► ● ───┐
                      ├──► ●
  x₂ ●─────────► ● ───┤         ┌──► ŷ  (prédiction)
                      ├──► ● ───┤
  x₃ ●─────────► ● ───┘         └──► ŷ₂
                                    
 (features)   (apprend les       (résultat)
              représentations)
```

| Couche | Rôle |
|--------|------|
| **Entrée** | Reçoit les features (1 neurone par variable) |
| **Cachée(s)** | Apprend des représentations intermédiaires. « Profond » = plusieurs couches cachées |
| **Sortie** | Produit la prédiction (1 neurone en régression, N en classification) |

> 💡 **Réseau *dense* / *fully connected*** : chaque neurone d'une couche est relié à **tous** les neurones de la couche suivante. C'est le type de base (le *Perceptron multicouche*, MLP).

---

## 10. La propagation avant (Forward Propagation)

### 📖 Faire une prédiction

La **propagation avant** consiste à faire circuler les données de l'entrée vers la sortie, couche par couche, en appliquant à chaque fois **somme pondérée → activation**.

```
FORWARD PROPAGATION (le réseau "réfléchit")
                                                   
 Entrée  ──►  Couche 1  ──►  Couche 2  ──►  Sortie
   x         z=Wx+b          z=Wa+b          ŷ
             a=f(z)          a=f(z)
             
 →→→→→→→→→→→→→→ sens du calcul →→→→→→→→→→→→→→
```

En notation matricielle, pour une couche : $\mathbf{a} = f(\mathbf{W}\mathbf{x} + \mathbf{b})$.

```python
import numpy as np

def relu(z):    return np.maximum(0, z)
def sigmoid(z): return 1 / (1 + np.exp(-z))

# Un réseau : 3 entrées → 2 neurones cachés (ReLU) → 1 sortie (sigmoïde)
x  = np.array([0.5, 0.3, 0.2])
W1 = np.array([[0.4, 0.7, 0.1], [0.2, 0.5, 0.6]])   # (2 neurones, 3 entrées)
b1 = np.array([0.1, 0.2])
W2 = np.array([[0.3, 0.9]])                          # (1 neurone, 2 entrées)
b2 = np.array([0.05])

a1 = relu(W1 @ x + b1)       # couche cachée
y  = sigmoid(W2 @ a1 + b2)   # sortie
print("Prédiction :", y)
```

---

## 11. Comment un réseau apprend : loss, backprop, descente de gradient

### 📖 La boucle d'apprentissage

Au début, les poids sont **aléatoires** → les prédictions sont mauvaises. L'apprentissage corrige les poids en **répétant** ce cycle :

```
BOUCLE D'ENTRAÎNEMENT
│
1️⃣  FORWARD    : le réseau prédit ŷ à partir de x
        │
2️⃣  LOSS       : on mesure l'erreur entre ŷ et la vraie valeur y
        │        (ex. MSE en régression, cross-entropy en classification)
        │
3️⃣  BACKWARD   : rétropropagation — on calcule COMMENT chaque poids
   (backprop)    a contribué à l'erreur (gradient = dérivée de la loss)
        │
4️⃣  UPDATE     : descente de gradient — on ajuste chaque poids dans
        │        le sens qui RÉDUIT l'erreur :  w ← w - η × gradient
        │
        └──► on recommence (epoch suivante) jusqu'à convergence
```

### 11.1 La fonction de perte (Loss)

Elle **quantifie l'erreur**. Le but de l'entraînement : la **minimiser**.

| Problème | Loss typique |
|----------|--------------|
| Régression | MSE (erreur quadratique moyenne) |
| Classification binaire | Binary cross-entropy (log loss) |
| Classification multiclasse | Categorical cross-entropy |

### 11.2 La descente de gradient (intuition)

> 💡 **Analogie de la montagne dans le brouillard** : vous êtes en haut d'une vallée, dans le brouillard, et voulez descendre au point le plus bas (erreur minimale). Vous ne voyez rien, mais vous **sentez la pente** sous vos pieds (le **gradient**) et faites un pas vers le bas. En répétant, vous atteignez le fond.

```
 Loss │*                          η (learning rate) = taille du pas
      │ *                         
      │  *         w ← w - η × (∂Loss/∂w)
      │   *●  ← on descend        
      │    ╲___                   trop grand → on saute le minimum
      │        ╲___●              trop petit → on descend trop lentement
      │            ╲__●___ ← minimum (bons poids)
      └────────────────────── valeur du poids w
```

### 11.3 La rétropropagation (Backpropagation)

C'est l'algorithme qui calcule **efficacement** le gradient de la loss par rapport à **chaque** poids, en propageant l'erreur **de la sortie vers l'entrée** (sens inverse du forward), via la **règle de dérivation en chaîne**.

> 🔑 **En une phrase** : le *forward* calcule la prédiction ; la *loss* mesure l'erreur ; la *backprop* distribue la « responsabilité » de l'erreur à chaque poids ; la *descente de gradient* corrige les poids. On répète des milliers de fois.

---

## 12. Le vocabulaire de l'entraînement (epochs, batch, learning rate)

| Terme | Définition | Analogie |
|-------|------------|----------|
| **Epoch** | Un passage complet sur **tout** le jeu d'entraînement | une révision complète du cours |
| **Batch** | Un sous-groupe d'exemples traités ensemble avant une mise à jour | réviser par paquets de fiches |
| **Iteration** | Une mise à jour des poids (un batch) | une correction |
| **Learning rate (η)** | Taille du pas de la descente de gradient | vitesse d'apprentissage |
| **Optimiseur** | L'algorithme d'update (SGD, **Adam**…) | la stratégie de descente |

> ⚠️ **Le learning rate est l'hyperparamètre le plus sensible** : trop grand, l'apprentissage diverge ; trop petit, il rampe. **Adam** est l'optimiseur par défaut le plus robuste aujourd'hui.

> 💡 **Lien avec l'overfitting (cours métriques)** : trop d'epochs → le réseau **mémorise** le train (overfitting). On surveille la loss sur un jeu de **validation** et on arrête tôt (*early stopping*).

---

# PARTIE IV — PANORAMA ET PRATIQUE

## 13. Les grandes familles d'architectures (CNN, RNN, Transformers)

Le réseau *dense* (MLP) est la base. Pour des données spécifiques, on utilise des architectures spécialisées :

| Architecture | Spécialité | Idée clé | Applications |
|--------------|-----------|----------|--------------|
| **MLP / Dense** | Données tabulaires | Neurones tous connectés | Classification/régression de base |
| **CNN** (convolutif) | 🖼️ Images | Filtres qui balaient l'image, détectent des motifs locaux | Vision, reconnaissance faciale, imagerie médicale |
| **RNN / LSTM** | 🔤 Séquences | Mémoire de ce qui précède | Séries temporelles, texte (historiquement) |
| **Transformers** | 🔤 Langage, et + | Mécanisme d'**attention** (relie tous les éléments entre eux) | ⭐ ChatGPT, traduction, vision moderne |

> 🔑 **Les Transformers (2017)** ont révolutionné l'IA : ils sont au cœur des **grands modèles de langage** (LLM) comme Claude ou GPT. L'attention permet de traiter de longues séquences en parallèle, bien mieux que les RNN.

---

## 14. Frameworks et écosystème

| Outil | Rôle | Niveau |
|-------|------|--------|
| **scikit-learn** | ML classique + `MLPClassifier` (petit réseau) | Débutant, prototypage |
| **TensorFlow / Keras** | Deep Learning (Google) | Keras = haut niveau, accessible |
| **PyTorch** | Deep Learning (Meta) | ⭐ Standard de la recherche, flexible |
| **Hugging Face** | Modèles pré-entraînés (Transformers) | Réutiliser des modèles existants |

> 💡 **Transfer learning** : plutôt que d'entraîner un réseau **from scratch** (coûteux, exige énormément de données), on **réutilise** un modèle déjà entraîné et on l'**adapte** à sa tâche. C'est la pratique dominante en DL appliqué.

---

## 15. Forces, limites et considérations éthiques

### ✅ Forces du Deep Learning
- Performances **état de l'art** sur images, son, langage.
- **Apprend les features** automatiquement.
- **S'améliore** avec plus de données.

### ⚠️ Limites
- **Gourmand en données** et en calcul (coût, énergie).
- **Boîte noire** : difficile d'expliquer une décision → problème en santé, justice, crédit.
- **Sensible aux biais** des données d'entraînement.
- Peut se tromper avec **une confiance élevée** (pas de « je ne sais pas »).

### ⚖️ Éthique et responsabilité
> 🔑 Un modèle apprend **les biais présents dans ses données**. Un système de recrutement entraîné sur des données historiques biaisées **reproduira** ces discriminations. Le data scientist est **responsable** de : auditer les biais, protéger la vie privée, garantir l'explicabilité et mesurer l'impact environnemental. *La performance ne dispense jamais de l'éthique.*

---

# PARTIE V — SYNTHÈSE

## 16. Conclusion

### 🎓 Ce qu'il faut absolument retenir

1. **IA ⊃ ML ⊃ DL** : trois cercles emboîtés. L'IA est le but (simuler l'intelligence), le ML une approche (apprendre des données), le DL une technique du ML (réseaux profonds).

2. **La force du Deep Learning** : il **apprend lui-même** les représentations (features), des plus simples aux plus abstraites — là où le ML classique dépend d'un expert humain.

3. **Le neurone** = somme pondérée des entrées + biais, suivie d'une **activation non linéaire**. Ce que le réseau **apprend**, ce sont les **poids et les biais**.

4. **L'activation non linéaire** (ReLU, sigmoïde, softmax) est indispensable : sans elle, un réseau profond se réduit à une seule couche linéaire.

5. **Un réseau apprend** en boucle : *forward* (prédire) → *loss* (mesurer l'erreur) → *backprop* (calculer les gradients) → *descente de gradient* (corriger les poids). Répété sur de nombreuses **epochs**.

6. **ML vs DL** : sur des données **tabulaires**, le ML classique (Gradient Boosting) reste souvent le meilleur. Le DL domine sur le **non structuré** (images, son, texte).

7. **Architectures** : MLP (tabulaire), CNN (images), RNN (séquences), **Transformers** (langage, cœur des LLM).

8. **Responsabilité** : puissance ne veut pas dire neutralité. Biais, explicabilité, vie privée et éthique sont partie intégrante du métier.

### 🧭 Le mémo en une image

```
┌──────────────────────────────────────────────────────────────┐
│  IA ⊃ ML ⊃ DL                                                  │
│                                                                │
│  NEURONE : z = Σ wᵢxᵢ + b  →  a = f(z)   (f = ReLU/sigmoïde)   │
│  RÉSEAU  : entrée → couches cachées → sortie                   │
│  APPREND : forward → loss → backprop → descente de gradient    │
│                                                                │
│  Tabulaire → ML classique   |   Images/son/texte → Deep Learning│
└──────────────────────────────────────────────────────────────┘
```

> 🔑 **En une phrase** : *un réseau de neurones n'est qu'un empilement de « somme pondérée + activation » dont on ajuste les poids, encore et encore, pour réduire l'erreur — la « magie » de l'IA moderne, c'est ça, répété à très grande échelle.*

---

## 17. ✅ Point de contrôle — Fondamentaux IA/ML/DL

### 🧠 Questions de compréhension

<details>
<summary><b>1. Quelle est la relation entre IA, ML et DL ?</b></summary>

Trois cercles emboîtés : le **DL** est un sous-ensemble du **ML**, lui-même un sous-ensemble de l'**IA**. Tout DL est du ML et de l'IA ; mais toute IA n'est pas du ML (ex. systèmes à règles).
</details>

<details>
<summary><b>2. Qu'est-ce qui distingue fondamentalement le Deep Learning du ML classique ?</b></summary>

Le DL **apprend automatiquement les features** (représentations), des plus simples aux plus abstraites. En ML classique, c'est l'humain qui conçoit les features à partir de son expertise.
</details>

<details>
<summary><b>3. Que calcule un neurone artificiel ?</b></summary>

Deux étapes : (1) une **somme pondérée** des entrées plus un biais, $z = \sum w_i x_i + b$ ; (2) une **fonction d'activation** $a = f(z)$ qui introduit la non-linéarité.
</details>

<details>
<summary><b>4. Pourquoi une fonction d'activation non linéaire est-elle indispensable ?</b></summary>

Sans elle, empiler des couches revient à une seule transformation **linéaire** : le réseau ne pourrait apprendre que des relations linéaires. La non-linéarité (ReLU, sigmoïde…) donne au réseau profond sa puissance d'expression.
</details>

<details>
<summary><b>5. Que le réseau « apprend »-il exactement pendant l'entraînement ?</b></summary>

Les **poids** ($w$) et les **biais** ($b$) de tous les neurones. L'entraînement cherche les valeurs qui minimisent la fonction de perte.
</details>

<details>
<summary><b>6. Décrivez la boucle d'apprentissage en 4 étapes.</b></summary>

**Forward** (prédire ŷ) → **Loss** (mesurer l'erreur vs y) → **Backpropagation** (calculer le gradient de la loss pour chaque poids) → **Descente de gradient** (mettre à jour les poids : $w \leftarrow w - \eta \nabla$). On répète sur plusieurs epochs.
</details>

<details>
<summary><b>7. À quoi sert le learning rate, et que se passe-t-il s'il est mal réglé ?</b></summary>

Il fixe la **taille du pas** de la descente de gradient. Trop **grand** : l'apprentissage diverge ou saute le minimum. Trop **petit** : convergence très lente. C'est l'hyperparamètre le plus sensible.
</details>

<details>
<summary><b>8. Pour des données tabulaires, faut-il forcément du Deep Learning ?</b></summary>

Non. Sur du **tabulaire**, le ML classique — surtout le **Gradient Boosting** — est souvent **meilleur, plus simple et plus rapide** que le DL. Le DL s'impose sur les données **non structurées** (images, audio, texte).
</details>

<details>
<summary><b>9. Associez chaque architecture à son usage : CNN, RNN, Transformer.</b></summary>

**CNN** → images (motifs locaux via convolutions). **RNN/LSTM** → séquences/séries temporelles (mémoire du passé). **Transformer** → langage et modèles génératifs (mécanisme d'attention ; cœur des LLM comme Claude/GPT).
</details>

<details>
<summary><b>10. Citez deux limites ou risques majeurs du Deep Learning.</b></summary>

Par exemple : (1) **boîte noire** peu explicable (problématique en santé/justice/crédit) ; (2) **reproduction des biais** des données ; (3) besoin massif de **données et de calcul** ; (4) confiance élevée même quand il se trompe.
</details>

### 🛠️ Exercice pratique

Voir le **Checkpoint 9 — Réseau de neurones simple** ([`08-DataScience_Checkpoint9_Neural_Network.md`](08-DataScience_Checkpoint9_Neural_Network.md)) : construire un neurone puis un petit réseau en NumPy (forward), et entraîner un `MLPClassifier` sur un vrai dataset, avec explication de chaque étape.

---

*📘 Module Data Science — Fondamentaux de l'IA, du ML et du Deep Learning | Bootcamp Data Science*
