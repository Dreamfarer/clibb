import os
import requests
from subprocess import Popen, CREATE_NEW_CONSOLE

import windowFunctions

def vpn():

    if os.name in ('nt', 'dos'):
        global process
        process = Popen('cmd', creationflags=CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen("airmon-ng check kill", shell=True)

    #BOTTOM: What do you want to do?
    windowFunctions.seperator()
    windowFunctions.spacing()
    windowFunctions.text(["What do you want to do?", 41, 97])

    #command = input()
    #if command == "exit" or command == "e":
    main()

#WINDOW main
def main():
    windowFunctions.clear()

    #Main window top
    windowFunctions.text(["3P0H0PE 0.0.4", 41, 97], ["by BE3dARt with <3", 41, 97])
    windowFunctions.spacing()
    windowFunctions.text(["Public IPv4: " + windowFunctions.ANSI(32) + requests.get('https://api.ipify.org').text, 0, 97])

    #Seperator
    windowFunctions.seperator()
    windowFunctions.spacing()

    #Main list
    windowFunctions.list("v", "VPN settings", "Connected to HTB")
    windowFunctions.spacing()
    windowFunctions.list("a", "Applications", "")
    windowFunctions.spacing()
    windowFunctions.list("s", "Scripts", "")
    windowFunctions.spacing()
    windowFunctions.list("c", "Configuration", "")
    windowFunctions.spacing()
    windowFunctions.list("e", "Exit HOP3", "")

    #BOTTOM: What do you want to do?
    windowFunctions.seperator()
    windowFunctions.spacing()
    windowFunctions.text(["What do you want to do?", 41, 97])

    command = input()
    if command == "v":
        vpn()
    elif command == "c":
        if "process" in globals():
            print(process.poll())
            
        x = input()
        main()
    elif command == "exit" or command == "e":
        os.exit()
    else:
        main()
   
main()

#https://i.stack.imgur.com/9UVnC.png
#print("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM")


