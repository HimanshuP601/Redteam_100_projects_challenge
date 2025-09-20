# ROT13 Cipher Project

This project demonstrates a simple implementation of the ROT13 cipher in Python for encoding and decoding text.

---

## **ROT13 Cipher (`ROT13.py`)**

### **Description**
- Implements the ROT13 cipher, a substitution cipher that shifts each letter by 13 positions in the alphabet.
- Can both encode and decode text using the same function.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters remain unchanged.

### **Code**
```python
def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("Enter text: ")
    transformed = rot13(text)
    print("ROT13:", transformed)
```
### Run the ROT13 Script
```bash
python3 ROT13.py
```
#### Usage
- Enter the text you want to encode or decode.
- The program outputs the ROT13 transformation.

### Example
```bash
Enter text: Himanshu
ROT13: Uvznafuh

Enter text: Unznafuh
ROT13: Hamanshu
```
#### Notes
- ROT13 is symmetric: encoding and decoding are the same operation.
- The cipher preserves the case of letters.
- Non-alphabet characters remain unchanged.
---
