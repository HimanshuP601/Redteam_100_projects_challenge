import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    while True:
        try:
            data, _ = client.recvfrom(1024)
            print(f"[MESSAGE] {rot13(data.decode())}")  
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

# Send messages
while True:
    msg = input()
    client.sendto(rot13(msg).encode(), (HOST, PORT))  
