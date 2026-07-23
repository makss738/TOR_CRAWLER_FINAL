import json
import os


QUEUE_FILE = "data/queue.json"

VISITED_FILE = "data/visited.json"


MAX_URL = 200



def load_file(path):

    if not os.path.exists(path):

        return []


    with open(path,"r") as f:

        return json.load(f)



def save_file(path,data):

    with open(path,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def add_url(url):

    queue = load_file(
        QUEUE_FILE
    )


    visited = load_file(
        VISITED_FILE
    )


    if url not in queue and url not in visited:

        queue.append(url)


    save_file(
        QUEUE_FILE,
        queue
    )



def get_next_url():

    queue = load_file(
        QUEUE_FILE
    )


    if not queue:

        return None


    return queue.pop(0)



def mark_visited(url):

    visited = load_file(
        VISITED_FILE
    )


    if url not in visited:

        visited.append(url)


    save_file(
        VISITED_FILE,
        visited
    )



def can_continue():

    visited = load_file(
        VISITED_FILE
    )


    return len(visited) < MAX_URL
