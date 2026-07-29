# ✅ Correction — Checkpoint Mathématiques pour Data Science
## Statistiques, Types de données et Opérations matricielles

---

## 📋 Table des matières

1. [Rappel des données](#1-rappel-des-données)
2. [Partie 1 — Comprendre les données](#2-partie-1--comprendre-les-données)
3. [Partie 2 — Algèbre linéaire](#3-partie-2--algèbre-linéaire)
4. [Partie 3 — Questions conceptuelles](#4-partie-3--questions-conceptuelles)
5. [Récapitulatif des résultats](#5-récapitulatif-des-résultats)

---

## 1. Rappel des données

La matrice D représente les **quantités vendues** par région et par produit :

```
       Produit A   Produit B   Produit C
         ↓           ↓           ↓
D =  [  4           8          12  ]  ← Région 1
     [  6          10          15  ]  ← Région 2
     [  5           7           9  ]  ← Région 3
     [  3           6           9  ]  ← Région 4
```

**Colonnes extraites :**

| | Produit A | Produit B | Produit C |
|-|-----------|-----------|-----------|
| Région 1 | 4 | 8 | 12 |
| Région 2 | 6 | 10 | 15 |
| Région 3 | 5 | 7 | 9 |
| Région 4 | 3 | 6 | 9 |

---

## 2. Partie 1 — Comprendre les données

### 2.1 Types de données

Les éléments de la matrice D sont des **entiers naturels** (`ℤ⁺` / integers).

Plus précisément :

| Caractéristique | Détail |
|-----------------|--------|
| **Type mathématique** | Entiers positifs (ℤ⁺) |
| **Type informatique** | `int` (integer) |
| **Nature** | Données quantitatives discrètes |
| **Interprétation** | On ne peut pas vendre 4,5 unités → les quantités sont des valeurs entières |

> 💡 **Données quantitatives discrètes** : les valeurs sont numériques et ne peuvent prendre que des valeurs entières (on compte des unités, pas des mesures continues).

---

### 2.2 Statistiques descriptives

#### Formules utilisées

```
Moyenne   : x̄ = (Σ xᵢ) / n

Médiane   : valeur centrale après tri croissant
            - Si n pair : moyenne des deux valeurs centrales

Écart type : σ = √[ (Σ (xᵢ - x̄)²) / n ]
```

---

#### 📊 Produit A — colonne : [4, 6, 5, 3]

**Tri croissant :** 3, 4, 5, 6

**Moyenne :**
```
x̄_A = (4 + 6 + 5 + 3) / 4
     = 18 / 4
     = 4.5
```

**Médiane** (n=4, pair → moyenne des 2 valeurs centrales : 4 et 5) :
```
Médiane_A = (4 + 5) / 2 = 4.5
```

**Écart type :**
```
Écarts au carré :
  (4 - 4.5)² = (-0.5)² = 0.25
  (6 - 4.5)² = (1.5)²  = 2.25
  (5 - 4.5)² = (0.5)²  = 0.25
  (3 - 4.5)² = (-1.5)² = 2.25

Variance_A = (0.25 + 2.25 + 0.25 + 2.25) / 4
           = 5.00 / 4
           = 1.25

σ_A = √1.25 ≈ 1.118
```

---

#### 📊 Produit B — colonne : [8, 10, 7, 6]

**Tri croissant :** 6, 7, 8, 10

**Moyenne :**
```
x̄_B = (8 + 10 + 7 + 6) / 4
     = 31 / 4
     = 7.75
```

**Médiane** (valeurs centrales : 7 et 8) :
```
Médiane_B = (7 + 8) / 2 = 7.5
```

**Écart type :**
```
Écarts au carré :
  (8  - 7.75)² = (0.25)²  = 0.0625
  (10 - 7.75)² = (2.25)²  = 5.0625
  (7  - 7.75)² = (-0.75)² = 0.5625
  (6  - 7.75)² = (-1.75)² = 3.0625

Variance_B = (0.0625 + 5.0625 + 0.5625 + 3.0625) / 4
           = 8.75 / 4
           = 2.1875

σ_B = √2.1875 ≈ 1.479
```

---

#### 📊 Produit C — colonne : [12, 15, 9, 9]

**Tri croissant :** 9, 9, 12, 15

**Moyenne :**
```
x̄_C = (12 + 15 + 9 + 9) / 4
     = 45 / 4
     = 11.25
```

**Médiane** (valeurs centrales : 9 et 12) :
```
Médiane_C = (9 + 12) / 2 = 10.5
```

**Écart type :**
```
Écarts au carré :
  (12 - 11.25)² = (0.75)²  = 0.5625
  (15 - 11.25)² = (3.75)²  = 14.0625
  (9  - 11.25)² = (-2.25)² = 5.0625
  (9  - 11.25)² = (-2.25)² = 5.0625

Variance_C = (0.5625 + 14.0625 + 5.0625 + 5.0625) / 4
           = 24.75 / 4
           = 6.1875

σ_C = √6.1875 ≈ 2.487
```

---

#### Tableau récapitulatif — Statistiques descriptives

| Statistique | Produit A | Produit B | Produit C |
|-------------|-----------|-----------|-----------|
| **Moyenne** | 4.50 | 7.75 | 11.25 |
| **Médiane** | 4.50 | 7.50 | 10.50 |
| **Écart type** | ≈ 1.118 | ≈ 1.479 | ≈ 2.487 |

---

### 2.3 Variabilité

#### Formules utilisées

```
Étendue  : E = max - min
Variance : σ² = Σ (xᵢ - x̄)² / n
```

#### 📏 Produit A — [4, 6, 5, 3]

```
Étendue_A  = max - min = 6 - 3 = 3
Variance_A = 1.25   (calculée ci-dessus)
```

#### 📏 Produit B — [8, 10, 7, 6]

```
Étendue_B  = max - min = 10 - 6 = 4
Variance_B = 2.1875
```

#### 📏 Produit C — [12, 15, 9, 9]

```
Étendue_C  = max - min = 15 - 9 = 6
Variance_C = 6.1875
```

#### Tableau récapitulatif — Variabilité

| Mesure | Produit A | Produit B | Produit C |
|--------|-----------|-----------|-----------|
| **Minimum** | 3 | 6 | 9 |
| **Maximum** | 6 | 10 | 15 |
| **Étendue** | 3 | 4 | 6 |
| **Variance** | 1.25 | 2.1875 | 6.1875 |

> 💡 **Lecture** : Le Produit C a la plus grande variabilité (variance = 6.19, étendue = 6), ce qui signifie que les ventes de ce produit sont les plus irrégulières selon les régions.

---

## 3. Partie 2 — Algèbre linéaire

### 3.1 Transposée de la matrice D

La **transposée** d'une matrice consiste à **échanger les lignes et les colonnes** : la ligne i devient la colonne i.

```
        [ 4   8  12 ]              [ 4   6   5   3 ]
D    =  [ 6  10  15 ]    →  Dᵀ =  [ 8  10   7   6 ]
        [ 5   7   9 ]              [ 12  15   9   9 ]
        [ 3   6   9 ]
```

**Vérification :**
- D est de dimension **(4 × 3)**
- Dᵀ est de dimension **(3 × 4)** ✅
- L'élément D[1][2] = 8 devient Dᵀ[2][1] = 8 ✅

---

### 3.2 Multiplication D × P (Calcul des revenus)

Le vecteur de prix **P = [5, 10, 15]ᵀ** (colonne) représente le prix unitaire de chaque produit.

```
P = [ 5  ]   (Prix produit A)
    [ 10 ]   (Prix produit B)
    [ 15 ]   (Prix produit C)
```

La multiplication **D × P** donne le **revenu total par région** :

```
D (4×3)  ×  P (3×1)  =  R (4×1)
```

**Calcul pour chaque région :**

```
Région 1 : R₁ = (4×5) + (8×10)  + (12×15)
              =  20   +  80      +  180
              = 280

Région 2 : R₂ = (6×5) + (10×10) + (15×15)
              =  30   +  100     +  225
              = 355

Région 3 : R₃ = (5×5) + (7×10)  + (9×15)
              =  25   +  70      +  135
              = 230

Région 4 : R₄ = (3×5) + (6×10)  + (9×15)
              =  15   +  60      +  135
              = 210
```

**Résultat :**

```
        [ 280 ]   ← Région 1
R = D×P = [ 355 ]   ← Région 2
        [ 230 ]   ← Région 3
        [ 210 ]   ← Région 4
```

| Région | Calcul détaillé | Revenu total |
|--------|-----------------|--------------|
| Région 1 | (4×5) + (8×10) + (12×15) | **280** |
| Région 2 | (6×5) + (10×10) + (15×15) | **355** |
| Région 3 | (5×5) + (7×10) + (9×15) | **230** |
| Région 4 | (3×5) + (6×10) + (9×15) | **210** |

---

### 3.3 Identifier les modèles

#### 🏆 Région avec le revenu le plus élevé

```
R₁ = 280
R₂ = 355  ← MAXIMUM
R₃ = 230
R₄ = 210

→ La Région 2 génère le revenu le plus élevé : 355 unités monétaires.
```

> **Explication** : La Région 2 vend les plus grandes quantités sur les trois produits (6, 10, 15), en particulier sur le Produit C qui est le plus cher (prix = 15).

---

#### 📦 Chiffre d'affaires total par produit

Le CA total d'un produit = (somme des quantités vendues dans toutes les régions) × prix unitaire

**Produit A (prix = 5) :**
```
Total quantités A = 4 + 6 + 5 + 3 = 18
CA_A = 18 × 5 = 90
```

**Produit B (prix = 10) :**
```
Total quantités B = 8 + 10 + 7 + 6 = 31
CA_B = 31 × 10 = 310
```

**Produit C (prix = 15) :**
```
Total quantités C = 12 + 15 + 9 + 9 = 45
CA_C = 45 × 15 = 675
```

| Produit | Prix unitaire | Quantité totale | CA total |
|---------|---------------|-----------------|----------|
| Produit A | 5 | 18 | **90** |
| Produit B | 10 | 31 | **310** |
| Produit C | 15 | 45 | **675** |
| **TOTAL** | | **94** | **1 075** |

> 💡 **Vérification** : La somme des revenus par région doit égaler la somme des CA par produit :
> 280 + 355 + 230 + 210 = **1 075** ✅
> 90 + 310 + 675 = **1 075** ✅

> 💡 **Lecture** : Le Produit C contribue à lui seul à **62.8%** du chiffre d'affaires total (675/1075), malgré le fait que ses quantités vendues ne représentent que 47.9% du total. Son prix élevé (15) amplifie fortement son impact sur les revenus.

---

## 4. Partie 3 — Questions conceptuelles

### 4.1 Interprétation

#### Que nous indique la moyenne sur les ventes typiques ?

La moyenne représente la **valeur centrale attendue** des ventes de chaque produit, si toutes les régions avaient des performances uniformes.

| Produit | Moyenne | Interprétation |
|---------|---------|----------------|
| Produit A | **4.50** | En moyenne, chaque région vend 4 à 5 unités du Produit A — produit peu vendu |
| Produit B | **7.75** | En moyenne, chaque région vend environ 8 unités du Produit B — ventes modérées |
| Produit C | **11.25** | En moyenne, chaque région vend environ 11 unités du Produit C — produit le plus vendu |

> ⚠️ **Limite de la moyenne** : Elle peut être influencée par des valeurs extrêmes. Ici, pour le Produit C, la Région 2 (15 unités) tire la moyenne vers le haut par rapport aux Régions 3 et 4 (9 unités chacune). C'est pourquoi on compare toujours la moyenne **et** la médiane :
> - Produit C : moyenne = 11.25, médiane = 10.5 → la moyenne est légèrement tirée vers le haut par la Région 2.

---

#### Comment le coefficient de variation aide-t-il à comprendre la cohérence des ventes ?

Le **coefficient de variation (CV)** mesure la dispersion **relative** des données par rapport à leur moyenne :

```
CV = (σ / x̄) × 100   (exprimé en %)
```

Il permet de **comparer la variabilité** de produits qui n'ont pas les mêmes échelles de ventes.

**Calcul pour chaque produit :**

```
CV_A = (1.118 / 4.50)  × 100 ≈ 24.8%
CV_B = (1.479 / 7.75)  × 100 ≈ 19.1%
CV_C = (2.487 / 11.25) × 100 ≈ 22.1%
```

| Produit | Moyenne | Écart type | CV |
|---------|---------|------------|----|
| Produit A | 4.50 | 1.118 | **24.8%** |
| Produit B | 7.75 | 1.479 | **19.1%** |
| Produit C | 11.25 | 2.487 | **22.1%** |

**Interprétation :**

```
CV le plus faible → ventes les plus STABLES entre les régions
CV le plus élevé  → ventes les plus VARIABLES entre les régions

Produit B (CV = 19.1%) → ventes les plus homogènes entre régions
Produit A (CV = 24.8%) → ventes les plus variables relativement à sa moyenne
```

> 💡 **Sans le CV**, on pourrait croire que le Produit C est le plus instable car son écart type absolu (2.487) est le plus grand. Mais en proportion de sa moyenne, c'est le Produit A qui est le plus variable (24.8%). Le CV corrige ce biais d'échelle — indispensable pour comparer des produits avec des niveaux de ventes différents.

---

### 4.2 Application de la multiplication matricielle en Data Science

#### Calculs de revenus (notre exemple)

La multiplication **D × P** calcule simultanément le revenu de toutes les régions en **une seule opération** :

```
D (régions × produits)  ×  P (prix par produit)  =  R (revenus par région)
(4 × 3)                 ×  (3 × 1)               =  (4 × 1)
```

Sans algèbre matricielle, il faudrait faire 4 calculs séparés (un par région). Avec 1000 régions et 500 produits, la multiplication matricielle traite tout en un seul calcul vectorisé — c'est la base de l'**efficacité computationnelle** en Data Science.

---

#### Systèmes de recommandation

Dans Netflix ou Spotify, on utilise la **factorisation matricielle** :

```
Utilisateurs × Facteurs_latents  ×  Facteurs_latents × Films
        U     ×        Fᵀ        =        Scores de recommandation
```

- Chaque ligne = un utilisateur
- Chaque colonne = un film
- Les valeurs = score prédit de préférence

La multiplication matricielle prédit simultanément tous les scores de tous les films pour tous les utilisateurs.

---

#### Réseaux de neurones (Deep Learning)

Chaque couche d'un réseau de neurones est une multiplication matricielle :

```
Entrées × Poids + Biais = Sorties de la couche
```

Sans multiplication matricielle, le Deep Learning tel qu'on le connaît aujourd'hui serait impossible à calculer efficacement.

---

#### Autres applications en Data Science

| Domaine | Usage de la multiplication matricielle |
|---------|----------------------------------------|
| **Régression linéaire** | β = (XᵀX)⁻¹ Xᵀy (calcul des coefficients) |
| **ACP** | Décomposition de la matrice de covariance |
| **Traitement d'images** | Convolutions (filtrage, détection de contours) |
| **NLP** | Word embeddings (Word2Vec, transformers) |
| **Graphes** | Matrices d'adjacence pour analyser les réseaux |

---

## 5. Récapitulatif des résultats

### Statistiques descriptives

| Mesure | Produit A | Produit B | Produit C |
|--------|-----------|-----------|-----------|
| Moyenne | 4.50 | 7.75 | 11.25 |
| Médiane | 4.50 | 7.50 | 10.50 |
| Écart type | ≈ 1.118 | ≈ 1.479 | ≈ 2.487 |
| Variance | 1.25 | 2.1875 | 6.1875 |
| Étendue | 3 | 4 | 6 |
| CV | ≈ 24.8% | ≈ 19.1% | ≈ 22.1% |

### Algèbre linéaire

```
Transposée :
       [ 4   6   5   3 ]
Dᵀ  =  [ 8  10   7   6 ]
       [ 12  15   9   9 ]

Revenus par région (D × P) :
  Région 1 → 280
  Région 2 → 355  ← MAXIMUM
  Région 3 → 230
  Région 4 → 210

CA total par produit :
  Produit A → 90
  Produit B → 310
  Produit C → 675  ← MAXIMUM
  TOTAL     → 1 075
```

---

*📘 Correction du Checkpoint — Mathématiques pour Data Science | Bootcamp Data Science*
