import hashlib
import json
import os


HASH_FILE="data/hashes.json"



def load_hashes():

    if not os.path.exists(HASH_FILE):

        return {}


    with open(HASH_FILE,"r") as f:

        return json.load(f)



def save_hashes(data):

    with open(HASH_FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def generate_hash(content):

    return hashlib.sha256(

        content.encode(
            "utf-8",
            errors="ignore"
        )

    ).hexdigest()



def check_page(url,content):


    hashes = load_hashes()


    new_hash = generate_hash(
        content
    )


    old_hash = hashes.get(
        url
    )


    changed=False


    if old_hash:

        if old_hash != new_hash:

            changed=True



    hashes[url]=new_hash


    save_hashes(
        hashes
    )


    return {

        "hash":new_hash,

        "changed":changed

    }
