import requests
from bs4 import BeautifulSoup
from user_agent import get_headers

# Configuration du proxy Tor
proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}


def fetch_page(url):
    """
    Télécharge une page via le proxy Tor.
    Retourne un dictionnaire contenant le statut HTTP, le HTML
    et la liste des liens trouvés.
    """

    try:

        r = requests.get(
            url,
            proxies=proxies,
            headers=get_headers(),
            timeout=30
        )

        soup = BeautifulSoup(r.text, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):

            href = a["href"].strip()

            if href.startswith("http") or href.startswith("https") or href.startswith("http://") or href.startswith("https://"):
                links.append(href)

            elif href.startswith("/"):
                links.append(url.rstrip("/") + href)

        return {
            "status": r.status_code,
            "html": r.text,
            "links": list(set(links))
        }

    except Exception as e:

        print(f"[-] Error: {e}")

        return {
            "status": 0,
            "html": "",
            "links": []
        }


def extract_links(html):
    """
    Extrait les liens d'un document HTML.
    """

    soup = BeautifulSoup(html, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):

        href = a["href"].strip()

        if href.startswith("http") or href.startswith("https"):
            links.append(href)

    return list(set(links))


if __name__ == "__main__":

    url = input("Enter URL (normal ou onion): ").strip()

    data = fetch_page(url)

    print("\n[+] STATUS :", data["status"])

    print("\n[+] CONTENT PREVIEW :\n")

    print(data["html"][:1000])

    print("\n[+] LINKS FOUND :", len(data["links"]))

    for link in data["links"][:20]:
        print(link)
