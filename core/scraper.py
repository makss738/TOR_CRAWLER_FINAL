import requests

PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}


def fetch_page(url):
    """
    Fetch Tor page avec gestion d'erreur robuste
    """

    try:
        r = requests.get(
            url,
            proxies=PROXIES,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0 (CTI-Crawler)"}
        )

        return {
            "url": url,
            "status": r.status_code,
            "html": r.text
        }

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "error": "network_error",
            "detail": str(e)
        }


def extract_links(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if href.startswith("http"):
            links.append(href)

    return list(set(links))
