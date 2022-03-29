import os
import requests

import windowFunctions

#WINDOW main
def main():
    windowFunctions.clearConsole()
    
    #Main window top
    windowFunctions.main_twoside(["3P0H0PE 0.0.1", 41, 97], ["by BE3dARt with <3", 41, 97])
    print("")
    windowFunctions.main_oneside(["Public IPv4: " + windowFunctions.ANSI.color(32) + requests.get('https://api.ipify.org').text, 0, 97])
    windowFunctions.main_line(2)

    #1 Line is 50 Characters wide
    #printer("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM", 41, 97)

    windowFunctions.main_list("v", "VPN settings", "Connected to HTB")
    print("")
    windowFunctions.main_list("a", "Applications", "")
    print("")
    windowFunctions.main_list("s", "Scripts", "")
    print("")
    windowFunctions.main_list("c", "Configuration", "")
    print("")
    windowFunctions.main_list("e", "Exit HOP3", "")
    windowFunctions.main_line(2)

    windowFunctions.main_oneside(["What do you want to do?", 41, 97])

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


