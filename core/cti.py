from bs4 import BeautifulSoup
import re

ENTITIES = [
    "Air France",
    "ESIEE",
    "ESIEE Paris",
    "Hackuten",
    "OSINT FR",
    "CatTheFlag",
    "IUT Villetaneuse",
    "CyberV",
    "ANSSI"
]


def extract_text(html):
    """
    Nettoie le HTML → texte exploitable CTI
    """

    soup = BeautifulSoup(html, "html.parser")

    # suppression scripts/styles
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text(separator=" ")

    # nettoyage espaces
    text = re.sub(r"\s+", " ", text)

    return text


def detect_entities(text):
    found = []

    if not text:
        return found

    for entity in ENTITIES:
        if re.search(rf"\b{re.escape(entity)}\b", text, re.IGNORECASE):
            found.append(entity)

    return found


def compute_score(entities):
    return len(entities) * 10

