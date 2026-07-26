import json
import os
from datetime import datetime


RESULT_FILE = "data/results.json"

OUTPUT_DIR = "data/knowledge"



def load_results():

    try:

        with open(
            RESULT_FILE,
            "r"
        ) as file:

            return json.load(file)

    except Exception:

        return []



def create_folder():

    if not os.path.exists(
        OUTPUT_DIR
    ):

        os.makedirs(
            OUTPUT_DIR
        )



def write_file(
    filename,
    content
):

    path = os.path.join(
        OUTPUT_DIR,
        filename
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            content
        )



def generate_entities(results):

    md = "# Entités détectées\n\n"


    for item in results:


        entities = item.get(
            "entities",
            []
        )


        if entities:


            md += "## Source\n"

            md += item.get(
                "url",
                ""
            )

            md += "\n\n"


            for entity in entities:

                md += (
                    "- "
                    +
                    entity
                    +
                    "\n"
                )


            md += "\n---\n"



    write_file(
        "entities.md",
        md
    )



def generate_alerts(results):


    md = "# Alertes CTI\n\n"



    for item in results:


        score = item.get(
            "score",
            0
        )


        if score > 0:


            md += "## Alerte\n\n"


            md += (
                "URL : "
                +
                item.get(
                    "url",
                    ""
                )
                +
                "\n\n"
            )


            md += (
                "Score : "
                +
                str(score)
                +
                "\n\n"
            )


            md += "Signaux :\n"



            for signal in item.get(
                "signals",
                []
            ):

                md += (
                    "- "
                    +
                    signal
                    +
                    "\n"
                )


            md += "\n---\n"



    write_file(
        "alerts.md",
        md
    )



def generate_report(results):


    md = "# Rapport CTI\n\n"


    md += (
        "Date : "
        +
        str(datetime.now())
        +
        "\n\n"
    )


    md += (
        "Nombre de pages analysées : "
        +
        str(len(results))
        +
        "\n\n"
    )


    write_file(
        "reports.md",
        md
    )



def main():

    create_folder()


    results = load_results()


    generate_entities(
        results
    )


    generate_alerts(
        results
    )


    generate_report(
        results
    )


    print(
        "[+] Knowledge Base generated"
    )



if __name__ == "__main__":

    main()
