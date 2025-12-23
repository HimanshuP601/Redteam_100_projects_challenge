# FastLogin – Simple Threaded Web Login Brute-Force Tool

## Project Overview

FastLogin is a Python-based web login testing tool designed to demonstrate
how authentication mechanisms can be abused through repeated login attempts.

The project focuses on understanding the mechanics of login brute-forcing,
threaded request handling, and the importance of defensive protections
such as rate limiting and account lockouts.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Login Brute-Forcing?

Login brute-forcing is a technique where multiple username and password
combinations are tested against a login form.

Attackers abuse weak authentication controls when:
- No rate limiting exists
- Password policies are weak
- Account lockout is not enforced

FastLogin demonstrates this behavior in a controlled environment.

---

## How It Works

1. Load usernames and passwords from wordlists
2. Generate username/password combinations
3. Send HTTP POST requests to the login endpoint
4. Analyze server responses
5. Detect successful authentication attempts

Threading is used to increase speed while keeping the implementation simple.

---

## Architecture

User list + Password list
-> Threaded HTTP POST requests
-> Login endpoint
-> Response analysis
-> Success or failure detection

---

## Features

- Multithreaded login attempts
- Configurable form fields
- Custom success detection
- Lightweight and readable code
- Designed for lab environments

---

## Usage

Edit configuration in fastlogin.py:

    LOGIN_URL
    USERNAME_FIELD
    PASSWORD_FIELD
    SUCCESS_INDICATOR

Run the tool:
```bash
    python fastlogin.py
```
Example output:
```bash
    [FAIL] admin:123456
    [SUCCESS] admin:admin
```
---

## Accuracy and Limitations

- Relies on response text matching
- Does not bypass CAPTCHA
- Does not bypass CSRF tokens
- Does not handle JavaScript-based logins
- Intended for simple form-based authentication

This tool demonstrates fundamentals, not real-world evasion techniques.

---

## Security Implications

Weak authentication protections allow attackers to:
- Guess credentials
- Access restricted areas
- Escalate privileges

FastLogin highlights why strong authentication controls are critical.

---

## Mitigation and Defense

- Implement rate limiting
- Enforce account lockout policies
- Use strong password requirements
- Add CAPTCHA after failures
- Monitor authentication logs

---

## Skills Demonstrated

- HTTP authentication flows
- Multithreading
- Web request handling
- Brute-force mechanics
- Defensive security awareness

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Only test applications you own or have explicit permission to assess.
