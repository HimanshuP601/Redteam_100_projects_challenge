import socket
import threading
import subprocess
import sys
import re

TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 1024
TIMEOUT = 0.5

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def fingerprint_os():
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", TARGET],
            stderr=subprocess.DEVNULL,
            text=True
        )

        match = re.search(r"ttl=(\d+)", output, re.IGNORECASE)
        if not match:
            return "Unknown"

        ttl = int(match.group(1))

        if ttl <= 64:
            return f"Linux / Unix (TTL={ttl})"
        elif ttl <= 128:
            return f"Windows (TTL={ttl})"
        elif ttl <= 255:
            return f"Network Device / Cisco / BSD (TTL={ttl})"
        else:
            return f"Unknown (TTL={ttl})"

    except:
        return "Fingerprinting failed"

def main():
    threads = []

    print(f"[+] Scanning target: {TARGET}")

    for port in range(START_PORT, END_PORT + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Open Ports:")
    for port in open_ports:
        print(f"    {port}")

    print("\n[+] OS Fingerprint:")
    print(f"    {fingerprint_os()}")

if __name__ == "__main__":
    main()

