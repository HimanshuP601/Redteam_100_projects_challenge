# UDP ROT13 Chat

A simple UDP-based client-server chat application in Python that encrypts messages using the **ROT13 Cipher**. Messages sent between clients are encrypted using ROT13 and decrypted on reception. This project demonstrates basic **UDP socket programming** and **multithreading** in Python.

---

## Features

- Real-time client-server messaging over UDP.
- ROT13 encryption for message privacy.
- Supports multiple clients.
- Lightweight and easy-to-understand Python implementation.

---

## Project Structure

```
008.Project/
│
├── client.py        # Client script to send and receive messages
├── server.py        # UDP server script to handle multiple clients
└── README.md        # Project documentation
```

---

## Requirements

- Python 3.x
- No external libraries required (uses standard library modules `socket` and `threading`)

---

## How to Run

### 1. Start the UDP Server

```bash
python server.py
```

Output:

```
[LISTENING] UDP server running on 0.0.0.0:5000
```

### 2. Start the UDP Client

Open a new terminal and run:

```bash
python client.py
```

Output:

```
[CONNECTED] Connected to 127.0.0.1:5000
```

### 3. Chat

- Type messages in the client terminal.
- Messages are encrypted with ROT13 before sending and decrypted on reception.
- Multiple clients can join and chat simultaneously.

---

## ROT13 Cipher

- **Algorithm:** ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet.
- **Encrypt/Decrypt:** The same function is used for encryption and decryption.

---

## Example Terminal Session

**Server:**

```
[LISTENING] UDP server running on 0.0.0.0:5000
[NEW CLIENT] ('127.0.0.1', 50773) joined
[FROM ('127.0.0.1', 50773)] Hello
```

**Client:**

```
[MESSAGE] Hello
Hi there!
```

---

## Notes

- Only **alphabetical characters** are encrypted; numbers and symbols remain unchanged.
- UDP is connectionless, so message delivery is not guaranteed.
- Threads are used to allow simultaneous sending and receiving of messages.

---


