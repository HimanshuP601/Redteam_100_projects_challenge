import os
import socket

HOST = '127.0.0.1'
PORT = 5000

file_path = input("Enter file path:")
filesize = os.path.getsize(file_path)

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST , PORT))
    print(f"[CONNECTED] Connected to {HOST}:{PORT})")

    s.send(f"{os.path.basename(file_path)}|{filesize}".encode())

    with open(file_path , 'rb') as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    print(f"[DONE] Sent {file_path} ({filesize} bytes)")
    s.close()

