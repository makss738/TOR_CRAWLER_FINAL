import re


# ==========================
# Entités surveillées
# ==========================

ENTITIES = {

    "CyberV": [
        "cyberv",
        "cyber v"
    ],

    "ESIEE Paris": [
        "esiee",
        "esiee paris"
    ],

    "IUT de Villetaneuse": [
        "iut villetaneuse",
        "villetaneuse"
    ],

    "Hackuten": [
        "hackuten"
    ],

    "CatTheFlag": [
        "cattheflag",
        "ctf"
    ],

    "Air France": [
        "air france",
        "airfrance"
    ],

    "OSINT FR": [
        "osint fr",
        "osintfr"
    ]
}


# ==========================
# Signaux de menace
# ==========================

RISK_WORDS = {

    "leak": 20,

    "database": 15,

    "password": 20,

    "credentials": 25,

    "dump": 20,

    "ransomware": 30,

    "breach": 25,

    "stolen": 20

}



def detect_entities(text):

    """
    Recherche des organisations surveillées
    """

    found = []


    text = text.lower()


    for entity, keywords in ENTITIES.items():

        for word in keywords:

            if word.lower() in text:

                found.append(entity)

                break


    return list(set(found))



def detect_risk_signals(text):

    """
    Détection de mots liés aux menaces
    """

    signals = []


    text = text.lower()


    for word in RISK_WORDS:

        if word in text:

            signals.append(word)


    return signals



def compute_score(
        entities,
        signals
):

    score = 0


    # présence entité

    score += len(entities) * 10


    # signaux

    for signal in signals:

        score += RISK_WORDS.get(
            signal,
            0
        )


    return score



def classify_level(score):


    if score >= 50:

        return "CRITICAL"


    elif score >= 30:

        return "HIGH"


    elif score >= 10:

        return "MEDIUM"


    else:

        return "LOW"
