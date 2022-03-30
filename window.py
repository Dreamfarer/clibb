import os
import requests
import subprocess

if os.name in ('nt', 'dos'):
	from subprocess import CREATE_NEW_CONSOLE

import windowFunctions

def getVPNStatus():

    if os.name in ('nt', 'dos'):
        return windowFunctions.ANSI(33) + "Not supported"
    else:
        try:
            #subprocess.check_output(["ifconfig", "tun0"])
            stdout = subprocess.run(["ifconfig", "tun0"], check=True, capture_output=True, text=True).stdout
            return windowFunctions.ANSI(32) + "Connected"
        except:
            return windowFunctions.ANSI(31) + "Diconnected"
    
def vpn():
    windowFunctions.clear()
    
    windowFunctions.list("d", "Disconnect", "")
    windowFunctions.spacing()
    windowFunctions.list("e", "Exit", "Exit to main menu")
    
    #BOTTOM: What do you want to do?
    windowFunctions.seperator()
    windowFunctions.spacing()
    windowFunctions.text(["What do you want to do?", 41, 97])

    command = input()
    if command == "d":
        
        try:
            stdout = subprocess.run(["sudo", "killall", "openvpn"], check=True, capture_output=True, text=True).stdout
        except:
            main()
        main()
    elif command == "exit" or command == "e":
        main()
    else:
       vpn()

#WINDOW main
def main():
    windowFunctions.clear()

    #Main window top
    windowFunctions.text(["3P0H0PE 0.0.5", 41, 97], ["by BE3dARt with <3", 41, 97])
    windowFunctions.spacing()
    # + requests.get('https://api.ipify.org').text
    windowFunctions.text(["Public IPv4: " + windowFunctions.ANSI(32), 0, 97])

    #Seperator
    windowFunctions.seperator()
    windowFunctions.spacing()

    #Main list
    windowFunctions.list("v", "VPN settings", getVPNStatus())
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
    windowFunctions.spacing()

    command = input()
    if command == "v":
        vpn()
    elif command == "exit" or command == "e":
        quit()
    else:
        main()
   
main()

#https://i.stack.imgur.com/9UVnC.png
#print("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM")


