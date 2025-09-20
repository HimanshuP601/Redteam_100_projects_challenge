
# UDP and TCP Server Examples

This project demonstrates simple Python scripts for creating UDP and TCP servers using the `socket` library.

---

## **UDP Server (`udp.py`)**

### **Description**
- The UDP server listens for incoming datagrams on a specific host and port.
- It prints the address of the sender and the message received.

### **Code**
```python
import socket
HOST = '127.0.0.1'
PORT = 5000
with socket.socket(socket.AF_INET , socket.SOCK_DGRAM) as s:
    s.bind((HOST , PORT))
    
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        data , addr = s.recvfrom(1024)
        print(f"{addr} : {data.decode()}")
```

### **Run the UDP server**
```bash
python3 udp.py
```

---

## **TCP Server (`tcp.py`)**

### **Description**
- The TCP server listens for incoming connections on a specific host and port.
- Once a client connects, it accepts the connection and continuously receives messages until the client disconnects.

### **Code**
```python
import socket
HOST = '127.0.0.1'
PORT = 5000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT))
    s.listen(1)

    print(f'[+] Server is listening on {HOST}:{PORT}')

    conn , addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            print("Client disconnected.")
            break

        print("Received:" , data.decode())

    conn.close()
    server.close()
```

### **Run the TCP server**
```bash
python3 tcp.py
```

---

## **Testing the Servers**

### **Using `nc` (Netcat) for TCP**
1. Start the TCP server:
    ```bash
    python3 tcp.py
    ```
2. In another terminal, connect to the server:
    ```bash
    nc 127.0.0.1 5000
    ```
3. Type messages and see them appear in the server terminal.

---

### **Using `nc` for UDP**
1. Start the UDP server:
    ```bash
    python3 udp.py
    ```
2. In another terminal, send messages:
    ```bash
    nc -u 127.0.0.1 5000
    ```
3. Type messages and see them appear in the server terminal.

---

## **Notes**
- Replace `127.0.0.1` with your local or external IP if you want to receive connections from other devices on the same network.
- Make sure port `5000` is free before running these servers.
