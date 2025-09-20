import socket
import threading

HOST = '127.0.0.1'
PORT = 5001
SHIFT = 3  # Caesar cipher shift

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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"[CONNECTED] Connected to {HOST}:{PORT}")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            # Decrypt incoming message
            print(f"[MESSAGE] {decrypt(message, SHIFT)}")
        except:
            print("[ERROR] Connection closed")
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input()
    encrypted_msg = encrypt(msg, SHIFT)
    client.send(encrypted_msg.encode())
