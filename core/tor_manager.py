from stem import Signal
from stem.control import Controller
import requests


TOR_CONTROL_PORT = 9051
TOR_SOCKS_PORT = 9050



def renew_identity():

    """
    Demande un nouveau circuit Tor
    """

    try:

        with Controller.from_port(
            port=TOR_CONTROL_PORT
        ) as controller:


            controller.authenticate()


            controller.signal(
                Signal.NEWNYM
            )


        print(
            "[TOR] New identity requested"
        )


    except Exception as e:

        print(
            "[TOR ERROR]",
            e
        )



def get_current_ip():

    proxies = {

        "http":
        "socks5h://127.0.0.1:9050",

        "https":
        "socks5h://127.0.0.1:9050"

    }


    try:

        r=requests.get(

            "https://icanhazip.com",

            proxies=proxies,

            timeout=30

        )


        return r.text.strip()


    except Exception as e:

        return str(e)



if __name__=="__main__":


    print(
        "Current IP:"
    )

    print(
        get_current_ip()
    )


    renew_identity()


    print(
        "New IP:"
    )

    print(
        get_current_ip()
    )
