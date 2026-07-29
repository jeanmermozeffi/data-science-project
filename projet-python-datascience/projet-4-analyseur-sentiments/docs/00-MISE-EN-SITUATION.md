# 💬 Mise en situation — Projet 4 : Analyseur de sentiments

## Le contexte, en une phrase

CI-Shop (déjà croisée au projet 1) reçoit des dizaines d'avis clients en texte libre chaque semaine et personne n'a le temps de tous les lire. On vous demande un outil qui classe automatiquement chaque avis en **positif / neutre / négatif**, sans intelligence artificielle — juste avec un dictionnaire de mots-clés.

## Le principe : un lexique de sentiment

C'est la technique la plus simple qui existe en analyse de sentiment, bien avant le Machine Learning : on construit un dictionnaire `mot → score`.

```python
LEXIQUE = {"excellent": 2, "correct": 1, "nul": -2, "déçu": -1, ...}
```

Pour un avis, on additionne les scores des mots reconnus. Score final positif → avis positif, négatif → avis négatif, proche de zéro → neutre.

## Le piège : la négation

"Ce produit est **nul**" est négatif (score -2). Mais "Ce produit n'est **pas nul**" devrait être... positif ! Sans gérer la négation, un algorithme naïf se tromperait à chaque fois qu'un client utilise une tournure négative. Le projet vous demande donc de détecter les mots comme "pas", "jamais", "aucun" et d'**inverser le score du mot qui suit**.

> ⚠️ **Attention, ce n'est pas magique.** Même avec la négation gérée, regardez l'avis d'Adjoua dans le jeu de données : *"Ce n'est pas terrible, service peu sérieux."* L'outil le classe **positif** (score +2), alors qu'un humain sent bien que c'est un avis mitigé/négatif. Pourquoi ? Parce que "pas terrible" est pris **littéralement** ("pas" + "terrible" → inverse de -1 → +1), alors qu'en français c'est une **expression figée** qui veut dire "moyen/décevant", pas "l'inverse de terrible". **C'est une vraie limite des systèmes à base de règles** — exactement la raison pour laquelle le NLP moderne (que vous verrez plus tard) utilise des modèles statistiques/deep learning plutôt que des dictionnaires figés.

## Ce que vous allez construire

```
avis_clients.py + lexique.py  →  Avis.tokens (nettoyage)  →  AnalyseurSentiment.classifier()  →  rapport global
```

## Comment lire ce dossier

1. Essayez d'abord de coder votre version (cahier des charges : projet 4 dans `Python/06-PYTHON_TP_PROJET_FINAL.md`).
2. Bloqué sur la tokenisation ou la récursivité de la négation ? Lisez `01-EXPLICATION-CODE.md`.
3. Comparez avec `solution/`, puis lancez :
   ```bash
   cd solution
   python3 main.py
   ```

## Questions à vous poser en codant

- Pourquoi nettoyer le texte (minuscules, ponctuation) **avant** de chercher les mots dans le lexique, et pas après ?
- Dans `calculer_score`, que retourne la fonction quand `tokens` est une liste vide ? Pourquoi est-ce indispensable pour qu'une fonction récursive s'arrête un jour ?
- Trouvez un autre avis du jeu de données où la négation change complètement le sens et vérifiez à la main que le score correspond à votre lecture humaine du texte.
