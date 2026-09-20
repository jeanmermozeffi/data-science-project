# 🎬 Mise en situation — Projet 3 : Moteur de recommandation

## Le contexte, en une phrase

Une plateforme de streaming fictive vous demande : *"Netflix utilise du Machine Learning pour recommander des films — peux-tu nous montrer une première version simple, sans IA, juste en comparant les genres que regarde un utilisateur ?"*

## L'idée : recommander par ressemblance, pas par prédiction

Pas de Machine Learning ici (ça viendra dans un futur module). L'idée est **beaucoup plus simple et 100% compréhensible** :

1. On regarde les genres des films déjà vus par l'utilisateur (ex : Awa a vu des films "drame", "romance", "aventure").
2. Pour chaque film **non vu** du catalogue, on mesure à quel point ses genres **ressemblent** aux genres préférés d'Awa.
3. On recommande les films les plus ressemblants.

La mesure de ressemblance utilisée s'appelle l'**indice de Jaccard** — une formule extrêmement simple issue directement de ce que vous avez appris sur les `sets` :

```
similarité(A, B) = taille(A ∩ B) / taille(A ∪ B)
```

Exemple concret : Awa aime `{"drame", "romance", "aventure"}`. Un film "Trahison à Korhogo" a les genres `{"drame", "thriller"}`.
- Intersection : `{"drame"}` → taille 1
- Union : `{"drame", "romance", "aventure", "thriller"}` → taille 4
- Similarité = 1/4 = **0.25**

## Ce que vous allez construire

```
films.py (catalogue + historique)  →  Utilisateur.genres_preferes()  →  Recommandeur.recommander()
                                          (union des genres vus)         (trie par similarité de Jaccard)
```

## Comment lire ce dossier

1. Essayez d'abord de coder votre version (cahier des charges : projet 3 dans `Python/06-PYTHON_TP_PROJET_FINAL.md`).
2. Bloqué sur les sets ou le calcul de similarité ? Lisez `01-EXPLICATION-CODE.md`.
3. Comparez avec `solution/`, puis lancez :
   ```bash
   cd solution
   python3 main.py
   ```

## Questions à vous poser en codant

- Que se passe-t-il si `set_a` et `set_b` n'ont **aucun genre en commun** ? Pourquoi la fonction ne doit-elle pas planter dans ce cas (division par zéro) ?
- Pourquoi `genres_preferes()` utilise l'**union** (`|`) des genres et pas l'**intersection** (`&`) ?
- Le score "pondéré" (bonus) mélange similarité et note du film. Que se passerait-il si vous mettiez 100% du poids sur la note ? Est-ce encore une "recommandation personnalisée" ?
