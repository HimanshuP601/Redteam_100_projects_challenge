# PyCat – Custom Netcat Reimplementation

## Project Overview

PyCat is a lightweight reimplementation of the classic Netcat (nc) utility,
built in Python to understand how remote shells, command execution, and
socket-based communication work at a low level.

This project focuses on rebuilding Netcat’s core functionality from scratch
to gain hands-on understanding of client-server communication and
remote command execution.

This project is part of the Redteam_100_projects_challenge series.

---

## Architecture

Client (pycat.py or netcat)
-> TCP Socket
-> PyCat Listener (pycat_shell.py)
-> Command Execution
-> Output returned to client

---

## Implemented Features

- TCP client implementation
- TCP server (listener) mode
- Bidirectional communication
- Remote command execution
- Interactive shell behavior
- Compatibility with Netcat

---

## Files

pycat.py  
Client-side implementation that sends commands and receives output.

pycat_shell.py  
Server-side listener that executes received commands and returns results.

---

## How It Works

PyCat recreates Netcat’s behavior using Python sockets.

At a fundamental level, Netcat is simply:
```bash
    socket + stdin + stdout
```
The listener accepts a TCP connection, receives commands from the client,
executes them using the local shell, and sends the output back over the socket.

---

## Usage

### Start the Listener
```bash
    python pycat_shell.py
```
Expected output:
```bash
    [+] Listening on 0.0.0.0:4444
    [+] Connection from ('127.0.0.1', <port>)
```
---

### Connect Using Netcat
```bash
    nc localhost 4444
```
Example interaction:
```bash
    whoami
    id
    ls
    uname -a
```
---

### Connect Using PyCat Client
```bash
    python pycat.py
```
Commands typed in the client are executed remotely and results are returned
interactively.

---

## Demonstrated Behavior

- Interactive remote shell
- Remote command execution
- Output streaming over TCP
- Stable client-server communication

Example output:
```bash
    whoami
    himanshu

    id
    uid=1000(himanshu) gid=1000(himanshu)
```
---

## Address Already in Use Error

During development, the following error may appear:
```bash
    OSError: [Errno 98] Address already in use
```
### Cause

- Another process is already bound to the port
- Socket is in TIME_WAIT state after closing

### Solution

- Terminate the process using the port
- Enable socket reuse

Recommended fix:
```bash
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```
---

## Security Impact

This project demonstrates how tools like Netcat can enable:

- Remote command execution
- Interactive shell access
- Full system compromise if exposed improperly

It highlights why unrestricted socket listeners and command execution
must never be exposed in production environments.

---

## Mitigation and Defense

- Never expose raw command execution over sockets
- Require authentication for network services
- Restrict listening ports
- Run services as non-root users
- Monitor open ports and network activity

---

## Skills Demonstrated

- TCP socket programming
- Client-server architecture
- Interactive shell design
- Netcat internals understanding
- Remote command execution concepts
- Defensive security awareness

---

## Disclaimer

This project is intentionally insecure and built strictly for
educational and defensive security research purposes.

It must never be deployed in production environments.
