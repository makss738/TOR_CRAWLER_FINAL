import requests

PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

def test_tor():
    print("[+] Testing Tor connection...")

    try:
        r = requests.get(
            "http://icanhazip.com",
            proxies=PROXIES,
            timeout=20
        )

        print("[+] Tor OK")
        print("[+] Exit IP:", r.text.strip())

    except Exception as e:
        print("[-] Tor ERROR:", e)


if __name__ == "__main__":
    test_tor()

