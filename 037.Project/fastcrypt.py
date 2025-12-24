import sys
import base64
import os
from cryptography.fernet import Fernet
from hashlib import sha256

def derive_key(password: str) -> bytes:
    digest = sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_file(filename, password):
    key = derive_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as f:
        f.write(encrypted)

    print(f"[+] Encrypted file saved as {filename}.enc")

def decrypt_file(filename, password):
    key = derive_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    output = filename.replace(".enc", ".dec")

    with open(output, "wb") as f:
        f.write(decrypted)

    print(f"[+] Decrypted file saved as {output}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("  Encrypt: python fastcrypt.py encrypt <file> <password>")
        print("  Decrypt: python fastcrypt.py decrypt <file.enc> <password>")
        sys.exit(1)

    mode = sys.argv[1]
    file = sys.argv[2]
    password = sys.argv[3]

    if mode == "encrypt":
        encrypt_file(file, password)
    elif mode == "decrypt":
        decrypt_file(file, password)
    else:
        print("Invalid mode")
