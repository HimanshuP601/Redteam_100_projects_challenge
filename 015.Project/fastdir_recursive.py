import requests
import threading
import queue

TARGET = "http://127.0.0.1"
WORDLIST = "wordlist.txt"
THREADS = 10
TIMEOUT = 3
MAX_DEPTH = 2

q = queue.Queue()
visited = set()
lock = threading.Lock()

def worker():
    while True:
        try:
            base_path, depth = q.get(timeout=1)
        except:
            return

        if depth > MAX_DEPTH:
            q.task_done()
            continue

        with open(WORDLIST, "r") as f:
            for line in f:
                path = line.strip()
                full_path = f"{base_path}/{path}".replace("//", "/")
                url = f"{TARGET}{full_path}"

                with lock:
                    if url in visited:
                        continue
                    visited.add(url)

                try:
                    r = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 403]:
                        print(f"[FOUND] {url} ({r.status_code})")

                        # Peer recursion: queue discovered directories
                        if r.status_code in [200, 301, 302]:
                            q.put((full_path, depth + 1))
                except:
                    pass

        q.task_done()

def main():
    q.put(("", 0))

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

if __name__ == "__main__":
    main()
