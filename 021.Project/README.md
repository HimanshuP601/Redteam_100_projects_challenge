# FastGoogle – Simple Google-Based Web Recon Bot

## Project Overview

FastGoogle is a lightweight Python-based reconnaissance tool that automates
Google search queries (Google dorks) to identify publicly exposed web resources.

The project demonstrates how search engines can be leveraged for
open-source intelligence (OSINT) and web surface discovery.

This project is part of the Redteam_100_projects_challenge series.

---

## What Is Google-Based Reconnaissance?

Google-based reconnaissance uses advanced search queries
(commonly known as Google dorks) to discover:

- Admin panels
- Backup files
- Configuration leaks
- Directory listings
- Sensitive endpoints

These resources are often publicly indexed by search engines.

---

## How It Works

1. Load predefined Google dorks from a file
2. Replace target placeholders dynamically
3. Send low-rate Google search requests
4. Extract result URLs
5. Present findings for manual analysis

The tool intentionally runs slowly to avoid aggressive behavior.

---

## Architecture

Dork list
-> Google search query
-> HTML response
-> Result link extraction
-> Analyst review

---

## Features

- Automated Google dork execution
- Target placeholder support
- Lightweight HTML parsing
- Low request rate for safety
- Simple and readable implementation

---

## Usage

Edit the target domain in fastgoogle.py:
```bash
    TARGET = "example.com"
```
Run the tool:
```bash
    python fastgoogle.py
```
Example output:
```bash
    [DORK] site:example.com admin
      -> https://example.com/admin
```
---

## Accuracy and Limitations

- Dependent on Google indexing
- Results may change over time
- CAPTCHA or blocking may occur
- Not suitable for large-scale scanning

This tool is designed for learning and small-scale analysis only.

---

## Security Implications

Search engines can unintentionally expose sensitive resources.

Organizations should:
- Remove sensitive files from public access
- Use robots.txt appropriately
- Monitor indexed content regularly

---

## Mitigation and Defense

- Avoid exposing sensitive files publicly
- Disable directory listings
- Use proper access controls
- Monitor search engine indexing
- Conduct regular OSINT reviews

---

## Skills Demonstrated

- OSINT techniques
- Web reconnaissance
- HTTP request handling
- HTML parsing
- Ethical security research practices

---

## Disclaimer

This tool is intended strictly for educational and defensive security research.
Use responsibly and in accordance with applicable laws and service terms.
