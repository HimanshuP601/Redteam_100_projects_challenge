# ChaosShortcuts – Random Desktop Shortcut Generator

## Project Overview

ChaosShortcuts is a small Python application that generates
random desktop shortcut files as a local automation experiment.

The project demonstrates filesystem manipulation,
desktop entry formats, and controlled UI chaos.

This project is intended for learning and experimentation only.

---

## What It Does

- Creates random .desktop shortcut files
- Places them on the user's desktop
- Uses safe, non-destructive targets
- Requires no elevated privileges
- Can be easily cleaned up

---

## How It Works

1. Generate random shortcut names
2. Create Linux .desktop files
3. Assign executable permissions
4. Place them on the desktop

Each shortcut opens a harmless URL when clicked.

---

## Usage

Run the script:
```bash
    python chaos_shortcuts.py
```
Random shortcuts will appear on the desktop.

---

## Cleanup

Remove generated shortcuts with:
```bash
    rm ~/Desktop/*.desktop
```
---

## Safety Notes

- No persistence
- No background processes
- No network abuse
- No privilege escalation

The script runs once and exits.

---

## Skills Demonstrated

- Python filesystem automation
- Linux desktop entry format
- Randomization logic
- Ethical automation design

---

## Disclaimer

This project is intended for educational and local experimentation only.
Do not use to disrupt other users without consent.
