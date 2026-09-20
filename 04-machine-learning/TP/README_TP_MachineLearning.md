# 📚 TP Machine Learning — Guide d'organisation

Quatre travaux pratiques sur des **datasets réalistes** (>5 000 lignes), tous en **apprentissage supervisé** avec les **3 algorithmes vus en cours** : régression linéaire/logistique, arbre de décision, KNN.

---

## 🗂️ Vue d'ensemble des 4 TP

| TP | Sujet | Type ML | Dataset | Lignes | Statut |
|----|-------|---------|---------|--------|--------|
| **TP1** | Prédiction de loyer (Abidjan) | Régression | `loyers_abidjan.csv` | 6 000 | 🎓 **À traiter en classe** |
| **TP2** | Accord de crédit | Classification | `demandes_credit.csv` | 7 000 | 📝 Énoncé seul (autonomie) |
| **TP3** | Départ client / Churn | Classification | `clients_telecom.csv` | 8 000 | 📝 Énoncé seul (autonomie) |
| **TP4** | Facture mensuelle | Régression | `clients_telecom.csv` | 8 000 | 📝 Énoncé seul (autonomie) |

> 💡 Les TP3 et TP4 partagent le **même dataset** (`clients_telecom.csv`) mais résolvent deux problèmes différents : prédire une **catégorie** (churn) vs un **nombre** (facture). Excellente illustration que le même dataset peut servir à la classification ET à la régression selon la cible choisie.

---

## 📁 Fichiers fournis

### Pour le cours (TP1 — à traiter ensemble)
- **`TP1_Prediction_Loyer_GUIDE.md`** — cours guidé complet, pas à pas, avec solution
- **`TP1_Prediction_Loyer_GUIDE.ipynb`** — notebook Colab prêt à exécuter

### Pour les apprenants (énoncés seuls, SANS solution)
- **`TP2_Credit_ENONCE.md`** — accord de crédit (classification)
- **`TP3_Churn_ENONCE.md`** — départ client (classification)
- **`TP4_Facture_ENONCE.md`** — facture mensuelle (régression)

### Pour vous uniquement (🔐 NE PAS DISTRIBUER)
- **`SOLUTIONS_TP2_TP3_TP4_ENSEIGNANT.md`** — solutions complètes + grilles de correction

### Datasets (dossier `tp_datasets/`)
- `loyers_abidjan.csv` (6 000 lignes)
- `demandes_credit.csv` (7 000 lignes)
- `clients_telecom.csv` (8 000 lignes, avec colonnes `facture_mensuelle` et `churn`)

---

## 🎯 Ce que chaque TP fait travailler

### TP1 — Loyer (Régression) 🎓
```
Compétences : nettoyage, encodage, régression linéaire, arbre, KNN,
              métriques R²/MAE/RMSE, importance des variables, prédiction
Résultat attendu : R² ~0.83 (linéaire), ~0.80 (arbre), ~0.87 (KNN)
Message clé : comparer les 3 algos ; pas de meilleur algorithme universel (KNN gagne)
```

### TP2 — Crédit (Classification) 📝
```
Compétences : classification (régression logistique, arbre, KNN), matrice de confusion,
              precision/recall, RÉFLEXION MÉTIER (faux positifs vs faux négatifs)
Résultat attendu : précision ~0.90
Message clé : penser au COÛT des erreurs (accorder un mauvais crédit coûte cher)
```

### TP3 — Churn (Classification) 📝
```
Compétences : classification sur classes DÉSÉQUILIBRÉES, importance du RECALL,
              matrice de confusion, actions de fidélisation
Résultat attendu : précision ~0.85, mais recall classe "Part" ~0.61
Message clé : la précision globale trompe sur données déséquilibrées → regarder le recall
```

### TP4 — Facture (Régression) 📝
```
Compétences : régression, R²/MAE, overfitting de l'arbre, réflexion sur R² élevé
Résultat attendu : R² ~0.99 (facture calculée à partir des consommations)
Message clé : comprendre POURQUOI un R² est très élevé (relation déterministe / data leakage)
```

---

## 📊 Progression pédagogique recommandée

```
1. RÉGRESSION (TP1 en classe)
   → prédire un nombre, workflow complet ensemble
        │
        ▼
2. CLASSIFICATION (TP2 en autonomie)
   → prédire une catégorie, réflexion sur le coût des erreurs
        │
        ▼
3. CLASSIFICATION avancée (TP3 en autonomie)
   → classes déséquilibrées, importance du recall
        │
        ▼
4. RÉGRESSION (TP4 en autonomie)
   → consolidation, réflexion sur la qualité d'un R²
```

---

## 💡 Notes pédagogiques

**TP1 (en classe) :** insistez sur la comparaison des 3 algos — le KNN gagne, ce qui illustre "pas de meilleur algorithme universel". La démo de l'overfitting selon la profondeur de l'arbre est aussi un moment clé.

**TP2 (autonomie) :** la question 13 (faux positifs vs faux négatifs) différencie les bonnes copies. Vérifiez la normalisation appliquée pour la régression logistique/KNN mais pas pour l'arbre.

**TP3 (autonomie) :** **le piège pédagogique est le déséquilibre des classes** (25% de churn). Un apprenant qui ne regarde que la précision globale (~0.85) rate l'essentiel : le recall de la classe "Part" n'est que ~0.61. Le bon réflexe est d'analyser le recall et la matrice de confusion.

**TP4 (autonomie) :** le R² est exceptionnellement élevé (~0.99). Le point clé est de **comprendre pourquoi** : la facture est calculée à partir des consommations (relation déterministe). C'est l'occasion d'introduire la notion de **data leakage** (fuite de données).

---

## ⚙️ Prérequis techniques

```python
pip install pandas numpy scikit-learn matplotlib seaborn
```

Les datasets doivent être téléchargés dans l'environnement (Colab : panneau Fichiers → Importer).

Tous les TP n'utilisent que les **3 algorithmes du cours** : régression linéaire/logistique, arbre de décision, KNN.

---

*📘 Module Data Science — TP Machine Learning | Bootcamp Data Science*
