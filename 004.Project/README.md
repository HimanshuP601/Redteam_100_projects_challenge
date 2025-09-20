
# TCP File Transfer Project

This project demonstrates sending and receiving files over TCP using Python.

---

## **TCP File Transfer Client (`client.py`)**

### **Description**
- Connects to a TCP server on a specified host and port.
- Sends a file specified by the user to the server.
- Sends file metadata (filename and size) before transferring the file content.
- Prints connection status and transfer progress.

### **Code**
```python
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
```

## **TCP File Transfer Server (`server.py`)**

### **Description**
- Listens for incoming TCP connections on a specified host and port.
- Receives file metadata (filename and size) from the client.
- Receives the file data in chunks and saves it to disk.
- Prints connection and transfer status.

### **Code**
```python
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

    with open(filename , 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
    print(f"[DONE] Received {filename} ({filesize} bytes)")
    s.close()
```

### **Run the Server**
```bash
python3 server.py
```

### **Run the Client**
```bash
python3 client.py
```

### **Usage**
1. Start the server first in a terminal.
2. Run the client and enter the path to the file to send.
3. The server receives and saves the file with the same name.

---

## **Notes**
- Files are sent in chunks (4096 bytes) for efficient transfer.
- The client sends file metadata first to allow the server to prepare for receiving.
- Ensure the server is running and port `5000` is free before starting the client.
