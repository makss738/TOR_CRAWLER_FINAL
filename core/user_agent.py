import random



USER_AGENTS = [

"Mozilla/5.0 (Windows NT 10.0; Win64; x64)",

"Mozilla/5.0 (X11; Linux x86_64)",

"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",

"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"

]



def get_random_agent():

    return random.choice(
        USER_AGENTS
    )



def get_headers():

    return {

        "User-Agent":
            get_random_agent(),

        "Accept":
            "text/html,application/xhtml+xml"

    }



if __name__=="__main__":

    print(
        get_headers()
    )
