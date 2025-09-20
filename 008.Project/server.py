import socket

HOST = "0.0.0.0"
PORT = 5000
clients = []


def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"[LISTENING] UDP server running on {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    message = data.decode()
    
    if addr not in clients:
        clients.append(addr)
        print(f"[NEW CLIENT] {addr} joined")
    
    decrypted = rot13(message)
    print(f"[FROM {addr}] {decrypted}")
    
    
    for client_addr in clients:
        if client_addr != addr:
            server.sendto(message.encode(), client_addr)
