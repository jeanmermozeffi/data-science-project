# 💳 TP2 — Prédire l'Accord d'une Demande de Crédit (Classification)

> **Module Data Science — Machine Learning** | TP guidé (corrigé détaillé)
> **Dataset** : `demandes_credit.csv` (7 000 demandes)

---

## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Découverte du dataset](#2-découverte-du-dataset)
3. [Étape 1 — Exploration des données (EDA)](#3-étape-1--exploration-des-données-eda)
4. [Étape 2 — Nettoyage des données](#4-étape-2--nettoyage-des-données)
5. [Étape 3 — Préparation pour le ML](#5-étape-3--préparation-pour-le-ml)
6. [Étape 4 — Les 3 modèles de classification](#6-étape-4--les-3-modèles-de-classification)
7. [Étape 5 — Évaluation approfondie](#7-étape-5--évaluation-approfondie)
8. [Étape 6 — Réflexion métier (faux positifs vs faux négatifs)](#8-étape-6--réflexion-métier)
9. [Étape 7 — Interpréter et prédire](#9-étape-7--interpréter-et-prédire)
10. [Solution complète](#10-solution-complète)
11. [Pour aller plus loin](#11-pour-aller-plus-loin)

---

## 1. Contexte et objectif

### 🎯 Le problème métier

Une institution de **microfinance** en Afrique de l'Ouest reçoit chaque jour des centaines de demandes de crédit, examinées manuellement — un processus **long et subjectif**. La direction veut un outil qui **prédit automatiquement** si une demande devrait être accordée, comme **aide à la décision** pour les agents.

### 🤖 Le problème Machine Learning

```
TYPE DE PROBLÈME : CLASSIFICATION
│
├── On veut prédire : credit_accorde (0 = refusé / 1 = accordé)
├── À partir de : profil du demandeur (revenu, historique, contrat...)
└── Donc : problème de CLASSIFICATION binaire supervisée
```

> 💡 On prédit une **catégorie** (accordé/refusé) → **classification**. On utilise donc la **régression logistique**, l'**arbre de décision** et le **KNN** — surtout **pas** la régression linéaire (qui prédit des nombres).

---

## 2. Découverte du dataset

### 📋 Les colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `age` | numérique | Âge du demandeur |
| `revenu_mensuel` | numérique | Revenu mensuel (FCFA) |
| `anciennete_emploi` | numérique | Ancienneté dans l'emploi (années) — ⚠️ manquants |
| `type_contrat` | catégoriel | CDI / CDD / Indépendant / Fonctionnaire |
| `montant_demande` | numérique | Montant du crédit demandé (FCFA) |
| `duree_pret_mois` | numérique | Durée de remboursement (mois) |
| `nb_credits_actuels` | numérique | Nombre de crédits en cours |
| `historique_credit` | catégoriel | Bon / Moyen / Mauvais — ⚠️ manquants |
| `apport_personnel` | numérique | Apport personnel (FCFA) — ⚠️ manquants |
| `situation_familiale` | catégoriel | Célibataire / Marié / Divorcé |
| `nb_personnes_charge` | numérique | Nombre de personnes à charge |
| **`credit_accorde`** | binaire | **🎯 La cible : 1 = accordé, 0 = refusé** |

---

## 3. Étape 1 — Exploration des données (EDA)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Charger les données
df = pd.read_csv("demandes_credit.csv")

# Premiers réflexes
print("Dimensions :", df.shape)
df.head()
```

```python
# Diagnostic
df.info()
df.describe()

# Valeurs manquantes
print(df.isna().sum())

# Distribution de la cible — le jeu est-il équilibré ?
print("\nTaux d'accord :", round(df["credit_accorde"].mean() * 100, 1), "%")   # ~60%
print(df["credit_accorde"].value_counts())
```

### Visualisations exploratoires

```python
# 1) Taux d'accord selon l'historique de crédit
plt.figure(figsize=(8, 5))
df.groupby("historique_credit")["credit_accorde"].mean().sort_values().plot(kind="bar")
plt.title("Taux d'accord selon l'historique de crédit")
plt.ylabel("Taux d'accord")
plt.show()

# 2) Taux d'accord selon le type de contrat
plt.figure(figsize=(8, 5))
df.groupby("type_contrat")["credit_accorde"].mean().sort_values().plot(kind="bar", color="teal")
plt.title("Taux d'accord selon le type de contrat")
plt.ylabel("Taux d'accord")
plt.show()

# 3) Revenu selon la décision
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="credit_accorde", y="revenu_mensuel")
plt.title("Revenu mensuel selon la décision de crédit")
plt.xticks([0, 1], ["Refusé", "Accordé"])
plt.show()
```

> 🔑 **À observer** : un **bon historique de crédit** et un **revenu élevé** augmentent nettement le taux d'accord. Le jeu est **assez équilibré** (~60% d'accords) — la précision globale sera donc un indicateur raisonnable, mais on l'affinera avec la matrice de confusion.

---

## 4. Étape 2 — Nettoyage des données

```python
# Traiter les valeurs manquantes
# → médiane pour les numériques (robuste aux valeurs extrêmes)
df["anciennete_emploi"] = df["anciennete_emploi"].fillna(df["anciennete_emploi"].median())
df["apport_personnel"]  = df["apport_personnel"].fillna(df["apport_personnel"].median())
# → mode pour la catégorielle
df["historique_credit"] = df["historique_credit"].fillna(df["historique_credit"].mode()[0])

# Vérifier
print("Valeurs manquantes après nettoyage :", df.isna().sum().sum())
```

> 💡 On impute avec la **médiane** (numériques) et le **mode** (catégorielle) : simple, robuste, et sans fuite de données puisqu'on ne regarde pas la cible.

---

## 5. Étape 3 — Préparation pour le ML

### 5.1 Encoder les variables catégorielles

```python
# One-Hot Encoding pour les 3 variables catégorielles
df_ml = pd.get_dummies(
    df,
    columns=["type_contrat", "historique_credit", "situation_familiale"],
    drop_first=True
)
print("Colonnes après encodage :", df_ml.shape[1])
df_ml.head()
```

### 5.2 Séparer features (X) et cible (y)

```python
X = df_ml.drop(columns="credit_accorde")
y = df_ml["credit_accorde"]
print("Features :", X.shape, "| Cible :", y.shape)
```

### 5.3 Séparer train et test (avec `stratify`)

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y   # stratify garde le ratio 60/40
)
print(f"Train : {X_train.shape[0]} demandes | Test : {X_test.shape[0]} demandes")
```

### 5.4 Normaliser (pour LogReg et KNN)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)   # fit UNIQUEMENT sur le train
X_test_s  = scaler.transform(X_test)
```

> ⚠️ La **régression logistique** et le **KNN** sont sensibles à l'échelle → on normalise. L'**arbre de décision**, lui, n'a **pas** besoin de normalisation (il travaille par seuils).

---

## 6. Étape 4 — Les 3 modèles de classification

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

resultats = {}

# 1) Régression logistique (données normalisées)
logreg = LogisticRegression(max_iter=500).fit(X_train_s, y_train)
resultats["Régression logistique"] = accuracy_score(y_test, logreg.predict(X_test_s))

# 2) Arbre de décision (données brutes)
arbre = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)
resultats["Arbre de décision"] = accuracy_score(y_test, arbre.predict(X_test))

# 3) KNN (données normalisées)
knn = KNeighborsClassifier(n_neighbors=7).fit(X_train_s, y_train)
resultats["KNN (k=7)"] = accuracy_score(y_test, knn.predict(X_test_s))

print("=== PRÉCISION DES 3 MODÈLES ===")
for m, s in sorted(resultats.items(), key=lambda x: x[1], reverse=True):
    print(f"{m:25} : {s:.3f}")
```

**Résultat typique :**
```
Régression logistique   : ~0.903   ← meilleur
Arbre de décision       : ~0.831
KNN (k=7)               : ~0.791
```

> 🔑 Ici la **régression logistique** gagne. C'est fréquent quand la frontière entre les classes est proche d'une combinaison linéaire des variables (revenu, historique, endettement...).

---

## 7. Étape 5 — Évaluation approfondie

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# On évalue le meilleur modèle (régression logistique)
pred = logreg.predict(X_test_s)

# Matrice de confusion
cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Refusé", "Accordé"]).plot(cmap="Blues")
plt.title("Matrice de confusion — Régression logistique")
plt.show()

# Rapport de classification
print(classification_report(y_test, pred, target_names=["Refusé", "Accordé"]))
```

> 🔑 **Lire la matrice de confusion** :
> - **Vrais positifs** : crédits accordés qui devaient l'être ✅
> - **Faux positifs** : crédits **accordés à tort** (le client ne remboursera pas) 💸 → perte directe
> - **Faux négatifs** : bons clients **refusés à tort** → manque à gagner
> - La **precision** de "Accordé" = parmi les crédits accordés, combien étaient de bons dossiers.
> - Le **recall** de "Accordé" = parmi les bons dossiers, combien on a su accorder.

---

## 8. Étape 6 — Réflexion métier

> ### ❓ Question 13 — Quel type d'erreur coûte le plus cher ?

```
FAUX POSITIF  → accorder un crédit qui ne sera PAS remboursé
              → PERTE DIRECTE du capital prêté 💸  (erreur coûteuse)

FAUX NÉGATIF  → refuser un bon client
              → manque à gagner (intérêts perdus)   (erreur moins grave)
```

> 🔑 **Conclusion métier** : pour une banque, le **faux positif** est généralement le plus coûteux (on perd le capital). On cherche donc à **minimiser les faux positifs**, c'est-à-dire à **privilégier la _precision_ de la classe "Accordé"**, quitte à être plus strict et à refuser quelques bons dossiers. La matrice de confusion permet justement de quantifier ce compromis.

---

## 9. Étape 7 — Interpréter et prédire

### 9.1 Quelles variables comptent le plus ?

```python
# L'arbre de décision fournit l'importance de chaque variable
importances = pd.Series(arbre.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
importances.head(8).plot(kind="barh")
plt.title("Top 8 des variables les plus importantes")
plt.gca().invert_yaxis()
plt.show()

print(importances.head(8))
```

> 🔑 Variables typiquement décisives : **historique_credit**, **revenu_mensuel**, le **taux d'endettement** implicite (montant demandé / revenu), le **type_contrat** et l'**apport_personnel**.

### 9.2 Prédire pour un nouveau demandeur

```python
def predire_credit(modele, scaler, colonnes, **infos):
    """Prédit l'accord de crédit pour un nouveau demandeur (données normalisées)."""
    demande = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, val in infos.items():
        if cle in demande.columns:
            demande[cle] = val
    demande_s = scaler.transform(demande)
    pred  = modele.predict(demande_s)[0]
    proba = modele.predict_proba(demande_s)[0][1]
    return ("ACCORDÉ" if pred == 1 else "REFUSÉ"), proba

# Profil solide : fonctionnaire, bon historique, apport conséquent
decision, proba = predire_credit(
    logreg, scaler, X.columns,
    age=40, revenu_mensuel=800000, anciennete_emploi=10,
    montant_demande=5000000, duree_pret_mois=36, nb_credits_actuels=0,
    apport_personnel=1500000, nb_personnes_charge=1,
    type_contrat_Fonctionnaire=1, historique_credit_Bon=1)
print(f"Profil solide → {decision} (probabilité d'accord : {proba:.1%})")
```

---

## 10. Solution complète

```python
# ============================================================
# TP2 — PRÉDICTION D'ACCORD DE CRÉDIT (solution complète)
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
df = pd.read_csv("demandes_credit.csv")
print("Dimensions :", df.shape)
print("Taux d'accord :", round(df["credit_accorde"].mean() * 100, 1), "%")

# --- 2. Nettoyer ---
df["anciennete_emploi"] = df["anciennete_emploi"].fillna(df["anciennete_emploi"].median())
df["apport_personnel"]  = df["apport_personnel"].fillna(df["apport_personnel"].median())
df["historique_credit"] = df["historique_credit"].fillna(df["historique_credit"].mode()[0])

# --- 3. Préparer ---
df_ml = pd.get_dummies(df, columns=["type_contrat", "historique_credit", "situation_familiale"],
                       drop_first=True)
X = df_ml.drop(columns="credit_accorde")
y = df_ml["credit_accorde"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# --- 4. Les 3 modèles vus en cours ---
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

# --- 5. Évaluation du meilleur modèle ---
pred = logreg.predict(X_test_s)
cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Refusé", "Accordé"]).plot(cmap="Blues")
plt.title("Matrice de confusion — Régression logistique"); plt.show()
print(classification_report(y_test, pred, target_names=["Refusé", "Accordé"]))

# --- 6. Importance des variables ---
importances = pd.Series(arbre.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n=== TOP 8 VARIABLES ===\n", importances.head(8))

print("\n🏆 Meilleur modèle : régression logistique (~0.90).")
print("   → Erreur la plus coûteuse : le FAUX POSITIF (crédit non remboursé).")
```

**Résultats attendus :**
```
Taux d'accord : 60.0 %
Régression logistique   : ~0.903   ← meilleur
Arbre de décision       : ~0.831
KNN (k=7)               : ~0.791
Variables importantes : historique_credit, revenu_mensuel, taux d'endettement, type_contrat, apport
```

---

## 11. Pour aller plus loin

```
EXTENSIONS POSSIBLES
│
├── 🎯 Trouver le meilleur k pour le KNN (tester k de 1 à 20)
├── 🌳 Optimiser la profondeur de l'arbre (courbe précision selon max_depth)
├── ⚖️  Ajuster le seuil de décision pour minimiser les faux positifs
├── 🧮 Créer la feature "taux d'endettement" = montant_demande / (revenu × durée)
├── 🎯 Utiliser la validation croisée pour une évaluation plus robuste
└── 💾 Sauvegarder le modèle (joblib) + le scaler pour la mise en production
```

```python
# Exemple : ajuster le seuil pour être plus strict (moins de faux positifs)
proba = logreg.predict_proba(X_test_s)[:, 1]
for seuil in [0.5, 0.6, 0.7]:
    pred_seuil = (proba >= seuil).astype(int)
    cm = confusion_matrix(y_test, pred_seuil)
    fp = cm[0, 1]   # faux positifs
    print(f"Seuil {seuil} → faux positifs = {fp}")
# → Plus le seuil monte, moins on accorde à tort (mais on refuse plus de bons clients).
```

> 💡 **Note** : des algorithmes plus avancés (Random Forest, Gradient Boosting) feront mieux, mais avec la **régression logistique**, l'**arbre** et le **KNN** vous couvrez déjà l'essentiel de la classification.

---

*📘 Module Data Science — TP2 : Prédiction d'accord de crédit | Bootcamp Data Science*
