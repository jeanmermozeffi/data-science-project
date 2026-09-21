# 📱 TP3 — Prédire le Départ d'un Client Télécom (Churn — Classification)

> **Module Data Science — Machine Learning** | TP guidé (corrigé détaillé)
> **Dataset** : `clients_telecom.csv` (8 000 clients)

---

## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Découverte du dataset](#2-découverte-du-dataset)
3. [Étape 1 — Exploration des données (EDA)](#3-étape-1--exploration-des-données-eda)
4. [Étape 2 — Préparation des données](#4-étape-2--préparation-des-données)
5. [Étape 3 — Les 3 modèles de classification](#5-étape-3--les-3-modèles-de-classification)
6. [Étape 4 — Évaluation approfondie (le recall !)](#6-étape-4--évaluation-approfondie)
7. [Étape 5 — Réflexion métier (faux négatifs)](#7-étape-5--réflexion-métier)
8. [Étape 6 — Interpréter et agir (fidélisation)](#8-étape-6--interpréter-et-agir)
9. [Solution complète](#9-solution-complète)
10. [Pour aller plus loin](#10-pour-aller-plus-loin)

---

## 1. Contexte et objectif

### 🎯 Le problème métier

Un opérateur télécom perd chaque mois des clients qui résilient pour un concurrent : c'est le **churn** (attrition). Retenir un client coûte **bien moins cher** que d'en acquérir un nouveau. La direction veut prédire **à l'avance** quels clients risquent de partir, pour leur proposer des offres de fidélisation **avant** qu'ils ne résilient.

### 🤖 Le problème Machine Learning

```
TYPE DE PROBLÈME : CLASSIFICATION (déséquilibrée)
│
├── On veut prédire : churn (0 = reste / 1 = part)
├── À partir de : profil + comportement de consommation
└── Particularité : classe "part" MINORITAIRE (~25%) → le recall sera crucial
```

> 💡 On prédit une **catégorie** (part/reste) → **classification** (régression logistique, arbre, KNN). Comme les classes sont **déséquilibrées**, la précision globale ne suffira pas : on surveillera le **recall** de la classe "part".

---

## 2. Découverte du dataset

### 📋 Les colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `client_id` | identifiant | Numéro unique — ⚠️ **à exclure** des features |
| `age` | numérique | Âge du client |
| `anciennete_mois` | numérique | Ancienneté chez l'opérateur (mois) |
| `conso_data_go` | numérique | Consommation data mensuelle (Go) |
| `minutes_appel` | numérique | Minutes d'appel mensuelles |
| `nb_sms` | numérique | Nombre de SMS mensuels |
| `facture_mensuelle` | numérique | Facture mensuelle moyenne (FCFA) |
| `nb_reclamations` | numérique | Nombre de réclamations |
| **`churn`** | binaire | **🎯 La cible : 1 = parti, 0 = resté** |

> ⚠️ `client_id` est un simple identifiant : l'inclure comme variable prédictive n'a aucun sens (et peut créer une fausse corrélation).

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
df.describe()
print("Valeurs manquantes :\n", df.isna().sum())

# Distribution de la cible — DÉSÉQUILIBRE
print("\nTaux de churn :", round(df["churn"].mean() * 100, 1), "%")   # ~25%
print(df["churn"].value_counts())
```

### Visualisations exploratoires

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1) Taux de churn selon le nombre de réclamations
df.groupby("nb_reclamations")["churn"].mean().plot(kind="bar", ax=axes[0], color="orange")
axes[0].set_title("Taux de churn selon le nb de réclamations")
axes[0].set_ylabel("Taux de churn")

# 2) Ancienneté selon le churn
sns.boxplot(data=df, x="churn", y="anciennete_mois", ax=axes[1])
axes[1].set_title("Ancienneté selon le churn")
axes[1].set_xticklabels(["Reste", "Part"])

# 3) Facture selon le churn
sns.boxplot(data=df, x="churn", y="facture_mensuelle", ax=axes[2])
axes[2].set_title("Facture selon le churn")
axes[2].set_xticklabels(["Reste", "Part"])

plt.tight_layout(); plt.show()
```

> 🔑 **À observer (hypothèses)** : plus de **réclamations**, une **faible ancienneté** et une **facture élevée** vont de pair avec un churn plus élevé. Nos clients les plus à risque sont donc probablement les **nouveaux clients mécontents avec une grosse facture**.

---

## 4. Étape 2 — Préparation des données

### 4.1 Sélectionner les features (exclure `client_id`)

```python
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "facture_mensuelle", "nb_reclamations"]   # client_id EXCLU
X = df[features]
y = df["churn"]
print("Features :", X.shape, "| Cible :", y.shape)
```

### 4.2 Séparer train et test (avec `stratify`)

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y   # garde ~25% de churn des deux côtés
)
print(f"Train : {X_train.shape[0]} | Test : {X_test.shape[0]}")
```

> ⚠️ `stratify=y` est **essentiel** ici : sans lui, un split malchanceux pourrait sous-représenter la classe minoritaire "part" dans le test.

### 4.3 Normaliser (pour LogReg et KNN)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)
```

---

## 5. Étape 3 — Les 3 modèles de classification

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

resultats = {}
logreg = LogisticRegression(max_iter=500).fit(X_train_s, y_train)
resultats["Régression logistique"] = accuracy_score(y_test, logreg.predict(X_test_s))
arbre = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)
resultats["Arbre de décision"] = accuracy_score(y_test, arbre.predict(X_test))
knn = KNeighborsClassifier(n_neighbors=7).fit(X_train_s, y_train)
resultats["KNN (k=7)"] = accuracy_score(y_test, knn.predict(X_test_s))

print("=== PRÉCISION DES 3 MODÈLES ===")
for m, s in sorted(resultats.items(), key=lambda x: x[1], reverse=True):
    print(f"{m:25} : {s:.3f}")
```

**Résultat typique :**
```
Régression logistique   : ~0.858   ← meilleur
Arbre de décision       : ~0.848
KNN (k=7)               : ~0.836
```

> ⚠️ **Piège** : ~0.86 de précision **semble** bon... mais 75% des clients restent. Un modèle "bête" qui prédirait toujours "reste" aurait déjà ~0.75 ! La précision globale est donc **trompeuse** ici. Il faut regarder le **recall** de la classe "part".

---

## 6. Étape 4 — Évaluation approfondie

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

pred = logreg.predict(X_test_s)

cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Reste", "Part"]).plot(cmap="Oranges")
plt.title("Matrice de confusion — Churn"); plt.show()

print(classification_report(y_test, pred, target_names=["Reste", "Part"]))
```

**Rapport typique :**
```
              precision  recall  f1-score
   Reste        0.88      0.94      0.91
   Part         0.77      0.61      0.68    ← recall de "Part" = LE point clé
```

> 🔑 **Point pédagogique clé** : la précision globale est ~0.86, mais le **recall de la classe "Part" n'est que ~0.61** → le modèle **rate ~40% des partants** ! Dans un problème **déséquilibré**, c'est le recall de la classe minoritaire qui compte pour le métier, pas la précision globale.

---

## 7. Étape 5 — Réflexion métier

> ### ❓ Question 13 — Quel type d'erreur coûte le plus cher ?

```
FAUX NÉGATIF  → ne PAS détecter un client qui va partir
              → client perdu, non retenu = TRÈS COÛTEUX 💸 (acquérir un nouveau coûte cher)

FAUX POSITIF  → alerter à tort sur un client fidèle
              → coût d'une offre de fidélisation inutile = FAIBLE
```

> 🔑 **Conclusion métier** : pour l'opérateur, le **faux négatif** est le plus coûteux (on laisse filer un partant sans rien faire). On veut donc **maximiser le _recall_ de la classe "Part"** — détecter un maximum de partants — quitte à accepter quelques fausses alertes (offres envoyées à des clients qui seraient restés de toute façon). C'est l'inverse du TP2 crédit, où l'on privilégiait la precision !

---

## 8. Étape 6 — Interpréter et agir

### 8.1 Facteurs de churn

```python
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)

plt.figure(figsize=(9, 5))
importances.plot(kind="barh")
plt.title("Facteurs de churn (importance)")
plt.gca().invert_yaxis()
plt.show()

print(importances.head(5))
```

> 🔑 Facteurs typiques : **nb_reclamations**, **anciennete_mois** (les nouveaux partent plus), **facture_mensuelle**.

### 8.2 Prédire le risque d'un client

```python
def predire_churn(modele, scaler, colonnes, **infos):
    """Prédit le risque de départ d'un client (données normalisées)."""
    client = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, val in infos.items():
        if cle in client.columns:
            client[cle] = val
    client_s = scaler.transform(client)
    proba = modele.predict_proba(client_s)[0][1]
    return ("À RISQUE" if proba > 0.5 else "FIDÈLE"), proba

statut, proba = predire_churn(
    logreg, scaler, features,
    age=30, anciennete_mois=6, conso_data_go=3, minutes_appel=100,
    nb_sms=20, facture_mensuelle=45000, nb_reclamations=5)
print(f"Client récent mécontent → {statut} (probabilité de départ : {proba:.1%})")
```

### 8.3 Actions de fidélisation (Partie E)

```
ACTIONS CONCRÈTES BASÉES SUR LES FACTEURS DE CHURN
│
├── 📞 Clients avec BEAUCOUP de réclamations → renforcer le SAV, rappel proactif
├── 🎁 NOUVEAUX clients (faible ancienneté)  → programme d'accueil / onboarding
└── 💡 Clients à GROSSE facture               → proposer un forfait mieux adapté
```

---

## 9. Solution complète

```python
# ============================================================
# TP3 — PRÉDICTION DU CHURN CLIENT (solution complète)
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             ConfusionMatrixDisplay, classification_report)

sns.set_theme(style="whitegrid")

# --- 1. Charger ---
df = pd.read_csv("clients_telecom.csv")
print("Dimensions :", df.shape)
print("Taux de churn :", round(df["churn"].mean() * 100, 1), "%")

# --- 2. Préparer (client_id EXCLU) ---
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "facture_mensuelle", "nb_reclamations"]
X = df[features]
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# --- 3. Les 3 modèles vus en cours ---
resultats = {}
logreg = LogisticRegression(max_iter=500).fit(X_train_s, y_train)
resultats["Régression logistique"] = accuracy_score(y_test, logreg.predict(X_test_s))
arbre = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)
resultats["Arbre de décision"] = accuracy_score(y_test, arbre.predict(X_test))
knn = KNeighborsClassifier(n_neighbors=7).fit(X_train_s, y_train)
resultats["KNN (k=7)"] = accuracy_score(y_test, knn.predict(X_test_s))

print("\n=== RÉSULTATS ===")
for m, s in sorted(resultats.items(), key=lambda x: x[1], reverse=True):
    print(f"{m:25} : {s:.3f}")

# --- 4. Évaluation (recall crucial) ---
pred = logreg.predict(X_test_s)
cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Reste", "Part"]).plot(cmap="Oranges")
plt.title("Matrice de confusion — Churn"); plt.show()
print(classification_report(y_test, pred, target_names=["Reste", "Part"]))

# --- 5. Facteurs de churn ---
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)
print("\n=== FACTEURS DE CHURN ===\n", importances.head(5))

print("\n🏆 Meilleur modèle : régression logistique (~0.86).")
print("   ⚠️ Mais surveiller le RECALL de 'Part' (~0.61) : ~40% des partants ratés.")
print("   → Erreur la plus coûteuse : le FAUX NÉGATIF (partant non détecté).")
```

**Résultats attendus :**
```
Taux de churn : 25.0 %  (classes DÉSÉQUILIBRÉES → la précision seule trompe)
Régression logistique   : ~0.858   ← meilleur
Arbre de décision       : ~0.848
KNN (k=7)               : ~0.836
Recall de la classe "Part" : ~0.61   ← LE vrai enjeu du TP
Facteurs : nb_reclamations, anciennete_mois, facture_mensuelle
```

---

## 10. Pour aller plus loin

```
EXTENSIONS POSSIBLES
│
├── ⚖️  Gérer le déséquilibre : class_weight="balanced" dans LogReg / arbre
├── 🎯 Abaisser le seuil de décision pour AUGMENTER le recall des partants
├── 📊 Tracer la courbe précision/recall et choisir le meilleur compromis
├── 🌳 Optimiser la profondeur de l'arbre (courbe recall selon max_depth)
└── 💾 Sauvegarder le modèle + scaler (joblib) pour le scoring quotidien
```

```python
# Exemple : rééquilibrer les classes pour améliorer le recall des partants
from sklearn.metrics import classification_report
logreg_bal = LogisticRegression(max_iter=500, class_weight="balanced").fit(X_train_s, y_train)
print(classification_report(y_test, logreg_bal.predict(X_test_s), target_names=["Reste", "Part"]))
# → le recall de "Part" augmente (on détecte plus de partants), au prix de plus de fausses alertes.

# Exemple : abaisser le seuil pour détecter davantage de partants
proba = logreg.predict_proba(X_test_s)[:, 1]
for seuil in [0.5, 0.4, 0.3]:
    pred_seuil = (proba >= seuil).astype(int)
    cm = confusion_matrix(y_test, pred_seuil)
    recall_part = cm[1, 1] / (cm[1, 0] + cm[1, 1])
    print(f"Seuil {seuil} → recall 'Part' = {recall_part:.2f}")
```

> 💡 **Note** : le churn est un cas d'école pour comprendre que **la métrique doit suivre le métier**. Ici, le recall de la classe minoritaire prime — un principe qu'on retrouve en détection de fraude, diagnostic médical, etc.

---

*📘 Module Data Science — TP3 : Prédiction du churn client | Bootcamp Data Science*
