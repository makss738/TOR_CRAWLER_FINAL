import hashlib
import json
import os


HASH_FILE = "data/hashes.json"



def load_hashes():

    if not os.path.exists(HASH_FILE):

        return {}

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



def calculate_hash(content):

    """
    Génère un hash SHA256 du contenu HTML
    """

    return hashlib.sha256(

        content.encode(
            "utf-8",
            errors="ignore"
        )

    ).hexdigest()



def check_change(url, content):

    hashes = load_hashes()


    new_hash = calculate_hash(
        content
    )


    old_hash = hashes.get(
        url
    )


    changed = False


    if old_hash:

        if old_hash != new_hash:

            changed = True



    hashes[url] = new_hash


    save_hashes(
        hashes
    )


    return {

        "hash": new_hash,

        "changed": changed

    }
