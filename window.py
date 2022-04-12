#always import
import os
import requests

#import self made modules
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

#WINDOW window_testbed
def window_testbed():
    
    print('\033[?25l', end="")
    windowFunctions.temporary = [[1, "VPN", ["On", 0], ["Off", 1], ["Lol", 0]], [0, "IP Mode",["IPv4", 1], ["IPv6", 0]], [0, "Opt", ["Yes", 0], ["No", 1], ["May", 0]]]
    
    while (True):
        windowFunctions.clear()
        
        windowFunctions.matrix_text(windowFunctions.temporary )
        
        character = windowFunctions.getch()
        if character == "e":
            print('\033[?25h', end="")
            window_main()
            break
        elif character == "d":
            windowFunctions.change(1)
        elif character == "a":
            windowFunctions.change(0)
        elif character == "s":
            windowFunctions.change(3)
        elif character == "w":
            windowFunctions.change(2)
        elif character == "q":
            windowFunctions.accept()
    
def window_vpn():
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
            window_main()
        window_main()
    elif command == "exit" or command == "e":
        window_main()
    else:
       window_vpn()

#WINDOW main
def window_main():
    windowFunctions.clear()
    
    #Main window top
    windowFunctions.text(["3P0H0PE 0.1.2", 41, 97], ["by BE3dARt with <3", 41, 97])
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

    command = windowFunctions.getch()
    if command == "v":
        window_vpn()
    elif command == "c":
        window_testbed()
    elif command == "exit" or command == "e":
        quit()
    else:
        window_main()
   
window_main()

#https://i.stack.imgur.com/9UVnC.png
#print("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM")


