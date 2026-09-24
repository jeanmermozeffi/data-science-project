# 📏 Les Métriques d'Évaluation — Cours Bootcamp Data Science

> **Module Data Science — Machine Learning** | Prérequis : cours "Algorithmes de ML" et "Train/Test Split & Validation Croisée"

---

## Table des matières

### Partie I — Introduction
1. [Pourquoi les métriques ? Le score ne suffit pas](#1-pourquoi-les-métriques--le-score-ne-suffit-pas)
2. [Trois familles de problèmes, trois familles de métriques](#2-trois-familles-de-problèmes-trois-familles-de-métriques)

### Partie II — Métriques de Classification
3. [La matrice de confusion : la source de tout](#3-la-matrice-de-confusion--la-source-de-tout)
4. [Accuracy (exactitude)](#4-accuracy-exactitude)
5. [Precision (précision)](#5-precision-précision)
6. [Recall (rappel / sensibilité)](#6-recall-rappel--sensibilité)
7. [F1 Score](#7-f1-score)
8. [Courbe ROC et AUC](#8-courbe-roc-et-auc)
9. [Compléments : Log Loss, PR-AUC, moyennes multiclasses](#9-compléments--log-loss-pr-auc-moyennes-multiclasses)
10. [Quelle métrique de classification choisir ?](#10-quelle-métrique-de-classification-choisir-)

### Partie III — Métriques de Régression
11. [MAE — Erreur absolue moyenne](#11-mae--erreur-absolue-moyenne)
12. [MSE — Erreur quadratique moyenne](#12-mse--erreur-quadratique-moyenne)
13. [RMSE — Racine de l'erreur quadratique moyenne](#13-rmse--racine-de-lerreur-quadratique-moyenne)
14. [RMSLE — Erreur logarithmique](#14-rmsle--erreur-logarithmique)
15. [R² (coefficient de détermination)](#15-r-coefficient-de-détermination)
16. [Compléments : MAPE et R² ajusté](#16-compléments--mape-et-r-ajusté)
17. [Quelle métrique de régression choisir ?](#17-quelle-métrique-de-régression-choisir-)

### Partie IV — Métriques de Clustering
18. [Le défi : évaluer sans « bonne réponse »](#18-le-défi--évaluer-sans-bonne-réponse)
19. [Silhouette Score](#19-silhouette-score)
20. [Indice de Davies-Bouldin](#20-indice-de-davies-bouldin)
21. [Inertie (Within-Cluster Sum of Squares)](#21-inertie-within-cluster-sum-of-squares)
22. [Adjusted Rand Index (ARI)](#22-adjusted-rand-index-ari)
23. [Compléments : Calinski-Harabasz, NMI, V-measure](#23-compléments--calinski-harabasz-nmi-v-measure)
24. [Quelle métrique de clustering choisir ?](#24-quelle-métrique-de-clustering-choisir-)

### Partie V — Synthèse
25. [Tableau récapitulatif général](#25-tableau-récapitulatif-général)
26. [Conclusion](#26-conclusion)
27. [✅ Point de contrôle — Métriques](#27--point-de-contrôle--métriques)

---

# PARTIE I — INTRODUCTION

## 1. Pourquoi les métriques ? Le score ne suffit pas

### 📖 L'idée

Un modèle produit des prédictions. Une **métrique** est un **nombre** qui mesure à quel point ces prédictions sont **bonnes**. Sans métrique, impossible de comparer deux modèles, de détecter un problème, ou de décider si un modèle est prêt pour la production.

> 💡 **Analogie** : un médecin ne dit jamais « le patient va bien » sans chiffres. Il mesure la tension, la température, le rythme cardiaque… Chaque **mesure** éclaire un aspect différent. Une seule ne suffit jamais. Les métriques ML, c'est pareil : chacune raconte **une partie** de l'histoire.

### 1.1 Le piège du « 95 % de réussite »

Imaginez un modèle qui détecte une maladie rare touchant **1 personne sur 100**.

```
Modèle "paresseux" : il répond TOUJOURS "pas malade"
→ il a raison 99 fois sur 100
→ Accuracy = 99 % 🎉 ... mais il rate 100 % des malades ! 💀
```

Ce modèle est **inutile** — et pourtant son *accuracy* est excellente. C'est **la** leçon de ce cours :

> 🔑 **La bonne métrique dépend du problème.** Une métrique choisie à la légère peut cacher un modèle catastrophique. Choisir la métrique, c'est déjà faire de la data science.

---

## 2. Trois familles de problèmes, trois familles de métriques

On n'évalue pas de la même façon selon ce que le modèle prédit.

| Famille | Le modèle prédit… | A-t-on la « vraie réponse » ? | Métriques |
|---------|-------------------|-------------------------------|-----------|
| **Classification** | une **catégorie** (spam / pas spam) | ✅ Oui (supervisé) | Accuracy, Precision, Recall, F1, AUC |
| **Régression** | un **nombre** (prix, température) | ✅ Oui (supervisé) | MAE, MSE, RMSE, RMSLE, R² |
| **Clustering** | des **groupes** (segments) | ❌ Non (non supervisé) | Silhouette, Davies-Bouldin, Inertie, ARI |

> 🔑 **Règle de survie** : ne jamais évaluer une régression avec l'accuracy, ni un clustering avec le F1. Chaque famille a ses outils. Le premier réflexe : *« quel type de sortie mon modèle produit-il ? »*

---

# PARTIE II — MÉTRIQUES DE CLASSIFICATION

## 3. La matrice de confusion : la source de tout

### 📖 Définition

La **matrice de confusion** croise les prédictions du modèle avec la vérité. Pour un problème binaire (positif / négatif), elle a 4 cases. **Presque toutes les métriques de classification en découlent.**

```
                          PRÉDICTION du modèle
                     ┌─────────────┬─────────────┐
                     │  Positif    │  Négatif    │
        ┌────────────┼─────────────┼─────────────┤
  RÉEL  │  Positif   │  ✅ VP      │  ❌ FN      │
        │            │ (Vrai Pos.) │ (Faux Nég.) │
        ├────────────┼─────────────┼─────────────┤
        │  Négatif   │  ❌ FP      │  ✅ VN      │
        │            │ (Faux Pos.) │ (Vrai Nég.) │
        └────────────┴─────────────┴─────────────┘
```

| Terme | Signification | Exemple (test médical) |
|-------|---------------|------------------------|
| **VP** (Vrai Positif) | Prédit positif, **et c'est vrai** | Malade détecté malade ✅ |
| **VN** (Vrai Négatif) | Prédit négatif, **et c'est vrai** | Sain détecté sain ✅ |
| **FP** (Faux Positif) | Prédit positif, **mais faux** | Sain déclaré malade (fausse alerte) |
| **FN** (Faux Négatif) | Prédit négatif, **mais faux** | Malade déclaré sain (raté grave !) |

> 🔑 **FP vs FN, la vraie question métier** : une **fausse alerte** (FP) et un **raté** (FN) n'ont pas le même coût. Dépister un cancer : un FN (malade non détecté) est dramatique. Filtrer du spam : un FP (vrai email classé spam) est plus gênant qu'un FN. **La métrique doit refléter le coût le plus grave.**

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)
print(cm)
ConfusionMatrixDisplay(cm, display_labels=["Négatif", "Positif"]).plot()
plt.show()
```

---

## 4. Accuracy (exactitude)

### 📖 Définition

L'**accuracy** est la proportion de prédictions correctes, toutes classes confondues.

$$\text{Accuracy} = \frac{VP + VN}{VP + VN + FP + FN} = \frac{\text{bonnes prédictions}}{\text{total}}$$

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)   # ex. 0.92 → 92 % de prédictions correctes
```

### ✅ Quand l'utiliser / ❌ quand l'éviter

| ✅ Adaptée quand… | ❌ À éviter quand… |
|-------------------|--------------------|
| Les classes sont **équilibrées** (≈ 50/50) | Classes **déséquilibrées** (fraude, maladie rare) |
| Toutes les erreurs ont le **même coût** | FP et FN ont des coûts très différents |

> ⚠️ **Le piège de l'accuracy** (§1.1) : sur des données déséquilibrées, elle est **trompeuse**. Un modèle à 99 % d'accuracy peut ne rien détecter du tout. **Réflexe** : dès que les classes sont déséquilibrées, passez à Precision / Recall / F1.

---

## 5. Precision (précision)

### 📖 Définition

Parmi tout ce que le modèle a **prédit positif**, quelle proportion l'était **vraiment** ?

$$\text{Precision} = \frac{VP}{VP + FP}$$

> 💡 **En clair** : *« Quand mon modèle crie "positif !", a-t-il raison ? »* La précision **punit les faux positifs** (fausses alertes).

```python
from sklearn.metrics import precision_score
precision_score(y_test, y_pred)
```

### 🎯 Quand la privilégier

Quand le **coût d'un faux positif est élevé** — on veut éviter les fausses alertes :

- **Filtrage de spam** : classer un vrai email en spam (FP) fait perdre un message important.
- **Recommandation** : recommander un mauvais produit érode la confiance.
- **Justice / crédit** : accuser à tort (FP) a de lourdes conséquences.

> 🔑 **Precision haute = « quand je dis oui, c'est fiable ».**

---

## 6. Recall (rappel / sensibilité)

### 📖 Définition

Parmi tous les cas **réellement positifs**, quelle proportion le modèle a-t-il **retrouvée** ?

$$\text{Recall} = \frac{VP}{VP + FN}$$

> 💡 **En clair** : *« Parmi tous les vrais positifs, combien n'ai-je pas ratés ? »* Le rappel **punit les faux négatifs** (les oublis).

```python
from sklearn.metrics import recall_score
recall_score(y_test, y_pred)
```

### 🎯 Quand le privilégier

Quand le **coût d'un faux négatif est élevé** — rater un cas positif est grave :

- **Dépistage médical** : rater un malade (FN) peut être fatal → on veut un **recall maximal**.
- **Détection de fraude** : laisser passer une fraude coûte cher.
- **Sécurité** : ne pas détecter une menace est inacceptable.

> 🔑 **Recall haut = « je rate très peu de vrais positifs ».**

### ⚖️ Le compromis Precision ↔ Recall

Precision et Recall **s'opposent** souvent. Rendre le modèle plus « prudent » (ne dire positif que si très sûr) **augmente la précision** mais **baisse le rappel**, et inversement.

```
Seuil BAS (dit "positif" facilement)   Seuil HAUT (très exigeant)
→ attrape presque tous les positifs    → ne se trompe presque jamais
→ Recall ↑  mais  Precision ↓          → Precision ↑  mais  Recall ↓
   (beaucoup de fausses alertes)          (rate beaucoup de cas)
```

> 🔑 On règle ce curseur avec le **seuil de décision** (par défaut 0.5). Pas de réponse universelle : le bon seuil dépend du **coût métier** des FP et des FN.

---

## 7. F1 Score

### 📖 Définition

Le **F1 Score** combine Precision et Recall en un seul nombre : c'est leur **moyenne harmonique**.

$$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

> 💡 **Pourquoi la moyenne harmonique et pas la moyenne classique ?** La moyenne harmonique **pénalise les déséquilibres**. Precision = 1.0 et Recall = 0.0 → moyenne classique = 0.5 (flatteur), mais **F1 = 0** (juste : le modèle est nul). Le F1 n'est élevé que si **les deux** sont élevés.

```python
from sklearn.metrics import f1_score
f1_score(y_test, y_pred)
```

### 🎯 Quand l'utiliser

- Quand on veut **un seul chiffre** équilibrant Precision et Recall.
- Sur des données **déséquilibrées** (bien meilleur que l'accuracy).
- Quand FP et FN sont **tous deux** importants.

> 💡 **F-beta** : si on veut privilégier le rappel, on utilise le **F2** (β=2, poids au recall) ; pour privilégier la précision, le **F0.5**. `fbeta_score(y, y_pred, beta=2)`.

> 🔑 **Le rapport complet** : `classification_report` affiche Precision, Recall et F1 **pour chaque classe** en une commande.
>
> ```python
> from sklearn.metrics import classification_report
> print(classification_report(y_test, y_pred))
> ```

---

## 8. Courbe ROC et AUC

### 📖 L'idée

Les métriques précédentes dépendent d'un **seuil** (0.5). La **courbe ROC** évalue le modèle **à tous les seuils à la fois**, en traçant :

- en **ordonnée** : le **Taux de Vrais Positifs** (= Recall) ;
- en **abscisse** : le **Taux de Faux Positifs** (FP / (FP+VN)).

L'**AUC** (*Area Under the Curve*) est **l'aire sous cette courbe** : un seul nombre entre 0 et 1 qui résume la qualité du classifieur **indépendamment du seuil**.

```
   TVP │            ___________  ← modèle parfait (AUC = 1.0)
 (Recall)│         ╱
       │        ╱  ← bon modèle (AUC ≈ 0.9)
       │      ╱  ╱
       │    ╱  ╱
       │  ╱  ╱   ← - - - hasard (diagonale, AUC = 0.5)
       │╱ ╱
       └──────────────── TFP (Faux Positifs)
```

| AUC | Interprétation |
|-----|----------------|
| **1.0** | Classifieur parfait |
| **0.9 – 1.0** | Excellent |
| **0.7 – 0.9** | Bon à acceptable |
| **0.5** | Aléatoire (pile ou face) — inutile |
| **< 0.5** | Pire que le hasard (labels inversés ?) |

> 💡 **Interprétation intuitive de l'AUC** : c'est la **probabilité** que le modèle attribue un score plus élevé à un positif tiré au hasard qu'à un négatif tiré au hasard. AUC = 0.85 → dans 85 % des cas, il « classe bien » une paire positif/négatif.

```python
from sklearn.metrics import roc_auc_score, RocCurveDisplay

# ⚠️ AUC utilise les PROBABILITÉS, pas les classes prédites
y_proba = model.predict_proba(X_test)[:, 1]   # proba de la classe positive
print("AUC :", roc_auc_score(y_test, y_proba))
RocCurveDisplay.from_estimator(model, X_test, y_test)
```

### 🎯 Pourquoi et quand l'AUC ?

- **Indépendante du seuil** : mesure la capacité de **classement** globale du modèle.
- Idéale pour **comparer** des modèles entre eux.
- **Nécessite des probabilités** (`predict_proba`) → réservée aux modèles qui en produisent (régression logistique, arbres, forêts, gradient boosting…). Un classifieur qui ne sort que des classes « dures » ne permet pas de tracer la ROC.

> ⚠️ **Limite sur données très déséquilibrées** : l'AUC-ROC peut rester flatteuse. On lui préfère alors la **courbe Précision-Rappel (PR-AUC)**, plus sensible à la classe rare (§9).

---

## 9. Compléments : Log Loss, PR-AUC, moyennes multiclasses

> 🧩 *Ces métriques ne figuraient pas dans la liste de base mais sont incontournables en pratique.*

### 9.1 Log Loss (entropie croisée)

Mesure la qualité des **probabilités** prédites, pas seulement des classes. Elle **pénalise fortement** une prédiction confiante **et fausse** (prédire 0.99 pour une classe qui était l'autre). C'est **la fonction de coût** entraînée par la régression logistique et les réseaux de neurones.

```python
from sklearn.metrics import log_loss
log_loss(y_test, model.predict_proba(X_test))   # plus BAS = mieux
```

> 🎯 À utiliser quand la **qualité des probabilités** compte (scoring de risque, paris, calibration), pas seulement la décision finale.

### 9.2 PR-AUC (aire sous la courbe Précision-Rappel)

Alternative à l'AUC-ROC pour les données **fortement déséquilibrées** (fraude, maladie rare) : elle se concentre sur la **classe positive rare** et ignore les nombreux vrais négatifs qui gonflent l'AUC-ROC.

```python
from sklearn.metrics import average_precision_score
average_precision_score(y_test, y_proba)   # ≈ aire sous la courbe PR
```

### 9.3 Multiclasse : macro / micro / weighted

Avec **plus de deux classes**, Precision/Recall/F1 se calculent par classe, puis se **moyennent**. Le mode de moyenne change tout :

| Moyenne | Comment | Quand |
|---------|---------|-------|
| **macro** | moyenne simple des classes | traiter **chaque classe à égalité** (classe rare importante) |
| **weighted** | pondérée par l'effectif de chaque classe | refléter la **distribution réelle** |
| **micro** | agrège tous les VP/FP/FN globalement | ≈ accuracy globale |

```python
f1_score(y_test, y_pred, average="macro")      # classe rare = classe fréquente
f1_score(y_test, y_pred, average="weighted")   # pondéré par les effectifs
```

> 🔑 **Réflexe multiclasse déséquilibré** : préférez `macro` pour ne pas écraser les petites classes.

---

## 10. Quelle métrique de classification choisir ?

```
Mes classes sont-elles ÉQUILIBRÉES ?
│
├── OUI, et toutes les erreurs se valent
│        → Accuracy (simple et lisible)
│
└── NON (déséquilibrées) ou coûts d'erreur différents
         │
         ├── Rater un positif est GRAVE (médical, fraude, sécurité)
         │        → RECALL (minimiser les faux négatifs)
         │
         ├── Une fausse alerte est COÛTEUSE (spam, reco, crédit)
         │        → PRECISION (minimiser les faux positifs)
         │
         ├── Équilibrer les deux, un seul chiffre
         │        → F1 (ou F2/F0.5 selon la priorité)
         │
         └── Comparer des modèles, indépendamment du seuil
                  → AUC-ROC  (ou PR-AUC si très déséquilibré)
```

### 🔬 Pourquoi telle métrique sur tel algorithme ?

| Algorithme | Sort des probabilités ? | Métriques naturelles |
|------------|--------------------------|----------------------|
| **Régression logistique** | ✅ oui | Log Loss (coût entraîné), AUC, F1, seuil réglable |
| **Arbre / Forêt / Gradient Boosting** | ✅ oui (`predict_proba`) | AUC, F1, accuracy, PR-AUC |
| **KNN** | ✅ (proportion de voisins) | Accuracy, F1 ; AUC possible mais moins fine |
| **SVM (par défaut)** | ❌ pas de proba directe | Accuracy, F1 ; AUC via `decision_function` |

> 🔑 **La règle** : l'AUC et la Log Loss exigent des **probabilités**. Un modèle qui n'en produit pas (SVM standard) s'évalue par accuracy/F1 sur les classes dures. Ce n'est pas la métrique qui choisit l'algo, mais **le problème métier** (coût des erreurs) — l'algo détermine seulement quelles métriques sont **calculables**.

---

# PARTIE III — MÉTRIQUES DE RÉGRESSION

> En régression, le modèle prédit un **nombre**. On mesure donc l'**écart** entre la valeur prédite $\hat{y}$ et la valeur réelle $y$ : le **résidu** $(y - \hat{y})$.

## 11. MAE — Erreur absolue moyenne

### 📖 Définition

Moyenne des écarts en **valeur absolue**. C'est l'erreur moyenne « telle qu'on la ressent ».

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|$$

```python
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)   # ex. 15 000 → on se trompe de 15 000 FCFA en moyenne
```

### 🎯 Points clés

- **Même unité** que la cible → **très interprétable** (« 15 000 FCFA d'erreur moyenne »).
- **Robuste aux valeurs aberrantes** : une grosse erreur pèse proportionnellement, pas plus.
- ✅ **À privilégier** quand les **outliers ne doivent pas dominer** l'évaluation, ou pour communiquer un résultat clair à un non-technicien.

---

## 12. MSE — Erreur quadratique moyenne

### 📖 Définition

Moyenne des écarts **au carré**.

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)
```

### 🎯 Points clés

- Le carré **amplifie les grosses erreurs** : une erreur de 10 pèse 100, une erreur de 2 pèse 4.
- ✅ **À privilégier** quand les **grosses erreurs sont particulièrement graves** et doivent être fortement pénalisées.
- ⚠️ **Unité au carré** (FCFA²) → **non interprétable** directement. C'est surtout une **fonction de coût** d'entraînement (mathématiquement pratique, dérivable), d'où son omniprésence.

> 🔑 **MAE vs MSE en une phrase** : la MAE traite toutes les erreurs équitablement ; la MSE **déteste** les grosses erreurs. Le choix dépend de : *« une erreur deux fois plus grande est-elle deux fois pire (MAE) ou quatre fois pire (MSE) ? »*

---

## 13. RMSE — Racine de l'erreur quadratique moyenne

### 📖 Définition

La **racine carrée** de la MSE : on récupère l'**unité d'origine** tout en gardant la pénalisation des grosses erreurs.

$$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}$$

```python
from sklearn.metrics import mean_squared_error
import numpy as np
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# scikit-learn ≥ 1.4 :
from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(y_test, y_pred)
```

### 🎯 Points clés

- **Même unité** que la cible (comme la MAE) → interprétable.
- **Pénalise les grosses erreurs** (comme la MSE, dont elle hérite).
- **RMSE ≥ MAE toujours** ; l'écart entre les deux **révèle la présence d'outliers** (RMSE ≫ MAE = quelques grosses erreurs).

> 🔑 **RMSE = le meilleur des deux mondes** : lisible comme la MAE, sévère avec les gros écarts comme la MSE. C'est **la métrique de régression la plus rapportée** en pratique.

---

## 14. RMSLE — Erreur logarithmique

### 📖 Définition

RMSE calculée sur le **logarithme** des valeurs. On mesure l'erreur **relative (en %)** plutôt qu'absolue.

$$\text{RMSLE} = \sqrt{\frac{1}{n}\sum \big(\log(1 + y_i) - \log(1 + \hat{y}_i)\big)^2}$$

```python
from sklearn.metrics import mean_squared_log_error
import numpy as np
rmsle = np.sqrt(mean_squared_log_error(y_test, y_pred))   # y et y_pred ≥ 0 obligatoire
```

### 🎯 Quand et pourquoi ?

- ✅ La cible s'étale sur **plusieurs ordres de grandeur** (prix de 10 000 à 10 000 000).
- ✅ On se soucie de l'**erreur relative** : se tromper de 100 sur une valeur de 100 est bien pire que de se tromper de 100 sur 1 000 000.
- ✅ **Pénalise davantage la sous-estimation que la surestimation** — utile quand sous-estimer coûte cher (prévision de demande, de stock).
- ⚠️ Exige des valeurs **positives** (le log l'impose).

> 💡 **Exemples typiques** : prévision de ventes, prix immobiliers, trafic web — toute cible positive à forte dispersion.

---

## 15. R² (coefficient de détermination)

### 📖 Définition

Le **R²** mesure la **proportion de variance** de la cible **expliquée** par le modèle. C'est un score **relatif**, sans unité.

$$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} = 1 - \frac{\text{erreur du modèle}}{\text{erreur d'un modèle "moyenne"}}$$

```python
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)
```

| R² | Interprétation |
|----|----------------|
| **1.0** | Prédictions parfaites |
| **0.8** | Le modèle explique 80 % de la variance — bon |
| **0.0** | Aussi nul que prédire **toujours la moyenne** |
| **< 0** | **Pire** que prédire la moyenne (modèle inadapté) |

### 🎯 Points clés

- **Sans unité** → permet de **comparer** des modèles sur des cibles différentes.
- Répond à *« mon modèle fait-il mieux que la bête moyenne ? »*.
- ⚠️ **Un R² élevé ne garantit pas de bonnes prédictions individuelles** ; à coupler avec RMSE/MAE (le concret) pour une vision complète.

> 🔑 **La bonne pratique** : rapporter **R² + RMSE (ou MAE)** ensemble. Le R² dit *« à quel point on explique »*, la RMSE dit *« de combien on se trompe, concrètement »*.

---

## 16. Compléments : MAPE et R² ajusté

> 🧩 *Deux métriques fréquentes non listées, utiles à connaître.*

### 16.1 MAPE — Erreur absolue moyenne en pourcentage

$$\text{MAPE} = \frac{100}{n}\sum \left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

Erreur exprimée en **%** → très parlante pour le métier (« on se trompe de 8 % en moyenne »).

```python
from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(y_test, y_pred)   # 0.08 → 8 %
```

> ⚠️ **Piège** : explose si des valeurs réelles sont **nulles ou proches de 0** (division par $y_i$). À éviter dans ce cas.

### 16.2 R² ajusté

Le R² **augmente mécaniquement** quand on ajoute des variables, même inutiles. Le **R² ajusté** pénalise l'ajout de features non pertinentes → indispensable pour **comparer des modèles au nombre de variables différent**.

$$R^2_{\text{ajusté}} = 1 - (1 - R^2)\frac{n-1}{n-p-1} \quad (p = \text{nb de features})$$

> 🔑 En régression **multiple**, comparez les modèles avec le **R² ajusté**, pas le R² brut.

---

## 17. Quelle métrique de régression choisir ?

```
Que veux-je mesurer / communiquer ?
│
├── Une erreur LISIBLE, dans l'unité de la cible
│        ├── robuste aux outliers          → MAE
│        └── sévère avec les grosses erreurs → RMSE  ⭐ (le standard)
│
├── Une erreur RELATIVE (en %)
│        ├── cible à forte dispersion, valeurs > 0 → RMSLE
│        └── communication métier simple (y ≠ 0)   → MAPE
│
├── Pénaliser TRÈS fort les grosses erreurs (fonction de coût)
│        → MSE
│
└── "Mon modèle explique-t-il quelque chose ?" (score relatif)
         → R²  (R² ajusté si régression multiple)
```

### 🔬 Pourquoi telle métrique selon l'algorithme / le contexte ?

- **Régression linéaire** : entraînée en minimisant la **MSE** → cohérent de l'évaluer avec RMSE/MSE. Le R² est le score renvoyé par défaut par `.score()`.
- **Modèles robustes** (régression Huber, quantile) : conçus pour résister aux outliers → les évaluer avec la **MAE**, cohérente avec leur objectif.
- **Cibles positives très dispersées** (prix, ventes) : **RMSLE**, quel que soit l'algorithme.
- ⚠️ **Cohérence entraînement/évaluation** : évaluer avec la métrique que le modèle a **cherché à optimiser** évite les mauvaises surprises. Un modèle entraîné sur la MSE ne sera pas forcément le meilleur au sens de la MAE.

---

# PARTIE IV — MÉTRIQUES DE CLUSTERING

## 18. Le défi : évaluer sans « bonne réponse »

### 📖 Le problème

En **clustering** (non supervisé, ex. K-Means), il n'y a **pas de labels** : le modèle invente des groupes. Comment noter un résultat sans corrigé ? Il existe **deux familles** de métriques :

```
MÉTRIQUES DE CLUSTERING
│
├── 🔵 INTERNES (sans labels vrais) ── le cas courant
│     On juge la GÉOMÉTRIE des clusters :
│     « sont-ils compacts et bien séparés ? »
│     → Silhouette · Davies-Bouldin · Inertie · Calinski-Harabasz
│
└── 🟢 EXTERNES (avec labels vrais) ── cas rare (jeu étiqueté pour valider)
      On compare les clusters aux vraies catégories :
      → ARI · NMI · V-measure
```

> 🔑 **Le principe d'un bon clustering** : **cohésion** (points d'un même cluster proches) **+** **séparation** (clusters éloignés les uns des autres). Les métriques internes mesurent ces deux qualités.

---

## 19. Silhouette Score

### 📖 Définition

Pour **chaque point**, on compare :
- **a** = sa distance moyenne aux points de **son** cluster (cohésion),
- **b** = sa distance moyenne au cluster **voisin le plus proche** (séparation).

$$s = \frac{b - a}{\max(a, b)} \quad \in [-1, 1]$$

Le **Silhouette Score** global est la moyenne sur tous les points.

| Valeur | Interprétation |
|--------|----------------|
| **≈ 1** | Point bien dans son cluster, loin des autres ✅ |
| **≈ 0** | Point **à la frontière** entre deux clusters |
| **< 0** | Point probablement **mal classé** (plus proche d'un autre cluster) ❌ |

```python
from sklearn.metrics import silhouette_score
silhouette_score(X, labels)   # plus HAUT = mieux
```

### 🎯 Points clés

- **Intuitif** et borné dans [-1, 1] → facile à interpréter.
- ✅ Sert à **choisir le nombre de clusters K** : on teste plusieurs K, on garde celui qui **maximise** la silhouette.
- ⚠️ Coûteux sur gros volumes (calcul de distances par paires) ; suppose des clusters plutôt **convexes** → adapté à **K-Means**, moins à des formes allongées (DBSCAN).

---

## 20. Indice de Davies-Bouldin

### 📖 Définition

Mesure le **rapport moyen** entre la dispersion **interne** des clusters et la distance **entre** clusters. Pour chaque cluster, on trouve son « pire voisin » (le plus similaire) et on moyenne.

$$\text{DB} = \frac{1}{k}\sum_{i} \max_{j \neq i} \frac{\sigma_i + \sigma_j}{d(c_i, c_j)}$$

```python
from sklearn.metrics import davies_bouldin_score
davies_bouldin_score(X, labels)   # ⬇️ plus BAS = mieux (0 = idéal)
```

### 🎯 Points clés

- ⚠️ **Sens inversé** : contrairement à la silhouette, **plus c'est bas, mieux c'est** (clusters compacts et bien séparés).
- ✅ **Rapide** à calculer (basé sur les centres) → bon pour comparer des configurations sur de gros jeux.
- Comme la silhouette, favorise les clusters **convexes/sphériques** (idéal pour valider un **K-Means**).

---

## 21. Inertie (Within-Cluster Sum of Squares)

### 📖 Définition

Somme des **distances au carré** de chaque point au **centre (centroïde)** de son cluster. C'est **exactement** ce que **K-Means minimise**.

$$\text{Inertie} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - c_i\|^2$$

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=4, random_state=42).fit(X)
print(km.inertia_)   # attribut fourni directement par K-Means
```

### 🎯 La méthode du coude (Elbow Method)

L'inertie **diminue toujours** quand K augmente (avec K = N points, elle vaut 0). On ne peut donc pas juste la minimiser. On cherche le **« coude »** : le K après lequel l'inertie ne baisse presque plus.

```
Inertie │*
        │ *
        │  *
        │   *
        │    ● ← LE COUDE : K optimal
        │     *___
        │         *____
        │              *______
        └──────────────────────── K (nombre de clusters)
          1  2  3  4  5  6  7  8
```

> 🔑 **Rôle de l'inertie** : outil **interne à K-Means** pour **choisir K** via la méthode du coude. Elle ne mesure **pas la séparation** entre clusters → à **compléter par la silhouette** pour une décision fiable.

---

## 22. Adjusted Rand Index (ARI)

### 📖 Définition

Métrique **externe** : elle compare les clusters trouvés aux **vraies catégories** (quand on les connaît). L'ARI compte les paires de points regroupées **de la même façon** dans les deux partitions, **corrigé du hasard**.

$$\text{ARI} \in [-1, 1]$$

| ARI | Interprétation |
|-----|----------------|
| **1.0** | Clustering **identique** à la vérité ✅ |
| **≈ 0** | Regroupement **aléatoire** (pas mieux que le hasard) |
| **< 0** | Pire que le hasard |

```python
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(labels_vrais, labels_predits)
```

### 🎯 Points clés

- ✅ **Insensible à la permutation des étiquettes** : peu importe que le « cluster 0 » s'appelle « 2 » — seule compte la façon de **regrouper** les points.
- ✅ **« Ajusté »** = corrigé du hasard (contrairement au Rand Index brut), donc comparable et honnête.
- ⚠️ **Nécessite les vrais labels** → sert surtout à **valider un algorithme de clustering** sur un jeu de données étiqueté (recherche, benchmark), pas en production non supervisée.

---

## 23. Compléments : Calinski-Harabasz, NMI, V-measure

> 🧩 *Métriques standard de scikit-learn, utiles à côté des quatre demandées.*

| Métrique | Type | Sens | Idée / Usage |
|----------|------|------|--------------|
| **Calinski-Harabasz** | interne | ⬆️ haut = mieux | Rapport dispersion inter/intra clusters. **Très rapide**, bon complément de la silhouette pour choisir K. `calinski_harabasz_score` |
| **NMI** (Norm. Mutual Info) | externe | ⬆️ [0,1] | Information partagée entre clusters et vrais labels. `normalized_mutual_info_score` |
| **Homogénéité / Complétude / V-measure** | externe | ⬆️ [0,1] | Homogénéité = un cluster = une seule classe ; Complétude = une classe = un seul cluster ; **V-measure** = leur moyenne harmonique. `v_measure_score` |

---

## 24. Quelle métrique de clustering choisir ?

```
Ai-je les VRAIS labels (jeu étiqueté pour valider) ?
│
├── OUI → métriques EXTERNES
│        ├── ARI          (robuste, corrigé du hasard) ⭐
│        ├── NMI          (information partagée)
│        └── V-measure    (homogénéité + complétude)
│
└── NON (cas réel non supervisé) → métriques INTERNES
         ├── Silhouette          (intuitive, choisir K) ⭐
         ├── Davies-Bouldin      (rapide, bas = mieux)
         ├── Calinski-Harabasz   (rapide, haut = mieux)
         └── Inertie             (coude, SPÉCIFIQUE K-Means)
```

### 🔬 Pourquoi telle métrique sur tel algorithme ?

| Algorithme | Métrique adaptée | Pourquoi |
|------------|------------------|----------|
| **K-Means** | Inertie (coude) + Silhouette / Davies-Bouldin | K-Means **minimise l'inertie** ; ses clusters sont convexes → la silhouette et DB (qui supposent la convexité) sont cohérentes |
| **DBSCAN** (formes arbitraires) | Silhouette **avec prudence**, ARI si labels | L'**inertie n'a pas de sens** (pas de centroïdes, K non fixé) ; les métriques géométriques convexes sous-estiment les clusters allongés |
| **Clustering hiérarchique** | Silhouette, Davies-Bouldin, dendrogramme | Pas de centroïdes obligatoires → on juge cohésion/séparation |

> 🔑 **Le point crucial** : l'**inertie est propre à K-Means** (elle suppose des centroïdes et des clusters sphériques). L'appliquer à DBSCAN n'a **aucun sens**. Toujours **croiser** une métrique interne (silhouette) avec la connaissance de l'algorithme et, si possible, une **inspection visuelle**.

---

# PARTIE V — SYNTHÈSE

## 25. Tableau récapitulatif général

| Famille | Métrique | Sens optimal | Unité | À retenir |
|---------|----------|--------------|-------|-----------|
| **Classif.** | Accuracy | ⬆️ | % | Simple, **piège si déséquilibré** |
| | Precision | ⬆️ | [0,1] | Punit les **faux positifs** |
| | Recall | ⬆️ | [0,1] | Punit les **faux négatifs** |
| | F1 | ⬆️ | [0,1] | Équilibre P & R, **données déséquilibrées** |
| | AUC-ROC | ⬆️ | [0,1] | **Indépendant du seuil**, exige des probas |
| **Régression** | MAE | ⬇️ | cible | Lisible, **robuste aux outliers** |
| | MSE | ⬇️ | cible² | Fonction de coût, **punit les gros écarts** |
| | RMSE | ⬇️ | cible | ⭐ Standard : lisible **et** sévère |
| | RMSLE | ⬇️ | log | Erreur **relative**, cibles > 0 dispersées |
| | R² | ⬆️ | sans | **% de variance expliquée** vs la moyenne |
| **Clustering** | Silhouette | ⬆️ [-1,1] | sans | ⭐ Intuitive, **choisir K** |
| | Davies-Bouldin | ⬇️ (0 idéal) | sans | Rapide, **bas = mieux** |
| | Inertie | ⬇️ (coude) | sans | **Spécifique K-Means** |
| | ARI | ⬆️ [-1,1] | sans | **Externe** (vrais labels requis) |

---

## 26. Conclusion

### 🎓 Ce qu'il faut absolument retenir

1. **Pas de métrique universelle.** Le bon choix dépend du **type de problème** (classification / régression / clustering) **et** du **coût métier des erreurs**. Choisir la métrique fait partie du travail de data scientist.

2. **En classification**, tout part de la **matrice de confusion**. L'accuracy **ment** sur données déséquilibrées : on lui préfère **Precision** (coût des faux positifs), **Recall** (coût des faux négatifs), **F1** (équilibre) et **AUC** (indépendant du seuil).

3. **En régression**, on mesure l'**écart** aux vraies valeurs : **MAE** (robuste, lisible), **RMSE** (le standard, sévère avec les gros écarts), **RMSLE** (erreur relative), **R²** (part de variance expliquée). On rapporte **RMSE + R²** ensemble.

4. **En clustering**, sans labels on juge la **géométrie** (Silhouette, Davies-Bouldin, Inertie/coude) ; avec des labels de validation, on compare à la vérité (**ARI**). L'**inertie est propre à K-Means**.

5. **La métrique doit être cohérente avec l'algorithme** : l'AUC/Log Loss exigent des probabilités ; l'inertie suppose des centroïdes (K-Means) ; évaluer un modèle avec la métrique qu'il a **optimisée** évite les surprises.

6. **Toujours croiser plusieurs métriques.** Une seule cache une partie de la réalité — exactement comme un médecin croise plusieurs mesures avant un diagnostic.

### 🧭 Le mémo en une image

```
┌───────────────────────────────────────────────────────────────┐
│  CLASSIFICATION → matrice de confusion d'abord                 │
│     équilibré ? Accuracy · sinon Precision/Recall/F1/AUC       │
│                                                                │
│  RÉGRESSION → RMSE (standard) + R², MAE si outliers,           │
│               RMSLE si cible positive très dispersée           │
│                                                                │
│  CLUSTERING → Silhouette + Davies-Bouldin (interne),           │
│               Inertie/coude (K-Means), ARI si vrais labels     │
│                                                                │
│  RÈGLE D'OR : la métrique suit le COÛT MÉTIER, jamais l'inverse│
└───────────────────────────────────────────────────────────────┘
```

> 🔑 **En une phrase** : *un bon modèle sans la bonne métrique, c'est un thermomètre qui affiche la vitesse du vent — la mesure est précise, mais elle ne répond pas à la question.*

---

## 27. ✅ Point de contrôle — Métriques

### 🧠 Questions de compréhension

<details>
<summary><b>1. Un modèle détecte une fraude touchant 1 % des transactions et affiche 99 % d'accuracy. Est-il forcément bon ?</b></summary>

Non. Un modèle qui répond **toujours « pas de fraude »** atteint 99 % d'accuracy tout en ratant **100 % des fraudes**. Sur données déséquilibrées, l'accuracy est trompeuse : il faut regarder le **Recall** (fraudes détectées) et la **Precision**.
</details>

<details>
<summary><b>2. Quelle est la différence entre Precision et Recall ?</b></summary>

**Precision** = parmi les prédictions positives, combien sont correctes (punit les **faux positifs**). **Recall** = parmi les vrais positifs, combien sont retrouvés (punit les **faux négatifs**). Precision = fiabilité des alertes ; Recall = capacité à ne rien rater.
</details>

<details>
<summary><b>3. Pour un dépistage de cancer, privilégie-t-on Precision ou Recall ? Pourquoi ?</b></summary>

**Recall.** Rater un malade (faux négatif) peut être fatal. On accepte quelques fausses alertes (FP, confirmées ensuite par d'autres examens) pour **ne manquer aucun** malade → on maximise le rappel.
</details>

<details>
<summary><b>4. Pourquoi le F1 utilise-t-il une moyenne harmonique plutôt qu'une moyenne classique ?</b></summary>

Parce qu'elle **pénalise les déséquilibres** : si Precision = 1 et Recall = 0, la moyenne classique donne 0.5 (flatteur) mais le F1 vaut **0**. Le F1 n'est élevé que si **Precision ET Recall** le sont.
</details>

<details>
<summary><b>5. Que signifie une AUC de 0.5 ? Et de 0.85 ?</b></summary>

**0.5** = le modèle ne fait pas mieux que le **hasard** (inutile). **0.85** = dans 85 % des cas, il attribue un score plus élevé à un positif tiré au hasard qu'à un négatif → bon pouvoir de **classement**, indépendamment du seuil.
</details>

<details>
<summary><b>6. Différence entre RMSE et MAE ? Que révèle un grand écart RMSE − MAE ?</b></summary>

La **RMSE** pénalise fortement les grosses erreurs (carrés), la **MAE** les traite proportionnellement. Comme RMSE ≥ MAE toujours, un **grand écart** signale la présence de quelques **grosses erreurs / outliers**.
</details>

<details>
<summary><b>7. Un R² vaut −0.3. Qu'est-ce que cela veut dire ?</b></summary>

Le modèle est **pire que la simple moyenne** de la cible : il « explique » la variance négativement. Le modèle est inadapté (mauvaises features, mauvaise forme de modèle, ou fuite/erreur de données).
</details>

<details>
<summary><b>8. Pourquoi l'inertie n'est-elle pas adaptée pour évaluer DBSCAN ?</b></summary>

L'inertie repose sur des **centroïdes** et suppose des clusters **sphériques** — c'est ce que **K-Means** minimise. DBSCAN n'a **pas de centroïdes** et trouve des formes **arbitraires** : l'inertie n'a donc aucun sens. On utilise plutôt la silhouette (avec prudence) ou l'ARI si des labels existent.
</details>

<details>
<summary><b>9. Silhouette et Davies-Bouldin vont-ils dans le même sens ?</b></summary>

Non : pour la **Silhouette**, plus c'est **haut** mieux c'est (max 1) ; pour **Davies-Bouldin**, plus c'est **bas** mieux c'est (0 = idéal). Attention au sens avant de conclure.
</details>

<details>
<summary><b>10. Quand utilise-t-on l'ARI plutôt que la silhouette ?</b></summary>

L'**ARI** quand on **dispose des vrais labels** (métrique externe, pour valider/benchmarker un algorithme). La **silhouette** dans le cas réel non supervisé, où **aucun label** n'est disponible (métrique interne).
</details>

### 🛠️ Exercice pratique

Sur `clients_telecom.csv` (dossier `TP/`), on prédit le **churn** (départ client — problème déséquilibré) :

1. Entraînez un classifieur, affichez la **matrice de confusion** et le `classification_report`.
2. Le churn est déséquilibré : **quelle métrique** privilégier et pourquoi ? Justifiez Precision vs Recall selon l'objectif « retenir un maximum de clients sur le point de partir ».
3. Calculez l'**AUC** à partir des probabilités et tracez la **courbe ROC**.
4. **Bonus régression** : sur `loyers_abidjan.csv`, comparez **MAE, RMSE et R²** d'une régression, et interprétez l'écart RMSE − MAE.

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (confusion_matrix, classification_report,
                             roc_auc_score, RocCurveDisplay)

# --- Classification : churn ---
df = pd.read_csv("clients_telecom.csv")
X = df.drop(columns=["churn"])   # adapter au vrai nom de la cible
y = df["churn"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

clf = RandomForestClassifier(random_state=42).fit(X_tr, y_tr)
y_pred  = clf.predict(X_te)
y_proba = clf.predict_proba(X_te)[:, 1]

print(confusion_matrix(y_te, y_pred))
print(classification_report(y_te, y_pred))
print("AUC :", round(roc_auc_score(y_te, y_proba), 3))
RocCurveDisplay.from_estimator(clf, X_te, y_te)

# 2. Churn déséquilibré → l'accuracy ment. Pour "retenir les partants",
#    on veut RATER le moins de churners possible → on privilégie le RECALL
#    (quitte à contacter par erreur quelques clients fidèles = faux positifs).

# --- Bonus régression : loyers ---
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

d = pd.read_csv("loyers_abidjan.csv")
Xr = d[["surface", "nb_pieces", "distance_centre"]]
yr = d["loyer"]
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(Xr, yr, test_size=0.2, random_state=42)
reg = LinearRegression().fit(Xr_tr, yr_tr)
p = reg.predict(Xr_te)

mae  = mean_absolute_error(yr_te, p)
rmse = np.sqrt(mean_squared_error(yr_te, p))
print(f"MAE  : {mae:,.0f} | RMSE : {rmse:,.0f} | R² : {r2_score(yr_te, p):.3f}")
print("RMSE ≫ MAE → présence de quelques grosses erreurs (outliers).")
```
</details>

---

*📘 Module Data Science — Les Métriques d'Évaluation | Bootcamp Data Science*
