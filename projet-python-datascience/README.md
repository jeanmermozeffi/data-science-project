# 🐍 Projets Python — Bootcamp Data Science

> Corrigés complets, jeux de données et explications pédagogiques pour les **5 projets** proposés dans le TP final (`Python/06-PYTHON_TP_PROJET_FINAL.md`), qui clôt les 5 chapitres Python du bootcamp.
>
> **100% Python pur** — pas de pandas/numpy/scikit-learn : tout est fait "from scratch" avec les notions déjà vues en cours (listes, dictionnaires, sets, tuples, fonctions, POO).

---

## 🎯 Les 5 projets

| # | Projet | Thème data science | Notions phares |
|---|---|---|---|
| 1 | [`projet-1-data-cleaner-ventes`](projet-1-data-cleaner-ventes/) | Nettoyage & analyse de ventes e-commerce | listes de dicts, `filter`, encapsulation, héritage (`Client`/`ClientVIP`) |
| 2 | [`projet-2-gestion-academique`](projet-2-gestion-academique/) | Moyennes, mentions et bourses d'une promotion | héritage multiple, polymorphisme, `lambda`+`sorted`+`filter` |
| 3 | [`projet-3-recommandation-films`](projet-3-recommandation-films/) | Moteur de recommandation par similarité | `sets`, indice de Jaccard, tri par clé composite |
| 4 | [`projet-4-analyseur-sentiments`](projet-4-analyseur-sentiments/) | Classification de sentiment d'avis clients | `map`/`filter`, dictionnaires, **récursivité** |
| 5 | [`projet-5-knn-from-scratch`](projet-5-knn-from-scratch/) | Mini-bibliothèque ML : classifieur KNN | distance euclidienne, train/test split, POO avancée |

Chaque projet est **autonome** : aucun ne dépend d'un autre, aucun n'a besoin d'une bibliothèque externe.

---

## 📂 Organisation de chaque projet

```
projet-X-nom/
├── docs/
│   ├── 00-MISE-EN-SITUATION.md   ← contexte simplifié, pourquoi ce projet, comment le lire
│   └── 01-EXPLICATION-CODE.md    ← le corrigé expliqué ligne par ligne, en langage simple
├── data/
│   └── ...py                     ← jeu de données fictif mais réaliste (avec ses "défauts" volontaires)
└── solution/
    ├── modeles.py                ← les classes (POO)
    ├── analyse.py / nettoyage.py ← les fonctions de calcul/nettoyage
    └── main.py                   ← point d'entrée à exécuter
```

---

## 🧭 Parcours conseillé (le même pour chaque projet)

1. **Lisez d'abord** `docs/00-MISE-EN-SITUATION.md` du projet qui vous intéresse : il pose le contexte comme si un client vous confiait la mission.
2. **Cherchez par vous-même**, à partir du cahier des charges dans `Python/06-PYTHON_TP_PROJET_FINAL.md` — sans regarder le corrigé. C'est cette étape qui vous fait progresser.
3. **Bloqué ?** Lisez `docs/01-EXPLICATION-CODE.md` : chaque classe et fonction du corrigé y est expliquée simplement (le "pourquoi", pas juste le "quoi").
4. **Comparez** avec votre propre code — il n'y a pas qu'une seule bonne solution.
5. **Exécutez le corrigé** pour voir le résultat de référence :
   ```bash
   cd projet-X-nom/solution
   python3 main.py
   ```

> ✅ Aucune installation nécessaire — juste **Python 3** (testé avec Python 3.13). Chaque `main.py` se lance tel quel depuis son dossier `solution/`.

### 🎮 Mode interactif

Après avoir affiché le rapport sur le jeu de données fourni, **chaque `main.py` propose un mode de test manuel** : il vous demande si vous voulez saisir vos propres données (une vente, un étudiant, vos genres préférés, un avis, une fleur...) et affiche immédiatement le résultat calculé par le programme. C'est la meilleure façon de vérifier que vous avez bien compris la logique — testez des cas limites (note à 20, quantité à 0, avis très négatif...) et voyez comment le code réagit.

Répondez `n` (ou appuyez sur Entrée) pour quitter le mode interactif à tout moment.

---

## 🔑 Ce que chaque projet démontre (en un coup d'œil)

- **Projet 1** : comment un dictionnaire imbriqué mal contrôlé (prix `None`, doublons, quantité négative) fausse silencieusement une analyse — et comment `filter()` + une clé de déduplication corrigent ça proprement.
- **Projet 2** : comment l'héritage évite un `if type == "boursier": ... elif ...` qui grossirait à chaque nouveau cas métier.
- **Projet 3** : comment un calcul aussi simple que l'indice de Jaccard (`|A∩B| / |A∪B|`) suffit à construire un premier moteur de recommandation, sans aucun Machine Learning.
- **Projet 4** : les limites réelles d'une analyse de sentiment à base de règles — y compris un cas volontairement piégeux ("pas terrible") mal classé, pour comprendre pourquoi le NLP moderne existe.
- **Projet 5** : ce qu'il y a "dans la boîte" d'un classifieur KNN — distance, vote majoritaire, split train/test, choix d'hyperparamètre — avant de le remplacer un jour par `scikit-learn`.

---

*Données 100% fictives, générées ou inventées pour l'entraînement. Devise : FCFA (XOF) où applicable.* 🇨🇮
