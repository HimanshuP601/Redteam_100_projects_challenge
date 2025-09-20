import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Welcome to the chatroom!\n".encode())

    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            print(f"[{addr}] {message.decode().strip()}")
            broadcast(message, conn)
        except:
            break

    print(f"[DISCONNECTED] {addr}")
    conn.close()
    if conn in clients:
        clients.remove(conn)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[TCP SERVER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    main()

