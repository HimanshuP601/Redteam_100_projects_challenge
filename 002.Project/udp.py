import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
clients = []
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s :
    s.bind((HOST , PORT))
    print(f"Server is running on {HOST}:{PORT}")

    while True:
        data , addr = s.recvfrom(1024)
        msg = data.decode().strip()

        if addr not in clients:
            clients.append(addr)
            print(f"[NEW CLIENT] {addr} joined the chat")
        print(f"[{addr}]: {msg}")
        for client in clients:
            if client != addr:
                s.sendto(f"{addr}: {msg}\n".encode() , client)

