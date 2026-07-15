import json
import hashlib
from datetime import datetime


HASH_FILE = "data/hashes.json"



def load_hashes():

    try:

        with open(HASH_FILE, "r") as f:
            return json.load(f)

    except:

        return {}



def save_hashes(data):

    with open(HASH_FILE, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def generate_hash(content):

    """
    Génération SHA256
    """

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()



def check_page(url, content):


    hashes = load_hashes()


    new_hash = generate_hash(
        content
    )


    result = {

        "url": url,

        "hash": new_hash,

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    }


    # Première fois

    if url not in hashes:

        hashes[url] = result

        save_hashes(
            hashes
        )

        return {
            "changed": False,
            "new": True
        }



    old_hash = hashes[url]["hash"]



    # comparaison

    if old_hash != new_hash:


        hashes[url] = result

        save_hashes(
            hashes
        )


        return {

            "changed": True,

            "old_hash": old_hash,

            "new_hash": new_hash

        }



    return {

        "changed": False,

        "new": False

    }



if __name__ == "__main__":

    test = check_page(
        "http://example.onion",
        "test page"
    )


    print(test)
