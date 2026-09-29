# 🧼 Checkpoint 8 — Focus Preprocessing (Nettoyage & Mise à l'Échelle)

> **Module Data Science — Preprocessing** | Prérequis : cours "Nettoyage des Données & Mise à l'Échelle"

---

## Table des matières

1. [Objectif du checkpoint](#1-objectif-du-checkpoint)
2. [Les jeux de données](#2-les-jeux-de-données)
3. [Partie A — Nettoyer des données réelles (`fiche_employes.csv`)](#3-partie-a--nettoyer-des-données-réelles-fiche_employescsv)
4. [Partie B — Feature Scaling & comparaison d'échelles](#4-partie-b--feature-scaling--comparaison-déchelles)
5. [Partie C — Pipeline de preprocessing complet (`demandes_credit.csv`)](#5-partie-c--pipeline-de-preprocessing-complet-demandes_creditcsv)
6. [Solution complète commentée](#6-solution-complète-commentée)
7. [Barème et critères de réussite](#7-barème-et-critères-de-réussite)
8. [Questions de compréhension](#8-questions-de-compréhension)

---

## 1. Objectif du checkpoint

### 🎯 Ce que vous allez réaliser

```
OBJECTIFS DU CHECKPOINT 8
│
├── ✅ Diagnostiquer la qualité d'un jeu de données réel et sale
├── ✅ Nettoyer : manquants, doublons, formats, types, outliers
├── ✅ Appliquer et COMPARER les 4 mises à l'échelle
├── ✅ Encoder correctement les variables catégorielles
├── ✅ Éviter la fuite de données (fit sur le train uniquement)
└── ✅ Construire un Pipeline + ColumnTransformer de bout en bout
```

> 💡 Ce checkpoint reproduit la **réalité du terrain** : des données brutes désordonnées qu'il faut rendre exploitables **avant** toute modélisation.

---

## 2. Les jeux de données

| Fichier | Emplacement | Usage dans ce checkpoint |
|---------|-------------|---------------------------|
| `fiche_employes.csv` | `03-data-science/TP/` | Partie A — nettoyage (données volontairement sales) |
| `demandes_credit.csv` | `04-machine-learning/TP/` | Parties B & C — scaling + pipeline |

### 2.1 Aperçu de `fiche_employes.csv`

Ce fichier contient des défauts **typiques du monde réel** :

```
DÉFAUTS À REPÉRER
├── Noms de colonnes incohérents : "Fist Name" (typo), espaces, casse mélangée
├── Adresses sur PLUSIEURS lignes (retours à la ligne dans le CSV)
├── Téléphones en formats variés : "+33 2 47..." / "03 23 42..."
├── Intitulés de poste stockés en tuple texte : "('Chef de projet finance',)"
├── Villes en casses différentes, valeurs manquantes probables
└── Colonnes potentiellement inutiles pour une analyse RH
```

### 2.2 Aperçu de `demandes_credit.csv`

Données de scoring crédit, mêlant **numérique** et **catégoriel** :

```
Numériques  : age, revenu_mensuel, anciennete_emploi, montant_demande,
              duree_pret_mois, nb_credits_actuels, apport_personnel, nb_personnes_charge
Catégoriels : type_contrat (CDI/CDD/...), historique_credit (Bon/Mauvais),
              situation_familiale (Célibataire/Marié/Divorcé)
Cible (y)   : credit_accorde (0 / 1)
```

---

## 3. Partie A — Nettoyer des données réelles (`fiche_employes.csv`)

> 🎯 **But** : transformer un CSV désordonné en un DataFrame propre et fiable.

### 📋 Consignes

1. **Charger** le fichier et faire un **diagnostic** complet (`info`, `describe`, `isna`, `duplicated`).
2. **Normaliser les noms de colonnes** : minuscules, sans espaces, corriger la typo `fist_name → first_name`.
3. **Corriger les types** : `age` en entier, `salary` en numérique, `join_date` en datetime.
4. **Nettoyer le texte** : mettre `ville` en minuscules sans espaces ; extraire l'intitulé de poste propre depuis `"('Chef de projet finance',)"`.
5. **Gérer les manquants** : quantifier, puis imputer (médiane pour `salary`, mode pour les catégoriels) ou supprimer selon le taux.
6. **Corriger les inexactitudes** : `age` hors bornes plausibles (ex. > 100 ou < 16) → manquant, puis imputer.
7. **Dédupliquer** sur l'email (après standardisation).
8. **Détecter les outliers** de `salary` par la méthode IQR ; décider (garder/capper) et justifier.

> 💡 **Indices** :
> - Colonnes : `df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")`
> - Extraire un poste d'un tuple-texte : `str.extract(r"'([^']+)'")`
> - Dates mixtes : `pd.to_datetime(..., errors="coerce")`

---

## 4. Partie B — Feature Scaling & comparaison d'échelles

> 🎯 **But** : voir concrètement l'effet des 4 mises à l'échelle sur les mêmes variables.

### 📋 Consignes

Sur les colonnes numériques de `demandes_credit.csv` (`age`, `revenu_mensuel`, `montant_demande`) :

1. Affichez `describe()` **avant** tout scaling (constatez les écarts d'amplitude).
2. Appliquez et comparez, sur les mêmes colonnes, **MaxAbsScaler**, **MinMaxScaler**, **StandardScaler** et **RobustScaler**.
3. Pour chaque scaler, affichez min / max / moyenne / écart-type après transformation.
4. **Analysez** : quel scaler donne exactement [0,1] ? Lequel donne moyenne≈0 / écart-type≈1 ? Lequel résiste le mieux à un outlier ?
5. **Question de fond** : sur ces données, faut-il scaler pour un **Random Forest** ? Pour un **KNN** ? Justifiez.

---

## 5. Partie C — Pipeline de preprocessing complet (`demandes_credit.csv`)

> 🎯 **But** : assembler un pipeline **anti-fuite** qui nettoie, encode, scale et modélise.

### 📋 Consignes

1. Séparez `X` / `y` (`y = credit_accorde`), puis **train/test** (`test_size=0.2`, `random_state=42`, `stratify=y`).
2. Construisez un **ColumnTransformer** :
   - numériques → `SimpleImputer(median)` + `StandardScaler`
   - catégoriels → `SimpleImputer(most_frequent)` + `OneHotEncoder(handle_unknown="ignore")`
3. Emballez preprocessing + `LogisticRegression` dans un **Pipeline**.
4. Entraînez sur le **train uniquement**, évaluez sur le **test** (accuracy + F1).
5. **Vérifiez l'anti-fuite** : montrez que le scaler/imputer n'a jamais vu le test (le `fit` porte sur `X_train` seul).
6. **Bonus** : validez par `cross_val_score(pipe, X_train, y_train, cv=5)`.

---

## 6. Solution complète commentée

<details>
<summary>👀 <b>Partie A — Nettoyage de fiche_employes.csv</b></summary>

```python
import pandas as pd
import numpy as np

# --- 1. Charger + diagnostic ---
df = pd.read_csv("../../03-data-science/TP/fiche_employes.csv")
print(df.shape)
df.info()
print(df.isna().sum())
print("Doublons :", df.duplicated().sum())

df_clean = df.copy()   # ✅ toujours travailler sur une COPIE

# --- 2. Normaliser les noms de colonnes ---
df_clean.columns = (df_clean.columns.str.strip().str.lower()
                    .str.replace(" ", "_"))
df_clean = df_clean.rename(columns={"fist_name": "first_name",
                                    "djob_tilte": "job_title"})

# --- 3. Corriger les types ---
df_clean["salary"] = pd.to_numeric(df_clean["salary"], errors="coerce")
df_clean["join_date"] = pd.to_datetime(df_clean["join_date"], errors="coerce")

# --- 4. Nettoyer le texte ---
df_clean["ville"] = df_clean["ville"].str.strip().str.lower()
# Extraire le poste propre depuis "('Chef de projet finance',)"
df_clean["job_title"] = df_clean["job_title"].str.extract(r"'([^']+)'")

# --- 5 & 6. Inexactitudes + manquants ---
df_clean.loc[(df_clean["age"] > 100) | (df_clean["age"] < 16), "age"] = np.nan
df_clean["age"] = df_clean["age"].fillna(df_clean["age"].median()).astype(int)
df_clean["salary"] = df_clean["salary"].fillna(df_clean["salary"].median())
for col in ["department", "ville", "gender", "employment_status"]:
    df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

# --- 7. Dédupliquer sur l'email standardisé ---
df_clean["email"] = df_clean["email"].str.strip().str.lower()
df_clean = df_clean.drop_duplicates(subset=["email"], keep="first")

# --- 8. Outliers de salary (IQR) ---
Q1, Q3 = df_clean["salary"].quantile([0.25, 0.75])
IQR = Q3 - Q1
bas, haut = Q1 - 1.5*IQR, Q3 + 1.5*IQR
n_out = ((df_clean["salary"] < bas) | (df_clean["salary"] > haut)).sum()
print(f"Outliers salary : {n_out}")
# Décision : capping (les salaires élevés sont plausibles, on ne supprime pas)
df_clean["salary"] = df_clean["salary"].clip(bas, haut)

# --- Vérification finale ---
print(df_clean.isna().sum())
df_clean.info()
```
</details>

<details>
<summary>👀 <b>Partie B — Comparaison des scalers</b></summary>

```python
import pandas as pd
from sklearn.preprocessing import (MaxAbsScaler, MinMaxScaler,
                                   StandardScaler, RobustScaler)

df = pd.read_csv("demandes_credit.csv")
cols = ["age", "revenu_mensuel", "montant_demande"]
X = df[cols].dropna()

print("AVANT scaling :")
print(X.describe().loc[["min", "max", "mean", "std"]])

scalers = {
    "MaxAbs":   MaxAbsScaler(),
    "MinMax":   MinMaxScaler(),
    "Standard": StandardScaler(),
    "Robust":   RobustScaler(),
}
for nom, sc in scalers.items():
    Xs = pd.DataFrame(sc.fit_transform(X), columns=cols)
    print(f"\n=== {nom} ===")
    print(Xs.describe().loc[["min", "max", "mean", "std"]].round(3))

# Analyse :
# - MinMax  → min=0, max=1 exactement
# - Standard→ mean≈0, std≈1
# - Robust  → médiane centrée, résiste aux outliers
# Random Forest : PAS besoin de scaling (seuils).
# KNN          : scaling INDISPENSABLE (distances).
```
</details>

<details>
<summary>👀 <b>Partie C — Pipeline complet anti-fuite</b></summary>

```python
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv("demandes_credit.csv")
X = df.drop(columns=["credit_accorde"])
y = df["credit_accorde"]

# 1. Split (stratifié)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 2. Colonnes par type
num = X.select_dtypes("number").columns.tolist()
cat = X.select_dtypes("object").columns.tolist()

pipe_num = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler",  StandardScaler()),
])
pipe_cat = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot",  OneHotEncoder(handle_unknown="ignore")),
])
prep = ColumnTransformer([("num", pipe_num, num),
                          ("cat", pipe_cat, cat)])

# 3. Pipeline preprocessing + modèle
model = Pipeline([("prep", prep),
                  ("clf", LogisticRegression(max_iter=1000))])

# 4. Entraîner sur le TRAIN uniquement (anti-fuite garanti)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Accuracy : {accuracy_score(y_test, y_pred):.3f}")
print(f"F1       : {f1_score(y_test, y_pred):.3f}")

# 6. Bonus : validation croisée sur le train
cv = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
print(f"F1 CV    : {cv.mean():.3f} ± {cv.std():.3f}")
```

> 🔑 **Pourquoi c'est anti-fuite** : `model.fit(X_train, ...)` ajuste imputers, scaler et encoder **uniquement sur le train**. Sur `X_test`, le pipeline ne fait que `transform` avec les paramètres appris — le test n'enseigne **rien**.
</details>

---

## 7. Barème et critères de réussite

| Critère | Points | Ce qui est attendu |
|---------|--------|--------------------|
| Diagnostic qualité | 15 % | `info`, `isna`, `duplicated`, `describe` interprétés |
| Nettoyage (Partie A) | 30 % | Colonnes, types, texte, manquants, doublons, outliers traités et **justifiés** |
| Comparaison scalers (Partie B) | 20 % | 4 scalers appliqués + analyse correcte de leurs effets |
| Encodage catégoriel | 10 % | Nominal → One-Hot, choix cohérent |
| Pipeline anti-fuite (Partie C) | 20 % | `fit` sur train seul, ColumnTransformer + Pipeline fonctionnels |
| Reproductibilité & clarté | 5 % | Travail sur copie, code commenté, `random_state` fixé |

> ✅ **Réussite** : ≥ 60 %. **Excellence** : pipeline complet fonctionnel + justifications métier des choix de nettoyage.

---

## 8. Questions de compréhension

<details>
<summary><b>1. Pourquoi travailler sur <code>df.copy()</code> plutôt que sur <code>df</code> directement ?</b></summary>

Pour préserver les données brutes intactes : on peut ainsi comparer avant/après, recommencer en cas d'erreur, et garantir la traçabilité. Modifier l'original rend le nettoyage irréversible et non reproductible.
</details>

<details>
<summary><b>2. Dans la Partie A, pourquoi standardiser l'email (minuscules, strip) AVANT de dédupliquer ?</b></summary>

Parce que `"Jean@Ex.com "` et `"jean@ex.com"` désignent la même personne mais ne sont pas des doublons exacts. Sans standardisation préalable, `drop_duplicates(subset=["email"])` les raterait.
</details>

<details>
<summary><b>3. Faut-il mettre à l'échelle les données pour un Random Forest ? Et pour un KNN ?</b></summary>

**Random Forest : non** — il découpe par seuils, insensible à l'échelle. **KNN : oui, indispensable** — il calcule des distances euclidiennes, donc une variable de grande amplitude (revenu) écraserait les autres (âge) sans scaling.
</details>

<details>
<summary><b>4. Pourquoi la Partie C fait-elle le split AVANT de définir le pipeline ?</b></summary>

Pour éviter la **fuite de données** : le pipeline (imputer, scaler, encoder) doit être `fit` sur le train uniquement. Si on transformait tout le dataset avant le split, les statistiques du test contamineraient l'entraînement et gonfleraient artificiellement le score.
</details>

<details>
<summary><b>5. Quel est l'intérêt du ColumnTransformer par rapport à un traitement manuel colonne par colonne ?</b></summary>

Il applique automatiquement le bon preprocessing à chaque type de colonne (numérique vs catégoriel), en un seul objet réutilisable, intégré au Pipeline. Résultat : code plus court, sans fuite, reproductible, et directement compatible avec la validation croisée et `GridSearchCV`.
</details>

<details>
<summary><b>6. Dans la Partie A, on a cappé les salaires extrêmes plutôt que de les supprimer. Pourquoi ce choix ?</b></summary>

Parce qu'un salaire élevé est **plausible** (cadre dirigeant) : ce n'est pas forcément une erreur. Le supprimer perdrait de l'information ; le capping (le ramener à la borne IQR) limite son influence tout en gardant la ligne. Le choix dépend du contexte métier.
</details>

---

*📘 Module Data Science — Checkpoint 8 : Focus Preprocessing | Bootcamp Data Science*
