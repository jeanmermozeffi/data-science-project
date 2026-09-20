# 🕸️ Python Web Scraping — Cours Bootcamp Data Science

> **Module Data Science** | Prérequis : Module Python Pur (Chapitres 1 à 5) + NumPy

---

## Table des matières

1. [Explorer le Web Scraping](#1-explorer-le-web-scraping)
2. [Challenge & Legality of Web Scraping](#2-challenge--legality-of-web-scraping)
3. [Understanding HTML for Web Scraping](#3-understanding-html-for-web-scraping)
4. [Getting Started with Web Scraping](#4-getting-started-with-web-scraping)
5. [Scrape HTML Content from a Page](#5-scrape-html-content-from-a-page)
6. [Utilizing Classes and IDs for Efficient Web Scraping](#6-utilizing-classes-and-ids-for-efficient-web-scraping)
7. [Sélecteurs CSS — L'approche moderne](#7-sélecteurs-css--lapproche-moderne)
8. [Gérer les erreurs et être un bon scraper](#8-gérer-les-erreurs-et-être-un-bon-scraper)
9. [Practical Example — Prévisions météo (NWS)](#9-practical-example--prévisions-météo-nws)
10. [Practical Example bonus — Cours de la BRVM](#10-practical-example-bonus--cours-de-la-brvm)
11. [Conclusion](#11-conclusion)
12. [✅ Point de contrôle — Web Scraping](#12--point-de-contrôle--web-scraping)

---

## 1. Explorer le Web Scraping

### 📖 Qu'est-ce que le Web Scraping ?

Le **Web Scraping** (extraction de données web) est la technique qui consiste à **extraire automatiquement des informations** depuis des pages web, en écrivant un programme qui lit le code HTML d'une page comme le ferait un navigateur, puis en récupère les données qui vous intéressent.

> 💡 **Analogie** : Imaginez que vous devez recopier à la main les prix de 500 produits depuis un site e-commerce dans un tableau Excel. Ce serait long, fastidieux et source d'erreurs. Le web scraping, c'est comme **engager un assistant robot infatigable** qui visite chaque page à votre place, lit le contenu, et recopie exactement ce dont vous avez besoin — en quelques secondes plutôt qu'en plusieurs heures.

### 1.1 Pourquoi le Web Scraping est essentiel en Data Science ?

```
LE WEB SCRAPING DANS LE PIPELINE DATA SCIENCE
│
├── 🌐 Source de données   → Le web contient des données que personne
│                            ne vous fournira "toutes prêtes" en CSV
│
├── 📊 Alimentation de modèles → Prix, avis clients, actualités,
│                                données météo, cours de bourse...
│
├── 🔄 Automatisation      → Collecter des données à intervalles
│                            réguliers (ex : suivi quotidien de prix)
│
└── 🔗 Complément d'API     → Quand une API n'existe pas ou est payante,
                              le scraping est souvent l'alternative
```

### 1.2 Cas d'usage concrets

| Domaine | Exemple d'utilisation |
|---------|------------------------|
| **Finance** | Récupérer les cours d'actions de la BRVM en temps réel |
| **Météo** | Extraire des prévisions pour alimenter un modèle prédictif |
| **E-commerce** | Comparer les prix d'un produit sur plusieurs sites |
| **Immobilier** | Analyser les tendances de prix par quartier |
| **Recherche** | Construire un corpus de textes pour du NLP |
| **Veille** | Suivre les actualités d'un secteur automatiquement |

### 1.3 Le processus général du Web Scraping

```
    1. REQUÊTE                2. ANALYSE               3. EXTRACTION            4. STOCKAGE
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐    ┌──────────────────┐
│ Envoyer une       │      │ Parser le code    │      │ Cibler les         │    │ Sauvegarder dans │
│ requête HTTP au    │─────▶│ HTML reçu en une  │─────▶│ éléments voulus    │───▶│ un CSV, une base  │
│ serveur (comme un  │      │ structure          │      │ (classes, id,      │    │ de données, ou un │
│ navigateur)        │      │ navigable          │      │ balises)           │    │ DataFrame Pandas  │
└──────────────────┘      └──────────────────┘      └──────────────────┘    └──────────────────┘
     requests                 BeautifulSoup             .find() / .select()        pandas.DataFrame
```

---

## 2. Challenge & Legality of Web Scraping

### 📖 Le web scraping n'est pas automatiquement autorisé partout

Avant d'écrire la moindre ligne de code, il est **essentiel** de comprendre le cadre légal et éthique du web scraping. Ce n'est pas parce qu'une information est **visible** sur un site qu'elle est **libre d'être extraite en masse**.

> 🔑 **Règle d'or** : "Public" (visible par tous) ne signifie pas "libre de droits" ou "autorisé à l'extraction automatisée".

### 2.1 Les défis techniques du Web Scraping

```
DÉFIS COURANTS
│
├── 🔄 Sites dynamiques      → Contenu généré par JavaScript, invisible
│                              dans le HTML brut (nécessite Selenium/Playwright)
│
├── 🚧 Anti-bot / CAPTCHA    → Certains sites bloquent les robots
│
├── 🏗️  Structure changeante → Le HTML d'un site change régulièrement,
│                              cassant les scripts de scraping existants
│
├── 🐌 Limitation de débit   → Trop de requêtes trop vite = blocage IP
│
└── 🔐 Contenu derrière un login → Données accessibles uniquement
                                    après authentification
```

### 2.2 Le fichier `robots.txt` — La première chose à vérifier

Chaque site peut publier un fichier `robots.txt` à sa racine qui indique **quelles parties du site** les robots (dont les scrapers) sont autorisés ou non à visiter.

```python
# Exemple : consulter le robots.txt d'un site
# https://www.example.com/robots.txt

"""
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/
Crawl-delay: 10
"""
```

| Directive | Signification |
|-----------|----------------|
| `User-agent: *` | S'applique à tous les robots |
| `Disallow: /admin/` | Interdit de scraper cette section |
| `Allow: /public/` | Autorise explicitement cette section |
| `Crawl-delay: 10` | Attendre 10 secondes entre chaque requête |

```python
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.example.com/robots.txt")
rp.read()

# Vérifier si une URL précise peut être scrapée
peut_scraper = rp.can_fetch("*", "https://www.example.com/page")
print(peut_scraper)   # True ou False
```

> ⚠️ **Le `robots.txt` n'est qu'une convention** (il n'est pas techniquement "bloquant"), mais l'ignorer expose à des risques juridiques et éthiques.

### 2.3 Conditions d'utilisation (Terms of Service)

En plus du `robots.txt`, chaque site a ses **Conditions Générales d'Utilisation (CGU)**, qui peuvent explicitement interdire l'extraction automatisée de données. Les violer peut entraîner :

```
CONSÉQUENCES POSSIBLES D'UN SCRAPING NON AUTORISÉ
│
├── ⚖️  Poursuites judiciaires    → Violation des CGU, du droit d'auteur
├── 🚫 Blocage définitif de l'IP  → Perte d'accès au site
├── 📧 Mise en demeure            → Demande d'arrêt immédiat
└── 💰 Dommages et intérêts       → Dans les cas les plus graves (usage commercial)
```

### 2.4 Bonnes pratiques éthiques et légales

```
✅ À FAIRE                                  ❌ À ÉVITER
────────────────────────                    ────────────────────────
Vérifier robots.txt et les CGU              Ignorer les interdictions explicites
Utiliser des données publiques               Scraper des données personnelles
  et non sensibles                            sans consentement (RGPD)
Limiter la fréquence des requêtes            Envoyer des centaines de requêtes
  (time.sleep entre chaque requête)           par seconde (surcharge serveur)
Privilégier une API officielle si elle        Scraper du contenu protégé par
  existe                                       copyright pour le republier
S'identifier avec un User-Agent honnête       Se faire passer pour un humain
Utiliser les données à des fins               de manière trompeuse
  personnelles / éducatives / recherche       Revendre des données scrapées
                                               sans autorisation
```

> 💡 **Dans ce cours**, nous scraperons exclusivement des sources de **données publiques à vocation informative** (services météorologiques gouvernementaux, cours boursiers publiés publiquement), à des fins **strictement pédagogiques**, avec des délais raisonnables entre les requêtes.

---

## 3. Understanding HTML for Web Scraping

### 📖 Pourquoi comprendre le HTML est indispensable

Le web scraping consiste à **lire la structure HTML** d'une page pour en extraire des données. Sans comprendre HTML, impossible de dire à votre programme "va chercher cette information précise".

> 💡 **Analogie** : Le HTML d'une page web, c'est comme le **plan d'un immeuble**. Pour trouver "l'appartement 3B", il faut comprendre comment les étages, couloirs et portes sont organisés. De la même façon, pour extraire "le prix du produit", il faut comprendre où cette donnée se situe dans la structure de la page.

### 3.1 Structure de base d'une page HTML

```html
<html>
  <head>
    <title>Ma Page</title>
  </head>
  <body>
    <h1>Titre principal</h1>
    <p>Un paragraphe de texte.</p>
    <div class="produit">
      <span class="nom">Ordinateur portable</span>
      <span class="prix">850000 FCFA</span>
    </div>
  </body>
</html>
```

### 3.2 Le concept d'arbre (DOM)

Le HTML est organisé en **arbre hiérarchique** — chaque balise peut contenir d'autres balises (ses "enfants").

```
html
│
├── head
│   └── title ("Ma Page")
│
└── body
    ├── h1 ("Titre principal")
    ├── p ("Un paragraphe de texte.")
    └── div (class="produit")
        ├── span (class="nom")   → "Ordinateur portable"
        └── span (class="prix")  → "850000 FCFA"
```

### 3.3 Balises HTML courantes pour le scraping

| Balise | Signification | Utilité pour le scraping |
|--------|----------------|----------------------------|
| `<div>` | Conteneur générique (section) | Regroupe souvent un bloc de données |
| `<p>` | Paragraphe | Contient du texte |
| `<span>` | Conteneur en ligne | Souvent une donnée précise (prix, nom) |
| `<a href="...">` | Lien hypertexte | Contient une URL à extraire |
| `<img src="...">` | Image | Contient une URL d'image |
| `<table>`, `<tr>`, `<td>` | Tableau, ligne, cellule | Données tabulaires (prix, statistiques) |
| `<ul>`, `<li>` | Liste, élément de liste | Séries d'éléments répétés |
| `<h1>` à `<h6>` | Titres | Titres de sections |

### 3.4 Attributs `class` et `id` — Les clés du scraping

C'est **LA notion la plus importante** pour le web scraping : les développeurs utilisent des attributs `class` et `id` pour **styliser** et **identifier** des éléments — et ce sont ces mêmes attributs qui permettent de **cibler précisément** une donnée.

```html
<div id="meteo-actuelle" class="widget">
    <span class="temperature">24°C</span>
    <span class="ville">Abidjan</span>
</div>
```

| Attribut | Caractéristique | Analogie |
|----------|------------------|----------|
| `id="..."` | **Unique** dans toute la page | Le numéro de sécurité sociale d'un élément |
| `class="..."` | Peut être **partagé** par plusieurs éléments | Une étiquette de catégorie (ex : "tous les produits en promo") |

```html
<!-- id : un SEUL élément dans toute la page a cet id -->
<div id="header">...</div>

<!-- class : PLUSIEURS éléments peuvent partager cette classe -->
<p class="prix">1000 FCFA</p>
<p class="prix">2500 FCFA</p>
<p class="prix">500 FCFA</p>
```

### 3.5 Inspecter le HTML d'une page — L'outil indispensable

Avant d'écrire le moindre code de scraping, il faut **inspecter la page** dans le navigateur pour repérer les balises, classes et id à cibler.

```
COMMENT INSPECTER UNE PAGE WEB
│
├── 1. Ouvrir la page dans Chrome/Firefox
├── 2. Clic droit sur l'élément qui vous intéresse
├── 3. Sélectionner "Inspecter" (ou "Inspecter l'élément")
├── 4. Le panneau développeur s'ouvre, montrant le HTML exact
└── 5. Repérer la classe/id de l'élément à extraire
```

> 🔑 **C'est l'étape la plus importante de tout projet de scraping** : 90% du travail consiste à bien identifier la structure HTML avant même d'écrire du code Python.

---

## 4. Getting Started with Web Scraping

### 4.1 Les outils essentiels

```
BOÎTE À OUTILS DU WEB SCRAPING EN PYTHON
│
├── 📡 requests          → Envoyer des requêtes HTTP, récupérer le HTML brut
├── 🍜 BeautifulSoup4     → Parser (analyser) et naviguer dans le HTML
├── 🐼 pandas             → Structurer et sauvegarder les données extraites
└── (avancé) Selenium     → Scraper des sites avec contenu JavaScript dynamique
```

### 4.2 Installation

```python
# Dans un terminal ou une cellule Google Colab
!pip install requests beautifulsoup4 pandas
```

### 4.3 Importer les bibliothèques

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time    # pour espacer les requêtes (politesse envers le serveur)
```

### 4.4 requests vs BeautifulSoup — Qui fait quoi ?

```
requests                          BeautifulSoup
─────────────────                 ─────────────────────
Va chercher la page                Comprend et organise
sur Internet                       le contenu HTML récupéré

   Internet                            HTML brut
      │                                    │
      ▼                                    ▼
requests.get(url)  ───► texte HTML ───►  BeautifulSoup(html)
                        (une longue        │
                        chaîne de           ▼
                        caractères)      Objet navigable
                                         (comme un arbre)
```

> 💡 **Analogie** : `requests` est le **facteur** qui va chercher le courrier (la page HTML) chez le destinataire (le serveur web). `BeautifulSoup` est le **secrétaire** qui ouvre l'enveloppe, lit le document, et vous aide à retrouver rapidement l'information précise que vous cherchez dedans.

---

## 5. Scrape HTML Content from a Page

### 5.1 Envoyer une requête avec `requests`

```python
import requests

url = "https://www.example.com"
reponse = requests.get(url)

print(reponse.status_code)   # 200 = succès !
print(reponse.text[:500])     # les 500 premiers caractères du HTML
```

### 5.2 Comprendre les codes de statut HTTP

| Code | Signification | Action |
|------|----------------|--------|
| `200` | ✅ Succès | Continuer, la page a été récupérée |
| `301` / `302` | 🔄 Redirection | La page a été déplacée |
| `403` | 🚫 Interdit | Accès refusé (souvent anti-bot) |
| `404` | ❓ Non trouvé | L'URL n'existe pas |
| `429` | ⏳ Trop de requêtes | Vous scrapez trop vite, ralentissez ! |
| `500` | 💥 Erreur serveur | Problème du côté du site |

```python
reponse = requests.get(url)

if reponse.status_code == 200:
    print("✅ Page récupérée avec succès")
else:
    print(f"❌ Erreur : code {reponse.status_code}")
```

### 5.3 S'identifier avec un User-Agent

Certains sites bloquent les requêtes qui n'ont pas d'en-tête `User-Agent` (car cela ressemble à un robot suspect). Il est poli et souvent nécessaire de s'identifier.

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) — Bootcamp Data Science / usage pédagogique"
}

reponse = requests.get(url, headers=headers)
print(reponse.status_code)
```

### 5.4 Transformer le HTML en objet BeautifulSoup

```python
from bs4 import BeautifulSoup

reponse = requests.get(url, headers=headers)
soup = BeautifulSoup(reponse.text, "html.parser")

# Afficher le HTML de façon indentée et lisible
print(soup.prettify()[:1000])

# Récupérer le titre de la page
print(soup.title)         # <title>Titre de la page</title>
print(soup.title.text)    # Titre de la page (texte seul)
```

> 💡 `"html.parser"` est l'analyseur (parser) intégré à Python. D'autres parsers existent (`"lxml"`, plus rapide, nécessite `pip install lxml`), mais `html.parser` suffit pour débuter.

### 5.5 Extraire tout le texte d'une page

```python
# Récupérer tout le texte visible, sans le HTML
texte_complet = soup.get_text()
print(texte_complet[:500])
```

---

## 6. Utilizing Classes and IDs for Efficient Web Scraping

### 📖 Cibler précisément les données

Une fois la page transformée en objet `BeautifulSoup`, on utilise ses méthodes `.find()` et `.find_all()` pour **naviguer et cibler** des éléments précis — généralement via leur balise, leur `class`, ou leur `id`.

### 6.1 `.find()` — Trouver le PREMIER élément correspondant

```python
html_exemple = """
<div class="produit">
    <span class="nom">Ordinateur portable</span>
    <span class="prix">850000 FCFA</span>
</div>
<div class="produit">
    <span class="nom">Souris sans fil</span>
    <span class="prix">15000 FCFA</span>
</div>
"""

soup = BeautifulSoup(html_exemple, "html.parser")

# Trouver le PREMIER élément <div> ayant class="produit"
premier_produit = soup.find("div", class_="produit")
print(premier_produit)

# Trouver un élément par son id
element = soup.find(id="mon-id")
```

> ⚠️ **Piège classique** : en Python, `class` est un mot réservé (pour les classes POO). BeautifulSoup utilise donc `class_` (avec un underscore) pour cibler l'attribut HTML `class`.

### 6.2 `.find_all()` — Trouver TOUS les éléments correspondants

```python
# Trouver TOUS les <div class="produit"> de la page
tous_les_produits = soup.find_all("div", class_="produit")
print(f"Nombre de produits trouvés : {len(tous_les_produits)}")

for produit in tous_les_produits:
    nom  = produit.find("span", class_="nom").text
    prix = produit.find("span", class_="prix").text
    print(f"{nom} — {prix}")
```

**Résultat :**
```
Nombre de produits trouvés : 2
Ordinateur portable — 850000 FCFA
Souris sans fil — 15000 FCFA
```

### 6.3 Naviguer par balise seule

```python
# Trouver toutes les balises <a> (liens)
liens = soup.find_all("a")
for lien in liens[:5]:
    print(lien.get("href"))    # récupérer l'attribut href

# Trouver tous les titres h2
titres = soup.find_all("h2")
for titre in titres:
    print(titre.text.strip())
```

### 6.4 Extraire des attributs

```python
image = soup.find("img")
print(image.get("src"))     # récupère l'URL de l'image
print(image.get("alt"))     # récupère le texte alternatif
print(image["src"])         # syntaxe alternative (équivalente)
```

### 6.5 Chaîner les recherches (navigation imbriquée)

```python
html_exemple = """
<div id="tableau-bord">
    <div class="section">
        <h3>Ventes</h3>
        <p class="valeur">45000</p>
    </div>
</div>
"""

soup = BeautifulSoup(html_exemple, "html.parser")

# Chaîner : d'abord le conteneur, puis l'élément à l'intérieur
tableau = soup.find("div", id="tableau-bord")
section = tableau.find("div", class_="section")
valeur  = section.find("p", class_="valeur")

print(valeur.text)   # 45000
```

### 6.6 `.find()` avec plusieurs critères

```python
# Combiner balise + classe + attribut supplémentaire
element = soup.find("div", class_="produit", attrs={"data-id": "123"})

# Rechercher un texte précis
element_texte = soup.find("span", string="Ordinateur portable")
```

### 6.7 Tableau récapitulatif

| Méthode | Description | Exemple |
|---------|-------------|---------|
| `.find(balise)` | Premier élément de cette balise | `soup.find("div")` |
| `.find(balise, class_="x")` | Premier élément avec cette classe | `soup.find("p", class_="prix")` |
| `.find(id="x")` | Élément avec cet id (unique) | `soup.find(id="header")` |
| `.find_all(balise)` | TOUS les éléments de cette balise | `soup.find_all("a")` |
| `.find_all(balise, class_="x")` | TOUS les éléments avec cette classe | `soup.find_all("div", class_="produit")` |
| `.text` / `.get_text()` | Texte contenu dans l'élément | `element.text` |
| `.get("attribut")` | Valeur d'un attribut HTML | `lien.get("href")` |

---

## 7. Sélecteurs CSS — L'approche moderne

### 📖 `.select()` — Une alternative puissante

En plus de `.find()`/`.find_all()`, BeautifulSoup permet d'utiliser directement des **sélecteurs CSS** (comme ceux utilisés pour le style des pages web) via `.select()`. Beaucoup de développeurs trouvent cette syntaxe plus rapide à écrire.

```python
soup = BeautifulSoup(html_exemple, "html.parser")

# Sélectionner par classe (le point . signifie "classe")
produits = soup.select(".produit")

# Sélectionner par id (le dièse # signifie "id")
header = soup.select_one("#header")

# Sélectionner une balise à l'intérieur d'une autre (descendant)
noms = soup.select(".produit .nom")

# Sélectionner le n-ième élément
premier = soup.select("div.produit")[0]
```

### 7.1 Tableau des sélecteurs CSS courants

| Sélecteur CSS | Signification | Exemple |
|----------------|----------------|---------|
| `div` | Toutes les balises `<div>` | `soup.select("div")` |
| `.classe` | Éléments avec cette classe | `soup.select(".prix")` |
| `#id` | Élément avec cet id | `soup.select_one("#header")` |
| `div.produit` | `<div>` ayant la classe `produit` | `soup.select("div.produit")` |
| `div .nom` | `.nom` À L'INTÉRIEUR d'un `div` | `soup.select("div .nom")` |
| `div > p` | `<p>` **enfant direct** d'un `div` | `soup.select("div > p")` |
| `a[href]` | Balises `<a>` ayant un attribut `href` | `soup.select("a[href]")` |

### 7.2 `.find_all()` vs `.select()` — Comparaison

```python
# Équivalence entre les deux approches
methode_find    = soup.find_all("div", class_="produit")
methode_select  = soup.select("div.produit")

# Les deux retournent le même résultat !
print(len(methode_find) == len(methode_select))   # True
```

| Approche | Avantages |
|----------|-----------|
| `.find()` / `.find_all()` | Plus explicite pour les débutants, gestion fine des attributs |
| `.select()` | Syntaxe CSS concise, pratique si vous connaissez déjà le CSS |

---

## 8. Gérer les erreurs et être un bon scraper

### 8.1 Toujours vérifier le statut de la réponse

```python
import requests
from bs4 import BeautifulSoup

def recuperer_page(url, headers=None):
    """Récupère une page de façon sécurisée, avec gestion d'erreurs."""
    try:
        reponse = requests.get(url, headers=headers, timeout=10)
        reponse.raise_for_status()   # lève une erreur si code != 200
        return BeautifulSoup(reponse.text, "html.parser")
    except requests.exceptions.Timeout:
        print("❌ Le serveur a mis trop de temps à répondre")
    except requests.exceptions.HTTPError as erreur:
        print(f"❌ Erreur HTTP : {erreur}")
    except requests.exceptions.RequestException as erreur:
        print(f"❌ Erreur de connexion : {erreur}")
    return None
```

### 8.2 Espacer les requêtes — La politesse envers les serveurs

```python
import time

urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]

for url in urls:
    soup = recuperer_page(url)
    if soup:
        # ... traiter les données ...
        pass
    time.sleep(2)   # attendre 2 secondes avant la requête suivante
```

> 🔑 **Pourquoi attendre ?** Envoyer des centaines de requêtes en une seconde peut **surcharger le serveur** (comportement proche d'une attaque) et vous fera très probablement **bannir** votre adresse IP. `time.sleep()` simule un rythme de navigation humain et respectueux.

### 8.3 Vérifier qu'un élément existe avant de l'utiliser

```python
# ❌ Risque d'erreur si l'élément n'existe pas
prix = soup.find("span", class_="prix").text   # AttributeError si None !

# ✅ Vérifier avant d'accéder au texte
element_prix = soup.find("span", class_="prix")
if element_prix:
    prix = element_prix.text
else:
    prix = "Non disponible"
```

---

## 9. Practical Example — Prévisions météo (NWS)

Mettons tout en pratique avec un exemple réel : extraire les **prévisions météo sur 7 jours** depuis le site du **National Weather Service** (service météorologique public américain).

> 📍 **Source utilisée** : `https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168` (prévisions pour San Francisco). Ce site gouvernemental publie des données météo publiques, sans restriction de `robots.txt` sur ces pages de prévisions — un excellent terrain d'entraînement légal et éthique.

### 9.1 Étape 1 — Inspecter la structure de la page

En inspectant la page dans le navigateur, on découvre que les prévisions sont structurées ainsi :

```html
<div id="seven-day-forecast">
    <ul id="seven-day-forecast-list">
        <li class="forecast-tombstone">
            <div class="tombstone-container">
                <p class="period-name">Overnight</p>
                <p><img class="forecast-icon" src="..." alt="..." title="..."></p>
                <p class="short-desc">Mostly Cloudy</p>
                <p class="temp temp-low">Low: 58 °F</p>
            </div>
        </li>
        <li class="forecast-tombstone">
            <div class="tombstone-container">
                <p class="period-name">Wednesday</p>
                <p><img class="forecast-icon" src="..." alt="..." title="..."></p>
                <p class="short-desc">Becoming Sunny</p>
                <p class="temp temp-high">High: 72 °F</p>
            </div>
        </li>
        <!-- ... 7 autres périodes ... -->
    </ul>
</div>
```

> 🔑 On repère la structure clé : un conteneur `id="seven-day-forecast"`, contenant plusieurs blocs `class="tombstone-container"` (un par période), chacun avec `period-name`, `short-desc` et `temp`.

### 9.2 Étape 2 — Récupérer et parser la page

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}

reponse = requests.get(url, headers=headers, timeout=10)
print("Statut :", reponse.status_code)   # 200 attendu

soup = BeautifulSoup(reponse.text, "html.parser")
```

### 9.3 Étape 3 — Cibler le conteneur des prévisions

```python
# Cibler le conteneur principal via son id (unique dans la page)
conteneur_meteo = soup.find(id="seven-day-forecast")

# Trouver chaque bloc de prévision (un par période)
periodes = conteneur_meteo.find_all("div", class_="tombstone-container")
print(f"Nombre de périodes trouvées : {len(periodes)}")   # 9 en général
```

### 9.4 Étape 4 — Extraire les données de chaque période

```python
donnees_meteo = []

for periode in periodes:
    # Nom de la période (ex: "Overnight", "Wednesday")
    nom_element = periode.find("p", class_="period-name")
    nom = nom_element.text.strip() if nom_element else "N/A"

    # Description courte (ex: "Mostly Cloudy")
    desc_element = periode.find("p", class_="short-desc")
    description = desc_element.text.strip() if desc_element else "N/A"

    # Température (peut être "temp-high" ou "temp-low")
    temp_element = periode.find("p", class_=lambda c: c and "temp" in c)
    temperature = temp_element.text.strip() if temp_element else "N/A"

    donnees_meteo.append({
        "periode"     : nom,
        "description" : description,
        "temperature" : temperature
    })

# Afficher les résultats
for entree in donnees_meteo:
    print(entree)
```

**Résultat attendu :**
```
{'periode': 'Overnight', 'description': 'Mostly Cloudy', 'temperature': 'Low: 58 °F'}
{'periode': 'Wednesday', 'description': 'Becoming Sunny', 'temperature': 'High: 72 °F'}
{'periode': 'Wednesday Night', 'description': 'Increasing Clouds', 'temperature': 'Low: 57 °F'}
...
```

### 9.5 Étape 5 — Structurer avec Pandas et nettoyer les données

```python
# Transformer en DataFrame Pandas (aperçu du prochain chapitre !)
df_meteo = pd.DataFrame(donnees_meteo)

# Extraire uniquement le nombre de la température (nettoyage)
df_meteo["temp_valeur"] = df_meteo["temperature"].str.extract(r"(\d+)").astype(float)
df_meteo["temp_type"]   = df_meteo["temperature"].apply(
    lambda x: "Max" if "High" in x else ("Min" if "Low" in x else "N/A")
)

print(df_meteo)

# Sauvegarder en CSV pour analyse ultérieure
df_meteo.to_csv("previsions_meteo.csv", index=False, encoding="utf-8")
print("✅ Données sauvegardées dans previsions_meteo.csv")
```

### 9.6 Étape 6 — Une petite analyse

```python
# Température maximale prévue sur la période
temp_max = df_meteo[df_meteo["temp_type"] == "Max"]["temp_valeur"].max()
print(f"Température maximale prévue : {temp_max}°F")

# Toutes les descriptions mentionnant "Sunny"
jours_ensoleilles = df_meteo[df_meteo["description"].str.contains("Sunny", case=False)]
print(jours_ensoleilles[["periode", "description"]])
```

---

## 10. Practical Example bonus — Cours de la BRVM

Deuxième exemple pratique, plus proche du contexte régional : extraire les **cours des actions** de la **Bourse Régionale des Valeurs Mobilières** (BRVM), qui couvre 8 pays d'Afrique de l'Ouest francophone.

> 📍 **Source utilisée** : `https://www.brvm.org/fr/cours-actions/0` — page publique listant tous les titres cotés, leur volume, cours d'ouverture/clôture et variation du jour.

### 10.1 Cas d'usage — Données tabulaires (`<table>`)

Contrairement à l'exemple météo (des blocs `<div>` répétés), les cours boursiers de la BRVM sont typiquement présentés dans un **tableau HTML** (`<table>`). C'est un cas extrêmement fréquent en Data Science (finance, statistiques officielles, classements sportifs...).

```
STRUCTURE TYPIQUE D'UN TABLEAU DE COURS BOURSIERS
│
<table>
├── <thead>                          ← en-têtes de colonnes
│   └── <tr><th>Symbole</th><th>Nom</th><th>Cours Clôture</th>...</tr>
└── <tbody>                          ← les lignes de données
    ├── <tr><td>ABJC</td><td>SERVAIR...</td><td>3 180</td>...</tr>
    ├── <tr><td>BICB</td><td>BANQUE...</td><td>8 000</td>...</tr>
    └── ... (une ligne par titre coté)
```

### 10.2 Méthode 1 — Avec `pandas.read_html()` (la plus rapide)

Quand les données sont dans un `<table>` HTML standard, **Pandas peut directement lire le tableau** sans même passer par BeautifulSoup !

> ⚠️ **Piège fréquent** : appeler directement `pd.read_html(url)` échoue souvent en pratique — la fonction va chercher la page elle-même via `urllib`, **sans en-tête `User-Agent`** et sans gérer les certificats SSL de la même façon qu'un vrai navigateur. Résultat typique : un `DataFrame` vide, une liste de tableaux incomplète, ou une erreur SSL — **alors que le tableau existe bel et bien** dans le HTML de la page (comme on peut le vérifier en faisant un clic droit → "Afficher le code source" dans le navigateur).
>
> La solution robuste, déjà vue en §5.3 : récupérer la page soi-même avec `requests` (+ `headers`), puis donner le **texte HTML** obtenu à `pd.read_html()` — pas l'URL. Depuis les versions récentes de pandas, il faut envelopper ce texte dans `io.StringIO(...)`, sinon pandas tente de le traiter comme un chemin de fichier ou une URL et lève une erreur.

```python
import io
import requests
import pandas as pd

url = "https://www.brvm.org/fr/cours-actions/0"
headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}

# 1. On récupère la page nous-mêmes (comme un navigateur), pas via pd.read_html(url)
reponse = requests.get(url, headers=headers, timeout=10)
reponse.raise_for_status()

# 2. On donne le TEXTE HTML (enveloppé dans StringIO) à read_html, pas l'URL
tableaux = pd.read_html(io.StringIO(reponse.text))
print(f"Nombre de tableaux trouvés sur la page : {len(tableaux)}")

# Identifier celui qui contient les cours (généralement en inspectant chaque tableau)
for i, tab in enumerate(tableaux):
    print(f"--- Tableau {i} — colonnes : {list(tab.columns)} ---")
    print(tab.head(2))
    print()
```

**Résultat attendu sur la page BRVM** — la page contient en réalité **4 tableaux** (les mini-tableaux "Top 5" et "Flop 5" affichés en haut de page, un résumé de "l'activité du marché", puis le tableau complet des cours) :

```
Tableau 0 — colonnes : ['Top 5', 'Cours', 'Variation']        (5 lignes)
Tableau 1 — colonnes : ['Flop 5', 'Cours', 'Variation']       (5 lignes)
Tableau 2 — colonnes : ['Activités du marché', ...]           (résumé du marché)
Tableau 3 — colonnes : ['Symbole', 'Nom', 'Volume', ...]      (47 lignes → celui qu'on veut !)
```

> 💡 **Astuce pratique** : `pd.read_html()` est souvent le moyen **le plus rapide** de scraper des données tabulaires — à condition (1) que les données soient dans une vraie balise `<table>` (et non générées dynamiquement par JavaScript), et (2) qu'on lui fournisse un HTML déjà récupéré avec des en-têtes corrects plutôt qu'une URL brute.

### 10.3 Méthode 2 — Avec BeautifulSoup (plus de contrôle)

Si vous avez besoin de plus de contrôle (par exemple pour cibler un tableau précis via sa classe), utilisez BeautifulSoup directement :

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.brvm.org/fr/cours-actions/0"
headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}

reponse = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(reponse.text, "html.parser")

# ⚠️ Piège : la page BRVM contient PLUSIEURS <table> qui partagent les mêmes
# classes CSS ("table table-hover table-striped") — les mini-tableaux "Top 5"
# et "Flop 5" affichés en haut de page, puis le tableau complet des cours.
# soup.find("table") tout seul attraperait donc le mauvais tableau (le "Top 5",
# qui n'a que 3 colonnes) ! On cible plutôt le tableau via son en-tête, qui est
# unique : celui qui commence par la colonne "Symbole".
tableau = None
for t in soup.find_all("table"):
    premier_entete = t.find("th")
    if premier_entete and premier_entete.text.strip() == "Symbole":
        tableau = t
        break

lignes_donnees = []
if tableau:
    lignes = tableau.find_all("tr")[1:]   # [1:] pour ignorer la ligne d'en-tête
    for ligne in lignes:
        cellules = ligne.find_all("td")
        if len(cellules) >= 7:
            lignes_donnees.append({
                "symbole"        : cellules[0].text.strip(),
                "nom"            : cellules[1].text.strip(),
                "volume"         : cellules[2].text.strip(),
                "cours_veille"   : cellules[3].text.strip(),
                "cours_ouverture": cellules[4].text.strip(),
                "cours_cloture"  : cellules[5].text.strip(),
                "variation"      : cellules[6].text.strip(),
            })

df_brvm = pd.DataFrame(lignes_donnees)
print(df_brvm.head())
```

> ⚠️ **Important** : Les sites web changent régulièrement de structure HTML (mises à jour, refontes). **Ne recopiez jamais un code de scraping sans d'abord inspecter vous-même la page actuelle** dans votre navigateur — les classes CSS exactes indiquées ici sont des exemples pédagogiques à valider/adapter.

### 10.4 Nettoyer les données financières extraites

Les nombres extraits du web sont du **texte** (avec espaces, symboles `%`, virgules) — il faut les convertir en valeurs numériques exploitables.

```python
# Exemple de nettoyage typique de données financières scrapées
def nettoyer_nombre(texte):
    """Convertit '12 155' ou '3,28%' en valeur numérique."""
    if not texte or texte == "N/A":
        return None
    texte_propre = texte.replace(" ", "").replace("\xa0", "").replace("%", "").replace(",", ".")
    try:
        return float(texte_propre)
    except ValueError:
        return None

# Application sur le DataFrame
df_brvm["cours_cloture_num"] = df_brvm["cours_cloture"].apply(nettoyer_nombre)
df_brvm["variation_num"]     = df_brvm["variation"].apply(nettoyer_nombre)

# Trouver le titre avec la plus forte hausse
meilleur = df_brvm.loc[df_brvm["variation_num"].idxmax()]
print(f"Plus forte hausse : {meilleur['nom']} ({meilleur['variation_num']}%)")
```

---

## 11. Conclusion

### 📌 Récapitulatif du chapitre

```
WEB SCRAPING AVEC PYTHON
│
├── Légalité & éthique   → robots.txt, CGU, RGPD, time.sleep() (politesse)
│
├── Comprendre le HTML    → balises, arbre DOM, class vs id
│
├── Outils                → requests (récupérer) + BeautifulSoup (parser)
│
├── Extraction ciblée
│   ├── .find() / .find_all()   → par balise, classe, id
│   └── .select() / .select_one() → sélecteurs CSS
│
├── Cas tabulaire          → pandas.read_html() pour les <table>
│
├── Robustesse             → try/except, vérifier avant d'accéder,
│                            gérer les codes de statut HTTP
│
└── Pipeline complet        → requête → parsing → extraction →
                              nettoyage → DataFrame → CSV
```

### 🔑 Points clés à retenir

1. **Toujours vérifier la légalité** (`robots.txt`, CGU) avant de scraper un site.
2. Le HTML est un **arbre** ; `class` et `id` sont les clés pour cibler des éléments précis.
3. `requests` récupère la page, `BeautifulSoup` la transforme en structure navigable.
4. `.find()` retourne le **premier** résultat, `.find_all()` retourne **tous** les résultats (une liste).
5. Pour des données dans un `<table>` HTML, `pandas.read_html()` est souvent le chemin le plus rapide.
6. **Être un bon citoyen du web** : `time.sleep()` entre les requêtes, `User-Agent` honnête, ne pas surcharger les serveurs.
7. Les données extraites du web sont du **texte brut** — il faut presque toujours les **nettoyer** avant analyse.

### 🗺️ Ce qui vient ensuite

Dans le prochain chapitre, nous découvrirons **Pandas** en profondeur — la bibliothèque idéale pour **structurer, nettoyer et analyser** les données que vous venez d'apprendre à extraire du web (DataFrames, filtres, `groupby`, fusion de tableaux, gestion des valeurs manquantes).

---

## 12. ✅ Point de contrôle — Web Scraping

### 📝 Questions théoriques

**Q1.** Pourquoi est-il important de consulter le fichier `robots.txt` avant de scraper un site ?

<details>
<summary>👀 Voir la réponse</summary>

> Le `robots.txt` indique quelles parties d'un site les robots sont autorisés ou non à visiter. L'ignorer expose à des risques juridiques (violation potentielle des CGU), éthiques, et peut entraîner un blocage de votre adresse IP. C'est la première vérification à faire avant tout projet de scraping.
</details>

---

**Q2.** Quelle est la différence entre `class` et `id` en HTML, du point de vue du scraping ?

<details>
<summary>👀 Voir la réponse</summary>

> Un `id` est **unique** dans toute la page — un seul élément peut avoir un `id` donné, ce qui le rend idéal pour cibler un conteneur précis avec `.find(id="...")`. Une `class` peut être **partagée** par plusieurs éléments, ce qui est utile pour cibler tous les éléments similaires (ex : tous les prix d'une page) avec `.find_all(class_="...")`.
</details>

---

**Q3.** Quelle est la différence entre `.find()` et `.find_all()` en BeautifulSoup ?

<details>
<summary>👀 Voir la réponse</summary>

> `.find()` retourne le **premier** élément correspondant aux critères (ou `None` s'il n'existe pas). `.find_all()` retourne **une liste de tous** les éléments correspondants (liste vide si aucun résultat).
</details>

---

**Q4.** Pourquoi utilise-t-on `time.sleep()` entre les requêtes lors d'un scraping de plusieurs pages ?

<details>
<summary>👀 Voir la réponse</summary>

> `time.sleep()` espace les requêtes dans le temps pour éviter de **surcharger le serveur** cible et de se faire **bloquer** (l'envoi de centaines de requêtes en une seconde peut être perçu comme une attaque). C'est une pratique de politesse et de responsabilité envers l'infrastructure du site scrapé.
</details>

---

**Q5.** Dans quel cas privilégier `pandas.read_html()` plutôt que BeautifulSoup ?

<details>
<summary>👀 Voir la réponse</summary>

> `pandas.read_html()` est idéal quand les données sont déjà structurées dans une vraie balise HTML `<table>` — il extrait automatiquement tous les tableaux de la page en DataFrames, sans code de parsing manuel. BeautifulSoup reste nécessaire pour des structures plus complexes (divs répétés, données non tabulaires) ou quand on a besoin de cibler un tableau précis parmi plusieurs.
</details>

---

### 💻 Exercices pratiques

**Exercice 1 — Requête et statut**

Envoyez une requête GET vers `https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168`, affichez le code de statut, et vérifiez qu'il vaut 200.

<details>
<summary>👀 Voir la solution</summary>

```python
import requests

url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}

reponse = requests.get(url, headers=headers, timeout=10)
print("Statut :", reponse.status_code)

if reponse.status_code == 200:
    print("✅ Page récupérée avec succès")
```
</details>

---

**Exercice 2 — Parsing et titre**

À partir de la réponse de l'exercice 1, créez un objet `BeautifulSoup` et affichez le titre de la page (`<title>`).

<details>
<summary>👀 Voir la solution</summary>

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(reponse.text, "html.parser")
print(soup.title.text)
```
</details>

---

**Exercice 3 — Extraction ciblée**

Cherchez tous les éléments `<p class="period-name">` de la page météo et affichez leur texte (les noms des périodes : "Overnight", "Wednesday"...).

<details>
<summary>👀 Voir la solution</summary>

```python
periodes = soup.find_all("p", class_="period-name")
for p in periodes:
    print(p.text.strip())
```
</details>

---

**Exercice 4 — Sélecteurs CSS**

Refaites l'exercice 3, mais en utilisant `.select()` avec un sélecteur CSS plutôt que `.find_all()`.

<details>
<summary>👀 Voir la solution</summary>

```python
periodes = soup.select("p.period-name")
for p in periodes:
    print(p.text.strip())
```
</details>

---

**Exercice 5 — Pipeline complet**

Construisez une fonction `scraper_meteo(url)` qui retourne un DataFrame Pandas avec les colonnes `periode`, `description`, `temperature` pour une URL météo donnée.

<details>
<summary>👀 Voir la solution</summary>

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraper_meteo(url):
    headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}
    reponse = requests.get(url, headers=headers, timeout=10)

    if reponse.status_code != 200:
        print(f"❌ Erreur : statut {reponse.status_code}")
        return None

    soup = BeautifulSoup(reponse.text, "html.parser")
    conteneur = soup.find(id="seven-day-forecast")
    periodes = conteneur.find_all("div", class_="tombstone-container")

    donnees = []
    for p in periodes:
        nom  = p.find("p", class_="period-name")
        desc = p.find("p", class_="short-desc")
        temp = p.find("p", class_=lambda c: c and "temp" in c)
        donnees.append({
            "periode"     : nom.text.strip() if nom else "N/A",
            "description" : desc.text.strip() if desc else "N/A",
            "temperature" : temp.text.strip() if temp else "N/A"
        })

    return pd.DataFrame(donnees)

df = scraper_meteo("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
print(df)
```
</details>

---

### 🏆 Challenge bonus

En utilisant `pandas.read_html()` sur la page `https://www.brvm.org/fr/cours-actions/0` :
1. Identifiez le tableau contenant les cours des actions
2. Nettoyez la colonne de variation (`%`) pour la convertir en nombre
3. Affichez les 5 titres ayant la plus forte variation positive
4. Affichez les 5 titres ayant la plus forte variation négative

*Indice : après avoir identifié le bon tableau avec `pd.read_html()`, utilisez `.sort_values()` sur la colonne de variation numérique.*

<details>
<summary>👀 Voir une piste de solution</summary>

```python
import io
import requests
import pandas as pd

url = "https://www.brvm.org/fr/cours-actions/0"
headers = {"User-Agent": "Bootcamp Data Science - usage pédagogique"}

# On récupère nous-mêmes le HTML (cf. §10.2) plutôt que de passer l'URL
# directement à pd.read_html() — voir l'encart "Piège fréquent" plus haut.
reponse = requests.get(url, headers=headers, timeout=10)
tableaux = pd.read_html(io.StringIO(reponse.text))

# Inspecter chaque tableau pour trouver celui des cours
for i, t in enumerate(tableaux):
    print(f"Tableau {i} — colonnes : {list(t.columns)}")

# Une fois identifié (à adapter selon l'indice trouvé) :
df_cours = tableaux[i]   # remplacer i par l'indice du bon tableau

# Nettoyer la colonne de variation (adapter le nom de colonne)
df_cours["variation_num"] = (
    df_cours["Variation (%)"]
    .astype(str)
    .str.replace(",", ".")
    .astype(float)
)

top5_hausse  = df_cours.sort_values("variation_num", ascending=False).head(5)
top5_baisse  = df_cours.sort_values("variation_num", ascending=True).head(5)

print("Top 5 hausses :\n", top5_hausse)
print("\nTop 5 baisses :\n", top5_baisse)
```
</details>

---

*📘 Module Data Science — Python Web Scraping | Bootcamp Data Science*
