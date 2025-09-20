import socket 
import threading
HOST = '127.0.0.1'
PORT = 5001
SHIFT = 3
clients = []
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT))
    s.listen()
    print(f"[LISTENING] Server running on {HOST}:{PORT}")


    def encrypt(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                result += chr((ord(char) - offset + shift) % 26 + offset)
            else:
                result += char
        return result

    def decrypt(text, shift):
        return encrypt(text, -shift)
    def broadcast(msg , sender):
        for client in clients:
            if client != sender:
                client.send(msg)
    def handle_client(client):
        while True:
            try:
                msg = client.recv(1024).decode()
                if not msg:
                    break
                decrypted = decrypt(msg , SHIFT)
                print(f"[RECEIVED] {decrypted}")
                broadcast(msg.encode() , client)
            except:
                clients.remove(client)
                client.close()
                break
    while True:
        client , addr = s.accept()
        print(f"[CONNECTED] {addr}")
        clients.append(client)
        threading.Thread(target=handle_client , args=(client,) , daemon=True).start()
