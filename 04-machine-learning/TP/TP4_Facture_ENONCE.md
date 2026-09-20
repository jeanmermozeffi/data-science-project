# 💰 TP4 — Prédire la Facture Mensuelle d'un Client Télécom

> **Module Data Science — Machine Learning** | Projet pratique à réaliser en autonomie
> **Dataset** : `clients_telecom.csv` (8 000 clients)

---

## 1. Contexte

Le même opérateur télécom souhaite maintenant **estimer la facture mensuelle** d'un client à partir de son profil et de son comportement de consommation. Cet outil servirait à :
- Simuler la facture d'un nouveau client selon ses usages prévus
- Détecter les factures anormales (erreurs de facturation, fraude)
- Proposer le forfait le plus adapté à chaque profil

---

## 2. Objectif

Construire et évaluer un modèle de **régression** qui prédit la variable `facture_mensuelle` (un montant en FCFA) à partir des caractéristiques du client.

Vous devrez évaluer la qualité de vos prédictions et identifier les facteurs qui influencent le plus la facture.

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
| **`facture_mensuelle`** | numérique | **🎯 Cible à prédire (FCFA)** |
| `nb_reclamations` | numérique | Nombre de réclamations |
| `churn` | binaire | 1 = le client est parti (peut servir de feature ou être ignoré) |

> ⚠️ `client_id` est un simple identifiant : il ne doit **pas** servir de variable prédictive.

---

## 4. Travail demandé

Réalisez un notebook complet structuré selon les étapes suivantes.

### Partie A — Exploration et compréhension (EDA)

1. Chargez le dataset et affichez ses dimensions, types et statistiques descriptives.
2. Analysez la **distribution de la cible** `facture_mensuelle` (histogramme, statistiques).
3. Étudiez les **corrélations** entre les variables de consommation et la facture (heatmap). Quelles variables semblent le plus liées à la facture ?
4. Produisez au moins **2 nuages de points** montrant la relation entre une variable de consommation et la facture.

### Partie B — Préparation

5. Vérifiez et traitez d'éventuelles valeurs manquantes ou anomalies.
6. Sélectionnez les features pertinentes (n'incluez pas `client_id`).
7. Séparez les données en features (X) et cible (y), puis en train (80%) et test (20%).
8. Réfléchissez à la nécessité de **normaliser** les données selon les modèles utilisés.

### Partie C — Modélisation

9. Entraînez **les 3 modèles de régression vus en cours** : régression linéaire, arbre de décision et KNN.
10. Pour chaque modèle, calculez le **R²** et le **MAE** (erreur absolue moyenne) sur le test set.

### Partie D — Évaluation approfondie

11. Comparez les 3 modèles dans un tableau récapitulatif (R² et MAE).
12. Pour votre meilleur modèle, tracez un graphique **prédictions vs valeurs réelles** (avec la diagonale de référence).
13. **Question de réflexion** : le R² obtenu est-il très élevé ? Selon vous, pourquoi la facture est-elle aussi bien prédictible à partir des consommations ? (indice : réfléchissez à la façon dont une facture télécom est réellement calculée).
14. **Attention à l'overfitting** : pour l'arbre de décision, testez plusieurs profondeurs (`max_depth`) et observez l'effet sur le R² du test.

### Partie E — Interprétation et prédiction

15. Identifiez les **variables les plus importantes** pour prédire la facture.
16. Créez une **fonction** qui prend les caractéristiques d'un client (consommation data, minutes, SMS...) et prédit sa facture mensuelle.
17. Testez votre fonction sur 2-3 profils de clients de votre invention (ex : un gros consommateur data, un petit consommateur).

---

## 5. Critères d'évaluation

| Critère | Points |
|---------|--------|
| Exploration des données (EDA) + analyse des corrélations | /20 |
| Préparation correcte (features, split, normalisation justifiée) | /20 |
| Entraînement des 3 modèles vus et comparaison (R², MAE) | /20 |
| Évaluation approfondie (graphique préd. vs réel, overfitting, réflexion) | /20 |
| Interprétation, fonction de prédiction et tests sur profils | /20 |
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
├── 📊 Le R² mesure la qualité, le MAE donne l'erreur concrète en FCFA
├── 🌳 Pour l'arbre : trop profond = overfitting (testez plusieurs max_depth)
├── 📏 Le KNN nécessite la NORMALISATION (basé sur les distances)
├── 🚫 N'utilisez PAS client_id comme variable prédictive
└── 📝 Documentez vos choix et vos interprétations tout au long
```

> 💡 **Rappel important** : pour prédire un **nombre** (la facture en FCFA), on utilise des algorithmes de **régression** (régression linéaire, arbre de décision, KNN) — la régression logistique, elle, sert à la classification.

---

## 8. Question bonus (facultatif)

Comparez les **temps de prédiction** des 3 modèles sur le test set (avec le module `time`). Lequel est le plus lent en prédiction, et pourquoi ? (indice : rappelez-vous que le KNN est un algorithme "paresseux" qui calcule les distances au moment de la prédiction).

---

*📘 Module Data Science — TP4 : Prédiction de la facture mensuelle | Bootcamp Data Science*
