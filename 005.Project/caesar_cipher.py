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

