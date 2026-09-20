# 📖 Explication simplifiée du corrigé — Projet 3

## 1. `data/films.py` — les genres comme `set`

```python
{"titre": "Abidjan Nights", "genres": {"drame", "romance"}, "note": 7.8, "annee": 2021}
```
Les genres sont stockés comme un **ensemble** (`set`), pas une liste. Pourquoi ? Parce qu'on ne se soucie ni de l'ordre des genres, ni des doublons, et qu'on va faire des **opérations ensemblistes** (union, intersection) dessus — exactement le cas d'usage des sets vu au Chapitre 03.

## 2. `solution/analyse.py` — l'indice de Jaccard, ligne par ligne

```python
def similarite_jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)
```
- `set_a & set_b` : l'**intersection**, les genres présents dans les deux ensembles.
- `set_a | set_b` : l'**union**, tous les genres des deux ensembles réunis (sans doublons, propriété native du set).
- Le `if not set_a and not set_b` évite une division par zéro si les deux ensembles sont vides (union de taille 0).

Le résultat est toujours entre 0 (aucun genre commun) et 1 (exactement les mêmes genres).

## 3. `Utilisateur.genres_preferes()` — construire le profil de goûts

```python
def genres_preferes(self):
    preferes = set()
    for film in self.films_vus:
        preferes |= film.genres
    return preferes
```
`preferes |= film.genres` est équivalent à `preferes = preferes | film.genres` : à chaque film vu, on **ajoute** ses genres à l'ensemble des goûts. Après la boucle, `preferes` contient l'union de tous les genres de tous les films vus — c'est le "profil goûts" de l'utilisateur, sans aucun genre en double (propriété automatique du `set`).

## 4. `Recommandeur.recommander()` — trier avec une clé composite

```python
candidats_tries = sorted(
    candidats,
    key=lambda film: (similarite_jaccard(genres_utilisateur, film.genres), film.note),
    reverse=True,
)
```
La `key` retourne un **tuple** `(similarité, note)`. Python compare d'abord la similarité ; en cas d'égalité parfaite, il compare la note pour départager. C'est le même principe que trier une liste de tuples vu au Chapitre 03 — appliqué ici à des objets `Film` via une `lambda`.

## 5. Le bonus : `recommander_pondere()` — un score mélangé

```python
def score(film):
    sim = similarite_jaccard(genres_utilisateur, film.genres)
    note_norm = normaliser_note(film.note)
    return poids_similarite * sim + poids_note * note_norm
```
Ici on ne compare plus deux critères séparément (similarité puis note) : on fusionne les deux en **un seul nombre**, une moyenne pondérée (70% similarité + 30% note par défaut). C'est une technique très courante en recommandation : combiner plusieurs signaux en un score unique pour pouvoir trier une seule fois.

`normaliser_note()` ramène la note (potentiellement sur une échelle 0-10) vers 0-1, pour qu'elle soit sur la **même échelle** que la similarité (déjà entre 0 et 1) — sinon la note écraserait complètement la similarité dans la somme.

## 6. Pourquoi `Film.__eq__` est défini ?

```python
def __eq__(self, other):
    return isinstance(other, Film) and self.titre == other.titre
```
C'est une **méthode spéciale** (dunder, vue au Chapitre 05). Elle permet de comparer deux `Film` avec `==` en se basant uniquement sur le titre (deux films avec le même titre sont "le même film"). C'est utilisé implicitement par `Utilisateur.a_vu()` via `f.titre == film.titre` — ici on compare directement les titres pour rester simple, mais `__eq__` reste disponible si vous préférez écrire `film in utilisateur.films_vus` ailleurs dans votre propre code.
