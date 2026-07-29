# 📖 Explication simplifiée du corrigé — Projet 4

## 1. `solution/nettoyage.py` — tokeniser avec `map` et `filter`

```python
mots_bruts = texte_minuscule.split()
mots_sans_ponctuation = list(map(lambda mot: mot.strip(string.punctuation), mots_bruts))
tokens = list(filter(lambda mot: mot != "", mots_sans_ponctuation))
```
Trois étapes bien distinctes :
1. `.split()` découpe le texte en mots sur les espaces (Chapitre 02/03).
2. `map(lambda mot: mot.strip(string.punctuation), ...)` applique `.strip(...)` à **chaque mot** de la liste : ça retire la ponctuation en début/fin de chaque mot (ex: `"excellent,"` → `"excellent"`, `"arnaque."` → `"arnaque"`). C'est l'usage typique de `map()` vu au Chapitre 04 : transformer chaque élément d'une liste par la même opération.
3. `filter(lambda mot: mot != "", ...)` élimine les tokens devenus vides (ex: un mot qui n'était que de la ponctuation, comme `"!"` tout seul, devient `""` après le `strip` et doit être supprimé).

## 2. `solution/analyse.py` — `calculer_score`, la fonction récursive

C'est le point le plus délicat du projet. Décortiquons :

```python
def calculer_score(tokens, lexique, negations):
    if not tokens:
        return 0                                   # ← cas de base

    mot = tokens[0]
    reste = tokens[1:]

    if mot in negations and reste:
        mot_suivant = reste[0]
        score_inverse = -lexique.get(mot_suivant, 0)
        return score_inverse + calculer_score(reste[1:], lexique, negations)

    return lexique.get(mot, 0) + calculer_score(reste, lexique, negations)
```

**Pourquoi c'est récursif et pas une simple boucle `for` ?** Parce qu'on doit parfois **sauter deux tokens d'un coup** (le mot de négation + le mot qu'il inverse), ce qui est plus naturel à exprimer en "traite le premier élément, puis appelle-toi toi-même sur le reste" qu'avec un `for` classique (qui devrait gérer un index qu'on avance manuellement de 1 ou 2 selon le cas).

Trace à la main sur `["jamais", "recommande"]` :
1. `calculer_score(["jamais", "recommande"], ...)` → `mot="jamais"`, c'est une négation, `mot_suivant="recommande"` (score +1 dans le lexique) → `score_inverse = -1`. On appelle `calculer_score([], ...)` (on a sauté les deux mots).
2. `calculer_score([], ...)` → liste vide → **cas de base** → retourne `0`.
3. Résultat final : `-1 + 0 = -1`.

Sans le cas de base (`if not tokens: return 0`), la fonction s'appellerait indéfiniment sur une liste de plus en plus courte jusqu'à un `IndexError` — **toute fonction récursive a besoin d'une condition d'arrêt**, exactement comme vu dans la section "Fonctions récursives (bonus)" du Chapitre 04.

## 3. `solution/modeles.py` — où le nettoyage a lieu **une seule fois**

```python
class Avis:
    def __init__(self, texte, client, note_etoiles):
        self.texte = texte
        self.tokens = nettoyer_texte(texte)   # calculé UNE FOIS, à la création de l'objet
```
On tokenise le texte dans `__init__`, pas à chaque fois qu'on calcule un score. Si `AnalyseurSentiment.score()` re-nettoyait le texte à chaque appel, on referait le même travail inutilement à chaque fois qu'on classe le même avis (par exemple dans `repartition_sentiments()` **et** dans `mots_frequents_avis_negatifs()`, qui appellent chacun `classifier()`).

## 4. `AnalyseurSentiment` — séparer le "calcul" de la "présentation"

`score()` retourne un nombre, `classifier()` traduit ce nombre en `"positif"/"neutre"/"négatif"` selon deux seuils, et `rapport()` assemble le tout en texte lisible. Cette séparation permet de réutiliser `score()` ailleurs (par exemple pour trier les avis du plus positif au plus négatif) sans être obligé de reformater du texte à chaque fois.

## 5. Le tableau croisé — un dictionnaire de dictionnaires

```python
tableau.setdefault(etoiles, {"positif": 0, "neutre": 0, "négatif": 0})
tableau[etoiles][sentiment] += 1
```
`dict.setdefault(cle, valeur_par_defaut)` : si `etoiles` n'existe pas encore comme clé, on l'initialise avec le dictionnaire `{"positif": 0, ...}` ; si elle existe déjà, on ne touche à rien. C'est un raccourci pour éviter un `if cle not in tableau: tableau[cle] = ...` — utile dès que vous construisez une structure imbriquée (dictionnaire de dictionnaires, vu au Chapitre 03) au fil d'une boucle.
