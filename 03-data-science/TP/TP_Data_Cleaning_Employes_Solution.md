# ✅ TD — Nettoyage d'un fichier d'employés · **CORRIGÉ COMMENTÉ**

> Corrigé du TD `TP_Data_Cleaning_Employes_Questions.md`.
> Chaque question donne : le **code attendu**, le **résultat** et une **explication**.
> Toutes les techniques employées viennent du chapitre *Data Cleaning & Transformation with Pandas*.

**Chiffres de référence** (utiles pour se vérifier) :

| Étape | Valeur attendue |
|-------|-----------------|
| Fichier brut | `(5100, 13)` |
| Lignes dupliquées | `100` → après suppression `(5000, 13)` |
| Emails manquants (brut / après dédoublonnage) | `51` / `50` |
| Salaires aberrants (`|z| > 3`) | `20` (à partir de **221 334**) |
| Salaire max avant / après traitement | `494 263` → `149 995` |
| Moyenne des salaires non aberrants | ≈ `84 877` |
| Ancienneté min / max | `2` / `6` ans |
| Intitulés de poste distincts | `50` |

---

# Partie 0 — Mise en place

```python
import pandas as pd
import numpy as np

df_raw = pd.read_csv("fiche_employes.csv")   # adapter le chemin si besoin
df = df_raw.copy()
```

**Q0.3 — Pourquoi une copie ?**
Le nettoyage est une suite d'opérations *destructives* (on supprime des lignes, on écrase des
valeurs). En gardant `df_raw` intact, on peut à tout moment **comparer avant/après**, recommencer
une étape ratée, ou vérifier qu'on n'a pas dénaturé les données. `copy()` crée un objet
indépendant : modifier `df` ne touchera pas `df_raw`.

---

# Partie 1 — Diagnostic

### Q1.1 — Aperçu

```python
df.head()
df.tail()
```

### Q1.2 — Dimensions

```python
df.shape        # (5100, 13)
```

> 5 100 lignes, 13 colonnes.

### Q1.3 — Problèmes dans les noms de colonnes

```python
list(df.columns)
# ['Age', 'Email', 'Phone', 'Address', 'Salary', 'Join_Date', 'Employment_Status',
#  'Gender', 'Department', 'Ville', 'Djob_tilte', 'Fist Name', 'Last Name']
```

| Problème | Colonnes concernées |
|----------|---------------------|
| **Faute d'orthographe** | `Djob_tilte` (pour *Job title*), `Fist Name` (pour *First Name*) |
| **Espace dans le nom** | `Fist Name`, `Last Name` (gênant pour la notation `df.col`) |
| **Langue mélangée** | `Ville` (français) au milieu de colonnes anglaises |
| **Style incohérent** | mélange `PascalCase` (`Join_Date`), mots simples (`Age`), etc. |

➡️ On uniformisera tout en `snake_case` minuscule anglais (Partie 4).

### Q1.4 — Types

```python
df.info()
```

| Colonne | dtype actuel | Verdict |
|---------|--------------|---------|
| `Age` | `int64` | ✅ correct |
| `Email` | `object` | ✅ (texte) — mais **51 valeurs manquantes** |
| `Phone` | `object` | ✅ (texte) — formats hétérogènes |
| `Address` | `object` | ✅ (texte) — contient des `\n` |
| `Salary` | `int64` | ⚠️ correct mais **valeurs aberrantes** |
| `Join_Date` | `object` | ❌ **à convertir en `datetime`** |
| `Employment_Status` | `object` | ⚠️ catégories incohérentes (FR + EN) |
| `Gender`, `Department`, `Ville` | `object` | ✅ |
| `Djob_tilte` | `object` | ❌ texte « sale » (`('...',)`) |
| `Fist Name`, `Last Name` | `object` | ✅ |

### Q1.5 — `describe()`

```python
df.describe()
```

```
              Age         Salary
count  5100.00000    5100.000000
mean     44.32059   85832.415686
std      15.21708   40888.110962
min      18.00000   20016.000000
25%      31.00000   52680.000000
50%      44.00000   84494.000000
75%      57.00000  117588.250000
max      70.00000  494263.000000
```

- **`Salary`** : `max = 494 263` alors que le 3ᵉ quartile est à `≈ 117 588`. L'écart est
  énorme → **valeurs aberrantes probables** (à traiter Partie 7).
- **`Age`** : `min = 18`, `max = 70`. Rien d'impossible pour des employés → **RAS**.

### Q1.6 — Valeurs manquantes

```python
df.isna().sum()
```

```
Email    51
(toutes les autres colonnes : 0)
```

> Seule la colonne **`Email`** est concernée : **51** valeurs manquantes.

### Q1.7 — Doublons

```python
df.duplicated().sum()      # 100
```

> **100** lignes sont des copies exactes d'autres lignes.

### Q1.8 — Répartitions

```python
df["Employment_Status"].value_counts()
# CDD          1312
# CDI          1288
# Full-Time    1257
# Part-Time    1243

df["Gender"].value_counts()       # F 2589 / M 2511
df["Department"].value_counts()   # HR, IT, Marketing, Finance, Engineering (~1000 chacun)
```

➡️ **`Employment_Status` n'est pas cohérente** : elle mélange deux logiques différentes —
le **type de contrat** français (`CDD`, `CDI`) et le **temps de travail** anglais
(`Full-Time`, `Part-Time`). Ces catégories ne sont pas comparables entre elles. Traitement
proposé en **Bonus B1**.

### Q1.9 — Plan de nettoyage

1. Supprimer les **100 doublons** puis réindexer.
2. **Reconstruire** les 50 emails manquants à partir du prénom + nom.
3. **Renommer** toutes les colonnes (`snake_case`, anglais, sans faute).
4. Convertir `join_date` en **datetime**, créer `years_employed`.
5. Nettoyer le **texte** : `\n` dans `address`, format tuple dans `job_title`, casse des noms.
6. Détecter et corriger les **salaires aberrants** (z-score).
7. **Transformer/analyser** : tranches, séniorité, `groupby` par département et par ville.
8. **Contrôle qualité** + export `fiche_employes_clean.csv`.

---

# Partie 2 — Doublons

```python
df[df.duplicated()]                 # affiche les 100 lignes en double
df.duplicated().sum()               # 100

df = df.drop_duplicates()           # suppression
df.shape                            # (5000, 13)

df = df.reset_index(drop=True)      # réindexation 0..4999 ; drop=True → on jette l'ancien index
df.duplicated().sum()               # 0  ✅
```

**Explication.**
`duplicated()` renvoie une Series de booléens : `True` sur chaque ligne **déjà vue plus haut**
(la 1ʳᵉ occurrence est gardée). `drop_duplicates()` supprime ces lignes.
Après toute suppression de lignes, l'index garde des « trous » (0, 1, 5, 8…) ; `reset_index(drop=True)`
recrée un index propre `0..n-1`. Sans `drop=True`, l'ancien index serait ajouté comme colonne.

---

# Partie 3 — Valeurs manquantes

```python
# Q3.1 — repérer
manquants = df[df["Email"].isna()]
len(manquants)                      # 50 (il y en avait 51 dans le brut ; 1 était dans une ligne dupliquée)

# Q3.2 — reconstruire puis compléter
emails_reconstruits = (
    df["Fist Name"].str.lower() + "." + df["Last Name"].str.lower() + "@entreprise.ci"
)
df["Email"] = df["Email"].fillna(emails_reconstruits)

# Q3.3 — vérifier
df.isna().sum().sum()               # 0  ✅
```

**Explication.**
- `df["Email"].isna()` → masque booléen ; `df[masque]` → seulement les lignes sans email.
- On calcule d'abord une Series `emails_reconstruits` **pour toutes les lignes** (peu importe,
  on ne s'en servira que là où il manque un email).
- `fillna(autre_series)` remplace chaque `NaN` par la valeur **de même index** dans la Series
  passée. Les emails déjà présents ne sont pas touchés.

**Q3.4 — Justification.**
`dropna()` ferait perdre 50 employés parfaitement valides (on ne jette pas des gens pour une
adresse mail manquante). `fillna("inconnu")` créerait 50 emails identiques et inutilisables.
Reconstruire `prenom.nom@entreprise.ci` produit une adresse **plausible et unique dans la
plupart des cas**, cohérente avec une convention d'entreprise.

---

# Partie 4 — Renommer les colonnes

```python
df = df.rename(columns={
    "Fist Name"        : "first_name",
    "Last Name"        : "last_name",
    "Djob_tilte"       : "job_title",
    "Ville"            : "city",
    "Join_Date"        : "join_date",
    "Age"              : "age",
    "Email"            : "email",
    "Phone"           : "phone",
    "Address"          : "address",
    "Salary"           : "salary",
    "Employment_Status": "employment_status",
    "Gender"           : "gender",
    "Department"       : "department",
})

list(df.columns)
# ['age','email','phone','address','salary','join_date','employment_status',
#  'gender','department','city','job_title','first_name','last_name']
```

**Explication.**
`rename(columns={ancien: nouveau})` ne renomme que les clés fournies et **renvoie une copie**
(d'où la réaffectation `df = df.rename(...)`). Des noms en `snake_case` minuscule, sans espace
ni accent, évitent les fautes et permettent la notation courte `df.first_name`.

---

# Partie 5 — Types de données & dates

```python
# Q5.1
df["join_date"].head()
df["join_date"].dtype               # dtype('O')  → texte
```

Une colonne texte ne permet **aucun calcul de durée** : `"2024-01-15" - "2020-01-15"` n'a pas
de sens pour Python. Il faut un vrai type date.

```python
# Q5.2
df["join_date"] = pd.to_datetime(df["join_date"])
df["join_date"].dtype               # datetime64[ns]  ✅

# Q5.3
annee_courante = pd.Timestamp.now().year          # 2026
df["years_employed"] = annee_courante - df["join_date"].dt.year

# Q5.4
df[["join_date", "years_employed"]].head()

# Q5.5
df["years_employed"].min(), df["years_employed"].max()   # (2, 6)
```

**Explication.**
`pd.to_datetime()` interprète les chaînes `AAAA-MM-JJ` et renvoie un type `datetime64`.
On accède ensuite aux composantes via l'accesseur **`.dt`** (`.dt.year`, `.dt.month`, `.dt.day`…).
`pd.Timestamp.now().year` donne l'année courante. La soustraction se fait terme à terme
(vectorisée, comme en NumPy).

> ℹ️ Version plus précise (facultative) : `(pd.Timestamp.now() - df["join_date"]).dt.days // 365`.

---

# Partie 6 — Nettoyage de texte

### Q6.1 — `address` : retirer les retours à la ligne

```python
df["address"].head()
# "rue Rey\n64616 Saint Michelle"   ← un \n au milieu de la chaîne

df["address"] = df["address"].str.replace("\n", " ", regex=False)
df["address"].head()
# "rue Rey 64616 Saint Michelle"    ✅
```

`\n` (retour à la ligne) casserait un affichage, un export CSV, une recherche.
`.str.replace(ancien, nouveau, regex=False)` remplace le motif littéral dans **chaque** chaîne
de la Series.

### Q6.2 / Q6.3 — `job_title` : sortir la valeur du « faux tuple »

```python
df["job_title"].head()
# "('Chef de projet finance',)"          ← un tuple Python transformé en texte
# "(\"Responsable de la diversité et de l'inclusion\",)"  ← ici, guillemets DOUBLES
```

**Méthode 1 — `str.strip()` (rapide mais fragile) :**

```python
df["job_title"].str.strip("(),'\"").head(20)
```

`strip` retire les caractères `(`, `)`, `,`, `'`, `"` **en début et fin** de chaîne. Il faut
bien penser à inclure le guillemet double, sinon les ≈ 100 lignes concernées gardent un `"`.

**Méthode 2 — `str.extract()` avec une expression régulière (robuste, recommandée) :**

```python
df["job_title"] = df["job_title"].str.extract(r"\(['\"](.+?)['\"],?\)")[0]
```

- `\( ... \)` : les parenthèses littérales du tuple ;
- `['\"]` : un guillemet simple **ou** double ;
- `(.+?)` : le **groupe capturé** = l'intitulé réel (non gourmand) ;
- `,?\)` : la virgule finale du tuple à un élément, puis la parenthèse ;
- `[0]` : `extract` renvoie un DataFrame ; on prend la 1ʳᵉ (et seule) colonne capturée.

**Vérification :**

```python
df["job_title"].str.contains(r"[()\"]", regex=True).sum()   # 0  → plus aucun artefact
df["job_title"].nunique()                                   # 50
df["job_title"].value_counts().head()
```

### Q6.4 — Casse des noms

```python
df["first_name"] = df["first_name"].str.title()
df["last_name"]  = df["last_name"].str.title()
```

`.str.title()` met la 1ʳᵉ lettre de chaque mot en majuscule et le reste en minuscule
(`"jean-marc" → "Jean-Marc"`). Ici les noms étaient déjà propres, mais on **fiabilise** :
si un `"DUPONT"` ou `"dupont"` se glissait plus tard, il serait automatiquement normalisé.

---

# Partie 7 — Valeurs aberrantes (`salary`)

```python
# Q7.1 — les 10 plus gros salaires
df.sort_values("salary", ascending=False).head(10)["salary"].tolist()
# [494263, 466350, 456474, 447240, 435473, 426163, 421772, 377542, 347186, 294788]
```

```python
# Q7.2 — z-score (centrer-réduire, vu en NumPy)
df["salary_zscore"] = (df["salary"] - df["salary"].mean()) / df["salary"].std()

# Q7.3 — règle |z| > 3
df["is_outlier"] = df["salary_zscore"].abs() > 3
df["is_outlier"].sum()                       # 20

# Q7.4 — à partir de quel montant ?
df.loc[df["is_outlier"], "salary"].min()     # 221334
df[df["is_outlier"]].head()
```

**Explication du z-score.**
Le z-score mesure « à combien d'écarts-types de la moyenne » se trouve une valeur :
`z = (x − μ) / σ`. Une convention courante considère aberrant tout `|z| > 3`
(≈ 0,3 % des valeurs d'une distribution normale). Ici, les 20 salaires générés artificiellement
entre 200 000 et 500 000 ressortent nettement.

```python
# Q7.5 — remplacement par la moyenne des NON aberrants
mean_non_outliers = df.loc[~df["is_outlier"], "salary"].mean()   # ≈ 84876.66

df["salary"] = df["salary"].astype(float)          # éviter un avertissement de type
df.loc[df["is_outlier"], "salary"] = mean_non_outliers

# Q7.6 — retour en entier
df["salary"] = df["salary"].round().astype(int)

# Q7.7 — on jette les colonnes de travail
df = df.drop(columns=["salary_zscore", "is_outlier"])

# Q7.8 — contrôle
df["salary"].describe()
# max ≈ 149995, mean ≈ 84877  → distribution redevenue réaliste ✅
```

> `~df["is_outlier"]` = négation du masque (les lignes **non** aberrantes).
> `df.loc[masque, "colonne"] = valeur` écrase **uniquement** les cellules ciblées.
> On convertit d'abord en `float` car on injecte une moyenne décimale dans une colonne `int`.

**Q7.9 — Limites et alternatives.**
Remplacer par la moyenne **écrase l'information** (ces 20 personnes ont toutes le même salaire
« moyen » artificiel) et **réduit la variance** de la colonne. Autres stratégies :
- **Supprimer** les 20 lignes (`df = df[~df["is_outlier"]]`) — acceptable ici car peu de lignes ;
- **Plafonner / *capping*** : ramener toute valeur `> seuil` au seuil (ex. `q3 + 1.5·IQR`) —
  conserve un ordre de grandeur élevé sans laisser d'extrême ;
- **Remplacer par la médiane** — plus robuste que la moyenne.

---

# Partie 8 — Transformer & analyser

```python
# Q8.1 — tranches de salaire
df["tranche_salaire"] = pd.cut(
    df["salary"],
    bins=[0, 40000, 80000, 120000, np.inf],
    labels=["Bas", "Moyen", "Élevé", "Très élevé"],
)

# Q8.2 — séniorité (fonction + apply)
def seniorite(n):
    if n < 3:
        return "Junior"
    elif n <= 5:
        return "Confirmé"
    return "Senior"

df["seniorite"] = df["years_employed"].apply(seniorite)

# Q8.3 — libellé de genre (map + dictionnaire)
df["gender_label"] = df["gender"].map({"M": "Homme", "F": "Femme"})
```

```python
# Q8.4 — salaire moyen par département
df.groupby("department")["salary"].mean().round(0).sort_values(ascending=False)
# Marketing      85726
# IT             85506
# HR             85454
# Engineering    84122
# Finance        83466
```

```python
# Q8.5 — synthèse par ville
# Version "cours" : .agg([...]) colonne par colonne
df.groupby("city")["salary"].agg(["count", "mean"]).round(1)
df.groupby("city")["age"].mean().round(1)

# Version compacte équivalente (agrégations nommées) :
df.groupby("city").agg(
    effectif      =("salary", "count"),
    salaire_moyen =("salary", "mean"),
    age_moyen     =("age",    "mean"),
).round(1)
```

```python
# Q8.6 — répartition par tranche
df["tranche_salaire"].value_counts()
# Moyen 1576 / Élevé 1542 / Très élevé 1132 / Bas 750

# Q8.7 — ancienneté moyenne par département
df.groupby("department")["years_employed"].mean().round(2).sort_values(ascending=False)
# Engineering et Finance en tête (≈ 4,28 ans) — écarts très faibles entre départements
```

**Explication.**
- `pd.cut()` découpe une variable **continue** en **catégories** ordonnées (binning).
- `apply(fonction)` applique une logique conditionnelle ligne à ligne quand un simple calcul
  vectoriel ne suffit pas.
- `map(dict)` remplace chaque valeur par sa correspondance dans le dictionnaire (idéal pour un
  ré-encodage simple 1 → 1).
- `groupby("col")["mesure"].agg([...])` = le `GROUP BY` de SQL : **diviser** par catégorie,
  **agréger**, **recombiner**.

---

# Partie 9 — Contrôle qualité & export

```python
# Q9.1 — diagnostic final
df.info()
df.isna().sum().sum()        # 0
df.duplicated().sum()        # 0
df.dtypes                    # join_date → datetime64 ; salary → int64 ; age → int64
```

### Q9.2 — Récapitulatif « Problème → Traitement »

| Problème constaté | Traitement appliqué |
|-------------------|---------------------|
| 100 lignes strictement dupliquées | `drop_duplicates()` + `reset_index(drop=True)` |
| 50 emails manquants | reconstruction `prenom.nom@entreprise.ci` via `fillna()` |
| Noms de colonnes fautifs / hétérogènes | `rename()` → `snake_case` anglais |
| `join_date` stockée en texte | `pd.to_datetime()` + colonne `years_employed` |
| `\n` dans `address` | `.str.replace("\n", " ")` |
| `job_title` au format `('...',)` | `.str.extract(r"\(['\"](.+?)['\"],?\)")` |
| 20 salaires aberrants (jusqu'à 494 263) | z-score `|z|>3` → remplacement par la moyenne des non-aberrants |
| Types finaux | `salary` → `int`, `join_date` → `datetime` |

```python
# Q9.3 — export
df.to_csv("fiche_employes_clean.csv", index=False, encoding="utf-8")

# Q9.4 — rechargement de contrôle
check = pd.read_csv("fiche_employes_clean.csv")
check.info()
check.isna().sum().sum()     # 0
check.shape                  # (5000, 17)   (13 colonnes d'origine + 4 colonnes créées)
```

> `index=False` : on n'écrit pas l'index Pandas comme 1ʳᵉ colonne.
> `encoding="utf-8"` : conserve les accents (`é`, `è`, `ô`…).
> Au rechargement, `join_date` **redevient du texte** : c'est normal, le CSV ne stocke pas les
> types. Si on veut la date typée : `pd.read_csv(..., parse_dates=["join_date"])`.

---

# 🎁 Bonus — corrigés

### B1 — Uniformiser `employment_status`

```python
correspondance = {
    "CDI"      : "CDI",
    "CDD"      : "CDD",
    "Full-Time": "CDI",     # choix : un plein temps sans autre info → CDI
    "Part-Time": "CDD",     # choix : un temps partiel → CDD
}
df["employment_status"] = df["employment_status"].replace(correspondance)
df["employment_status"].value_counts()
```

**Justification.** La colonne mélangeait *type de contrat* (CDI/CDD) et *temps de travail*
(plein/partiel), deux dimensions différentes. Faute d'information supplémentaire, on ramène tout
à une seule échelle cohérente (CDI/CDD). *Variante défendable* : garder `employment_status` en
CDI/CDD **et** créer une 2ᵉ colonne `temps_travail` (`Temps plein`/`Temps partiel`) — mais
l'information manque pour les lignes déjà en CDI/CDD.

### B2 — Normaliser `phone`

```python
df["phone_clean"] = df["phone"].str.replace(r"\D", "", regex=True)
df["phone_clean"].head()
# '33247218196', '0323423511', '33489103413', ...
```

`\D` = « tout caractère qui n'est pas un chiffre » (espaces, `+`, `(`, `)`, `.`).
`regex=True` autorise ce motif. On obtient des chaînes de 10 à 12 chiffres selon que le préfixe
était `0…` ou `+33…`. Pour aller plus loin (hors périmètre du cours) : reformer un format
national unique.

### B3 — Emails en doublon

```python
df["email"].duplicated().sum()          # 39
df[df["email"].duplicated(keep=False)].sort_values("email").head(10)
```

**Analyse.** Après reconstruction, deux employés **homonymes** (même prénom + même nom)
obtiennent la même adresse `prenom.nom@entreprise.ci`. Ce ne sont **pas** des doublons de
lignes (âge, ville, salaire diffèrent) : ce sont de vraies personnes distinctes.
**Traitement possible** : rendre l'email unique en ajoutant un suffixe, par exemple

```python
doublons = df["email"].duplicated(keep=False)
df.loc[doublons, "email"] = (
    df.loc[doublons, "first_name"].str.lower() + "." +
    df.loc[doublons, "last_name"].str.lower() + "." +
    df.loc[doublons].groupby("email").cumcount().add(1).astype(str) +
    "@entreprise.ci"
)
```

*(Non exigé : la simple identification + explication suffit pour ce TD.)*

---

## 🧩 Script complet (récapitulatif exécutable)

```python
import pandas as pd
import numpy as np

# --- 0. Chargement
df_raw = pd.read_csv("fiche_employes.csv")
df = df_raw.copy()

# --- 2. Doublons
df = df.drop_duplicates().reset_index(drop=True)

# --- 3. Emails manquants
emails = df["Fist Name"].str.lower() + "." + df["Last Name"].str.lower() + "@entreprise.ci"
df["Email"] = df["Email"].fillna(emails)

# --- 4. Renommage
df = df.rename(columns={
    "Fist Name": "first_name", "Last Name": "last_name", "Djob_tilte": "job_title",
    "Ville": "city", "Join_Date": "join_date", "Age": "age", "Email": "email",
    "Phone": "phone", "Address": "address", "Salary": "salary",
    "Employment_Status": "employment_status", "Gender": "gender", "Department": "department",
})

# --- 5. Dates
df["join_date"] = pd.to_datetime(df["join_date"])
df["years_employed"] = pd.Timestamp.now().year - df["join_date"].dt.year

# --- 6. Texte
df["address"] = df["address"].str.replace("\n", " ", regex=False)
df["job_title"] = df["job_title"].str.extract(r"\(['\"](.+?)['\"],?\)")[0]
df["first_name"] = df["first_name"].str.title()
df["last_name"] = df["last_name"].str.title()

# --- 7. Salaires aberrants
z = (df["salary"] - df["salary"].mean()) / df["salary"].std()
is_outlier = z.abs() > 3
mean_ok = df.loc[~is_outlier, "salary"].mean()
df["salary"] = df["salary"].astype(float)
df.loc[is_outlier, "salary"] = mean_ok
df["salary"] = df["salary"].round().astype(int)

# --- 8. Transformation & analyse
df["tranche_salaire"] = pd.cut(df["salary"], [0, 40000, 80000, 120000, np.inf],
                               labels=["Bas", "Moyen", "Élevé", "Très élevé"])
df["seniorite"] = df["years_employed"].apply(
    lambda n: "Junior" if n < 3 else ("Confirmé" if n <= 5 else "Senior"))
df["gender_label"] = df["gender"].map({"M": "Homme", "F": "Femme"})

print(df.groupby("department")["salary"].mean().round(0).sort_values(ascending=False))

# --- 9. Contrôle & export
assert df.isna().sum().sum() == 0
assert df.duplicated().sum() == 0
df.to_csv("fiche_employes_clean.csv", index=False, encoding="utf-8")
print("✅ Fichier nettoyé :", df.shape)
```

---

*📗 Module Data Science — Corrigé du TD « Nettoyage d'un fichier d'employés » | Bootcamp Data Science*
