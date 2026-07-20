import json
import os
from datetime import datetime


RESULT_FILE = "data/results.json"

KNOWLEDGE_DIR = "data/knowledge"



def load_results():

    try:

        with open(
            RESULT_FILE,
            "r"
        ) as f:

            return json.load(f)


    except Exception:

        return []



def create_directory():

    if not os.path.exists(KNOWLEDGE_DIR):

        os.makedirs(
            KNOWLEDGE_DIR
        )



def generate_entity_report(results):


    path = os.path.join(
        KNOWLEDGE_DIR,
        "entities.md"
    )


    with open(
        path,
        "w"
    ) as f:


        f.write(
            "# CTI Entities Report\n\n"
        )


        for item in results:


            if item.get("entities"):


                f.write(
                    "## URL\n"
                )

                f.write(
                    item["url"] + "\n\n"
                )


                f.write(
                    "### Entities détectées\n"
                )


                for entity in item["entities"]:

                    f.write(
                        "- " + entity + "\n"
                    )


                f.write("\n---\n")



def generate_threat_report(results):


    path = os.path.join(
        KNOWLEDGE_DIR,
        "threats.md"
    )


    with open(
        path,
        "w"
    ) as f:


        f.write(
            "# Threat Intelligence Report\n\n"
        )


        for item in results:


            if item.get("score",0) > 0:


                f.write(
                    "## Alerte\n\n"
                )


                f.write(
                    "URL : "
                    +
                    item["url"]
                    +
                    "\n\n"
                )


                f.write(
                    "Score : "
                    +
                    str(item["score"])
                    +
                    "\n\n"
                )


                f.write(
                    "Signaux :\n"
                )


                for signal in item.get(
                    "signals",
                    []
                ):

                    f.write(
                        "- "
                        +
                        signal
                        +
                        "\n"
                    )


                f.write("\n---\n")



def generate_daily_report(results):


    path = os.path.join(
        KNOWLEDGE_DIR,
        "reports.md"
    )


    with open(
        path,
        "w"
    ) as f:


        f.write(
            "# CTI Daily Report\n\n"
        )


        f.write(
            "Date : "
        )


        f.write(
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )


        f.write(
            "\n\n"
        )


        f.write(
            "Nombre de pages analysées : "
        )


        f.write(
            str(len(results))
        )



def main():


    create_directory()


    results = load_results()


    generate_entity_report(
        results
    )


    generate_threat_report(
        results
    )


    generate_daily_report(
        results
    )


    print(
        "[+] Obsidian knowledge base generated"
    )



if __name__ == "__main__":

    main()
