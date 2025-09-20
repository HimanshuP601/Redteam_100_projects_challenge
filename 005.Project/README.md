
# Caesar Cipher Project

This project demonstrates a simple implementation of the Caesar Cipher in Python for encrypting and decrypting text.

---

## **Caesar Cipher (`caesar_cipher.py`)**

### **Description**
- Implements the Caesar Cipher, a substitution cipher that shifts letters by a fixed number.
- Can encrypt or decrypt text based on user input.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters are not changed.

### **Code**
```python
def encrypt(text , shift):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text , shift):
    return encrypt(text , -shift)

text = input("Enter text: ")
shift = int(input("Enter shift value:"))
mode = input("Encrypt or Decrypt? (E/D): ").upper()

if mode == "E":
    print("Encrypted:" , encrypt(text, shift))
elif mode == "D":
    print("decrypted:" , decrypt(text , shift))
else:
    print("Invalid option!")
```

### **Run the Caesar Cipher Script**
```bash
python3 caesar_cipher.py
```

### **Usage**
1. Enter the text to encrypt or decrypt.
2. Enter the shift value (number of positions to shift letters).
3. Enter `E` to encrypt or `D` to decrypt.
4. The program outputs the resulting text.

---

## **Example**
```
Enter text: Himanshu
Enter shift value:3
Encrypt or Decrypt? (E/D): E
Encrypted: Klpdqvkx

Enter text: Klpdqvkx
Enter shift value:3
Encrypt or Decrypt? (E/D): D
decrypted: Himanshu
```

### **Notes**
- The cipher preserves the case of letters.
- Non-alphabet characters remain unchanged.
