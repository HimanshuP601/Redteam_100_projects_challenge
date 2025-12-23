import requests
import threading
import queue

TARGET = "http://127.0.0.1"
WORDLIST = "wordlist.txt"
THREADS = 10
TIMEOUT = 3

q = queue.Queue()

def worker():
    while not q.empty():
        path = q.get()
        url = f"{TARGET}/{path}"
        try:
            r = requests.get(url, timeout=TIMEOUT)
            if r.status_code in [200, 301, 302, 403]:
                print(f"[FOUND] {url} ({r.status_code})")
        except:
            pass
        q.task_done()

def main():
    with open(WORDLIST, "r") as f:
        for line in f:
            q.put(line.strip())

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

if __name__ == "__main__":
    main()

