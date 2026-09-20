# 💳 TP2 — Prédire l'Accord d'une Demande de Crédit

> **Module Data Science — Machine Learning** | Projet pratique à réaliser en autonomie
> **Dataset** : `demandes_credit.csv` (7 000 demandes)

---

## 1. Contexte

Une institution de microfinance en Afrique de l'Ouest reçoit chaque jour des centaines de demandes de crédit. Actuellement, chaque dossier est examiné manuellement par un agent, ce qui est **long et subjectif**.

La direction souhaite développer un **modèle de Machine Learning** capable de prédire automatiquement si une demande de crédit devrait être **accordée (1)** ou **refusée (0)**, à partir des informations du demandeur. Ce modèle servira d'**aide à la décision** pour les agents.

---

## 2. Objectif

Construire et évaluer un modèle de **classification** qui prédit la variable `credit_accorde` (0 ou 1) à partir des caractéristiques du demandeur.

Votre modèle devra atteindre une **précision satisfaisante** et vous devrez être capable d'**expliquer** quels facteurs influencent le plus la décision.

---

## 3. Description du dataset

Le fichier `demandes_credit.csv` contient **7 000 demandes** avec les colonnes suivantes :

| Colonne | Type | Description |
|---------|------|-------------|
| `age` | numérique | Âge du demandeur |
| `revenu_mensuel` | numérique | Revenu mensuel en FCFA |
| `anciennete_emploi` | numérique | Ancienneté dans l'emploi (années) |
| `type_contrat` | catégoriel | CDI / CDD / Indépendant / Fonctionnaire |
| `montant_demande` | numérique | Montant du crédit demandé (FCFA) |
| `duree_pret_mois` | numérique | Durée de remboursement (mois) |
| `nb_credits_actuels` | numérique | Nombre de crédits en cours |
| `historique_credit` | catégoriel | Bon / Moyen / Mauvais |
| `apport_personnel` | numérique | Apport personnel (FCFA) |
| `situation_familiale` | catégoriel | Célibataire / Marié / Divorcé |
| `nb_personnes_charge` | numérique | Nombre de personnes à charge |
| **`credit_accorde`** | binaire | **🎯 Cible : 1 = accordé, 0 = refusé** |

> ⚠️ Le dataset contient des **valeurs manquantes** dans certaines colonnes — à vous de les traiter.

---

## 4. Travail demandé

Réalisez un notebook complet structuré selon les étapes suivantes.

### Partie A — Exploration et compréhension (EDA)

1. Chargez le dataset et affichez ses dimensions, types et statistiques descriptives.
2. Identifiez les colonnes contenant des valeurs manquantes et leur pourcentage.
3. Analysez la **distribution de la cible** : quelle proportion de crédits sont accordés/refusés ? Le jeu de données est-il équilibré ?
4. Produisez au moins **3 visualisations pertinentes** explorant le lien entre les variables et la décision de crédit (ex : taux d'accord selon le type de contrat, selon l'historique, selon le revenu...).

### Partie B — Nettoyage et préparation

5. Traitez les valeurs manquantes en justifiant votre stratégie.
6. Encodez les variables catégorielles de manière appropriée.
7. Séparez les données en features (X) et cible (y), puis en train (80%) et test (20%).
8. Réfléchissez à la nécessité de normaliser les données selon les modèles utilisés.

### Partie C — Modélisation

9. Entraînez **les 3 modèles de classification vus en cours** : régression logistique, arbre de décision et KNN.
10. Pour chaque modèle, mesurez la **précision** sur le test set.

### Partie D — Évaluation approfondie

11. Pour votre meilleur modèle, affichez la **matrice de confusion** et interprétez-la.
12. Affichez le **rapport de classification** (precision, recall, f1-score) et expliquez ce que signifient ces métriques dans le contexte du crédit.
13. **Question de réflexion métier** : dans le cas d'un crédit, quel type d'erreur est le plus coûteux pour la banque — accorder un crédit à quelqu'un qui ne remboursera pas (faux positif), ou refuser un bon client (faux négatif) ? Comment votre analyse de la matrice de confusion éclaire-t-elle cette question ?

### Partie E — Interprétation

14. Identifiez les **variables les plus importantes** dans la décision de crédit.
15. Créez une **fonction** qui prend les caractéristiques d'un nouveau demandeur et prédit si son crédit sera accordé ou non.
16. Testez votre fonction sur 2-3 profils de demandeurs de votre invention.

---

## 5. Critères d'évaluation

| Critère | Points |
|---------|--------|
| Exploration des données (EDA) pertinente et visualisations claires | /20 |
| Nettoyage et préparation corrects et justifiés | /20 |
| Entraînement d'au moins 3 modèles fonctionnels | /20 |
| Évaluation approfondie (matrice de confusion, métriques, réflexion métier) | /20 |
| Interprétation, fonction de prédiction et qualité générale du notebook | /20 |
| **Total** | **/100** |

---

## 6. Livrable attendu

Un **notebook Jupyter/Colab** (`.ipynb`) :
- Bien structuré (titres, sections, commentaires)
- Avec du code **propre et commenté**
- Contenant vos **interprétations écrites** (pas seulement du code)
- Se terminant par une **conclusion** résumant votre meilleur modèle et vos découvertes

---

## 7. Conseils

```
CONSEILS POUR RÉUSSIR
│
├── 📖 Réutilisez la démarche des chapitres précédents (nettoyage, EDA, ML)
├── 🧹 Ne négligez pas le nettoyage : "garbage in, garbage out"
├── ⚖️  Vérifiez si les classes sont équilibrées avant d'interpréter la précision
├── 🔍 Une précision élevée ne suffit pas : analysez la matrice de confusion
├── 💡 Pensez au contexte MÉTIER, pas seulement aux chiffres
└── 📝 Documentez vos choix et vos interprétations tout au long
```

> 💡 **Rappel important** : pour prédire une **catégorie** (accordé/refusé), on utilise des algorithmes de **classification** (régression logistique, arbre de décision, KNN) — **pas** la régression linéaire, qui prédit des nombres.

---

*📘 Module Data Science — TP2 : Prédiction d'accord de crédit | Bootcamp Data Science*
