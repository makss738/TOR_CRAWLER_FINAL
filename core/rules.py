import re

# 🎯 Entités surveillées (obligatoire consigne)
ENTITIES = [
    "CyberV",
    "ESIEE Paris",
    "ESIEE",
    "IUT de Villetaneuse",
    "Hackuten",
    "CatTheFlag",
    "Air France",
    "OSINT FR"
]

# 🚨 patterns à risque (le vrai CTI)
RISK_PATTERNS = {
    "leak": r"(leak|database leak|leaked|dump|credentials)",
    "breach": r"(breach|compromised|hacked|intrusion)",
    "sale": r"(sell|for sale|buy|marketplace)",
    "credentials": r"(password|login|credential|token|apikey)"
}


def detect_entities(text):
    found = []

    if not text:
        return found

    for entity in ENTITIES:
        if re.search(rf"\b{re.escape(entity)}\b", text, re.IGNORECASE):
            found.append(entity)

    return found


def detect_risk_signals(text):
    """
    Détecte les signaux de menace (CTI réel)
    """
    signals = []

    if not text:
        return signals

    for label, pattern in RISK_PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            signals.append(label)

    return signals


def compute_score(entities, signals):
    """
    Score CTI avancé (niveau SOC)
    """
    score = 0

    # poids entités
    score += len(entities) * 10

    # poids signaux critiques
    score += len(signals) * 15

    return score


def classify_level(score):
    """
    classification SOC
    """
    if score >= 30:
        return "CRITICAL"
    elif score >= 15:
        return "HIGH"
    elif score > 0:
        return "MEDIUM"
    return "LOW"
