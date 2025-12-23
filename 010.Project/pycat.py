import socket
import sys
import threading

def recv_loop(sock):
    while True:
        data = sock.recv(4096)
        if not data:
            break
        print(data.decode(), end="")

def client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    t = threading.Thread(target=recv_loop, args=(s,))
    t.daemon = True
    t.start()

    while True:
        cmd = input()
        s.sendall(cmd.encode() + b"\n")

if __name__ == "__main__":
    client("127.0.0.1", 4444)
