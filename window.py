#always import
import os
import requests
import subprocess
import getpass
import sys

#import dependent on OS
if os.name in ('nt', 'dos'):
    from subprocess import CREATE_NEW_CONSOLE
    import msvcrt
else:
    import tty
    import termios

#import self made modules
import windowFunctions

def getch():
    if os.name in ('nt', 'dos'):
        #Windows
        try:
            character = msvcrt.getch().decode("utf-8")
        except:
            character = "Error"
        return character
    else:
        #Linux
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            character = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return character

#WINDOW testbed
def testbed():
    windowFunctions.clear()

    character = getch()

    if character == "e":
        main()
    elif character == "w":
        main()
    elif character == "s":
        main()
    else:
        testbed()
    

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
    windowFunctions.text(["3P0H0PE 0.0.6", 41, 97], ["by BE3dARt with <3", 41, 97])
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

    windowFunctions.matrix_text([["VPN", ["On", 0], ["Off", 1]], ["IP Mode", ["IPv4", 1], ["IPv6", 0]]])
    
    #BOTTOM: What do you want to do?
    windowFunctions.seperator()
    windowFunctions.spacing()
    windowFunctions.text(["What do you want to do?", 41, 97])
    windowFunctions.spacing()

    #silentInput = getpass.getpass(prompt='')

    command = input()
    if command == "v":
        vpn()
    elif command == "t":
        testbed()
    elif command == "exit" or command == "e":
        quit()
    else:
        main()
   
main()

#https://i.stack.imgur.com/9UVnC.png
#print("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM")


