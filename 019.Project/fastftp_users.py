import socket

# ===== CONFIG =====
FTP_HOST = "127.0.0.1"
FTP_PORT = 21
TIMEOUT = 5
# ==================

def check_user(username):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        s.connect((FTP_HOST, FTP_PORT))

        banner = s.recv(1024).decode(errors="ignore")

        s.sendall(f"USER {username}\r\n".encode())
        response = s.recv(1024).decode(errors="ignore")

        s.close()

        if response.startswith("331"):
            return "VALID USER (password required)"
        elif response.startswith("230"):
            return "VALID USER (logged in)"
        elif response.startswith("530"):
            return "INVALID or RESTRICTED"
        else:
            return f"UNKNOWN RESPONSE: {response.strip()}"

    except Exception as e:
        return f"ERROR: {e}"

def main():
    print(f"[+] FTP User Footprinting on {FTP_HOST}:{FTP_PORT}\n")

    with open("users.txt") as f:
        for user in f:
            user = user.strip()
            if not user:
                continue
            result = check_user(user)
            print(f"{user}: {result}")

if __name__ == "__main__":
    main()
