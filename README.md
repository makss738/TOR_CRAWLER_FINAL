# TOR_CRAWLER_FINAL

## Présentation

**TOR_CRAWLER_FINAL** est un outil de collecte et d'analyse automatisée développé dans le cadre d'un projet universitaire en cybersécurité.

L'objectif principal est de fournir un environnement permettant de :

* récupérer le contenu de pages web via un scraper Python ;
* parcourir automatiquement plusieurs pages à partir d'une URL de départ grâce à un crawler ;
* extraire les liens présents dans les pages analysées ;
* enregistrer les résultats pour une analyse ultérieure ;
* détecter des informations liées à des règles CTI (Cyber Threat Intelligence).

L'outil possède également :

* un système de comparaison par hash pour identifier les changements de contenu ;
* une base de connaissances générée automatiquement ;
* un dashboard Streamlit de visualisation.

---

# Architecture du projet

```
TOR_CRAWLER_FINAL/

├── core/
│   ├── crawler.py          # Moteur de crawl
│   ├── scraper.py          # Récupération du contenu des pages
│   ├── cti.py              # Analyse CTI
│   ├── rules.py             # Règles de détection
│   ├── hash_checker.py      # Vérification des changements
│   ├── url_manager.py       # Gestion des URLs
│   ├── alerts.py            # Gestion des alertes
│   ├── knowledge.py         # Génération de la base documentaire
│   ├── rag.py               # Recherche intelligente
│   ├── tor_test.py          # Test de connexion Tor
│   └── tor_manager.py       # Gestion Tor
│
├── dashboard/
│   └── app.py               # Interface Streamlit
│
├── data/
│   ├── results.json         # Résultats des scans
│   ├── visited.json         # URLs déjà visitées
│   ├── hashes.json          # Empreintes des pages
│   └── alerts.json           # Alertes détectées
│
├── onions.txt               # Liste des URLs à analyser
├── requirements.txt         # Dépendances Python
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Prérequis

* Linux recommandé (Ubuntu/Debian)
* Python 3.10+
* Tor installé
* Git

Vérifier Python :

```bash
python3 --version
```

Vérifier Tor :

```bash
tor --version
```

---

# Installation

## 1. Cloner le projet

```bash
git clone <URL_DU_DEPOT>
```

Entrer dans le dossier :

```bash
cd TOR_CRAWLER_FINAL
```

---

## 2. Créer l'environnement virtuel Python

Créer le venv :

```bash
python3 -m venv venv
```

Activer :

```bash
source venv/bin/activate
```

Le terminal doit afficher :

```
(venv)
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Utilisation de l'outil

## 1. Vérifier la connexion Tor

Avant tout lancement, tester Tor :

```bash
python core/tor_test.py
```

Résultat attendu :

```
[+] Testing Tor IP...

xxx.xxx.xxx.xxx
```

Si une adresse IP apparaît, Tor fonctionne correctement.

---

# 2. Tester le scraper

Le scraper permet de récupérer le contenu HTML d'une page.

Lancer :

```bash
python core/scraper.py
```

Entrer une URL :

Exemple :

```
https://www.wikipedia.org
```

Le programme affiche :

* le code HTTP ;
* un aperçu du contenu HTML.

---

# 3. Lancer le crawler

Le crawler permet de parcourir automatiquement les pages découvertes.

Lancer :

```bash
python core/crawler.py
```

Entrer l'URL de départ :

Exemple :

```
https://www.wikipedia.org
```

Le crawler va :

1. récupérer la page ;
2. analyser son contenu ;
3. extraire les liens présents ;
4. ajouter les nouvelles URLs ;
5. enregistrer les résultats.

---

# Résultats générés

Après un crawl, les résultats sont enregistrés dans :

## results.json

Contient les informations principales :

```json
{
"url": "https://example.com",
"status":200,
"score":0,
"entities":[],
"links_found":20
}
```

---

## visited.json

Liste des pages déjà analysées.

Permet d'éviter de traiter plusieurs fois la même URL.

---

## hashes.json

Contient l'empreinte des pages.

Le système compare les hashes afin d'identifier si une page a été modifiée entre deux analyses.

---

## alerts.json

Stocke les alertes CTI générées.

---

# Analyse CTI

Après collecte, l'outil analyse les contenus récupérés.

Fonctionnalités :

* recherche d'entités surveillées ;
* application de règles ;
* calcul d'un score ;
* génération d'alertes.

---

# Génération de la base de connaissances

Pour générer les fichiers documentaires :

```bash
python core/knowledge.py
```

Les fichiers sont générés dans :

```
data/knowledge/
```

Ils peuvent être ouverts avec Obsidian.

---

# Lancement du dashboard

Installer Streamlit si nécessaire :

```bash
pip install streamlit
```

Lancer :

```bash
streamlit run dashboard/app.py
```

Accès :

```
http://localhost:8501
```

Le dashboard affiche :

* nombre de pages analysées ;
* résultats CTI ;
* alertes ;
* scores ;
* données collectées.

---

# Réinitialiser une analyse

Pour recommencer un scan propre :

```bash
echo "[]" > data/results.json
echo "[]" > data/visited.json
echo "{}" > data/hashes.json
echo "[]" > data/alerts.json
```

---

# Utilisation avec Docker

Construction :

```bash
docker compose build
```

Lancement :

```bash
docker compose up
```

---

# Dépannage

## Erreur :

```
externally-managed-environment
```

Solution :

Utiliser un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Erreur :

```
Permission denied venv/bin/pip
```

Le venv a probablement été créé avec sudo.

Supprimer :

```bash
rm -rf venv
```

Puis recréer sans sudo :

```bash
python3 -m venv venv
```

---

## Tor ne répond pas

Vérifier le service :

```bash
sudo systemctl status tor
```

Démarrer :

```bash
sudo systemctl start tor
```

---

# Commandes principales

| Action                 | Commande                         |
| ---------------------- | -------------------------------- |
| Tester Tor             | `python core/tor_test.py`        |
| Tester scraper         | `python core/scraper.py`         |
| Lancer crawler         | `python core/crawler.py`         |
| Générer Knowledge Base | `python core/knowledge.py`       |
| Dashboard              | `streamlit run dashboard/app.py` |

---

# Licence

Projet réalisé dans un cadre universitaire.
