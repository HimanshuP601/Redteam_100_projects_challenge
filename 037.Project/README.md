# FastCrypt – Simple File Encryption Application

## Project Overview

FastCrypt is a Python-based file encryption application that allows
users to securely encrypt and decrypt files using a password.

The project demonstrates practical cryptography usage
with modern encryption standards.

This project is part of the Redteam_100_projects_challenge series.

---

## What It Does

- Encrypts files using AES-based encryption
- Protects files with a user-provided password
- Decrypts files back to original form
- Uses secure cryptographic libraries

---

## How It Works

1. User provides a password
2. Password is hashed into a cryptographic key
3. File contents are encrypted using symmetric encryption
4. Encrypted file is written to disk
5. Decryption reverses the process with the same password

---

## Usage

Encrypt a file:
```bash
    python fastcrypt.py encrypt file.txt password123
```
Decrypt a file:
```bash
    python fastcrypt.py decrypt file.txt.enc password123
```
---

## Security Notes

- Strong encryption via Fernet (AES)
- No custom cryptography
- Password must be kept secret
- Losing the password means data cannot be recovered

---

## Limitations

- Single-file encryption
- No password recovery
- No key rotation
- Intended for learning and small utilities

---

## Skills Demonstrated

- Applied cryptography
- Secure file handling
- Python scripting
- Security-aware design

---

## Disclaimer

This tool is intended for educational and personal use.
Do not rely on it for enterprise-grade key management.
