
# TCP Chat Client

This project demonstrates a simple TCP chat client in Python that can connect to a multi-client TCP chat server.

---

## **TCP Chat Client (`client.py`)**

### **Description**
- Connects to a TCP chat server on a specified host and port.
- Receives messages from the server in a separate thread and prints them in real-time.
- Sends messages to the server typed by the user.
- Type `exit` to close the connection.

### **Code**
```python
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input()
    if msg.lower() == "exit":
        client.close()
        break
    client.send(msg.encode())
```

### **Run the TCP Client**
```bash
python3 client.py
```

### **Usage**
1. Start the TCP chat server in a separate terminal.
2. Run this client script to connect to the server.
3. Type messages to send them to the server and other connected clients.
4. Type `exit` to disconnect from the server.

---

## **Notes**
- The client runs a separate thread to continuously listen for incoming messages.
- Ensure the server is running before starting the client.
- Replace `127.0.0.1` with the server IP if connecting over a network.
