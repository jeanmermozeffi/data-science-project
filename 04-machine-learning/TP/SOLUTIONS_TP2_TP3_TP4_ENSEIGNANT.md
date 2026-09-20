# 🔐 Solutions — TP2 (Crédit), TP3 (Churn) & TP4 (Facture)

> **⚠️ DOCUMENT ENSEIGNANT — NE PAS DISTRIBUER AUX APPRENANTS**
> Solutions de référence pour la correction des TP2, TP3 et TP4.
> Tous les TP utilisent uniquement les **3 algorithmes vus en cours** : régression linéaire/logistique, arbre de décision, KNN.

---

## Table des matières

1. [Solution TP2 — Prédiction d'accord de crédit (classification)](#solution-tp2--prédiction-daccord-de-crédit-classification)
2. [Solution TP3 — Prédiction du churn (classification)](#solution-tp3--prédiction-du-churn-classification)
3. [Solution TP4 — Prédiction de la facture (régression)](#solution-tp4--prédiction-de-la-facture-régression)
4. [Grilles de correction](#grilles-de-correction)

---

# Solution TP2 — Prédiction d'accord de crédit (classification)

## Code complet

```python
# ============================================================
# SOLUTION TP2 — PRÉDICTION D'ACCORD DE CRÉDIT
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

# ---------- A : EXPLORATION ----------
df = pd.read_csv("demandes_credit.csv")
print("Dimensions :", df.shape)
print("Taux d'accord :", round(df["credit_accorde"].mean() * 100, 1), "%")  # ~60%
print("Manquants :\n", df.isna().sum())

# ---------- B : NETTOYAGE & PRÉPARATION ----------
df["anciennete_emploi"] = df["anciennete_emploi"].fillna(df["anciennete_emploi"].median())
df["apport_personnel"]  = df["apport_personnel"].fillna(df["apport_personnel"].median())
df["historique_credit"] = df["historique_credit"].fillna(df["historique_credit"].mode()[0])

df_ml = pd.get_dummies(df, columns=["type_contrat", "historique_credit", "situation_familiale"],
                       drop_first=True)
X = df_ml.drop(columns="credit_accorde")
y = df_ml["credit_accorde"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# ---------- C : MODÉLISATION (3 modèles vus) ----------
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

# ---------- D : ÉVALUATION ----------
pred = logreg.predict(X_test_s)   # meilleur modèle
cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Refusé", "Accordé"]).plot(cmap="Blues")
plt.title("Matrice de confusion — Régression logistique"); plt.show()
print(classification_report(y_test, pred, target_names=["Refusé", "Accordé"]))

# RÉFLEXION MÉTIER (Q13) :
# → FAUX POSITIF (accorder un crédit non remboursé) = perte directe du capital.
# → FAUX NÉGATIF (refuser un bon client) = manque à gagner (intérêts perdus).
# → La banque cherche souvent à MINIMISER les faux positifs (être stricte),
#   donc à privilégier la PRECISION sur la classe "Accordé".

# ---------- E : INTERPRÉTATION ----------
importances = pd.Series(arbre.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n=== TOP 8 VARIABLES ===\n", importances.head(8))

def predire_credit(modele, scaler, colonnes, **infos):
    demande = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, val in infos.items():
        if cle in demande.columns:
            demande[cle] = val
    demande_s = scaler.transform(demande)
    pred = modele.predict(demande_s)[0]
    proba = modele.predict_proba(demande_s)[0][1]
    return ("ACCORDÉ" if pred == 1 else "REFUSÉ"), proba

decision, proba = predire_credit(
    logreg, scaler, X.columns,
    age=40, revenu_mensuel=800000, anciennete_emploi=10,
    montant_demande=5000000, duree_pret_mois=36, nb_credits_actuels=0,
    apport_personnel=1500000, nb_personnes_charge=1,
    type_contrat_Fonctionnaire=1, historique_credit_Bon=1)
print(f"\nProfil solide → {decision} (probabilité : {proba:.1%})")
```

## Résultats attendus TP2

```
Taux d'accord : 60.0 %
Régression logistique   : ~0.903   ← meilleur
Arbre de décision       : ~0.831
KNN (k=7)               : ~0.791
Variables importantes : historique_credit, revenu_mensuel, taux d'endettement,
                        type_contrat, apport_personnel
```

**Points clés attendus :** gestion des manquants, encodage One-Hot, normalisation pour LogReg/KNN mais pas pour l'arbre, 3 modèles comparés, matrice de confusion interprétée, **réflexion métier Q13** (faux positifs vs faux négatifs), fonction de prédiction.

---

# Solution TP3 — Prédiction du churn (classification)

## Code complet

```python
# ============================================================
# SOLUTION TP3 — PRÉDICTION DU CHURN CLIENT
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

# ---------- A : EXPLORATION ----------
df = pd.read_csv("clients_telecom.csv")
print("Dimensions :", df.shape)
print("Taux de churn :", round(df["churn"].mean() * 100, 1), "%")   # ~25% (déséquilibré !)

# Visualisations clés
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
df.groupby("nb_reclamations")["churn"].mean().plot(kind="bar", ax=axes[0])
axes[0].set_title("Taux de churn selon nb réclamations")
sns.boxplot(data=df, x="churn", y="anciennete_mois", ax=axes[1])
axes[1].set_title("Ancienneté selon churn")
sns.boxplot(data=df, x="churn", y="facture_mensuelle", ax=axes[2])
axes[2].set_title("Facture selon churn")
plt.tight_layout(); plt.show()
# → Plus de réclamations + faible ancienneté + facture élevée = plus de churn

# ---------- B : PRÉPARATION ----------
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "facture_mensuelle", "nb_reclamations"]   # client_id EXCLU
X = df[features]
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# ---------- C : MODÉLISATION (3 modèles vus) ----------
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

# ---------- D : ÉVALUATION (recall crucial pour le churn) ----------
pred = logreg.predict(X_test_s)
cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm, display_labels=["Reste", "Part"]).plot(cmap="Oranges")
plt.title("Matrice de confusion — Churn"); plt.show()
print(classification_report(y_test, pred, target_names=["Reste", "Part"]))

# RÉFLEXION MÉTIER (Q13) :
# → FAUX NÉGATIF (ne pas détecter un partant) = client perdu = très coûteux.
# → FAUX POSITIF (fausse alerte sur un fidèle) = coût d'une offre inutile = faible.
# → On privilégie donc le RECALL de la classe "Part" (détecter un max de partants),
#   quitte à accepter quelques fausses alertes.

# ---------- E : INTERPRÉTATION & ACTION ----------
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)
print("\n=== FACTEURS DE CHURN ===\n", importances.head(5))

def predire_churn(modele, scaler, colonnes, **infos):
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
print(f"\nClient récent mécontent → {statut} (probabilité de départ : {proba:.1%})")
```

## Résultats attendus TP3

```
Taux de churn : 25.0 %  (classes DÉSÉQUILIBRÉES → la précision seule trompe)

Régression logistique   : ~0.858   ← meilleur
Arbre de décision       : ~0.848
KNN (k=7)               : ~0.836

Rapport de classification (régression logistique) :
              precision  recall  f1-score
   Reste        0.88      0.94      0.91
   Part         0.77      0.61      0.68    ← recall de "Part" = point clé !

Facteurs de churn : nb_reclamations, anciennete_mois, facture_mensuelle
```

> 💡 **Point pédagogique clé** : la précision globale (~0.86) semble bonne, mais le **recall de la classe "Part" n'est que ~0.61** : le modèle rate ~40% des partants ! C'est **le** point de différenciation du TP. Un bon apprenant doit remarquer que dans un problème **déséquilibré** (25% de churn), la précision globale est trompeuse et le **recall** de la classe minoritaire est ce qui compte vraiment pour le métier.

**Actions de fidélisation attendues (Partie E) :** cibler les clients avec beaucoup de réclamations (améliorer le SAV), les nouveaux clients (programme d'accueil/onboarding), les grosses factures (offres d'optimisation de forfait).

---

# Solution TP4 — Prédiction de la facture (régression)

## Code complet

```python
# ============================================================
# SOLUTION TP4 — PRÉDICTION DE LA FACTURE MENSUELLE
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

# ---------- A : EXPLORATION ----------
df = pd.read_csv("clients_telecom.csv")
print("Dimensions :", df.shape)
print(df["facture_mensuelle"].describe())

# Corrélations
plt.figure(figsize=(8, 6))
cols = ["age","anciennete_mois","conso_data_go","minutes_appel","nb_sms","facture_mensuelle"]
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Corrélations"); plt.show()
# → conso_data_go et minutes_appel très corrélées à la facture

# ---------- B : PRÉPARATION ----------
features = ["age", "anciennete_mois", "conso_data_go", "minutes_appel",
            "nb_sms", "nb_reclamations"]   # client_id et facture EXCLUS de X
X = df[features]
y = df["facture_mensuelle"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# ---------- C : MODÉLISATION (3 modèles vus) ----------
lr    = LinearRegression().fit(X_train, y_train)
arbre = DecisionTreeRegressor(max_depth=8, random_state=42).fit(X_train, y_train)
knn   = KNeighborsRegressor(n_neighbors=5).fit(X_train_s, y_train)

pred_lr    = lr.predict(X_test)
pred_arbre = arbre.predict(X_test)
pred_knn   = knn.predict(X_test_s)

# ---------- D : ÉVALUATION ----------
print("\n=== COMPARAISON ===")
for nom, pred in [("Régression linéaire", pred_lr),
                  ("Arbre de décision", pred_arbre),
                  ("KNN (k=5)", pred_knn)]:
    print(f"{nom:22} | R² = {r2_score(y_test, pred):.3f} | "
          f"MAE = {mean_absolute_error(y_test, pred):,.0f} FCFA")

# Prédictions vs réel (meilleur modèle)
plt.figure(figsize=(8, 8))
plt.scatter(y_test, pred_lr, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
plt.xlabel("Facture réelle"); plt.ylabel("Facture prédite")
plt.title("Prédictions vs Réalité"); plt.show()

# Overfitting de l'arbre (Q14)
print("\nEffet de la profondeur de l'arbre :")
for prof in [3, 5, 8, 12, None]:
    a = DecisionTreeRegressor(max_depth=prof, random_state=42).fit(X_train, y_train)
    print(f"  max_depth={str(prof):5} → R² = {r2_score(y_test, a.predict(X_test)):.3f}")

# RÉFLEXION (Q13) : le R² est très élevé (~0.99) car la facture est CALCULÉE
# directement à partir des consommations (data, minutes, SMS). C'est une relation
# quasi déterministe → le modèle la retrouve presque parfaitement.

# ---------- E : INTERPRÉTATION & PRÉDICTION ----------
importances = pd.Series(arbre.feature_importances_, index=features).sort_values(ascending=False)
print("\n=== VARIABLES IMPORTANTES ===\n", importances.head(5))

def predire_facture(modele, colonnes, **infos):
    client = pd.DataFrame(0, index=[0], columns=colonnes)
    for cle, val in infos.items():
        if cle in client.columns:
            client[cle] = val
    return modele.predict(client)[0]

# Gros consommateur data
f1 = predire_facture(lr, features, age=28, anciennete_mois=24,
                     conso_data_go=40, minutes_appel=300, nb_sms=100, nb_reclamations=0)
print(f"\nGros consommateur data → {f1:,.0f} FCFA")
# Petit consommateur
f2 = predire_facture(lr, features, age=55, anciennete_mois=60,
                     conso_data_go=3, minutes_appel=80, nb_sms=15, nb_reclamations=1)
print(f"Petit consommateur → {f2:,.0f} FCFA")
```

## Résultats attendus TP4

```
Régression linéaire   : R² ~0.994 | MAE ~1 570 FCFA   ← excellent
Arbre de décision     : R² ~0.992
KNN (k=5)             : R² ~0.979

Variables importantes : conso_data_go, minutes_appel (les gros postes de la facture)
```

> 💡 **Point pédagogique clé (Q13)** : le R² est **exceptionnellement élevé (~0.99)** — c'est inhabituel dans la vraie vie ! La raison : la facture est **calculée directement** à partir des consommations (data × prix + minutes × prix + SMS × prix). La relation est donc quasi **déterministe**, et le modèle la retrouve presque parfaitement. C'est une excellente occasion d'expliquer qu'un R² proche de 1 peut signaler soit un problème "facile", soit une **fuite de données** (data leakage) — ici c'est le premier cas, mais l'apprenant doit se poser la question.

> ⚠️ **Piège à surveiller** : un apprenant qui inclurait `churn` comme feature n'aurait pas de problème ici (pas de fuite). Mais s'il incluait accidentellement une variable dérivée de la facture, ce serait de la fuite de données. Bonne occasion d'aborder ce concept.

---

## Grilles de correction

### TP2 — Crédit (/100)
| Partie | Critère | Points |
|--------|---------|--------|
| A | EDA + 3 visualisations | /20 |
| B | Nettoyage + encodage + split | /20 |
| C | 3 modèles vus comparés | /20 |
| D | Matrice confusion + rapport + **réflexion métier** | /20 |
| E | Variables importantes + fonction | /20 |

Repère : meilleur modèle ~0.90.

### TP3 — Churn (/100)
| Partie | Critère | Points |
|--------|---------|--------|
| A | EDA + 3 visualisations + hypothèses | /20 |
| B | Préparation + split stratifié + client_id exclu | /20 |
| C | 3 modèles vus comparés | /20 |
| D | Matrice confusion + **importance du recall** (Q13) | /20 |
| E | Facteurs de churn + fonction + **actions fidélisation** | /20 |

Repère : précision ~0.85, mais **surveiller le recall de "Part" (~0.61)** — c'est le vrai enjeu. Un apprenant qui ne discute que la précision globale sans mentionner le recall/déséquilibre perd les points de la Partie D.

### TP4 — Facture (/100)
| Partie | Critère | Points |
|--------|---------|--------|
| A | EDA + corrélations + nuages de points | /20 |
| B | Préparation + normalisation justifiée + client_id exclu | /20 |
| C | 3 modèles vus comparés (R² + MAE) | /20 |
| D | Graphique préd/réel + overfitting + **réflexion sur R² élevé** (Q13) | /20 |
| E | Variables importantes + fonction + tests profils | /20 |

Repère : R² ~0.99. Le point clé (Q13) est de **comprendre pourquoi** le R² est si élevé (facture calculée à partir des consommations).

---

*🔐 Document enseignant — Solutions TP2, TP3 & TP4 | Bootcamp Data Science*
