# FastPassive – Simple Passive Web Scanner

## Project Overview

FastPassive is a non-intrusive web security scanner that performs
passive analysis of HTTP responses to identify common
misconfigurations and information disclosures.

The scanner does not send attack payloads or modify requests.
It is designed for safe reconnaissance and baseline assessments.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Passive Web Scanning?

Passive web scanning observes normal responses from a web application
and analyzes metadata such as headers, cookies, and HTML structure.

It does not exploit vulnerabilities or perform fuzzing.

---

## What FastPassive Checks

- Presence of common security headers
- Server and framework banner disclosure
- Cookie security flags (Secure, HttpOnly, SameSite)
- robots.txt availability
- Read-only HTML hints (forms, comments)

---

## How It Works

1. Send a normal HTTP GET request
2. Follow redirects safely
3. Analyze response headers
4. Inspect cookies and HTML content
5. Report findings without altering the target

---

## Usage

Edit the target in fastpassive.py:
```bash
    TARGET = "http://example.com"
```
Run the scanner:
```bash
    python fastpassive.py
```
---

## Accuracy and Limitations

- Does not detect exploitable vulnerabilities
- No JavaScript execution analysis
- No authenticated scanning
- Intended for baseline visibility only

Passive results should be followed by deeper testing where permitted.

---

## Security Implications

Missing security headers and verbose banners can increase risk
by exposing application behavior and configuration details.

Passive scanning helps identify low-effort hardening opportunities.

---

## Mitigation and Defense

- Enable appropriate security headers
- Reduce server banner disclosure
- Set secure cookie flags
- Review publicly exposed resources

---

## Skills Demonstrated

- HTTP protocol analysis
- Web security fundamentals
- Ethical reconnaissance
- Automation scripting
- Defensive security mindset

---

## Disclaimer

This tool is intended for educational and defensive security research.
Only scan systems you own or have permission to assess.
