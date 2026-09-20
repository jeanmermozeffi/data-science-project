# 📱 TP3 — Prédire le Départ d'un Client Télécom (Churn)

> **Module Data Science — Machine Learning** | Projet pratique à réaliser en autonomie
> **Dataset** : `clients_telecom.csv` (8 000 clients)

---

## 1. Contexte

Un opérateur de téléphonie mobile en Afrique de l'Ouest perd chaque mois des clients qui résilient leur abonnement pour aller chez un concurrent : c'est ce qu'on appelle le **churn** (attrition). Retenir un client existant coûte **bien moins cher** que d'en acquérir un nouveau.

La direction souhaite un **modèle de Machine Learning** capable de prédire **à l'avance** quels clients risquent de partir (`churn = 1`) afin de leur proposer des offres de fidélisation ciblées **avant** qu'ils ne résilient.

---

## 2. Objectif

Construire et évaluer un modèle de **classification** qui prédit la variable `churn` (0 = reste, 1 = part) à partir des caractéristiques et du comportement de consommation du client.

Vous devrez identifier les **facteurs de risque** de départ et proposer des actions de fidélisation.

---

## 3. Description du dataset

Le fichier `clients_telecom.csv` contient **8 000 clients** avec les colonnes suivantes :

| Colonne | Type | Description |
|---------|------|-------------|
| `client_id` | identifiant | Numéro unique du client |
| `age` | numérique | Âge du client |
| `anciennete_mois` | numérique | Ancienneté chez l'opérateur (mois) |
| `conso_data_go` | numérique | Consommation data mensuelle (Go) |
| `minutes_appel` | numérique | Minutes d'appel mensuelles |
| `nb_sms` | numérique | Nombre de SMS mensuels |
| `facture_mensuelle` | numérique | Facture mensuelle moyenne (FCFA) |
| `nb_reclamations` | numérique | Nombre de réclamations |
| **`churn`** | binaire | **🎯 Cible : 1 = le client est parti, 0 = il est resté** |

> ⚠️ `client_id` est un simple identifiant : il ne doit **pas** servir de variable prédictive.

---

## 4. Travail demandé

Réalisez un notebook complet structuré selon les étapes suivantes.

### Partie A — Exploration et compréhension (EDA)

1. Chargez le dataset et affichez ses dimensions, types et statistiques descriptives.
2. Analysez la **distribution de la cible** : quelle proportion de clients ont résilié ? Le jeu de données est-il équilibré ?
3. Produisez au moins **3 visualisations pertinentes** explorant le lien entre les variables et le churn (par exemple : taux de churn selon le nombre de réclamations, selon l'ancienneté, selon la facture...).
4. Formulez des **hypothèses** : quels clients vous semblent les plus à risque de partir ?

### Partie B — Préparation

5. Vérifiez et traitez d'éventuelles valeurs manquantes ou anomalies.
6. Sélectionnez les features pertinentes (n'incluez pas `client_id`).
7. Séparez les données en features (X) et cible (y), puis en train (80%) et test (20%). Pensez à `stratify` pour conserver les proportions de churn.
8. Réfléchissez à la nécessité de **normaliser** les données selon les modèles utilisés.

### Partie C — Modélisation

9. Entraînez **les 3 modèles de classification vus en cours** : régression logistique, arbre de décision et KNN.
10. Pour chaque modèle, mesurez la **précision** sur le test set.

### Partie D — Évaluation approfondie

11. Pour votre meilleur modèle, affichez la **matrice de confusion** et interprétez-la.
12. Affichez le **rapport de classification** (precision, recall, f1-score) et expliquez ces métriques dans le contexte du churn.
13. **Question de réflexion métier** : pour l'opérateur, quel type d'erreur est le plus coûteux — ne pas détecter un client qui va partir (faux négatif) ou alerter à tort sur un client fidèle (faux positif) ? Justifiez, et expliquez pourquoi le **recall** (rappel) est particulièrement important dans ce cas.

### Partie E — Interprétation et action

14. Identifiez les **variables les plus importantes** dans la prédiction du churn.
15. Créez une **fonction** qui prend les caractéristiques d'un client et prédit son risque de départ.
16. Sur la base de vos découvertes, proposez **2-3 actions de fidélisation concrètes** ciblant les clients à risque.

---

## 5. Critères d'évaluation

| Critère | Points |
|---------|--------|
| Exploration des données (EDA) pertinente et visualisations claires | /20 |
| Préparation correcte (features, split stratifié, normalisation justifiée) | /20 |
| Entraînement des 3 modèles vus et comparaison | /20 |
| Évaluation approfondie (matrice de confusion, métriques, réflexion métier) | /20 |
| Interprétation, fonction de prédiction et actions de fidélisation | /20 |
| **Total** | **/100** |

---

## 6. Livrable attendu

Un **notebook Jupyter/Colab** (`.ipynb`) :
- Bien structuré (titres, sections, commentaires)
- Avec du code **propre et commenté**
- Contenant vos **interprétations écrites** (pas seulement du code)
- Se terminant par une **conclusion** résumant votre meilleur modèle, les facteurs de churn identifiés et vos recommandations

---

## 7. Conseils

```
CONSEILS POUR RÉUSSIR
│
├── 📖 Réutilisez la démarche des chapitres précédents (nettoyage, EDA, ML)
├── ⚖️  Vérifiez si les classes sont équilibrées (churn souvent minoritaire)
├── 🔍 La précision seule ne suffit pas : analysez recall et matrice de confusion
├── 💡 Pensez au contexte MÉTIER : détecter les partants est l'objectif principal
├── 🚫 N'utilisez PAS client_id comme variable prédictive
└── 📝 Documentez vos choix et vos interprétations tout au long
```

> 💡 **Rappel important** : pour prédire une **catégorie** (part / reste), on utilise des algorithmes de **classification** (régression logistique, arbre de décision, KNN) — **pas** la régression linéaire, qui prédit des nombres.

> 💡 **Astuce sur le recall** : dans un problème de churn, on préfère souvent "sur-détecter" les partants potentiels (quitte à quelques fausses alertes) plutôt que d'en laisser filer. Regardez donc attentivement le **recall de la classe "churn = 1"**, pas seulement la précision globale.

---

*📘 Module Data Science — TP3 : Prédiction du churn client | Bootcamp Data Science*
