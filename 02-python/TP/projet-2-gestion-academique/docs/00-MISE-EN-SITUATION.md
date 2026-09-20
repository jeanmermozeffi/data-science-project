# 🎓 Mise en situation — Projet 2 : Gestion académique

## Le contexte, en une phrase

Le bootcamp vous demande de coder l'outil qui calcule automatiquement les **moyennes, mentions, bourses et classement** de la promotion "Data Science Batch 7" — 12 étudiants fictifs, chacun avec des notes dans 4 matières pondérées par un coefficient différent.

## Pourquoi ce n'est pas juste "faire une moyenne"

Trois types d'étudiants existent, avec des règles **différentes** :

| Type | Particularité |
|---|---|
| `Etudiant` (normal) | Mention standard selon la moyenne pondérée |
| `EtudiantBoursier` | En plus de la mention, une **bourse** calculée selon un barème de moyennes |
| `EtudiantRedoublant` | Les seuils de mention sont **plus indulgents** (on valorise la progression) |

Si vous codez ça avec une seule classe et des `if type == "boursier": ... elif type == "redoublant": ...` partout dans votre code, chaque nouvelle règle vous oblige à modifier toutes les fonctions. C'est exactement le problème que l'**héritage** et le **polymorphisme** résolvent : chaque type d'étudiant porte sa propre logique.

## Ce que vous allez construire

```
etudiants_bruts.py  →  construire_etudiant()  →  Etudiant / EtudiantBoursier / EtudiantRedoublant
     (dict bruts)         (choisit la classe)              (chacun avec son comportement)
                                                                        ↓
                                                            Promotion (classement, stats, rapport)
```

## Comment lire ce dossier

1. Essayez d'abord de coder votre version à partir du cahier des charges (projet 2 dans `Python/06-PYTHON_TP_PROJET_FINAL.md`).
2. Bloqué sur l'héritage ou le polymorphisme ? Lisez `01-EXPLICATION-CODE.md`.
3. Comparez avec `solution/`, puis lancez :
   ```bash
   cd solution
   python3 main.py
   ```

## Questions à vous poser en codant

- Pourquoi `EtudiantBoursier.__init__` appelle-t-il `super().__init__(nom, notes)` au lieu de recopier le même code ?
- Que se passe-t-il dans `promotion.rapport()` quand on appelle `etudiant.mention()` sur une liste mélangeant les 3 types d'étudiants ? Comment Python sait-il laquelle des 3 versions de `mention()` exécuter ?
- Si un 4ᵉ type d'étudiant apparaissait (`EtudiantEchange`, en programme d'échange), combien de fichiers devriez-vous modifier avec cette architecture ?
