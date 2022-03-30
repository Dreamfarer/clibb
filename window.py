import os
import requests

import windowFunctions

#WINDOW main
def main():
    windowFunctions.clear()

    #Main window top
    windowFunctions.normal(["3P0H0PE 0.0.3", 41, 97], ["by BE3dARt with <3", 41, 97])
    print("")
    windowFunctions.normal(["Public IPv4: " + windowFunctions.ANSI(32) + requests.get('https://api.ipify.org').text, 0, 97])
    windowFunctions.line(2)

    #1 Line is 50 Characters wide
    #print("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM")

    windowFunctions.list("v", "VPN settings", "Connected to HTB")
    print("")
    windowFunctions.list("a", "Applications", "")
    print("")
    windowFunctions.list("s", "Scripts", "")
    print("")
    windowFunctions.list("c", "Configuration", "")
    print("")
    windowFunctions.list("e", "Exit HOP3", "")
    windowFunctions.line(2)

    windowFunctions.normal(["What do you want to do?", 41, 97])

    command = input()
    if command == "v":
        vpn()
    #elif command == "exit" or command == "e":
        #sys.exit()
    #else:
    #    main()
    

#my first Python program
main()

#https://i.stack.imgur.com/9UVnC.png


