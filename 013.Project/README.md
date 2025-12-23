# FastPort-Footprint – Port Scanner with Service Identification

## Project Overview

FastPort-Footprint is a lightweight Python-based port scanner that identifies
open TCP ports and attempts to determine the services running on them.

The project focuses on service footprinting using common port mappings
and minimal protocol-aware probing.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Port Footprinting?

Port footprinting goes beyond identifying open ports.

It attempts to answer:
- What service is running?
- What protocol is exposed?
- What attack surface exists?

FastPort-Footprint performs basic service detection without intrusive scanning.

---

## How It Works

1. Scan a range of TCP ports using socket connections
2. Identify open ports
3. Send minimal probes to retrieve banners (if available)
4. Match results against known service patterns

---

## Architecture

Scanner
-> TCP socket connection
-> Open port detection
-> Minimal probe
-> Service identification

---

## Features

- Multithreaded TCP port scanning
- Common service detection
- Lightweight banner probing
- Fast execution
- Clean and readable implementation

---

## Supported Service Identification

FastPort-Footprint can identify common services such as:

- HTTP / HTTPS
- FTP
- SSH
- SMTP
- DNS
- IRC
- POP3 / IMAP
- MySQL
- Redis

Unknown services are reported as Unknown.

---

## Usage

Run the scanner:
```bash
    python fastport_footprint.py
```
By default, it scans ports 1–1024 on localhost.

Example output:
```bash
    22/tcp -> SSH
    80/tcp -> HTTP
    443/tcp -> HTTPS
    6667/tcp -> IRC
```
---

## Accuracy and Limitations

This tool uses heuristic-based identification.

Limitations include:
- Services running on non-standard ports
- Disabled banners
- Encrypted protocols hiding responses
- Firewalls filtering probes

For higher accuracy, deeper protocol analysis is required.

---

## Security Implications

Service footprinting is a key reconnaissance step.

Identifying exposed services helps attackers:
- Choose appropriate exploits
- Narrow attack surface
- Prioritize targets

Defenders should minimize exposed services and avoid unnecessary banners.

---

## Mitigation and Defense

- Disable unused services
- Restrict open ports via firewall rules
- Hide or limit service banners
- Monitor for scanning behavior

---

## Skills Demonstrated

- TCP networking
- Socket programming
- Multithreading
- Service fingerprinting
- Network reconnaissance fundamentals

---

## Disclaimer

This tool is intended for educational and defensive security research only.
Scan only systems you own or have explicit permission to test.
