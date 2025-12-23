# FastSSH – Simple Threaded SSH Login Testing Tool

## Project Overview

FastSSH is a Python-based SSH authentication testing tool designed to
demonstrate how weak SSH credentials can be abused when proper
security controls are not in place.

The project focuses on understanding SSH authentication mechanics,
threaded connection handling, and defensive countermeasures.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is SSH Login Brute-Forcing?

SSH login brute-forcing involves repeatedly attempting authentication
using different username and password combinations.

This becomes possible when:
- Password authentication is enabled
- Weak or reused credentials exist
- Rate limiting is absent
- Lockout protections are misconfigured

FastSSH demonstrates this behavior in a controlled lab environment.

---

## How It Works

1. Load usernames and passwords from wordlists
2. Attempt SSH authentication using Paramiko
3. Detect successful logins
4. Stop scanning when valid credentials are found

Threading is used to improve testing speed.

---

## Architecture

User list + Password list
-> Threaded SSH connections
-> SSH authentication
-> Success or failure detection

---

## Features

- Multithreaded SSH login testing
- Uses Paramiko SSH library
- Simple and readable implementation
- Designed for lab and learning environments

---

## Usage

Edit configuration in fastssh.py:

    SSH_HOST
    SSH_PORT
    THREADS

Run the tool:
```bash
    python fastssh.py
```
Example output:
```bash
    [FAIL] admin:admin
    [SUCCESS] user:test123
```
---

## Accuracy and Limitations

- Uses password-based SSH authentication only
- Does not support key-based authentication testing
- No rate-limit evasion
- No fail2ban bypass
- Stops after first valid credential is found

This tool is intentionally minimal.

---

## Security Implications

Weak SSH credentials can allow attackers to:
- Gain remote shell access
- Execute commands
- Pivot further into networks

FastSSH highlights why SSH must be hardened.

---

## Mitigation and Defense

- Disable password authentication
- Use SSH key-based authentication
- Enable fail2ban or similar tools
- Enforce strong password policies
- Restrict SSH access via firewall rules
- Monitor authentication logs

---

## Skills Demonstrated

- SSH protocol understanding
- Network authentication testing
- Multithreading
- Python networking libraries
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only test SSH servers you own or have explicit permission to assess.
