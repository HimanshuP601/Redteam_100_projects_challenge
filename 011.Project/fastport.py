import socket
import threading
import sys

TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 1024
TIMEOUT = 0.5

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

def main():
    threads = []

    for port in range(START_PORT, END_PORT + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

