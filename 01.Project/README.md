
# Multi-Client TCP Chat Server

This project demonstrates a simple multi-client chat server in Python using `socket` and `threading`.

---

## **TCP Chat Server (`tcp.py`)**

### **Description**
- The server listens for incoming TCP connections on a specific host and port.
- Supports multiple clients using threads.
- Broadcasts messages from one client to all others.
- Prints connection status and received messages in the server terminal.

### **Code**
```python
import threading
import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    s.bind((HOST , PORT))
    s.listen(5)
    print(f"[+] Server running on {HOST}:{PORT}")

    clients = []

    def broadcasr(msg , sender):
        for client in clients:
            if client != sender:
                try:
                    client.send(msg)
                except:
                    client.close()
                    clients.remove(client)

    def handle_client(conn , addr):
         print(f"[NEW CONNECTION] {addr} connected. ")
         conn.send("Welcome to the chatroom!\n".encode())

         while True:
             try:
                 msg = conn.recv(1024)
                 if not msg:
                     break
                 print(f"[{addr}] {msg.decode().strip()}")
             except:
                 break
         print(f"[DISCONNECTED] {addr}")
         conn.close()
         if conn in clients:
             clients.remove(conn)

    while True:
        conn , addr = s.accept()
        print(f"[CONNECTED] {addr} joined the chat.")
        clients.append(conn)
        thread = threading.Thread(target=handle_client , args=(conn , addr))
        thread.daemon = True
        thread.start()
```

### **Run the Chat Server**
```bash
python3 tcp.py
```

### **Test the Server**
1. Start the server in one terminal:
```bash
python3 tcp.py
```
2. Connect multiple clients using `nc` (Netcat) in separate terminals:
```bash
nc 127.0.0.1 5000
```
3. Type messages and see them broadcasted to all connected clients.
4. Disconnect a client by pressing `Ctrl+C` or closing the terminal. The server handles disconnections gracefully.

---

## **Notes**
- `threading.Thread` is used to handle multiple clients concurrently.
- `SO_REUSEADDR` allows quick restart of the server on the same port.
- Ensure port `5000` is free before running the server.
