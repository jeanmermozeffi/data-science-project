# 📋 Jeu de données `bootcamp_500.csv`

Jeu de données pédagogique de **510 lignes** (500 + 10 doublons) simulant les inscriptions
d'un bootcamp Data Science en Afrique de l'Ouest. Conçu pour les chapitres
**Data Exploration** et **Pandas Profiling**.

## Colonnes

| Colonne | Type | Description |
|---------|------|-------------|
| `id_etudiant` | entier | Identifiant unique (haute cardinalité) |
| `prenom` | texte | Prénom de l'étudiant |
| `nom` | texte | Nom de famille |
| `age` | entier | Âge (⚠️ contient des valeurs aberrantes) |
| `ville` | texte | Ville (⚠️ casse/espaces incohérents + valeurs manquantes) |
| `niveau` | catégoriel | Débutant / Intermédiaire / Avancé (variable ordinale) |
| `heures_etude` | décimal | Heures d'étude hebdomadaires |
| `note_sql` | décimal | Note SQL /20 (⚠️ valeurs manquantes + quelques > 20) |
| `note_python` | décimal | Note Python /20 (⚠️ valeurs manquantes) |
| `salaire_stage` | entier | Salaire de stage en FCFA (⚠️ quelques outliers élevés) |

## Problèmes volontairement intégrés (pour la pratique)

| Problème | Localisation | Compétence travaillée |
|----------|--------------|------------------------|
| **Valeurs manquantes** | `ville` (15), `note_sql` (25), `note_python` (20) | Imputation |
| **Âges aberrants** | 6 lignes : 150, 200, 175, -5, -1, 0 | Outliers / valeurs impossibles |
| **Notes impossibles** | 3 lignes : note_sql > 20 (25, 22, 30) | Anomalies / règles métier |
| **Salaires extrêmes** | 4 lignes : ~480k à 750k FCFA | Outliers (réels mais rares) |
| **Casse/espaces** | ~8% des villes (`ABIDJAN`, `  Dakar`, `abidjan`...) | Nettoyage de texte |
| **Doublons** | 10 lignes dupliquées entièrement | `drop_duplicates()` |

## Signaux exploitables (pour l'EDA / le profiling)

- **Corrélation forte** : `heures_etude` ↔ `note_sql`/`note_python` (~0.79)
- **Corrélation forte** : `note_sql` ↔ `note_python` (~0.84) → alerte "High correlation"
- **Absence de corrélation** : `age` et `salaire_stage` vs les notes (~0) → bon contre-exemple
- **Haute cardinalité** : `id_etudiant`, `prenom`, `nom`

## Chargement

```python
import pandas as pd
df = pd.read_csv("bootcamp_500.csv")
print(df.shape)   # (510, 10)
```

*Généré avec `np.random.seed(42)` — reproductible.*
