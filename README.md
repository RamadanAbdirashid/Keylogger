# Keylogger

> ⚠️ **Disclaimer**: This project is intended **solely for educational use** and ethical testing on devices you own or have explicit permission to monitor. Unauthorized use may violate laws and privacy regulations.

---

## Overview

A simple Python-based keylogger that captures and logs keyboard input to a local file. Built for learning purposes to understand keyboard event handling in Python.

---

## Features

- Captures all keyboard input in real-time
- Logs keystrokes to a local file (`keyfile.txt`)
- Handles special keys (e.g., `[SHIFT]`, `[CTRL]`, `[TAB]`)
- Press **ESC** to safely stop the logger
- Lightweight — minimal external dependencies

---

## Project Structure

```
Keylogger-main/
├── keylogger.py   # Main script that captures keystrokes
├── keyfile.txt    # Auto-generated log file (created on first run)
└── README.md      # Project overview and usage instructions
```

---

## Requirements

- Python 3.6+
- [`pynput`](https://pypi.org/project/pynput/) package

---

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com/yourusername/Keylogger-main.git
   cd Keylogger-main
   ```

2. **Install the required package**:
   ```bash
   pip install pynput
   ```

---

## Usage

Run the keylogger from your terminal:

```bash
python keylogger.py
```

- All keystrokes will be saved to **`keyfile.txt`** in the same directory.
- Press **ESC** to stop the logger gracefully.

---

## Key Mapping

| Input          | Logged As       |
|----------------|-----------------|
| Regular chars  | `a`, `b`, `1`…  |
| Space          | ` ` (space)     |
| Enter          | newline (`\n`)  |
| Special keys   | `[SHIFT]`, `[CTRL]`, `[ALT]`… |
| ESC            | Stops the logger |

---

## How It Works

1. `pynput.keyboard.Listener` runs a background thread that fires `on_press` for every keypress.
2. The `keyPressed` callback:
   - Returns `False` on ESC → stops the listener.
   - Writes printable characters directly to `keyfile.txt`.
   - Maps `Space` → `" "` and `Enter` → `"\n"`.
   - Wraps all other special keys in `[KEYNAME]` brackets.

---

## Ethical Use Only

This tool should **only** be run on:
- Your own personal device
- A device where you have **written permission** from the owner

Using this tool without consent is **illegal** in most jurisdictions.
