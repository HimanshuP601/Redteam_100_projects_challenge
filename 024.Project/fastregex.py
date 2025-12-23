import requests
import re

# ===== CONFIG =====
TARGET_URL = "http://example.com"
TIMEOUT = 5
# ==================

def fetch_page(url):
    r = requests.get(url, timeout=TIMEOUT)
    return r.text

def extract_links(html):
    # Extract href values
    pattern = r'href=["\'](.*?)["\']'
    return re.findall(pattern, html, re.IGNORECASE)

def extract_titles(html):
    pattern = r'<title>(.*?)</title>'
    return re.findall(pattern, html, re.IGNORECASE | re.DOTALL)

def extract_emails(html):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, html)

def main():
    print(f"[+] Fetching: {TARGET_URL}\n")

    html = fetch_page(TARGET_URL)

    links = extract_links(html)
    titles = extract_titles(html)
    emails = extract_emails(html)

    print("[+] Titles:")
    for t in titles:
        print(f"  {t.strip()}")

    print("\n[+] Links:")
    for l in links:
        print(f"  {l}")

    print("\n[+] Emails:")
    for e in emails:
        print(f"  {e}")

if __name__ == "__main__":
    main()
