import os
import requests

import windowFunctions

#WINDOW main
def main():
    windowFunctions.clearConsole()
    
    #Main window top
    windowFunctions.main_twoside(["HOP3 0.0.2", 41, 97], ["by BE3dARt with <3", 41, 97])
    #print("")
    #window-functions.main_oneside(["Public IPv4: " + window-functions.ANSI.color(32) + requests.get('https://api.ipify.org').text, 40, 97])
    #window-functions.main_line(2)

    #1 Line is 50 Characters wide
    #printer("MMMMMMMMMMMMMMMMMMMMMMMMFMMMMMMMMMMMMMMMMMMMMMMMMM", 41, 97)

    #window-functions.main_list("v", "VPN settings", "Connected to HTB")
    #print("")
    #window-functions.main_list("a", "Applications", "")
    #print("")
    #window-functions.main_list("s", "Scripts", "")
    #print("")
    #window-functions.main_list("e", "Exit HOP3", "")
    #window-functions.main_line(2)

    #window-functions.main_oneside(["What do you want to do?", 41, 97])

    command = input()
    if command == "v":
        vpn()
    elif command == "exit" or command == "e":
        sys.exit()
    else:
        main()
    

#my first Python program
main()

#https://i.stack.imgur.com/9UVnC.png


