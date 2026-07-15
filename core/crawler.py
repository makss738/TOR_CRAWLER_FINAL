import json

from scraper import fetch_page, extract_links

from rules import (
    detect_entities,
    detect_risk_signals,
    compute_score,
    classify_level
)

from hash_checker import check_change



MAX_PAGES = 50


visited = set()

queue = []



def load_seeds(file="onions.txt"):

    with open(file,"r") as f:

        for line in f:

            url=line.strip()

            if url:

                queue.append(url)



def is_valid_url(url):

    return ".onion" in url



def save_json(data, filename):

    with open(filename,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def crawl():

    results=[]

    count=0



    while queue and count < MAX_PAGES:


        url = queue.pop(0)



        if url in visited:

            continue



        if not is_valid_url(url):

            continue



        print(
            "[+] Crawling:",
            url
        )


        visited.add(url)



        page = fetch_page(url)



        if "error" in page:


            print(
                "[-] Error:",
                page["detail"]
            )

            continue



        html = page["html"]



        # =========================
        # HASH CHECK
        # =========================

        hash_result = check_change(

            url,

            html

        )



        # =========================
        # CTI ANALYSIS
        # =========================


        entities = detect_entities(
            html
        )


        signals = detect_risk_signals(
            html
        )


        score = compute_score(

            entities,

            signals

        )


        level = classify_level(
            score
        )



        links = extract_links(
            html
        )



        result = {


            "url":

                url,


            "status":

                page["status"],



            "entities":

                entities,



            "signals":

                signals,



            "score":

                score,



            "level":

                level,



            "hash":

                hash_result["hash"],



            "content_changed":

                hash_result["changed"],



            "links_found":

                len(links),



            "links":

                links

        }



        results.append(
            result
        )



        print(
            "[CTI] Entities:",
            entities
        )


        print(
            "[CTI] Signals:",
            signals
        )


        print(
            "[CTI] Score:",
            score
        )


        print(
            "[HASH] Changed:",
            hash_result["changed"]
        )



        for link in links:


            if link not in visited:

                queue.append(link)



        count +=1



    save_json(

        results,

        "data/results.json"

    )


    save_json(

        list(visited),

        "data/visited.json"

    )



    print(
        "[+] Crawl finished"
    )




if __name__=="__main__":

    load_seeds()

    crawl()

