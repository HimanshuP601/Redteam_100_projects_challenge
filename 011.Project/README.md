# FastPort – Simple and Fast Port Scanner

## Project Overview

FastPort is a lightweight TCP port scanner written in Python to demonstrate
how network services can be discovered using basic socket connections.

The goal of this project is to understand the fundamentals of port scanning,
threading for performance, and the security implications of exposed services.

This project is part of the Redteam_100_projects_challenge series.

---

## How Port Scanning Works

A TCP port scan attempts to establish a connection to a target port.

- If the connection succeeds, the port is considered open
- If the connection fails or times out, the port is closed or filtered

FastPort uses TCP connect scans, which are simple and reliable.

---

## Architecture

Scanner
-> TCP socket
-> Target host and port
-> Connection result
-> Open port identified

---

## Features

- Multithreaded scanning for speed
- Configurable port range
- Connection timeout handling
- Minimal and readable implementation

---

## File Description

fastport.py  
Implements a multithreaded TCP connect port scanner using Python sockets.

---

## Usage

Run the scanner:
```bash
    python fastport.py
```
By default, it scans ports 1–1024 on localhost.

Example output:
```bash
    [OPEN] Port 22
    [OPEN] Port 80
```
---

## Why Multithreading is Used

Scanning ports sequentially is slow due to network timeouts.
Threads allow multiple ports to be scanned in parallel,
significantly improving scan speed.

---

## Security Implications

Port scanning is often the first step in reconnaissance.

Exposed services may:
- Leak version information
- Contain vulnerabilities
- Allow unauthorized access

This project demonstrates why unused services should be closed
and firewalls properly configured.

---

## Limitations

- No service fingerprinting
- No UDP scanning
- No stealth scanning techniques
- Detectable by intrusion detection systems

---

## Mitigation and Defense

- Use firewalls to restrict ports
- Disable unused services
- Monitor for scan patterns
- Implement rate limiting

---

## Skills Demonstrated

- TCP networking
- Socket programming
- Multithreading
- Network reconnaissance fundamentals
- Defensive security awareness

---

## Disclaimer

This tool is intended for educational and defensive security research only.
Scan only systems you own or have permission to test.
