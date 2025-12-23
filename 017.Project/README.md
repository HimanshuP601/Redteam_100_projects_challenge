# FastFTP – Simple Threaded FTP Login Testing Tool

## Project Overview

FastFTP is a Python-based FTP authentication testing tool designed to
demonstrate how weak or default FTP credentials can be abused.

The project focuses on understanding FTP authentication mechanics,
threaded connection handling, and the importance of securing legacy services.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is FTP Login Brute-Forcing?

FTP login brute-forcing involves testing multiple username and password
combinations against an FTP server.

This is possible when:
- Weak credentials are used
- Anonymous login is enabled
- No rate limiting exists
- Legacy services are exposed

FastFTP demonstrates this behavior in a controlled lab environment.

---

## How It Works

1. Load usernames and passwords from wordlists
2. Attempt FTP connections using standard authentication
3. Detect successful logins
4. Stop scanning when valid credentials are found

Threading is used to improve testing speed.

---

## Architecture

User list + Password list
-> Threaded FTP connections
-> FTP authentication
-> Success or failure detection

---

## Features

- Multithreaded FTP login testing
- Uses Python ftplib (standard library)
- Simple and readable implementation
- Designed for lab and learning environments

---

## Usage

Edit configuration in fastftp.py:

    FTP_HOST
    FTP_PORT
    THREADS

Run the tool:
```bash
    python fastftp.py
```
Example output:
```bash
    [FAIL] admin:123456
    [SUCCESS] ftp:ftp
```
---

## Accuracy and Limitations

- Uses standard FTP authentication only
- No support for FTPS or SFTP
- No rate-limit evasion
- Stops after first valid credential is found

This tool is intentionally minimal.

---

## Security Implications

Exposed FTP services with weak credentials allow attackers to:
- Upload or download files
- Modify hosted content
- Steal sensitive data
- Gain further system access

FastFTP highlights why FTP should be secured or disabled.

---

## Mitigation and Defense

- Disable FTP if not required
- Enforce strong passwords
- Disable anonymous login
- Use SFTP instead of FTP
- Apply firewall restrictions
- Monitor authentication logs

---

## Skills Demonstrated

- FTP protocol understanding
- Multithreading
- Network authentication testing
- Python standard libraries
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only test FTP servers you own or have explicit permission to assess.
