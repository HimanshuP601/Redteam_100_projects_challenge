# FastDir-Recursive – Threaded Recursive Web Directory Brute-Forcer

## Project Overview

FastDir-Recursive is a Python-based web directory brute-forcing tool that
supports recursive discovery using threaded peer recursion.

Unlike basic directory scanners, this tool dynamically explores newly
discovered directories while scanning, allowing deeper enumeration
of hidden web paths.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Recursive Web Directory Brute-Forcing?

Recursive directory brute-forcing goes beyond single-level scanning.

When a directory is discovered, the scanner:
- Treats it as a new base path
- Brute-forces additional subdirectories within it
- Continues until a defined depth is reached

This technique closely resembles real-world reconnaissance tools.

---

## How It Works

1. Load initial wordlist
2. Scan the root directory
3. When a valid directory is found, enqueue it
4. Worker threads pick up new directories
5. Scanning continues recursively up to a maximum depth

All workers operate concurrently using a shared task queue.

---

## Architecture

Shared queue
-> Worker threads
-> HTTP requests
-> Directory discovery
-> Peer recursion (enqueue new paths)

---

## Features

- Recursive directory enumeration
- Multithreaded scanning
- Peer-based recursion model
- Depth limiting to avoid infinite scans
- Duplicate path tracking
- Fast and lightweight execution

---

## Usage

Edit the target URL in fastdir_recursive.py:
```bash
    TARGET = "http://127.0.0.1"
```
Run the scanner:
```bash
    python fastdir_recursive.py
```
Example output:
```bash
    [FOUND] http://127.0.0.1/admin (403)
    [FOUND] http://127.0.0.1/admin/login (200)
    [FOUND] http://127.0.0.1/api (200)
    [FOUND] http://127.0.0.1/api/v1 (200)
```
---

## HTTP Status Codes Considered

- 200 – Resource exists and is accessible
- 301 / 302 – Redirect (directory exists)
- 403 – Forbidden (directory exists but restricted)
- 404 – Ignored

---

## Accuracy and Limitations

- Depends on wordlist quality
- Dynamic routes may not be detected
- Rate limiting may reduce effectiveness
- Deep recursion increases noise

Depth limiting is intentionally enforced to maintain control.

---

## Security Implications

Recursive directory discovery significantly increases attack surface visibility.

Hidden admin panels, APIs, and backup directories are common entry points
for further exploitation.

This project demonstrates why unused or unprotected endpoints
should be removed or restricted.

---

## Mitigation and Defense

- Remove unused endpoints
- Enforce authentication
- Apply access controls
- Implement rate limiting
- Monitor web access logs

---

## Skills Demonstrated

- Recursive algorithms
- Multithreading
- Web reconnaissance techniques
- HTTP protocol behavior
- Queue-based task coordination
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only scan systems you own or have explicit permission to test.
