import json
import os
from datetime import datetime

RESULTS_FILE = "data/results.json"
KNOWLEDGE_DIR = "data/knowledge"


def load_results():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def ensure_directory():
    os.makedirs(KNOWLEDGE_DIR, exist_ok=True)


def write_entities(results):
    path = os.path.join(KNOWLEDGE_DIR, "entities.md")

    entities = {}

    for item in results:
        for entity in item.get("entities", []):
            entities.setdefault(entity, []).append(item["url"])

    with open(path, "w", encoding="utf-8") as f:
        f.write("# Entités détectées\n\n")

        if not entities:
            f.write("Aucune entité détectée.\n")
            return

        for entity in sorted(entities):
            f.write(f"## {entity}\n\n")
            for url in entities[entity]:
                f.write(f"- {url}\n")
            f.write("\n")


def write_threats(results):
    path = os.path.join(KNOWLEDGE_DIR, "threats.md")

    with open(path, "w", encoding="utf-8") as f:

        f.write("# Menaces détectées\n\n")

        for item in results:

            if item.get("score", 0) == 0:
                continue

            f.write(f"## {item['url']}\n\n")
            f.write(f"Score : **{item['score']}**\n\n")

            signals = item.get("signals", [])

            if signals:
                f.write("Signaux :\n")
                for signal in signals:
                    f.write(f"- {signal}\n")

            f.write("\n---\n\n")


def write_urls(results):

    path = os.path.join(KNOWLEDGE_DIR, "urls.md")

    with open(path, "w", encoding="utf-8") as f:

        f.write("# URLs analysées\n\n")

        for item in results:

            f.write(f"- {item['url']}\n")


def write_report(results):

    path = os.path.join(KNOWLEDGE_DIR, "reports.md")

    with open(path, "w", encoding="utf-8") as f:

        f.write("# Rapport CTI\n\n")

        f.write(
            f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        f.write(f"Nombre de pages : {len(results)}\n\n")

        total_alerts = len(
            [r for r in results if r.get("score", 0) > 0]
        )

        f.write(f"Nombre d'alertes : {total_alerts}\n")


def main():

    ensure_directory()

    results = load_results()

    write_entities(results)
    write_threats(results)
    write_urls(results)
    write_report(results)

    print("[+] Knowledge Base générée")


if __name__ == "__main__":
    main()
