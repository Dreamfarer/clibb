#always import
import os
import requests #needs install via pip

#import self made modules
import windowFunctions

#Important Functions I'd like to keep:
#stdout = subprocess.run(["sudo", "killall", "openvpn"], check=True, capture_output=True, text=True).stdout

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

def window_vpn():
    windowFunctions.window("window_vpn")

    command = windowFunctions.getch()

    match command:
        case "y":
            window_vpn()
        case "x":
            window_vpn()
        case "d":
            windowFunctions.change(1)
        case "a":
            windowFunctions.change(0)
        case "s":
            windowFunctions.change(3)
        case "w":
            windowFunctions.change(2)
        case "q":
            windowFunctions.accept()
        case "e":
            window_main()
        case _:
            window_vpn()
    window_vpn()

#WINDOW main
def window_main():

    windowFunctions.window("window_main")

    command = windowFunctions.getch()
    if command == "v":
        window_vpn()
    elif command == "c":
        window_main()
    elif command == "a":
        window_main()
    elif command == "exit" or command == "e":
        quit()
    else:
        window_main()

window_main()
