# 🏠 TP1 — Prédire le Loyer d'un Logement à Abidjan (Régression)

> **Module Data Science — Machine Learning** | TP guidé (à traiter en classe)
> **Dataset** : `loyers_abidjan.csv` (6 000 logements)

---

## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Découverte du dataset](#2-découverte-du-dataset)
3. [Étape 1 — Exploration des données (EDA)](#3-étape-1--exploration-des-données-eda)
4. [Étape 2 — Nettoyage des données](#4-étape-2--nettoyage-des-données)
5. [Étape 3 — Préparation pour le ML](#5-étape-3--préparation-pour-le-ml)
6. [Étape 4 — Premier modèle : régression linéaire](#6-étape-4--premier-modèle--régression-linéaire)
7. [Étape 5 — Évaluation du modèle](#7-étape-5--évaluation-du-modèle)
8. [Étape 6 — Comparer avec l'arbre de décision et le KNN](#8-étape-6--comparer-avec-larbre-de-décision-et-le-knn)
9. [Étape 7 — Interpréter et prédire](#9-étape-7--interpréter-et-prédire)
10. [Solution complète](#10-solution-complète)
11. [Pour aller plus loin](#11-pour-aller-plus-loin)

---

## 1. Contexte et objectif

### 🎯 Le problème métier

Une agence immobilière d'Abidjan veut créer un outil qui **estime automatiquement le loyer** d'un logement en fonction de ses caractéristiques (commune, superficie, standing...). Cela permettrait de :
- Conseiller les propriétaires sur un prix de mise en location juste
- Détecter les annonces sur/sous-évaluées
- Accélérer les estimations

### 🤖 Le problème Machine Learning

```
TYPE DE PROBLÈME : RÉGRESSION
│
├── On veut prédire : le LOYER (un NOMBRE en FCFA)
├── À partir de : caractéristiques du logement (features)
└── Donc : problème de RÉGRESSION supervisée
```

> 💡 On prédit un **nombre continu** (le loyer) → c'est de la **régression**. Si on prédisait une catégorie (cher/pas cher), ce serait de la classification.

---

## 2. Découverte du dataset

### 📋 Les colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `commune` | texte | Commune d'Abidjan (Cocody, Yopougon...) |
| `superficie_m2` | numérique | Surface en m² |
| `nb_pieces` | numérique | Nombre de pièces |
| `age_batiment` | numérique | Âge du bâtiment (années) |
| `etage` | numérique | Étage du logement |
| `standing` | texte | Économique / Moyen / Haut standing |
| `meuble` | binaire | 1 si meublé, 0 sinon |
| `parking` | binaire | 1 si parking, 0 sinon |
| `securite` | binaire | 1 si gardiennage, 0 sinon |
| **`loyer_fcfa`** | numérique | **🎯 La cible à prédire** (loyer mensuel en FCFA) |

---

## 3. Étape 1 — Exploration des données (EDA)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Charger les données
df = pd.read_csv("loyers_abidjan.csv")

# Premiers réflexes (chapitres précédents !)
print("Dimensions :", df.shape)
df.head()
```

```python
# Diagnostic
df.info()
df.describe()

# Valeurs manquantes
print(df.isna().sum())
```

### Visualisations exploratoires

```python
# Distribution du loyer (la cible)
plt.figure(figsize=(8, 5))
sns.histplot(df["loyer_fcfa"], bins=50, kde=True)
plt.title("Distribution des loyers")
plt.xlabel("Loyer (FCFA)")
plt.show()

# Loyer moyen par commune
plt.figure(figsize=(10, 5))
df.groupby("commune")["loyer_fcfa"].median().sort_values().plot(kind="barh")
plt.title("Loyer médian par commune")
plt.xlabel("Loyer médian (FCFA)")
plt.show()

# Relation superficie / loyer
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="superficie_m2", y="loyer_fcfa", alpha=0.3)
plt.title("Superficie vs Loyer")
plt.show()

# Matrice de corrélation
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes("number").corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Corrélations")
plt.show()
```

> 🔑 **À observer** : la superficie est fortement corrélée au loyer, Cocody/Plateau/Riviera sont les communes les plus chères, et la distribution des loyers est asymétrique (quelques loyers très élevés).

---

## 4. Étape 2 — Nettoyage des données

```python
# Traiter les valeurs manquantes (superficie, âge, nb_pieces)
df["superficie_m2"] = df["superficie_m2"].fillna(df["superficie_m2"].median())
df["age_batiment"]  = df["age_batiment"].fillna(df["age_batiment"].median())
df["nb_pieces"]     = df["nb_pieces"].fillna(df["nb_pieces"].median())

# Vérifier
print("Valeurs manquantes après nettoyage :", df.isna().sum().sum())

# Supprimer d'éventuels doublons
df = df.drop_duplicates().reset_index(drop=True)
print("Dimensions après nettoyage :", df.shape)
```

---

## 5. Étape 3 — Préparation pour le ML

### 5.1 Encoder les variables catégorielles

Rappel : les modèles ne comprennent que des **nombres**. Il faut encoder `commune` et `standing`.

```python
# One-Hot Encoding pour les variables catégorielles
df_ml = pd.get_dummies(df, columns=["commune", "standing"], drop_first=True)

print("Colonnes après encodage :", df_ml.shape[1])
df_ml.head()
```

> 💡 `drop_first=True` évite la redondance (si ce n'est aucune des autres communes, c'est forcément la première).

### 5.2 Séparer features (X) et cible (y)

```python
X = df_ml.drop(columns="loyer_fcfa")   # toutes les colonnes SAUF la cible
y = df_ml["loyer_fcfa"]                 # la cible

print("Features :", X.shape)
print("Cible :", y.shape)
```

### 5.3 Séparer train et test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train : {X_train.shape[0]} logements")
print(f"Test  : {X_test.shape[0]} logements")
```

---

## 6. Étape 4 — Premier modèle : régression linéaire

```python
from sklearn.linear_model import LinearRegression

# Créer et entraîner
modele_lr = LinearRegression()
modele_lr.fit(X_train, y_train)

# Prédire sur le test
predictions_lr = modele_lr.predict(X_test)

print("✅ Modèle de régression linéaire entraîné")
```

---

## 7. Étape 5 — Évaluation du modèle

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae  = mean_absolute_error(y_test, predictions_lr)
rmse = np.sqrt(mean_squared_error(y_test, predictions_lr))
r2   = r2_score(y_test, predictions_lr)

print("=== RÉGRESSION LINÉAIRE ===")
print(f"MAE  : {mae:,.0f} FCFA (erreur moyenne)")
print(f"RMSE : {rmse:,.0f} FCFA")
print(f"R²   : {r2:.3f}")
```

**Résultat typique :**
```
MAE  : ~55 000 FCFA
RMSE : ~85 000 FCFA
R²   : 0.856
```

> 🔑 Un R² de 0.856 signifie que le modèle explique ~86% de la variation des loyers. L'erreur moyenne (MAE) donne une idée concrète : on se trompe en moyenne de ~55 000 FCFA sur l'estimation.

### Visualiser prédictions vs réalité

```python
plt.figure(figsize=(8, 8))
plt.scatter(y_test, predictions_lr, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         "r--", linewidth=2, label="Prédiction parfaite")
plt.xlabel("Loyer réel (FCFA)")
plt.ylabel("Loyer prédit (FCFA)")
plt.title("Prédictions vs Réalité")
plt.legend()
plt.show()
```

> 💡 Plus les points sont proches de la diagonale rouge, meilleures sont les prédictions.

---

## 8. Étape 6 — Comparer avec l'arbre de décision et le KNN

La régression linéaire suppose une relation linéaire. Comparons-la avec les deux autres algorithmes vus en cours : l'**arbre de décision** et le **KNN**.

### 8.1 Arbre de décision (régression)

```python
from sklearn.tree import DecisionTreeRegressor

# L'arbre de décision peut aussi faire de la régression (prédire un nombre)
modele_arbre = DecisionTreeRegressor(max_depth=8, random_state=42)
modele_arbre.fit(X_train, y_train)   # l'arbre n'a pas besoin de normalisation

predictions_arbre = modele_arbre.predict(X_test)

print("=== ARBRE DE DÉCISION ===")
print(f"MAE : {mean_absolute_error(y_test, predictions_arbre):,.0f} FCFA")
print(f"R²  : {r2_score(y_test, predictions_arbre):.3f}")
```

> ⚠️ **Attention à la profondeur !** Un arbre trop profond fait de l'**overfitting**. Testons plusieurs profondeurs :

```python
print("Effet de la profondeur de l'arbre :")
for profondeur in [3, 5, 8, 12, None]:
    arbre = DecisionTreeRegressor(max_depth=profondeur, random_state=42)
    arbre.fit(X_train, y_train)
    r2 = r2_score(y_test, arbre.predict(X_test))
    print(f"  max_depth={str(profondeur):5} → R² = {r2:.3f}")
# → on observe que trop profond (None) n'est PAS le meilleur : c'est l'overfitting !
```

### 8.2 KNN (régression)

```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

# ⚠️ Le KNN nécessite la NORMALISATION (basé sur les distances)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

modele_knn = KNeighborsRegressor(n_neighbors=5)
modele_knn.fit(X_train_scaled, y_train)

predictions_knn = modele_knn.predict(X_test_scaled)

print("=== KNN (k=5) ===")
print(f"MAE : {mean_absolute_error(y_test, predictions_knn):,.0f} FCFA")
print(f"R²  : {r2_score(y_test, predictions_knn):.3f}")
```

### 8.3 Comparer les trois modèles

```python
comparaison = pd.DataFrame({
    "Modèle": ["Régression linéaire", "Arbre de décision", "KNN (k=5)"],
    "R²": [
        r2_score(y_test, predictions_lr),
        r2_score(y_test, predictions_arbre),
        r2_score(y_test, predictions_knn)
    ],
    "MAE (FCFA)": [
        mean_absolute_error(y_test, predictions_lr),
        mean_absolute_error(y_test, predictions_arbre),
        mean_absolute_error(y_test, predictions_knn)
    ]
})
print(comparaison)
```

**Résultat typique :**
```
              Modèle       R²    MAE (FCFA)
0  Régression linéaire   0.833      ~67 000
1    Arbre de décision   0.800      ~67 000
2            KNN (k=5)   0.870      ~56 000   ← meilleur ici !
```

> 🔑 **Message important** : sur ce problème, le **KNN** obtient le meilleur R² ! Cela confirme un principe fondamental du ML : **il n'y a pas de meilleur algorithme universel**. On teste toujours plusieurs modèles et on garde celui qui performe le mieux sur nos données.

---

## 9. Étape 7 — Interpréter et prédire

### 9.1 Quelles variables comptent le plus ?

L'**arbre de décision** fournit l'importance de chaque variable (le KNN, lui, ne le permet pas facilement).

```python
# Importance des variables selon l'arbre de décision
modele_arbre = DecisionTreeRegressor(max_depth=8, random_state=42).fit(X_train, y_train)
importances = pd.Series(modele_arbre.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
importances.plot(kind="barh")
plt.title("Top 10 des variables les plus importantes")
plt.xlabel("Importance")
plt.gca().invert_yaxis()
plt.show()
```

> 🔑 On découvre quels facteurs influencent le plus le loyer : généralement la superficie, la commune (Cocody/Plateau) et le standing.

### 9.2 Prédire le loyer d'un nouveau logement

On utilise le KNN (meilleur modèle ici). Attention : il faut normaliser le nouveau logement avec le **même scaler**.

```python
def predire_loyer_knn(modele, scaler, colonnes, **caracteristiques):
    """Prédit le loyer d'un logement avec le modèle KNN (données normalisées)."""
    logement = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, valeur in caracteristiques.items():
        if cle in logement.columns:
            logement[cle] = valeur
    logement_scaled = scaler.transform(logement)
    return modele.predict(logement_scaled)[0]

# Exemple : un 3 pièces de 80m² à Cocody, moyen standing, avec parking
loyer_estime = predire_loyer_knn(
    modele_knn, scaler, X.columns,
    superficie_m2=80, nb_pieces=3, age_batiment=5, etage=2,
    parking=1, securite=1, meuble=0,
    commune_Cocody=1, standing_Moyen=1
)
print(f"Loyer estimé : {loyer_estime:,.0f} FCFA/mois")
```

---

## 10. Solution complète

```python
# ============================================================
# TP1 — PRÉDICTION DE LOYER À ABIDJAN (solution complète)
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sns.set_theme(style="whitegrid")

# --- 1. Charger ---
df = pd.read_csv("loyers_abidjan.csv")
print("Dimensions :", df.shape)

# --- 2. Nettoyer ---
for col in ["superficie_m2", "age_batiment", "nb_pieces"]:
    df[col] = df[col].fillna(df[col].median())
df = df.drop_duplicates().reset_index(drop=True)

# --- 3. Préparer ---
df_ml = pd.get_dummies(df, columns=["commune", "standing"], drop_first=True)
X = df_ml.drop(columns="loyer_fcfa")
y = df_ml["loyer_fcfa"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation (pour le KNN)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# --- 4. Les 3 modèles vus en cours ---
lr    = LinearRegression().fit(X_train, y_train)
arbre = DecisionTreeRegressor(max_depth=8, random_state=42).fit(X_train, y_train)
knn   = KNeighborsRegressor(n_neighbors=5).fit(X_train_s, y_train)

pred_lr    = lr.predict(X_test)
pred_arbre = arbre.predict(X_test)
pred_knn   = knn.predict(X_test_s)

# --- 5. Comparer ---
print("\n=== COMPARAISON DES MODÈLES ===")
for nom, pred in [("Régression linéaire", pred_lr),
                  ("Arbre de décision", pred_arbre),
                  ("KNN (k=5)", pred_knn)]:
    print(f"{nom:22} | R² = {r2_score(y_test, pred):.3f} | "
          f"MAE = {mean_absolute_error(y_test, pred):,.0f} FCFA")

# --- 6. Importance des variables (via l'arbre) ---
importances = pd.Series(arbre.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n=== TOP 5 VARIABLES IMPORTANTES ===")
print(importances.head(5))

print("\n🏆 Le KNN obtient le meilleur R² sur ce problème.")
print("   → Rappel : pas de meilleur algorithme universel, on teste et on compare !")
```

---

## 11. Pour aller plus loin

Une fois le TP maîtrisé, essayez ces améliorations :

```
EXTENSIONS POSSIBLES
│
├── 🎯 Trouver le meilleur K pour le KNN (tester k de 1 à 20)
├── 🌳 Optimiser la profondeur de l'arbre (courbe R² selon max_depth)
├── 🧹 Créer de nouvelles features (loyer au m², ratio pièces/surface)
├── 📈 Analyser les résidus (où le modèle se trompe-t-il le plus ?)
├── 🎯 Utiliser la validation croisée pour une évaluation plus robuste
└── 💾 Sauvegarder le modèle entraîné (joblib) pour le réutiliser
```

```python
# Exemple : trouver le meilleur K pour le KNN
from sklearn.neighbors import KNeighborsRegressor

scores_k = {}
for k in range(1, 21):
    knn_k = KNeighborsRegressor(n_neighbors=k).fit(X_train_s, y_train)
    scores_k[k] = r2_score(y_test, knn_k.predict(X_test_s))
meilleur_k = max(scores_k, key=scores_k.get)
print(f"Meilleur K : {meilleur_k} (R² = {scores_k[meilleur_k]:.3f})")

# Exemple : validation croisée
from sklearn.model_selection import cross_val_score
scores = cross_val_score(lr, X, y, cv=5, scoring="r2")
print(f"R² moyen régression linéaire (5-fold) : {scores.mean():.3f} ± {scores.std():.3f}")

# Exemple : sauvegarder le modèle
import joblib
joblib.dump(knn, "modele_loyer_knn.pkl")
joblib.dump(scaler, "scaler_loyer.pkl")   # ne pas oublier le scaler pour le KNN !
# Recharger : modele = joblib.load("modele_loyer_knn.pkl")
```

> 💡 **Note** : il existe des algorithmes plus avancés (Random Forest, Gradient Boosting...) que vous découvrirez dans les prochains modules — ils combinent plusieurs arbres pour de meilleures performances. Mais avec seulement la régression linéaire, l'arbre et le KNN, vous couvrez déjà l'essentiel des problèmes de régression !

---

*📘 Module Data Science — TP1 : Prédiction de loyer | Bootcamp Data Science*
