# FastDir – Simple Threaded Web Directory Brute-Forcer

## Project Overview

FastDir is a lightweight web directory brute-forcing tool written in Python.
It discovers hidden or unlinked directories and files by sending HTTP requests
to common paths.

The project focuses on understanding web reconnaissance techniques and
threaded request handling for speed.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Web Directory Brute-Forcing?

Web directory brute-forcing attempts to discover hidden paths on a web server.

Examples:
- /admin
- /login
- /uploads
- /api
- /backup

Even if not linked publicly, these paths may still be accessible.

---

## How It Works

1. Load paths from a wordlist
2. Send HTTP GET requests to each path
3. Analyze HTTP response codes
4. Report discovered directories or files

Threading is used to perform requests concurrently for speed.

---

## Architecture

Wordlist
-> Threaded HTTP requests
-> Target web server
-> HTTP response analysis
-> Discovered paths

---

## Features

- Multithreaded scanning
- Configurable target and wordlist
- Lightweight and fast execution
- Simple and readable implementation

---

## Usage

Edit the target URL in fastdir.py:
```bash
    TARGET = "http://127.0.0.1"
```
Run the tool:
```bash
    python fastdir.py
```
Example output:
```bash
    [FOUND] http://127.0.0.1/admin (403)
    [FOUND] http://127.0.0.1/login (200)
    [FOUND] http://127.0.0.1/robots.txt (200)
```
---

## HTTP Status Codes Explained

- 200 – Resource exists and is accessible
- 301 / 302 – Redirect (resource exists)
- 403 – Forbidden (resource exists but restricted)
- 404 – Not found (ignored)

---

## Accuracy and Limitations

- Relies on the quality of the wordlist
- Cannot detect dynamically generated routes
- Rate-limited by the target server
- No recursion or extension fuzzing

---

## Security Implications

Hidden directories often expose:
- Admin panels
- Backup files
- APIs
- Sensitive resources

This demonstrates why directory listing and unused paths
should be properly secured or removed.

---

## Mitigation and Defense

- Disable unused endpoints
- Use authentication and authorization
- Configure proper access controls
- Implement rate limiting
- Monitor web access logs

---

## Skills Demonstrated

- HTTP protocol understanding
- Multithreading
- Web reconnaissance techniques
- Python requests library
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only scan systems you own or have explicit permission to test.
