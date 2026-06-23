import json
from scraper import fetch_page, extract_links
from cti import extract_text, detect_entities, compute_score

MAX_PAGES = 50

visited = set()
queue = []


def load_seeds(file="onions.txt"):
    with open(file, "r") as f:
        for line in f:
            url = line.strip()
            if url:
                queue.append(url)


def is_valid_url(url):
    return ".onion" in url


def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def crawl():
    results = []
    count = 0

    while queue and count < MAX_PAGES:

        url = queue.pop(0)

        if url in visited:
            continue

        if not is_valid_url(url):
            continue

        print(f"[+] Crawling: {url}")
        visited.add(url)

        data = fetch_page(url)
      
        # 🔥 GESTION ERREUR PROPRE
        if "error" in data:
            print(f"[-] Skipped ({data['error']}): {url}")
            continue

        html = data["html"]

        # CTI PIPELINE
        text = extract_text(html)
        entities = detect_entities(text)
        score = compute_score(entities)

        links = extract_links(html)

        results.append({
            "url": url,
            "status": data["status"],
            "entities": entities,
            "score": score,
            "links_found": len(links),
            "links": links
        })

        print(f"[CTI] Entities: {entities}")
        print(f"[CTI] Score: {score}")

        # queue links
        for link in links:
            if link not in visited:
                queue.append(link)

        count += 1

    save_json(results, "data/results.json")
    save_json(list(visited), "data/visited.json")

    print("[+] Crawl finished")


if __name__ == "__main__":
    load_seeds()
    crawl()


