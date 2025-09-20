import socket
import os
HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST , PORT))
    s.listen(1)
    print(f"[LISTENING] Server running on {HOST}:{PORT}")

    conn , addr = s.accept()
    print(f"[CONNECTED] Connection form {addr}")

    file_info = b""
    while b"|" not in file_info:
        part = conn.recv(1024)
        if not part:
            break
        file_info += part

    filename, filesize = file_info.decode().split('|')
    filename = os.path.basename(filename)
    filesize = int(filesize)


    with open (filename , 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
    print(f"[DON] Received {filename} ({filesize} bytes)")
    s.close()
