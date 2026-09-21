# 💰 TP4 — Prédire la Facture Mensuelle d'un Client Télécom (Régression)

> **Module Data Science — Machine Learning** | TP guidé (corrigé détaillé)
> **Dataset** : `clients_telecom.csv` (8 000 clients)

---

## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Découverte du dataset](#2-découverte-du-dataset)
3. [Étape 1 — Exploration des données (EDA)](#3-étape-1--exploration-des-données-eda)
4. [Étape 2 — Préparation des données](#4-étape-2--préparation-des-données)
5. [Étape 3 — Les 3 modèles de régression](#5-étape-3--les-3-modèles-de-régression)
6. [Étape 4 — Évaluation approfondie (R², MAE, overfitting)](#6-étape-4--évaluation-approfondie)
7. [Étape 5 — Réflexion : pourquoi le R² est si élevé ?](#7-étape-5--réflexion)
8. [Étape 6 — Interpréter et prédire](#8-étape-6--interpréter-et-prédire)
9. [Solution complète](#9-solution-complète)
10. [Pour aller plus loin (+ question bonus)](#10-pour-aller-plus-loin)

---

## 1. Contexte et objectif

### 🎯 Le problème métier

Le même opérateur télécom veut **estimer la facture mensuelle** d'un client à partir de son profil et de sa consommation. Utilité : simuler la facture d'un nouveau client, **détecter les factures anormales** (erreurs, fraude) et proposer le forfait le plus adapté.

### 🤖 Le problème Machine Learning

```
TYPE DE PROBLÈME : RÉGRESSION
│
├── On veut prédire : facture_mensuelle (un NOMBRE en FCFA)
├── À partir de : profil + comportement de consommation
└── Donc : problème de RÉGRESSION supervisée
```

> 💡 On prédit un **nombre continu** (la facture) → **régression** : régression **linéaire**, arbre de décision, KNN. La régression **logistique**, elle, servait à la classification (TP2, TP3).

---

## 2. Découverte du dataset

### 📋 Les colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `client_id` | identifiant | Numéro unique — ⚠️ **à exclure** |
| `age` | numérique | Âge du client |
| `anciennete_mois` | numérique | Ancienneté (mois) |
| `conso_data_go` | numérique | Consommation data mensuelle (Go) |
| `minutes_appel` | numérique | Minutes d'appel mensuelles |
| `nb_sms` | numérique | Nombre de SMS mensuels |
| **`facture_mensuelle`** | numérique | **🎯 La cible à prédire (FCFA)** |
| `nb_reclamations` | numérique | Nombre de réclamations |
| `churn` | binaire | 1 = parti (peut être ignoré ici) |

> ⚠️ `client_id` est un identifiant, jamais une variable prédictive.

---

## 3. Étape 1 — Exploration des données (EDA)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv("clients_telecom.csv")
print("Dimensions :", df.shape)
df.head()
```

```python
df.info()
# Distribution de la cible
print(df["facture_mensuelle"].describe())

plt.figure(figsize=(8, 5))
sns.histplot(df["facture_mensuelle"], bins=50, kde=True)
plt.title("Distribution de la facture mensuelle")
plt.xlabel("Facture (FCFA)")
plt.show()
```

### Corrélations et nuages de points

```python
# Heatmap des corrélations
plt.figure(figsize=(8, 6))
cols = ["age", "anciennete_mois", "conso_data_go", "minutes_appel", "nb_sms", "facture_mensuelle"]
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Corrélations")
plt.show()

# 2 nuages de points : consommation vs facture
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.scatterplot(data=df, x="conso_data_go", y="facture_mensuelle", alpha=0.3, ax=axes[0])
axes[0].set_title("Consommation data vs Facture")
sns.scatterplot(data=df, x="minutes_appel", y="facture_mensuelle", alpha=0.3, ax=axes[1])
axes[1].set_title("Minutes d'appel vs Facture")
plt.tight_layout(); plt.show()
```

> 🔑 **À observer** : `conso_data_go` et `minutes_appel` sont **très fortement corrélées** à la facture — logique, ce sont les principaux postes de consommation facturés.

---

## 4. Étape 2 — Préparation des données

### 4.1 Sélectionner les features (exclure `client_id` et la cible)

```python
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "nb_reclamations"]   # client_id et facture EXCLUS de X
X = df[features]
y = df["facture_mensuelle"]
print("Features :", X.shape, "| Cible :", y.shape)
```

### 4.2 Séparer train et test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42   # pas de stratify : la cible est continue
)
print(f"Train : {X_train.shape[0]} | Test : {X_test.shape[0]}")
```

### 4.3 Normaliser (pour le KNN)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)
```

> ⚠️ Le **KNN** est basé sur les distances → il **exige** la normalisation. La régression linéaire et l'arbre fonctionnent sur les données brutes.

---

## 5. Étape 3 — Les 3 modèles de régression

```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1) Régression linéaire (données brutes)
lr = LinearRegression().fit(X_train, y_train)
pred_lr = lr.predict(X_test)

# 2) Arbre de décision (données brutes)
arbre = DecisionTreeRegressor(max_depth=8, random_state=42).fit(X_train, y_train)
pred_arbre = arbre.predict(X_test)

# 3) KNN (données normalisées)
knn = KNeighborsRegressor(n_neighbors=5).fit(X_train_s, y_train)
pred_knn = knn.predict(X_test_s)

print("✅ Les 3 modèles sont entraînés")
```

---

## 6. Étape 4 — Évaluation approfondie

### 6.1 Comparer R² et MAE

```python
print("=== COMPARAISON DES MODÈLES ===")
for nom, pred in [("Régression linéaire", pred_lr),
                  ("Arbre de décision", pred_arbre),
                  ("KNN (k=5)", pred_knn)]:
    print(f"{nom:22} | R² = {r2_score(y_test, pred):.3f} | "
          f"MAE = {mean_absolute_error(y_test, pred):,.0f} FCFA")
```

**Résultat typique :**
```
Régression linéaire   | R² = 0.994 | MAE = ~1 570 FCFA   ← excellent
Arbre de décision     | R² = 0.992 | MAE = ~1 900 FCFA
KNN (k=5)             | R² = 0.979 | MAE = ~3 100 FCFA
```

> 🔑 Le **R²** mesure la part de variance expliquée (proche de 1 = très bon). Le **MAE** donne l'erreur concrète : on se trompe en moyenne de ~1 570 FCFA sur la facture.

### 6.2 Prédictions vs réalité

```python
plt.figure(figsize=(8, 8))
plt.scatter(y_test, pred_lr, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         "r--", linewidth=2, label="Prédiction parfaite")
plt.xlabel("Facture réelle (FCFA)")
plt.ylabel("Facture prédite (FCFA)")
plt.title("Prédictions vs Réalité")
plt.legend()
plt.show()
```

### 6.3 Attention à l'overfitting de l'arbre

```python
print("Effet de la profondeur de l'arbre :")
for prof in [3, 5, 8, 12, None]:
    a = DecisionTreeRegressor(max_depth=prof, random_state=42).fit(X_train, y_train)
    print(f"  max_depth={str(prof):5} → R² test = {r2_score(y_test, a.predict(X_test)):.3f}")
# → un arbre trop profond (None) mémorise le bruit du train : c'est l'OVERFITTING.
```

---

## 7. Étape 5 — Réflexion

> ### ❓ Question 13 — Pourquoi le R² est-il aussi élevé (~0.99) ?

```
La facture télécom est CALCULÉE directement à partir des consommations :
   facture ≈ (data × prix_Go) + (minutes × prix_min) + (SMS × prix_SMS) + abonnement
   → relation quasi DÉTERMINISTE
   → le modèle la retrouve presque parfaitement → R² proche de 1
```

> 🔑 **Point pédagogique clé** : un R² ~0.99 est **inhabituel dans la vraie vie**. Deux explications possibles : (1) le problème est réellement "facile" car quasi déterministe — **c'est le cas ici** ; (2) une **fuite de données** (data leakage) : une feature contient déjà l'information de la cible. Un bon réflexe : quand un R² est trop beau, **se demander pourquoi**.

> ⚠️ **Piège à éviter** : ne jamais inclure dans X une variable dérivée de la facture (ex : le montant d'un poste déjà facturé) — ce serait de la fuite de données et le modèle "tricherait".

---

## 8. Étape 6 — Interpréter et prédire

### 8.1 Variables les plus importantes

```python
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)

plt.figure(figsize=(9, 5))
importances.plot(kind="barh")
plt.title("Variables importantes pour la facture")
plt.gca().invert_yaxis()
plt.show()

print(importances.head(5))
```

> 🔑 Sans surprise : **conso_data_go** et **minutes_appel** dominent — les gros postes de la facture.

### 8.2 Prédire la facture d'un client

```python
def predire_facture(modele, colonnes, **infos):
    """Prédit la facture d'un client (régression linéaire, données brutes)."""
    client = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, val in infos.items():
        if cle in client.columns:
            client[cle] = val
    return modele.predict(client)[0]

# Gros consommateur data
f1 = predire_facture(lr, features, age=28, anciennete_mois=24,
                     conso_data_go=40, minutes_appel=300, nb_sms=100, nb_reclamations=0)
print(f"Gros consommateur data → {f1:,.0f} FCFA")

# Petit consommateur
f2 = predire_facture(lr, features, age=55, anciennete_mois=60,
                     conso_data_go=3, minutes_appel=80, nb_sms=15, nb_reclamations=1)
print(f"Petit consommateur → {f2:,.0f} FCFA")
```

---

## 9. Solution complète

```python
# ============================================================
# TP4 — PRÉDICTION DE LA FACTURE MENSUELLE (solution complète)
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
from sklearn.metrics import mean_absolute_error, r2_score

sns.set_theme(style="whitegrid")

# --- 1. Charger ---
df = pd.read_csv("clients_telecom.csv")
print("Dimensions :", df.shape)
print(df["facture_mensuelle"].describe())

# --- 2. Préparer (client_id et facture EXCLUS de X) ---
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "nb_reclamations"]
X = df[features]
y = df["facture_mensuelle"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# --- 3. Les 3 modèles vus en cours ---
lr    = LinearRegression().fit(X_train, y_train)
arbre = DecisionTreeRegressor(max_depth=8, random_state=42).fit(X_train, y_train)
knn   = KNeighborsRegressor(n_neighbors=5).fit(X_train_s, y_train)

pred_lr, pred_arbre, pred_knn = lr.predict(X_test), arbre.predict(X_test), knn.predict(X_test_s)

# --- 4. Comparer ---
print("\n=== COMPARAISON ===")
for nom, pred in [("Régression linéaire", pred_lr),
                  ("Arbre de décision", pred_arbre),
                  ("KNN (k=5)", pred_knn)]:
    print(f"{nom:22} | R² = {r2_score(y_test, pred):.3f} | "
          f"MAE = {mean_absolute_error(y_test, pred):,.0f} FCFA")

# --- 5. Prédictions vs réel ---
plt.figure(figsize=(8, 8))
plt.scatter(y_test, pred_lr, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
plt.xlabel("Facture réelle"); plt.ylabel("Facture prédite")
plt.title("Prédictions vs Réalité"); plt.show()

# --- 6. Overfitting de l'arbre ---
print("\nEffet de la profondeur de l'arbre :")
for prof in [3, 5, 8, 12, None]:
    a = DecisionTreeRegressor(max_depth=prof, random_state=42).fit(X_train, y_train)
    print(f"  max_depth={str(prof):5} → R² = {r2_score(y_test, a.predict(X_test)):.3f}")

# --- 7. Importance des variables ---
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)
print("\n=== VARIABLES IMPORTANTES ===\n", importances.head(5))

print("\n🏆 Meilleur modèle : régression linéaire (R² ~0.99).")
print("   → R² très élevé car la facture est CALCULÉE à partir des consommations.")
```

**Résultats attendus :**
```
Régression linéaire   : R² ~0.994 | MAE ~1 570 FCFA   ← excellent
Arbre de décision     : R² ~0.992
KNN (k=5)             : R² ~0.979
Variables importantes : conso_data_go, minutes_appel
```

---

## 10. Pour aller plus loin

```
EXTENSIONS POSSIBLES
│
├── 🎯 Trouver le meilleur k pour le KNN (tester k de 1 à 20)
├── 🌳 Tracer la courbe R² selon max_depth (visualiser l'overfitting)
├── 📈 Analyser les résidus (facture réelle − prédite) : où le modèle se trompe-t-il ?
├── 🚨 Utiliser le modèle pour détecter les factures anormales (gros écart préd/réel)
└── 💾 Sauvegarder le modèle (joblib) pour la simulation de facture
```

### ❓ Question bonus — Temps de prédiction des 3 modèles

```python
import time

for nom, modele, X_eval in [("Régression linéaire", lr, X_test),
                            ("Arbre de décision", arbre, X_test),
                            ("KNN (k=5)", knn, X_test_s)]:
    t0 = time.time()
    modele.predict(X_eval)
    print(f"{nom:22} → {time.time() - t0:.4f} s")
# → le KNN est le plus LENT en prédiction : c'est un algorithme "paresseux" (lazy)
#   qui calcule les distances à tous les points d'entraînement au moment de prédire.
```

> 💡 **Note** : la régression linéaire et l'arbre "apprennent" un modèle compact à l'entraînement puis prédisent instantanément. Le KNN, lui, ne fait rien à l'entraînement mais recalcule tout à la prédiction — d'où sa lenteur sur de gros jeux de données.

---

*📘 Module Data Science — TP4 : Prédiction de la facture mensuelle | Bootcamp Data Science*
