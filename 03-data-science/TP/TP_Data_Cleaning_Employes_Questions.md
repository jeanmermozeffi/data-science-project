# TD — Nettoyage d'un fichier d'employés avec Pandas

> **Module Data Science** · TD de synthèse du chapitre *Data Cleaning & Transformation with Pandas*
> **Prérequis** : NumPy, File Handling, et surtout le chapitre **Pandas** (Series, DataFrame, `loc`/`iloc`, filtrage booléen, nettoyage, `groupby`).
> **Durée conseillée** : 2 h à 3 h · **Fichier de données** : `fiche_employes.csv`

---

## 🎯 Contexte

Le service RH d'une entreprise vous transmet un export brut de sa base employés :
`fiche_employes.csv` (≈ 5 100 lignes, 13 colonnes).

Ce fichier a été généré automatiquement puis **volontairement dégradé** pour ressembler à un
jeu de données du monde réel : doublons, valeurs manquantes, colonnes mal nommées, dates au
mauvais format, texte « sale », salaires aberrants…

Votre mission : **produire une version propre et exploitable de ce fichier**, en suivant le cycle
vu en cours :

```
DIAGNOSTIQUER  →  NETTOYER  →  TRANSFORMER  →  ANALYSER  →  SAUVEGARDER
```

> ⚠️ Vous n'utiliserez **que des notions vues dans le chapitre Pandas**. Aucune bibliothèque de
> Machine Learning, aucun graphique n'est demandé.

---

## 📦 Consignes de rendu

Vous rendez **un seul notebook** (`TP_Data_Cleaning_Employes.ipynb`) contenant :

1. Une cellule de code par question (le code **et** son résultat exécuté).
2. Une cellule Markdown de commentaire à chaque fois que l'énoncé demande de **justifier un choix**.
3. En fin de notebook, l'export du fichier nettoyé : `fiche_employes_clean.csv`.

**Règle d'or** : on ne modifie jamais le DataFrame d'origine. On travaille toujours sur une copie
(`df = df_raw.copy()`), pour pouvoir comparer « avant / après ».

---

## 🧠 Notions mobilisées (rappel)

| Partie | Notions du cours |
|--------|------------------|
| 1. Diagnostic | `read_csv`, `head`/`tail`, `shape`, `info`, `describe`, `dtypes`, `isna().sum()`, `nunique`, `value_counts` |
| 2. Doublons | `duplicated()`, `drop_duplicates()`, `reset_index()` |
| 3. Valeurs manquantes | `isna()`, filtrage booléen, `fillna()`, `.str.lower()` |
| 4. Renommer les colonnes | `df.columns`, `rename(columns=...)` |
| 5. Types & dates | `astype()`, `pd.to_datetime()`, accès `.dt` |
| 6. Nettoyage de texte | `.str.replace()`, `.str.strip()`, `.str.extract()`, `.str.title()` |
| 7. Valeurs aberrantes | `describe()`, `sort_values()`, `mean()`/`std()`, filtrage booléen, `.loc[...] = ...` |
| 8. Transformation & analyse | nouvelle colonne calculée, `apply()`, `map()`, `pd.cut()`, `groupby()`, `value_counts()` |
| 9. Contrôle & export | `info()`, `isna().sum()`, `to_csv()` |

---

# Partie 0 — Mise en place

**Q0.1** Importez `pandas` (alias `pd`) et `numpy` (alias `np`).

**Q0.2** Chargez `fiche_employes.csv` dans un DataFrame nommé `df_raw` avec `pd.read_csv()`.

**Q0.3** Créez une copie de travail : `df = df_raw.copy()`.
Expliquez en une phrase (cellule Markdown) pourquoi on travaille sur une copie.

---

# Partie 1 — Diagnostic : comprendre les données

> Objectif : dresser l'état des lieux **avant de toucher à quoi que ce soit**.

**Q1.1** Affichez les **5 premières** et les **5 dernières** lignes du DataFrame.

**Q1.2** Combien de lignes et de colonnes contient le fichier ? (utilisez `.shape`)

**Q1.3** Affichez la liste des noms de colonnes.
Repérez et **listez dans une cellule Markdown** tous les problèmes que vous voyez dans ces noms
(fautes d'orthographe, espaces, langue, incohérence de style…).

**Q1.4** Affichez le résumé `df.info()`. Pour chaque colonne, notez :
- son type (`dtype`) ;
- si ce type vous paraît **correct** ou **à corriger** (ex. une date stockée en texte).

**Q1.5** Affichez `df.describe()` (statistiques des colonnes numériques).
Une valeur vous paraît-elle suspecte pour la colonne `Salary` ? Pour la colonne `Age` ?

**Q1.6** Comptez le nombre de **valeurs manquantes par colonne** (`isna().sum()`).
Quelle(s) colonne(s) sont concernées, et combien de valeurs manquent ?

**Q1.7** Comptez le nombre de **lignes entièrement dupliquées** (`duplicated().sum()`).

**Q1.8** Pour les colonnes `Employment_Status`, `Gender`, `Department`, affichez la répartition
des valeurs avec `value_counts()`.
La colonne `Employment_Status` vous semble-t-elle cohérente ? (indice : comparez les langues)

**Q1.9** Rédigez dans une cellule Markdown un **plan de nettoyage** en 6–8 points : la liste
ordonnée des opérations que vous allez effectuer dans les parties suivantes.

---

# Partie 2 — Traiter les doublons

**Q2.1** Affichez les lignes en double (`df[df.duplicated()]`). Combien y en a-t-il ?

**Q2.2** Supprimez les doublons avec `drop_duplicates()`. Combien de lignes reste-t-il ?

**Q2.3** Après suppression de lignes, l'index a des « trous ». Réinitialisez-le avec
`reset_index(drop=True)`.

**Q2.4** Vérifiez qu'il ne reste plus aucun doublon.

---

# Partie 3 — Traiter les valeurs manquantes

> D'après le diagnostic, seule la colonne `Email` contient des valeurs manquantes.

**Q3.1** Affichez uniquement les lignes où `Email` est manquant (filtrage booléen avec `isna()`).
Combien y en a-t-il maintenant (après la suppression des doublons) ?

**Q3.2** On décide de **reconstruire** les emails manquants à partir du nom et du prénom,
selon le format : `prenom.nom@entreprise.ci` (tout en minuscules).
Construisez cette adresse pour **toutes** les lignes dans une Series temporaire, puis
utilisez `fillna()` pour ne remplacer **que** les emails manquants.

> 💡 Astuce : `df["Fist Name"].str.lower() + "." + df["Last Name"].str.lower() + "@entreprise.ci"`

**Q3.3** Vérifiez qu'il ne reste plus aucune valeur manquante dans tout le DataFrame.

**Q3.4** (Justification) En une phrase : pourquoi reconstruire l'email est ici préférable à
`dropna()` ou à `fillna("inconnu")` ?

---

# Partie 4 — Renommer les colonnes

**Q4.1** À partir de la liste des problèmes repérés en **Q1.3**, renommez les colonnes avec
`df.rename(columns={...})` pour obtenir des noms **propres, en anglais, en `snake_case`, sans
faute** :

| Nom actuel | Nom attendu |
|------------|-------------|
| `Fist Name` | `first_name` |
| `Last Name` | `last_name` |
| `Djob_tilte` | `job_title` |
| `Ville` | `city` |
| `Join_Date` | `join_date` |
| *(les autres)* | tout en minuscules : `age`, `email`, `phone`, `address`, `salary`, `employment_status`, `gender`, `department` |

**Q4.2** Affichez `df.columns` pour vérifier le résultat.

---

# Partie 5 — Corriger les types de données

**Q5.1** Affichez les 5 premières valeurs de `join_date` et son `dtype`.
Pourquoi n'est-il pas possible de calculer une ancienneté avec cette colonne telle quelle ?

**Q5.2** Convertissez `join_date` en vrai type date avec `pd.to_datetime()`. Vérifiez le nouveau `dtype`.

**Q5.3** Créez une colonne `years_employed` = **année courante − année d'embauche**.
(indice : `pd.Timestamp.now().year` et l'accès `.dt.year`)

**Q5.4** Affichez `df[["join_date", "years_employed"]].head()` pour contrôler.

**Q5.5** Quelle est l'ancienneté **minimale** et **maximale** observée ?

---

# Partie 6 — Nettoyer les colonnes de texte

**Q6.1 — Adresse.** Affichez `df["address"].head()`. Que remarquez-vous à l'intérieur des chaînes ?
Remplacez le passage à la ligne `"\n"` par une espace avec `.str.replace()`.

**Q6.2 — Intitulé de poste.** Affichez `df["job_title"].head()`.
Les valeurs ressemblent à `('Chef de projet finance',)` : ce sont des **tuples transformés en
texte** (artefact de génération). Récupérez uniquement l'intitulé réel, par exemple
`Chef de projet finance`.

> 💡 Deux pistes possibles :
> - `df["job_title"].str.strip("(),'\"")`
> - `df["job_title"].str.extract(r"\(['\"](.+?)['\"],?\)")`
>
> Testez les deux sur `.head(20)` et gardez celle qui nettoie **toutes** les lignes
> (attention : certaines valeurs utilisent des guillemets doubles).

**Q6.3** Vérifiez avec `df["job_title"].nunique()` et `df["job_title"].value_counts()` que les
intitulés sont maintenant homogènes (pas de parenthèses ni de guillemets résiduels).

**Q6.4** Uniformisez la casse des colonnes `first_name` et `last_name` avec `.str.title()`
(1re lettre en majuscule).

---

# Partie 7 — Traiter les valeurs aberrantes (`salary`)

> Le diagnostic de la Partie 1 a montré un `max` de salaire anormalement élevé.

**Q7.1** Affichez les 10 salaires les plus élevés avec `sort_values(..., ascending=False).head(10)`.

**Q7.2** On utilise la méthode du **z-score** (vue en NumPy : centrer-réduire) :
`z = (salary − moyenne) / écart-type`.
Créez une colonne `salary_zscore`.

**Q7.3** Une valeur est considérée **aberrante** si `|z| > 3`.
Créez une colonne booléenne `is_outlier` et comptez le nombre d'aberrations.

**Q7.4** Affichez les lignes aberrantes. À partir de quel montant de salaire commence-t-on
à être classé « aberrant » ici ?

**Q7.5** Stratégie de correction : on **remplace** le salaire des lignes aberrantes par la
**moyenne des salaires non aberrants**.
- calculez `mean_non_outliers` avec un filtre `~df["is_outlier"]` ;
- affectez cette valeur avec `df.loc[df["is_outlier"], "salary"] = mean_non_outliers`.

**Q7.6** Reconvertissez `salary` en entier (`astype(int)`).

**Q7.7** Supprimez les colonnes de travail `salary_zscore` et `is_outlier` (`df.drop(columns=...)`).

**Q7.8** Ré-affichez `df["salary"].describe()`. Le `max` est-il redevenu réaliste ?

**Q7.9** (Justification) En 2–3 phrases : quel est l'inconvénient de remplacer par la moyenne ?
Citez une autre stratégie possible (suppression des lignes, plafonnement / *capping*…).

---

# Partie 8 — Transformer et analyser

> On réutilise ici `apply()`, `map()`, `pd.cut()`, `groupby()` et `value_counts()`.

**Q8.1** Créez une colonne `tranche_salaire` avec `pd.cut()` sur `salary`, avec les bornes
`[0, 40000, 80000, 120000, np.inf]` et les libellés
`["Bas", "Moyen", "Élevé", "Très élevé"]`.

**Q8.2** Créez une colonne `seniorite` à partir de `years_employed` avec `apply()` et une
fonction :
- `< 3 ans` → `"Junior"`
- `3 à 5 ans` → `"Confirmé"`
- `> 5 ans` → `"Senior"`

**Q8.3** Créez une colonne `gender_label` avec `map()` : `{"M": "Homme", "F": "Femme"}`.

**Q8.4** Avec `groupby()`, calculez le **salaire moyen par département** (arrondi à l'entier),
trié du plus élevé au plus faible.

**Q8.5** Avec `groupby()`, calculez pour chaque **ville** : l'effectif (`count`), le salaire
moyen et l'âge moyen (utilisez `.agg([...])`).

**Q8.6** Affichez la répartition des employés par `tranche_salaire` (`value_counts()`).

**Q8.7** Quel département a l'ancienneté moyenne la plus élevée ?

---

# Partie 9 — Contrôle qualité final & export

**Q9.1** Ré-exécutez le « diagnostic de base » sur le DataFrame nettoyé :
`df.info()`, `df.isna().sum()`, `df.duplicated().sum()`, `df.dtypes`.

**Q9.2** Rédigez dans une cellule Markdown un **tableau récapitulatif** « Problème → Traitement
appliqué » (une ligne par opération de nettoyage).

**Q9.3** Exportez le résultat : `df.to_csv("fiche_employes_clean.csv", index=False, encoding="utf-8")`.

**Q9.4** Rechargez `fiche_employes_clean.csv` dans un nouveau DataFrame et vérifiez avec
`.info()` que tout est conforme (types, absence de valeurs manquantes, nombre de lignes).

---

# 🎁 Bonus (facultatif — uniquement avec les `.str` du cours)

**B1 — Uniformiser `employment_status`.**
La colonne mélange des types français (`CDD`, `CDI`) et anglais (`Full-Time`, `Part-Time`).
Proposez un ré-encodage cohérent avec `map()` ou `replace()` (par exemple, tout ramener à
`CDI` / `CDD` / `Temps plein` / `Temps partiel`, à vous de justifier votre choix dans une
cellule Markdown).

**B2 — Normaliser `phone`.**
Les numéros ont des formats très variés : `+33 2 47 21 81 96`, `03 23 42 35 11`, `0218388496`,
`+33 (0)4 57 57 01 54`…
En utilisant seulement `.str.replace()` (et éventuellement `.str.strip()`), produisez une
colonne `phone_clean` ne contenant **que des chiffres** (sans espaces, sans `+`, sans
parenthèses).

**B3 — Emails en doublon.**
Après nettoyage, combien d'adresses email apparaissent plus d'une fois
(`df["email"].duplicated().sum()`) ? Affichez ces lignes. Faut-il les traiter ? Justifiez.

---

## 🧾 Barème indicatif (sur 20)

| Partie | Points |
|--------|:------:|
| 1. Diagnostic + plan de nettoyage | 4 |
| 2. Doublons | 2 |
| 3. Valeurs manquantes | 2 |
| 4. Renommage des colonnes | 2 |
| 5. Types & dates | 2 |
| 6. Nettoyage de texte | 3 |
| 7. Valeurs aberrantes | 3 |
| 8. Transformation & analyse | 2 |
| 9. Contrôle & export | — *(condition de validation)* |
| Bonus | +2 |

---

## ✅ Checklist avant de rendre

- [ ] Je travaille sur `df` (copie), `df_raw` est resté intact.
- [ ] 0 doublon, 0 valeur manquante dans le DataFrame final.
- [ ] `join_date` est de type `datetime`, `salary` est de type `int`.
- [ ] Les noms de colonnes sont propres, en minuscules, sans faute ni espace.
- [ ] `address` et `job_title` ne contiennent plus d'artefacts (`\n`, parenthèses, guillemets).
- [ ] Chaque choix demandé est justifié dans une cellule Markdown.
- [ ] `fiche_employes_clean.csv` est généré et se recharge sans erreur.
