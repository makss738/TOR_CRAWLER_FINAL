# TOR_CRAWLER_FINAL

# 🕷️ Tor CTI Monitor

## Cyber Threat Intelligence Dark Web Monitoring Tool

Tor CTI Monitor est un outil de veille Cyber Threat Intelligence (CTI) permettant de collecter, analyser et visualiser des informations provenant du réseau Tor.

L'objectif est de détecter automatiquement :

- des mentions d'organisations surveillées
- des fuites potentielles de données
- des informations sensibles
- des changements sur des pages surveillées

Le projet utilise un crawler Tor, un moteur d'analyse CTI et un dashboard de visualisation.


---

# Fonctionnalités


## Infrastructure de collecte

- Connexion au réseau Tor via SOCKS5
- Scraping de pages .onion
- Crawling automatique des liens
- Gestion des erreurs réseau


## Analyse CTI

- Détection d'entités surveillées
- Analyse Regex
- Détection de mots-clés sensibles
- Score de risque


Exemples d'entités :

```
CyberV
ESIEE Paris
IUT de Villetaneuse
Hackuten
CatTheFlag
Air France
OSINT FR
```


## Historique et intégrité

- Sauvegarde des résultats
- Historique des URLs
- Calcul SHA256 des contenus
- Détection de modification d'une page


## Alerting

Détection automatique :

- score élevé
- contenu modifié
- présence d'informations sensibles


## Dashboard

Interface Streamlit permettant :

- visualisation des pages analysées
- affichage des entités détectées
- affichage des scores
- consultation des alertes


---

# Architecture du projet


```
Tor-Crawler/

├── core/
│   ├── crawler.py
│   ├── scraper.py
│   ├── rules.py
│   ├── cti.py
│   ├── alerts.py
│   ├── hash_checker.py
│   ├── tor_manager.py
│   ├── user_agent.py
│   └── tor_test.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── results.json
│   ├── visited.json
│   ├── alerts.json
│   └── hashes.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── onions.txt
└── README.md

```


---

# Installation


## Prérequis


Système recommandé :

- Linux (Ubuntu/Debian)
- Python 3.10+
- Tor
- Docker (optionnel)


---

# 1. Installation de Tor


Installation :

```bash
sudo apt update

sudo apt install tor
```


Démarrage :

```bash
sudo systemctl start tor
```


Vérification :

```bash
systemctl status tor
```


Tor doit écouter sur :

```
127.0.0.1:9050
```


---

# 2. Installation du projet


Cloner le dépôt :

```bash
git clone https://github.com/USER/Tor-Crawler.git
```


Entrer dans le dossier :

```bash
cd Tor-Crawler
```


---

# 3. Installation Python


Créer un environnement virtuel :

```bash
python3 -m venv venv
```


Activation :

Linux :

```bash
source venv/bin/activate
```


Installer les dépendances :

```bash
pip install -r requirements.txt
```


---

# Configuration


## Liste des sites à analyser


Modifier :

```
onions.txt
```


Exemple :

```
http://exampleonionxxxxx.onion
http://autresite.onion
```


---

# Utilisation complète


## Étape 1 : Tester Tor


Commande :

```bash
python3 core/tor_test.py
```


Résultat attendu :

```
[+] Testing Tor IP...

XXX.XXX.XXX.XXX
```


---

# Étape 2 : Tester le scraper


Commande :

```bash
python3 core/scraper.py
```


Entrer une URL :

```
http://adresse.onion
```


Le programme affiche :

- code HTTP
- aperçu HTML
- liens trouvés


---

# Étape 3 : Lancer le crawler


Commande :

```bash
python3 core/crawler.py
```


Le crawler :

- visite les URLs
- récupère le contenu
- extrait les liens
- analyse les entités
- calcule le score CTI


Les résultats sont enregistrés dans :

```
data/results.json
```


---

# Étape 4 : Générer les alertes


Commande :

```bash
python3 core/alerts.py
```


Les alertes sont enregistrées :

```
data/alerts.json
```


---

# Étape 5 : Vérifier les résultats


Afficher les résultats :

```bash
cat data/results.json
```


Afficher les alertes :

```bash
cat data/alerts.json
```


---

# Étape 6 : Lancer le Dashboard


Commande :

```bash
streamlit run dashboard/app.py
```


Accès :

```
http://localhost:8501
```


Le dashboard affiche :

- nombre de pages analysées
- entités détectées
- scores
- alertes
- changements détectés


---

# Utilisation avec Docker


## Construire l'image


```bash
docker compose build
```


## Démarrer le service


```bash
docker compose up
```


Dashboard :

```
http://localhost:8501
```


Arrêter :

```bash
docker compose down
```


---

# Tests rapides


## Test complet du pipeline


```bash
python3 core/tor_test.py

python3 core/crawler.py

python3 core/alerts.py

streamlit run dashboard/app.py
```


---

# Vérification Hash


Les empreintes SHA256 sont stockées dans :

```
data/hashes.json
```


Relancer plusieurs fois :

```bash
python3 core/crawler.py
```


Si une page change :

```
content_changed : true
```


---

# GitHub Actions CI/CD


À chaque :

```bash
git push
```


Le pipeline vérifie :

- installation dépendances
- syntax Python
- build Docker


---

# Dépannage


## Erreur SOCKS Tor


Erreur :

```
SOCKS server failure
```


Vérifier Tor :

```bash
sudo systemctl restart tor
```


Tester :

```bash
curl --socks5 127.0.0.1:9050 http://icanhazip.com
```


---

## Dashboard vide


Lancer avant :

```bash
python3 core/crawler.py
```


Vérifier :

```
data/results.json
```


---

# Technologies


## Langage

- Python


## Cyber

- Tor SOCKS5
- BeautifulSoup
- Requests
- Regex


## Data

- JSON
- SHA256


## Dashboard

- Streamlit
- Pandas


## DevOps

- Docker
- Docker Compose
- GitHub Actions


---

# Roadmap


- [x] Scraper Tor
- [x] Crawling .onion
- [x] Analyse CTI
- [x] Dashboard
- [x] Alertes
- [x] Docker
- [x] CI/CD
- [ ] Obsidian Knowledge Base
- [ ] RAG LLM
- [ ] Assistant IA CTI


---

# Auteur

Projet Cyber Threat Intelligence / DevOps Cybersécurité
