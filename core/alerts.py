import json
from datetime import datetime


ALERT_THRESHOLD = 20


def load_results():

    try:
        with open("data/results.json", "r") as f:
            return json.load(f)

    except Exception:
        return []



def generate_alerts(results):

    alerts = []


    for item in results:

        score = item.get("score", 0)

        level = item.get(
            "level",
            "LOW"
        )


        if score >= ALERT_THRESHOLD:


            alert = {

                "timestamp":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "url":
                    item.get(
                        "url"
                    ),

                "severity":
                    level,

                "score":
                    score,

                "entities":
                    item.get(
                        "entities",
                        []
                    ),

                "signals":
                    item.get(
                        "signals",
                        []
                    )
            }


            alerts.append(alert)


    return alerts



def save_alerts(alerts):

    with open(
        "data/alerts.json",
        "w"
    ) as f:

        json.dump(
            alerts,
            f,
            indent=4
        )



def main():

    results = load_results()


    alerts = generate_alerts(
        results
    )


    save_alerts(
        alerts
    )


    print(
        "[+] Alert system finished"
    )


    print(
        f"[+] Alerts detected : {len(alerts)}"
    )



if __name__ == "__main__":
    main()
