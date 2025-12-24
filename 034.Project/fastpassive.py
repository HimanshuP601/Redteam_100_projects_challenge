import requests
from urllib.parse import urljoin, urlparse

# ===== CONFIG =====
TARGET = "http://127.0.0.1:8081"
TIMEOUT = 8
# ==================

SEC_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def scan_headers(r):
    print("[+] Security Headers")
    for h in SEC_HEADERS:
        if h in r.headers:
            print(f"  [OK] {h}: {r.headers.get(h)}")
        else:
            print(f"  [MISS] {h}")


def scan_server_banner(r):
    print("\n[+] Server / Banner Disclosure")
    server = r.headers.get("Server")
    powered = r.headers.get("X-Powered-By")
    print(f"  Server: {server if server else 'Not disclosed'}")
    print(f"  X-Powered-By: {powered if powered else 'Not disclosed'}")


def scan_cookies(r):
    print("\n[+] Cookies")
    cookies = r.cookies
    if not cookies:
        print("  No cookies set")
        return
    for c in cookies:
        flags = []
        if c.secure:
            flags.append("Secure")
        if c.has_nonstandard_attr("HttpOnly") or c._rest.get("HttpOnly"):
            flags.append("HttpOnly")
        samesite = c._rest.get("SameSite")
        if samesite:
            flags.append(f"SameSite={samesite}")
        print(f"  {c.name}: {'; '.join(flags) if flags else 'No flags'}")


def scan_robots(base):
    print("\n[+] robots.txt")
    robots = urljoin(base, "/robots.txt")
    try:
        rr = requests.get(robots, timeout=TIMEOUT)
        if rr.status_code == 200:
            print("  Present")
        else:
            print("  Not present")
    except:
        print("  Error checking robots.txt")


def scan_html_hints(r):
    print("\n[+] HTML Hints (read-only)")
    text = r.text.lower()
    if "<form" in text:
        print("  Forms detected")
    if "<!--" in text:
        print("  HTML comments detected")


def main():
    print(f"[+] Passive scan for {TARGET}\n")
    try:
        r = requests.get(TARGET, timeout=TIMEOUT, allow_redirects=True)
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    print(f"[+] Final URL: {r.url}")
    print(f"[+] Status: {r.status_code}")
    print(f"[+] Scheme: {urlparse(r.url).scheme}")

    scan_headers(r)
    scan_server_banner(r)
    scan_cookies(r)
    scan_robots(r.url)
    scan_html_hints(r)


if __name__ == "__main__":
    main()
