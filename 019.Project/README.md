# FastFTP-Users – FTP User Footprinting Tool

## Project Overview

FastFTP-Users is a Python-based FTP reconnaissance tool designed to identify
potentially valid FTP usernames by analyzing server responses to authentication
requests.

The project demonstrates how protocol behavior can leak information
about valid user accounts when services are misconfigured.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is FTP User Footprinting?

FTP user footprinting is the process of identifying valid usernames
without attempting password authentication.

This is possible because some FTP servers respond differently
to valid and invalid usernames during the USER command phase.

FastFTP-Users leverages this behavior for reconnaissance purposes.

---

## How It Works

1. Connect to the FTP server
2. Send USER <username> command
3. Analyze FTP response codes
4. Infer whether the username exists

Common responses include:

- 331 – Username accepted, password required
- 230 – User logged in (anonymous access)
- 530 – Invalid user or access denied

---

## Architecture

Username list
-> TCP socket connection
-> FTP USER command
-> Server response analysis
-> User validity inference

---

## Features

- FTP username enumeration
- Protocol-level response analysis
- Lightweight socket-based implementation
- No password attempts
- Designed for lab environments

---

## Usage

Edit target configuration in fastftp_users.py:

    FTP_HOST
    FTP_PORT

Run the tool:
```bash
    python fastftp_users.py
```
Example output:
```bash
    ftp: VALID USER (password required)
    anonymous: VALID USER (logged in)
    admin: INVALID or RESTRICTED
```
---

## Accuracy and Limitations

- Depends on FTP server configuration
- Some servers hide user validity
- Firewalls or IDS may block attempts
- Does not work against hardened FTP servers

Results should be treated as heuristic, not absolute.

---

## Security Implications

Leaking valid usernames lowers the effort required for
password guessing and targeted attacks.

This project demonstrates why FTP servers should avoid
differentiating authentication responses.

---

## Mitigation and Defense

- Configure uniform authentication responses
- Disable anonymous FTP access
- Use SFTP instead of FTP
- Enforce strong authentication controls
- Monitor authentication attempts

---

## Skills Demonstrated

- FTP protocol understanding
- Socket programming
- Authentication reconnaissance
- Service fingerprinting
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only test FTP servers you own or have explicit permission to assess.
