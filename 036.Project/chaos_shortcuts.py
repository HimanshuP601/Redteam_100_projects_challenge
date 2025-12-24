import os
import random
import string

# ===== CONFIG =====
DESKTOP_PATH = os.path.expanduser("~/Desktop")
COUNT = 10
# ==================

def random_name(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def create_shortcut(name):
    filename = f"{name}.desktop"
    path = os.path.join(DESKTOP_PATH, filename)

    content = f"""[Desktop Entry]
Type=Application
Name={name}
Exec=xdg-open https://example.com
Icon=utilities-terminal
Terminal=false
"""

    with open(path, "w") as f:
        f.write(content)

    os.chmod(path, 0o755)

def main():
    print("[+] Creating random desktop shortcuts...\n")

    for _ in range(COUNT):
        name = random_name()
        create_shortcut(name)
        print(f"  Created: {name}.desktop")

    print("\n[+] Done. Refresh your desktop if needed.")

if __name__ == "__main__":
    main()
