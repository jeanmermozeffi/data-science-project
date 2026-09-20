# 📖 Explication simplifiée du corrigé — Projet 2

## 1. Représenter les notes : pourquoi un tuple `(note, coefficient)` ?

```python
"notes": {"Python": (16, 3), "Statistiques": (14, 2), ...}
```
Un dictionnaire `matière → (note, coefficient)`. On utilise un **tuple** (Chapitre 03) car la paire `(note, coefficient)` ne doit **jamais changer de forme** une fois créée — c'est exactement l'usage recommandé du tuple ("quand utiliser un tuple plutôt qu'une liste").

## 2. `Etudiant.moyenne_ponderee()` — la formule de base

```python
total_points = sum(note * coef for note, coef in self.notes.values())
total_coefs = sum(coef for _, coef in self.notes.values())
return total_points / total_coefs
```
C'est une moyenne pondérée classique : `Σ(note × coef) / Σ(coef)`. Le `_` dans `for _, coef in ...` est une convention Python pour dire "je n'utilise pas cette valeur" (ici la note, car on ne veut que le coefficient).

## 3. Héritage : `EtudiantBoursier` et `EtudiantRedoublant`

### `EtudiantBoursier` — hérite ET ajoute un comportement

```python
class EtudiantBoursier(Etudiant):
    def __init__(self, nom, notes, bareme, montant_plein):
        super().__init__(nom, notes)   # réutilise le __init__ du parent
        self.bareme = bareme
        self.montant_plein = montant_plein

    def calcul_bourse(self):
        ...
```
`super().__init__(nom, notes)` appelle le constructeur de `Etudiant` pour initialiser `nom` et `notes` **sans dupliquer ce code**. Ensuite, `EtudiantBoursier` ajoute ses propres attributs (`bareme`, `montant_plein`) et sa propre méthode `calcul_bourse()` que `Etudiant` n'a pas.

### `EtudiantRedoublant` — hérite ET redéfinit un comportement existant

```python
class EtudiantRedoublant(Etudiant):
    def mention(self):
        moyenne = self.moyenne_ponderee()
        if moyenne >= 14:
            return "Bien (progression notable)"
        ...
```
Ici, on ne **rajoute** rien : on **remplace** la méthode `mention()` héritée de `Etudiant` par une version aux seuils différents. `moyenne_ponderee()`, elle, n'est pas redéfinie : `EtudiantRedoublant` utilise directement celle du parent. C'est ça, l'héritage : on choisit **quoi garder** et **quoi remplacer**.

## 4. Le polymorphisme en action — `Promotion.rapport()`

```python
for etudiant in self.classement():
    lignes.append(f"... {etudiant.mention()} ...")
```
Cette ligne ne sait pas si `etudiant` est un `Etudiant`, un `EtudiantBoursier` ou un `EtudiantRedoublant`. Elle appelle juste `.mention()`. **Python appelle automatiquement la bonne version** selon la classe réelle de l'objet — c'est le polymorphisme : même appel, comportement différent selon le type.

C'est ce qui permet à `construire_etudiant()` dans `main.py` d'être le **seul endroit** du programme où on teste le type :
```python
def construire_etudiant(donnees):
    if donnees["type"] == "boursier":
        return EtudiantBoursier(...)
    if donnees["type"] == "redoublant":
        return EtudiantRedoublant(...)
    return Etudiant(...)
```
Partout ailleurs (`Promotion`, `rapport`, `bulletin`...), le code traite tous les étudiants de la même façon, sans jamais rouvrir un `if type == ...`.

## 5. `Promotion` — utilisation de `lambda` et `filter`

```python
def classement(self):
    return sorted(self.etudiants, key=lambda e: e.moyenne_ponderee(), reverse=True)

def etudiants_en_difficulte(self):
    return list(filter(lambda e: e.moyenne_ponderee() < 10, self.etudiants))
```
- `sorted(..., key=lambda e: e.moyenne_ponderee())` : trie les objets `Etudiant` en se basant sur le résultat de leur méthode `moyenne_ponderee()`, sans avoir besoin d'écrire une fonction nommée à part.
- `filter(lambda e: e.moyenne_ponderee() < 10, ...)` : ne garde que les étudiants dont la moyenne est sous la barre de 10/20.

## 6. Pourquoi `analyse.py` recalcule un `ecart_type` séparé du projet 1 ?

Chaque projet du TP est **indépendant et autonome** : on pourrait factoriser `ecart_type` dans un module commun partagé entre les 5 projets, mais ce serait une optimisation prématurée pour un TP pédagogique où chaque dossier doit pouvoir être lu et exécuté seul, sans dépendre des autres projets.
