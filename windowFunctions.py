import os
import sys

import ReadFile

global temporary

#import dependent on OS
if os.name in ('nt', 'dos'):
    from subprocess import CREATE_NEW_CONSOLE
    import msvcrt
else:
    import tty
    import termios

def ANSI(code):
    return "\33[{code}m".format(code=code)

windowWidth = 50

#Translate name to array index and insert it
def window(name):
    nameCounter = 1
    while (True):
        try:
            if configuration[nameCounter][0] == name:
                break
            else:
                nameCounter += 1
        except:
            print ("Nothing found! Please check spelling!")
            return

    moduleCounter = 0
    while (True):
        try:
            if configuration[nameCounter][1][moduleCounter][0] == "Two-Side":
                twoSide(configuration[nameCounter][1][moduleCounter][1])
            if configuration[nameCounter][1][moduleCounter][0] == "One-Side":
                oneSide(configuration[nameCounter][1][moduleCounter][1][0])
            if configuration[nameCounter][1][moduleCounter][0] == "Display":
                print ("Dis")
            if configuration[nameCounter][1][moduleCounter][0] == "Menu":
                print ("Menu")
            if configuration[nameCounter][1][moduleCounter][0] == "Menu-Display":
                menuDisplay(configuration[nameCounter][1][moduleCounter][1])
            if configuration[nameCounter][1][moduleCounter][0] == "Configuration":
                print ("Configurat")
            if len(configuration[nameCounter][1][moduleCounter][0]) == 1:
                if configuration[nameCounter][1][moduleCounter] == "Seperator-Filled":
                    seperator()
                if configuration[nameCounter][1][moduleCounter] == "Seperator-Empty":
                    spacing()
            moduleCounter += 1
        except:
            return

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

#Word string is always: ["Word", font-color, background-color]

def accept():

    outerCounter =0
    innerCounter = 2
    
    while(True):
        try:
            #Find the active element
            if temporary[outerCounter][0] != 0:
                
                #Make every other element to off first
                while(True):
                    try:
                        temporary[outerCounter][innerCounter][1] = 0
                    except:
                        break
                    else:
                        innerCounter += 1
                
                #Make the active element on
                temporary[outerCounter][temporary[outerCounter][0] + 1][1] = 1
            
        except:
            break
        outerCounter += 1    


def change_matchColumn(counter, add):

    index = 0

    try:
        temporary[counter + add][temporary[counter][0] + 1] == None
    except:
        while(True):
            try:
                temporary[counter + add][temporary[counter][0] - index] == None
            except:
                index += 1
            else:
                temporary[counter + add][0] = temporary[counter][0] - (index + 1)
                break
    else:
        temporary[counter + add][0] = temporary[counter][0]
    
    
    temporary[counter][0] = 0
        
def change(direction):

    #0: left, 1: right, 2: up, 3: down
    
    counter = 0
    
    while(True):
        try:
            #Find the active element
            if temporary[counter][0] != 0:
                
                #Move Left
                if direction == 0:
                    if temporary[counter][0] == 1:
                        temporary[counter][0] = 1
                    else:
                        temporary[counter][0] = temporary[counter][0] - 1
                        
                #Move Right
                elif direction == 1:
                    try:
                        #Difficult to understand because 2 represents the second element, but in pure index 2 means the first element.
                        #Everytime we try to use the element number as index, we need to + 1
                        temporary[counter][temporary[counter][0] + 2] == None 
                    except:
                        break
                    temporary[counter][0] = temporary[counter][0] + 1
                
                #Move Down
                elif direction == 3:
                    
                    #Try if I can get LOWER
                    try:
                        temporary[counter + 1][0] = 1
                    except:
                        break
                    
                    change_matchColumn(counter, 1)

                    break
                
                #Move Up
                elif direction == 2:
                    
                    #Try if I can get HIGHER
                    if counter - 1 < 0:
                        break
                    
                    change_matchColumn(counter, -1)
                    
                    break
                    
                break               
            
        except:
            break
        counter += 1
            
#Clear console
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

#Draw spacing
def spacing():
    print("")

#Center given word and put space around it to make it given length
def center(word, length):
    space = length - len(word[0])
    
    spaceB = ""
    for x in range(space // 2):
        spaceB = spaceB + " "

    spaceE = ""
    for x in range(space - (space // 2)):
        spaceE = spaceE + " "
    
    return ANSI(word[2]) + ANSI(word[1]) + spaceB + word[0] + spaceE  + ANSI(0) + ANSI(97)
    

#Draw text
def matrix_text(test):

    outerCounter = 0
    innerCounter = 2
    while (True):
        try:
            outString = test[outerCounter][1]
            
            #Now find how much space needs to be added
            spaces = ""
            for x in range(15-len(outString)):
              spaces = spaces + " "
              
            outString = outString + spaces
            
            while(True):
                try:
                
                    if test[outerCounter][0] == innerCounter - 1:
                        outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 102], 8) + ANSI(0) + ANSI(97) + " "
                    else:
                        if test[outerCounter][innerCounter][1] == 1:
                            outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 41], 8) + ANSI(0) + ANSI(97) + " "
                        else:
                            outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 0], 8) + ANSI(0) + ANSI(97) + " "
                    
                    innerCounter += 1
                except:
                    innerCounter = 2
                    break

            #Complete string and print it
            outString = "\n" + outString
            print (outString)
            outerCounter += 1
        except:
            break;

def oneSide(content):
    content = " " + content + " "
    print (ANSI(configuration[0][0]) + ANSI(configuration[0][1]) + content + ANSI(0) + ANSI(configuration[0][0]))
    
def twoSide(content):
    content[0] = " " + content[0]
    content[1] = content[1] + " "

    spaces = ""
    for x in range(windowWidth-len(content[1])-len(content[0])):
        spaces = spaces + " "

    print (ANSI(configuration[0][0]) + ANSI(configuration[0][1]) + content[0] + spaces + content[1] + ANSI(0) + ANSI(configuration[0][0]))
    
#Draw normal text
def text(left = None, right = None):
    left[0] = " " + left[0]

    if right == None:
        print (ANSI(left[1])+ ANSI(left[2]) + left[0] + ANSI(0) + ANSI(97))
    else:
        right[0] = right[0] + " "
        spaces = ""
        for x in range(windowWidth-len(right[0])-len(left[0])):
          spaces = spaces + " "
        print (ANSI(left[1])+ ANSI(left[2]) + left[0] + spaces + right[0] + ANSI(0) + ANSI(97))

#Draw a seperator across whole width
def seperator():

    lineString = ""
    for x in range(windowWidth):
        lineString = lineString + "_"

    print(ANSI(int(configuration[0][1])-10) + lineString + ANSI(0) + ANSI(configuration[0][0]))

def menuDisplay(content):
    
    #Correct "abbreviation"
    if len(content[0]) > 2:
        content[0] == "xx"
    elif len(content[0]) == 1:
        content[0] = content[0] + " "

    #Find string lengths
    lengthDetail = len(content[1])
    lengthAbbrevation = len(content[0]) + 2

    #Indent variable
    spaces = ""
    for x in range((windowWidth // 2 - 2)-lengthAbbrevation-lengthDetail):
      spaces = spaces + " "

    #Form strings
    content[0] = ANSI(configuration[0][0])+ ANSI(configuration[0][1]) + " " + content[0] + " "
    content[1] = ANSI(0)+ ANSI(configuration[0][0]) + " " + content[1] + spaces

    #NEED TO CALCULATE VARIABLE
    
    print(content[0] + content[1] + content[2] + ANSI(0) + ANSI(configuration[0][0]))

#Draw a list with an abbreviation, a detail and a status
def list(abbreviation, detail, status):

    #Correction "abbreviation"
    if len(abbreviation) > 2:
        abbreviation == "xx"
    elif len(abbreviation) == 1:
        abbreviation = abbreviation + " "

    #Find string lengths
    lengthDetail = len(detail)
    lengthAbbrevation = len(abbreviation) + 2

    #Indent status
    spaces = ""
    for x in range((windowWidth // 2 - 2)-lengthAbbrevation-lengthDetail):
      spaces = spaces + " "

    #Form strings
    abbreviation = ANSI(41)+ ANSI(97) + " " + abbreviation + " "
    detail = ANSI(0)+ ANSI(97) + " " + detail + spaces
    
    print(abbreviation + detail + status + ANSI(0) + ANSI(97))

configuration = ReadFile.configuration("configuration.b3d")

#COLORS
#Text-Color         configuration[0][0]
#Background-Color   configuration[0][1]
#OK                 configuration[0][2]
#Fail               configuration[0][3]
#Alert              configuration[0][4]
