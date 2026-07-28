# 🕷️ Tor-CTI Monitor

## Présentation

Tor-CTI Monitor est un projet universitaire réalisé dans le cadre d'un projet DevOps Cybersécurité.

L'objectif est de développer une plateforme de **Cyber Threat Intelligence (CTI)** permettant d'automatiser la collecte, l'analyse et la visualisation d'informations provenant de sources web accessibles via Tor ou du web classique, afin de détecter des mentions d'entités surveillées et de centraliser les résultats dans une base de connaissances.

Le projet met en œuvre des techniques de :

- Scraping
- Crawling
- Analyse CTI
- Détection d'entités
- Dashboard interactif
- Knowledge Base
- RAG (Retrieval Augmented Generation)
- Docker
- GitHub Actions

---

# Fonctionnalités

## Infrastructure

- Navigation via le proxy Tor (SOCKS5)
- Test automatique de la connexion Tor
- Gestion du User-Agent
- Architecture modulaire

## Collecte

- Scraping de pages HTML
- Crawling automatique
- Découverte de nouveaux liens
- Historique des URLs visitées

## Cyber Threat Intelligence

- Détection d'entités surveillées
- Détection de mots-clés sensibles
- Attribution d'un score de risque
- Génération d'alertes

Exemple d'entités :

- CyberV
- ESIEE Paris
- IUT de Villetaneuse
- Hackuten
- CatTheFlag
- Air France
- OSINT FR

## Intégrité

Chaque page analysée possède un hash SHA256.

Si le contenu évolue :

- le changement est détecté ;
- la page peut être rescannée.

## Dashboard

Dashboard développé avec Streamlit.

Affichage :

- nombre de pages crawlées
- score global
- entités détectées
- alertes
- tableau des résultats
- assistant IA

## Intelligence Artificielle

Le projet génère automatiquement une base de connaissances compatible Obsidian.

Les documents sont ensuite indexés grâce à LlamaIndex afin de permettre des recherches en langage naturel.

Exemples :

> Quelles entités ont été détectées ?

> Résume les dernières alertes.

> Quels sites présentent le risque le plus élevé ?

---

# Architecture

```
Tor-Crawler/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── core/
│   ├── alerts.py
│   ├── crawler.py
│   ├── cti.py
│   ├── dashboard.py
│   ├── data_manager.py
│   ├── hash_checker.py
│   ├── knowledge.py
│   ├── rag.py
│   ├── rules.py
│   ├── scraper.py
│   ├── tor_manager.py
│   ├── tor_test.py
│   ├── url_manager.py
│   └── user_agent.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── alerts.json
│   ├── hashes.json
│   ├── results.json
│   ├── visited.json
│   └── knowledge/
│
├── Dockerfile
├── docker-compose.yml
├── onions.txt
├── requirements.txt
└── README.md
```

---

# Architecture logicielle

```
           +---------------------+
           |      Tor Proxy      |
           +----------+----------+
                      |
                      |
               scraper.py
                      |
                      |
               crawler.py
                      |
                      |
            Analyse CTI (Regex)
                      |
                      |
             Détection d'entités
                      |
                      |
             Calcul du score
                      |
                      |
            Sauvegarde JSON
                      |
          +-----------+-----------+
          |                       |
          |                       |
Knowledge Base            Dashboard
    Obsidian              Streamlit
          |                       |
          +-----------+-----------+
                      |
                 RAG LlamaIndex
```

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/<utilisateur>/Tor-Crawler.git

cd Tor-Crawler
```

---

## 2. Installer Tor

Ubuntu

```bash
sudo apt update

sudo apt install tor
```

---

## 3. Démarrer Tor

```bash
sudo systemctl start tor
```

Vérification

```bash
python3 core/tor_test.py
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 5. Lancer le crawler

```bash
python3 core/crawler.py
```

---

## 6. Générer la base de connaissances

```bash
python3 core/knowledge.py
```

---

## 7. Lancer le dashboard

```bash
streamlit run dashboard/app.py
```

Le tableau de bord est accessible sur :

```
http://localhost:8501
```

---

# Docker

Construction

```bash
docker compose build
```

Exécution

```bash
docker compose up
```

---

# GitHub Actions

Le pipeline CI vérifie automatiquement :

- installation des dépendances
- compilation Python
- tests unitaires

Le workflow est situé dans :

```
.github/workflows/ci.yml
```

---

# Données générées

## results.json

Contient les résultats complets du crawler.

Exemple

```json
{
    "url": "https://example.com",
    "status": 200,
    "score": 30,
    "entities": [
        "Air France"
    ]
}
```

---

## alerts.json

Liste des alertes détectées.

---

## hashes.json

Hash SHA256 de chaque page analysée.

---

## visited.json

Historique des URLs visitées.

---

# Dashboard

Le dashboard affiche :

- Nombre de pages analysées
- Entités détectées
- Score global
- Alertes
- Tableau détaillé
- Assistant IA

---

# Technologies utilisées

## Langages

- Python 3

## Scraping

- Requests
- BeautifulSoup

## Dashboard

- Streamlit

## Data

- JSON

## IA

- LlamaIndex

## Documentation

- Obsidian

## DevOps

- Docker
- Docker Compose
- GitHub Actions

---

# Perspectives

Le projet peut être amélioré avec :

- Base PostgreSQL
- Elasticsearch
- RabbitMQ
- API REST
- Authentification
- Déploiement Kubernetes
- Détection par modèles NLP
- Supervision Prometheus/Grafana

---

# Auteur

Projet réalisé dans le cadre d'un projet universitaire DevOps Cybersécurité.

Année universitaire : 2025-2026.
