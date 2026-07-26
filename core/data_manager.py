import json
import os
from datetime import datetime


HISTORY_FILE = "data/history.json"



def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []


    with open(HISTORY_FILE, "r") as f:

        return json.load(f)



def save_history(data):

    with open(HISTORY_FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def add_scan(result):


    history = load_history()


    entry = {

        "date":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "url":
            result.get(
                "url"
            ),

        "hash":
            result.get(
                "hash"
            ),

        "changed":
            result.get(
                "changed"
            ),

        "score":
            result.get(
                "score"
            ),

        "entities":
            result.get(
                "entities",
                []
            )

    }


    history.append(
        entry
    )


    save_history(
        history
    )
