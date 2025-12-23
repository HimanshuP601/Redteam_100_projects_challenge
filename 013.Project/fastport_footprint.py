import socket
import threading

TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 1024
TIMEOUT = 0.5

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    6379: "Redis",
    6667: "IRC",
    8080: "HTTP-ALT"
}

results = []

def identify_service(port, banner):
    if port in COMMON_SERVICES:
        return COMMON_SERVICES[port]

    banner = banner.lower()

    if "http" in banner:
        return "HTTP"
    if "ftp" in banner:
        return "FTP"
    if "ssh" in banner:
        return "SSH"
    if "smtp" in banner:
        return "SMTP"
    if "irc" in banner:
        return "IRC"

    return "Unknown"

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((TARGET, port))

        if result == 0:
            try:
                s.sendall(b"\r\n")
                banner = s.recv(1024).decode(errors="ignore")
            except:
                banner = ""

            service = identify_service(port, banner)
            results.append((port, service))

        s.close()
    except:
        pass

def main():
    threads = []

    print(f"[+] Scanning {TARGET}")

    for port in range(START_PORT, END_PORT + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Open Ports and Services:")
    for port, service in sorted(results):
        print(f"    {port}/tcp -> {service}")

if __name__ == "__main__":
    main()

