# FastPort-TTL – Port Scanner with OS Fingerprinting

## Project Overview

FastPort-TTL is a lightweight Python tool that combines TCP port scanning
with basic operating system fingerprinting using IP packet TTL values.

The project demonstrates how reconnaissance tools can infer system details
using simple networking techniques.

This project is part of the Redteam_100_projects_challenge series.

---

## How It Works

### Port Scanning

The scanner attempts to establish TCP connections to a range of ports.

- Successful connection → port is open
- Failed connection → port is closed or filtered

Multithreading is used to improve scan speed.

---

### OS Fingerprinting Using TTL

Different operating systems use different default TTL values:

- Linux / Unix: ~64
- Windows: ~128
- Network devices (Cisco, BSD): ~255

By sending a single ICMP echo request (ping) and inspecting the TTL value
in the response, FastPort-TTL estimates the target operating system.

This method provides a heuristic guess, not a guarantee.

---

## Architecture

Scanner
-> TCP socket connections (port scan)
-> ICMP ping request
-> TTL extraction
-> OS fingerprint estimation

---

## Features

- Multithreaded TCP port scanning
- OS fingerprinting via TTL analysis
- Fast execution
- Minimal and readable code

---

## Usage

Run the scanner:
```bash
    python fastport_ttl.py
```
By default, it scans ports 1–1024 on localhost.

Example output:
```bash
    [+] Open Ports:
        22
        4444

    [+] OS Fingerprint:
        Linux / Unix (TTL=64)
```
---

## Accuracy and Limitations

TTL-based OS fingerprinting is not always accurate.

Limitations include:
- Routers decrement TTL values
- Firewalls may block ICMP
- Custom TTL values may be configured
- Virtualized environments may alter behavior

This technique should be combined with other fingerprinting methods
for higher confidence.

---

## Security Implications

Port scanning and OS fingerprinting are common reconnaissance techniques.

Exposed services and identifiable operating systems increase
an attacker's situational awareness.

Defensive measures should minimize exposed ports
and restrict ICMP responses where appropriate.

---

## Mitigation and Defense

- Disable unnecessary services
- Use firewalls to restrict port access
- Monitor for scanning activity
- Limit ICMP exposure when possible

---

## Skills Demonstrated

- TCP networking fundamentals
- Multithreading in Python
- Socket programming
- OS fingerprinting concepts
- Network reconnaissance techniques

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only scan systems you own or have explicit permission to test.
