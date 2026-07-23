import json

from scraper import fetch_page, extract_links

from url_manager import (
    add_url,
    get_next_url,
    mark_visited,
    can_continue
)

from hash_checker import check_page

from cti import analyze_text



RESULT_FILE="data/results.json"



def load_results():

    try:

        with open(
            RESULT_FILE
        ) as f:

            return json.load(f)

    except:

        return []



def save_results(data):

    with open(
        RESULT_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )



def crawl():


    results=load_results()


    print(
        "[+] Starting CTI crawler"
    )


    while can_continue():


        url=get_next_url()


        if not url:

            print(
                "[+] Queue empty"
            )

            break



        print(
            "[+] Crawling:",
            url
        )


        page=fetch_page(
            url
        )


        html=page["html"]


        if not html:

            continue



        hash_info=check_page(

            url,

            html

        )


        links=extract_links(
            html
        )


        for link in links:

            add_url(
                link
            )



        cti=analyze_text(
            html
        )



        result={

            "url":url,

            "status":
                page["status"],

            "hash":
                hash_info["hash"],

            "changed":
                hash_info["changed"],

            "entities":
                cti["entities"],

            "signals":
                cti["signals"],

            "score":
                cti["score"],

            "links_found":
                len(links)

        }


        results.append(
            result
        )


        mark_visited(
            url
        )


        save_results(
            results
        )



    print(
        "[+] Crawl finished"
    )

    print(
        "[+] Pages:",
        len(results)
    )



if __name__=="__main__":


    start=input(
        "URL de départ : "
    )


    add_url(
        start
    )


    crawl()

