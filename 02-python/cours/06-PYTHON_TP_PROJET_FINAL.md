# 🎓 TP Projet Final — Bootcamp Data Science

> Ce TP clôture les 5 chapitres Python du bootcamp (Introduction, Bases, Data Structures, Fonctions, POO). Il ne fait appel à **aucune bibliothèque externe** (pas de pandas/numpy) : tout doit être réalisé en Python pur, avec les outils déjà vus en cours. L'objectif est de prouver que vous savez **combiner** ces notions pour construire un petit outil de traitement de données de bout en bout.

## Table des matières
1. [Contexte et objectifs](#1-contexte-et-objectifs)
2. [Compétences mobilisées](#2-compétences-mobilisées)
3. [Consignes générales](#3-consignes-générales)
4. [Les 5 projets proposés](#4-les-5-projets-proposés)
5. [Grille d'évaluation](#5-grille-dévaluation)
6. [Livrables attendus](#6-livrables-attendus)
7. [Calendrier suggéré](#7-calendrier-suggéré)
8. [Conseils et ressources](#8-conseils-et-ressources)

---

## 1. Contexte et objectifs

Vous avez terminé la partie "Python fondamental" du bootcamp. Avant d'attaquer les bibliothèques data science (NumPy, Pandas, Matplotlib, scikit-learn), vous devez démontrer que vous maîtrisez :

- la manipulation de données brutes (listes, dictionnaires, sets, tuples, structures imbriquées) ;
- l'écriture de fonctions propres et réutilisables (y compris `lambda`, `map`, `filter`) ;
- la modélisation d'un problème avec des **classes** (POO : encapsulation, héritage, polymorphisme) ;
- un minimum de rigueur d'ingénieur data (nettoyage de données, calculs statistiques "from scratch", présentation de résultats).

**Chaque apprenant (ou binôme) choisit UN projet parmi les 5 proposés** ci-dessous et le développe intégralement.

## 2. Compétences mobilisées

| Chapitre | Notions que le projet doit réinvestir |
|---|---|
| 02 — Bases | variables, opérateurs, conditions |
| 03 — Data Structures | listes, dictionnaires, sets, tuples, structures imbriquées, compréhensions |
| 04 — Fonctions | fonctions, arguments par défaut/nommés, `lambda`, `map`/`filter`, fonctions de nettoyage/statistiques, récursivité (bonus) |
| 05 — POO | classes, `__init__`/`self`, attributs d'instance vs classe, méthodes spéciales, encapsulation, héritage, polymorphisme |

Un projet qui n'utilise **aucune classe** ou **aucune structure de données composée** (liste de dicts, etc.) sera considéré comme incomplet, quel que soit le résultat final.

## 3. Consignes générales

### 📁 Structure de projet attendue

```
mon-projet/
├── README.md              # présentation, choix techniques, comment lancer
├── data/
│   └── jeu_de_donnees.py  # ou .csv/.json si vous préférez lire un fichier
├── src/
│   ├── modeles.py          # vos classes
│   ├── nettoyage.py        # fonctions de nettoyage/validation
│   ├── analyse.py          # fonctions de calcul (stats, agrégations...)
│   └── main.py             # point d'entrée qui orchestre tout
└── tests/
    └── test_analyse.py     # quelques tests manuels ou avec assert
```

### ✅ Règles à respecter

1. **Données réalistes mais imparfaites** : votre jeu de données (30 à 100 enregistrements minimum) doit contenir volontairement des valeurs manquantes, des doublons ou des incohérences (ex : âge négatif, prix à `None`, texte mal formaté). Le nettoyage doit être visible et justifié.
2. **Pas de calcul "boîte noire"** : les statistiques (moyenne, médiane, écart-type, min/max, pourcentages...) doivent être calculées **à la main** (pas de `statistics.mean()` ni pandas). C'est le but pédagogique du TP.
3. **Au moins une hiérarchie de classes** avec héritage + polymorphisme (une méthode redéfinie qui se comporte différemment selon la sous-classe).
4. **Au moins un usage justifié** de `lambda`/`map`/`filter` (ex: filtrer les enregistrements invalides, transformer une liste).
5. **Un rapport texte final** généré par le programme (`print` structuré ou fichier `.txt`) qui résume les résultats de l'analyse — c'est le "livrable" que verrait un client.
6. Code versionné avec Git (commits réguliers, messages clairs), poussé sur GitHub.

### 🚫 Ce qui n'est pas demandé (hors périmètre du bootcamp à ce stade)

- pandas, numpy, matplotlib, scikit-learn (vous les utiliserez dans les prochains modules) ;
- interface graphique ou web ;
- base de données (SQL) — sauf si vous voulez faire le lien avec le module SQL déjà vu, en bonus uniquement.

---

## 4. Les 5 projets proposés

### 🅰️ Projet 1 — Data Cleaner & Analyzer : ventes e-commerce

**Contexte.** Une boutique en ligne vous fournit un export brut de ses ventes (liste de dictionnaires). Les données sont sales : prix manquants, quantités négatives, doublons de commandes, dates mal formatées.

**Objectifs pédagogiques.** Structures imbriquées, fonctions de nettoyage, statistiques "from scratch", encapsulation.

**Cahier des charges.**
1. Modéliser une classe `Vente` (produit, quantité, prix_unitaire, date, client) et une classe `CatalogueVentes` qui contient une liste de `Vente`.
2. Fonctions de nettoyage : supprimer les doublons, exclure/corriger les valeurs manquantes ou aberrantes (prix ≤ 0, quantité négative).
3. Calculs : chiffre d'affaires total, panier moyen (calculé à la main), produit le plus vendu, top 5 clients, répartition des ventes par mois.
4. Une méthode `rapport()` sur `CatalogueVentes` qui affiche un résumé formaté.
5. Bonus : détecter les "clients VIP" (règle métier de votre choix) via héritage (`Client` → `ClientVIP`).

**Squelette de données de départ :**
```python
ventes_brutes = [
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-01-05", "client": "Awa"},
    {"produit": "Souris", "quantite": -1, "prix_unitaire": 5000, "date": "2026-01-06", "client": "Koffi"},
    {"produit": "Ecran", "quantite": 1, "prix_unitaire": None, "date": "2026-01-07", "client": "Awa"},
    {"produit": "Clavier", "quantite": 2, "prix_unitaire": 15000, "date": "2026-01-05", "client": "Awa"},  # doublon
    # ... au moins 40 lignes avec des cas similaires
]
```

**Difficulté :** ⭐⭐ (accessible — bon point de départ)

---

### 🅱️ Projet 2 — Système de gestion académique et de performance

**Contexte.** Vous construisez l'outil qui calcule les moyennes et classements d'une promotion du bootcamp.

**Objectifs pédagogiques.** Héritage, polymorphisme, moyenne pondérée, classement.

**Cahier des charges.**
1. Classe mère `Etudiant` (nom, notes par matière avec coefficients, méthode `moyenne_ponderee()`).
2. Deux classes filles avec un comportement différent (polymorphisme) : `EtudiantBoursier` (méthode `calcul_bourse()` selon la moyenne) et `EtudiantRedoublant` (méthode `mention()` avec des seuils différents).
3. Classe `Promotion` qui regroupe une liste d'`Etudiant`, avec méthodes : classement décroissant, moyenne de la promotion, écart-type des moyennes (calculé à la main), identification des étudiants en difficulté (< 10/20).
4. Utiliser `lambda` + `sorted()` pour le classement, `filter()` pour isoler les étudiants en difficulté.
5. Bonus : méthode d'export du bulletin de chaque étudiant sous forme de texte formaté.

**Difficulté :** ⭐⭐ (accessible)

---

### 🅲️ Projet 3 — Moteur de recommandation par similarité

**Contexte.** Un service de streaming veut recommander des films à un utilisateur en fonction de ses goûts, sans machine learning — juste par similarité de genres/tags (indice de Jaccard).

**Objectifs pédagogiques.** Sets et opérations ensemblistes, POO, algorithmie simple.

**Cahier des charges.**
1. Classe `Film` (titre, genres: set, note_moyenne, année).
2. Classe `Utilisateur` (nom, films_vus: liste de `Film`, genres_preferes déduits automatiquement des films vus).
3. Fonction `similarite_jaccard(set_a, set_b)` calculée à la main : `|A ∩ B| / |A ∪ B|`.
4. Classe `Recommandeur` qui, à partir d'un `Utilisateur` et d'un catalogue de films non vus, retourne le top 5 des films les plus proches de ses goûts (triés par similarité puis par note).
5. Bonus : pondérer la recommandation par la note moyenne du film (score = 0.7 × similarité + 0.3 × note normalisée).

**Difficulté :** ⭐⭐⭐ (intermédiaire — nécessite de bien manipuler les sets)

---

### 🅳️ Projet 4 — Analyseur de sentiments basé sur des règles (texte en français)

**Contexte.** Avant d'apprendre le NLP avec des bibliothèques, vous construisez un classifieur de sentiment "à la main" sur des avis clients (positif / négatif / neutre) à partir d'un dictionnaire de mots-clés pondérés.

**Objectifs pédagogiques.** Manipulation de chaînes, dictionnaires, `map`/`filter`, POO.

**Cahier des charges.**
1. Un dictionnaire `LEXIQUE` associant des mots à un score (`{"excellent": +2, "nul": -2, "correct": +1, "déçu": -1, ...}`), d'au moins 30 mots.
2. Classe `Avis` (texte brut, client, note_etoiles) avec une méthode de nettoyage (minuscules, suppression ponctuation, tokenisation en liste de mots) utilisant `map`/`filter`.
3. Classe `AnalyseurSentiment` qui calcule un score par avis (somme des scores des mots trouvés dans le lexique) et classe l'avis en `positif`/`neutre`/`négatif` selon des seuils.
4. Rapport global : répartition des sentiments (%), mots les plus fréquents dans les avis négatifs (top 10), corrélation simple entre note en étoiles et sentiment détecté (juste un tableau croisé, pas de stats avancées).
5. Bonus : fonction récursive pour découper les négations simples (ex: "pas terrible" → inverse le score du mot suivant).

**Difficulté :** ⭐⭐⭐ (intermédiaire — manipulation de texte)

---

### 🅴️ Projet 5 — Mini-bibliothèque ML "from scratch" (KNN)

**Contexte.** Le projet le plus avancé : vous codez, sans aucune bibliothèque, un classifieur K-Nearest Neighbors capable de prédire une catégorie (ex : espèce de fleur, type de client) à partir de quelques variables numériques. C'est le pont direct vers le module Machine Learning à venir.

**Objectifs pédagogiques.** POO avancée, calculs mathématiques manuels, séparation train/test, évaluation de modèle.

**Cahier des charges.**
1. Un jeu de données simple sous forme de liste de dictionnaires (ex : 3 mesures numériques + 1 catégorie), au moins 60 lignes, réparties en 3 classes.
2. Fonction `distance_euclidienne(point_a, point_b)` calculée à la main (racine carrée de la somme des carrés des écarts).
3. Classe `ModeleKNN` avec : `entrainer(donnees_entrainement)`, `predire(nouveau_point, k=3)` (vote majoritaire parmi les k plus proches voisins), `evaluer(donnees_test)` (calcul manuel de l'accuracy).
4. Fonction de split `train_test_split(donnees, ratio=0.8)` (aléatoire avec le module `random`, sans sklearn).
5. Bonus : tester plusieurs valeurs de `k` (1, 3, 5, 7) et afficher celle qui donne la meilleure accuracy sur le jeu de test — introduction en douceur à la notion de choix d'hyperparamètre.

**Difficulté :** ⭐⭐⭐⭐ (avancé — recommandé aux apprenants à l'aise)

---

## 5. Grille d'évaluation

| Critère | Points |
|---|---|
| Nettoyage et validation des données | 20 |
| Utilisation pertinente des structures de données (Ch.3) | 15 |
| Qualité et réutilisabilité des fonctions (Ch.4) | 20 |
| Modélisation orientée objet : encapsulation, héritage, polymorphisme (Ch.5) | 25 |
| Rapport/sortie finale claire et exploitable | 10 |
| Qualité du code (nommage, lisibilité, README, git) | 10 |
| **Total** | **100** |

Bonus (+10 points max) : fonctionnalité bonus du projet choisi, tests automatisés, gestion d'erreurs avec `try/except`.

## 6. Livrables attendus

1. Dépôt Git (ou dossier) contenant le code source structuré comme indiqué en section 3.
2. Un `README.md` expliquant : le projet choisi, comment l'exécuter, les choix de modélisation (classes créées), un exemple de sortie.
3. Une courte présentation orale (5–10 min) le jour de la soutenance : démonstration + explication d'un extrait de code (une classe ou une fonction clé).

## 7. Calendrier suggéré

| Jour | Étape |
|---|---|
| J1 | Choix du projet, conception du jeu de données, schéma des classes (papier/diagramme) |
| J2 | Implémentation des classes de base + nettoyage des données |
| J3 | Implémentation des fonctions d'analyse/statistiques |
| J4 | Rapport final, tests, README, finitions |
| J5 | Soutenances |

## 8. Conseils et ressources

- Relisez la section "Choisir la bonne structure" du chapitre 03 avant de modéliser vos données.
- Relisez la section "Fonctions et Data Science" (nettoyage, normalisation, pipeline) du chapitre 04 : elle contient des patterns directement réutilisables.
- Relisez la section "4 piliers de la POO" du chapitre 05 pour vérifier que votre hiérarchie de classes a un vrai sens métier (pas d'héritage artificiel juste pour cocher la case).
- Un projet **simple mais propre et bien testé** vaut toujours mieux qu'un projet ambitieux mais bâclé.
