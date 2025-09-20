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
