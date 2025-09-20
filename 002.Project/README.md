
# Multi-Client UDP Chat Server

This project demonstrates a simple multi-client chat server using UDP in Python.

---

## **UDP Chat Server (`udp.py`)**

### **Description**
- The UDP server listens for incoming datagrams on a specific host and port.
- Supports multiple clients by tracking their addresses.
- Broadcasts messages from one client to all others.
- Prints new client joins and received messages in the server terminal.

### **Code**
```python
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
clients = []

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
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
                s.sendto(f"{addr}: {msg}\n".encode(), client)
```

### **Run the UDP Server**
```bash
python3 udp.py
```

### **Test the Server**
1. Start the server in one terminal:
```bash
python3 udp.py
```
2. Connect multiple clients using `nc` (Netcat) in separate terminals with the `-u` flag for UDP:
```bash
nc -u 127.0.0.1 5000
```
3. Type messages and see them broadcasted to all connected clients.
4. Disconnect a client by pressing `Ctrl+C` or closing the terminal. The server handles new client joins dynamically.

---

## **Notes**
- UDP is connectionless, so clients are tracked manually by their address.
- Broadcast messages are sent to all known clients except the sender.
- Ensure port `5000` is free before running the server.
