# Caesar Cipher TCP Chat

A simple client-server chat application in Python that encrypts messages using the **Caesar Cipher**. Messages sent between clients are encrypted with a fixed shift and decrypted on reception. This project demonstrates basic **socket programming**, **multithreading**, and **encryption** in Python.

---

## Features

- Real-time client-server messaging.
- Caesar Cipher encryption for message privacy.
- Supports multiple clients simultaneously.
- Easy-to-understand Python implementation.

---

## Project Structure

```
006.Project/
│
├── client.py        # Client script to connect and send messages
├── server.py        # Server script to handle multiple clients
└── README.md        # Project documentation
```

---

## Requirements

- Python 3.x
- No external libraries required (uses standard library modules `socket` and `threading`)

---

## How to Run

### 1. Start the Server

```bash
python server.py
```

Output:

```
[LISTENING] Server running on 127.0.0.1:5001
```

### 2. Start the Client

Open a new terminal and run:

```bash
python client.py
```

Output:

```
[CONNECTED] Connected to 127.0.0.1:5001
```

### 3. Chat

- Type messages in the client terminal.
- Messages are encrypted before sending and decrypted on reception.
- Multiple clients can connect to the server and chat simultaneously.

---

## Caesar Cipher

- **Shift Value:** 3 (configurable in `client.py` and `server.py`)
- **Encrypt:** Each alphabetical character is shifted by the shift value.
- **Decrypt:** The reverse operation of encryption.

---

## Screenshots

Example terminal session:

**Server:**

```
[LISTENING] Server running on 127.0.0.1:5001
[CONNECTED] ('127.0.0.1', 53412)
[RECEIVED] Hello
[RECEIVED] How are you?
```

**Client:**

```
[CONNECTED] Connected to 127.0.0.1:5001
Hello
How are you?
[MESSAGE] Hi there!
```

---

## Notes

- Only **alphabetical characters** are encrypted; numbers and symbols remain unchanged.
- Threads are used to allow simultaneous sending and receiving of messages.

---

