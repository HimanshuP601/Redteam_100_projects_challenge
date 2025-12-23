import requests
import time
import urllib.parse
from bs4 import BeautifulSoup

# ===== CONFIG =====
TARGET = "example.com"
DELAY = 5     # seconds between requests (important)
USER_AGENT = "Mozilla/5.0 (ReconBot)"
# ==================

HEADERS = {
    "User-Agent": USER_AGENT
}

def search_google(query):
    encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded}&num=10"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return []

        soup = BeautifulSoup(r.text, "html.parser")
        links = []

        for a in soup.select("a"):
            href = a.get("href", "")
            if href.startswith("/url?q="):
                clean = href.split("/url?q=")[1].split("&")[0]
                links.append(clean)

        return links

    except:
        return []

def main():
    print(f"[+] Google Recon Bot for target: {TARGET}\n")

    with open("dorks.txt") as f:
        for line in f:
            dork = line.strip()
            if not dork:
                continue

            query = dork.replace("{target}", TARGET)
            print(f"[DORK] {query}")

            results = search_google(query)
            for link in results:
                print(f"  -> {link}")

            print()
            time.sleep(DELAY)

if __name__ == "__main__":
    main()
