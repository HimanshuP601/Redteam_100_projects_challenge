# FastMySQL-Users – MySQL User Footprinting Tool

## Project Overview

FastMySQL-Users is a Python-based reconnaissance tool designed to identify
potentially valid MySQL usernames by analyzing authentication error responses.

The project demonstrates how database authentication behavior can leak
information about existing users when error handling is not uniform.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is MySQL User Footprinting?

MySQL user footprinting is the process of identifying valid database users
without attempting password brute-forcing.

This is possible because MySQL returns different error codes depending on
whether a username exists, the password is incorrect, or the host is not allowed.

FastMySQL-Users leverages these differences for reconnaissance purposes.

---

## How It Works

1. Attempt to authenticate using a dummy password
2. Capture MySQL authentication error codes
3. Analyze the error to infer user validity

Common MySQL responses include:

- 1045 – Access denied (user exists, wrong password)
- 1130 – Host not allowed or user does not exist
- 1698 – Authentication plugin restrictions

---

## Architecture

Username list
-> MySQL authentication attempt
-> Error code analysis
-> User validity inference

---

## Features

- MySQL user enumeration
- Error-code based fingerprinting
- No password brute-forcing
- Uses official MySQL client library
- Designed for lab environments

---

## Usage

Edit configuration in fastmysql_users.py:

    MYSQL_HOST
    MYSQL_PORT

Run the tool:
```bash
    python fastmysql_users.py
```
Example output:
```bash
    root: VALID USER (password incorrect)
    mysql: VALID USER (password incorrect)
    admin: UNKNOWN RESPONSE (1130)
```
---

## Accuracy and Limitations

- Depends on MySQL server configuration
- Hardened servers may hide user validity
- Error codes may differ by version
- Results are heuristic, not absolute

This technique should be combined with other reconnaissance methods
for higher confidence.

---

## Security Implications

Leaking valid database usernames reduces the effort required for
targeted attacks and credential guessing.

This project demonstrates why authentication error responses
should be uniform and non-informative.

---

## Mitigation and Defense

- Use generic authentication error messages
- Restrict database network access
- Disable remote root login
- Enforce strong authentication plugins
- Monitor authentication attempts

---

## Skills Demonstrated

- MySQL authentication behavior
- Error handling and analysis
- Database reconnaissance techniques
- Python database libraries
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only test database servers you own or have explicit permission to assess.
