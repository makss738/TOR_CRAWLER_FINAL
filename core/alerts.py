import json
from rules import classify_level

ALERT_THRESHOLD = 20


def load_results():
    try:
        with open("data/results.json", "r") as f:
            return json.load(f)
    except:
        return []


def check_alerts(data):
    alerts = []

    for item in data:

        score = item.get("score", 0)
        level = item.get("level", "LOW")

        if score >= ALERT_THRESHOLD or level == "CRITICAL":
            alerts.append({
                "url": item.get("url"),
                "score": score,
                "level": level,
                "entities": item.get("entities", []),
                "signals": item.get("signals", [])
            })

    return alerts


def main():
    data = load_results()

    alerts = check_alerts(data)

    print("\n🚨 CTI ALERT SYSTEM")

    if not alerts:
        print("[-] No threats detected")
        return

    print(f"[!] {len(alerts)} ALERT(S) DETECTED\n")

    for a in alerts:
        print("URL:", a["url"])
        print("Score:", a["score"])
        print("Level:", a["level"])
        print("Entities:", a["entities"])
        print("Signals:", a["signals"])
        print("-" * 50)


if __name__ == "__main__":
    main()
