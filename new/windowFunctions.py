import os
import sys

import ReadFileRecursive

global nameCounter
global moduleCounter
global currentConfiguration

#import dependent on OS
if os.name in ('nt', 'dos'):
    from subprocess import CREATE_NEW_CONSOLE
    import msvcrt
else:
    import tty
    import termios

def ANSI(mode, codeR = None, codeG = None, codeB = None):

    #Trigger only if first argument is filled
    if codeR is None and codeG is None and codeB is None:
        return "\33[{code}m".format(code=mode)
    
    #Trigger only if every RGB argument is filled
    elif not codeR is None and not codeG is None and not codeB is None:
        #mode 0: Foreground, mode 1: Background
        if mode == 0:
            return "\u001b[38;2;{r};{g};{b}m".format(r=codeR, g=codeG, b=codeB)
        else:
            return "\u001b[48;2;{r};{g};{b}m".format(r=codeR, g=codeG, b=codeB)
    else:
        return "Wrong argument!"
        

windowWidth = 50

#Clear console
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)



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

#Translate name to array index and insert it
def window(name):

    clear()
    
    global nameCounter
    nameCounter = 1
    
    while (True):
        try:
            if configuration[nameCounter][-1] == name:
                break
            else:
                nameCounter += 1
        except:
            print ("Nothing found! Please check spelling!")
            return

    
    global moduleCounter
    moduleCounter = 0
    
    while (True):
        try:
            if configuration[nameCounter][moduleCounter] == "Seperator-Filled":
                seperator()
            elif configuration[nameCounter][moduleCounter] == "Seperator-Empty":
                spacing()
            else:
                match configuration[nameCounter][moduleCounter][-1]:
                    case "Two-Side":
                        twoSide(configuration[nameCounter][moduleCounter][0])
                    case "One-Side":
                        oneSide(configuration[nameCounter][moduleCounter][0])
                    case "Display":
                        display(configuration[nameCounter][moduleCounter][0])
                    case "Menu":
                        menu(configuration[nameCounter][moduleCounter][0])
                    case "Menu-Display":
                        menuDisplay(configuration[nameCounter][moduleCounter][0])
                    case "Configuration":
                        global currentConfiguration
                        currentConfiguration = moduleCounter
                        matrix_text(configuration[nameCounter][moduleCounter])
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

def accept():

    outerCounter =0
    innerCounter = 2
    
    while(True):
        try:
            #Find the active element
            if configuration[nameCounter][1][currentConfiguration][1][outerCounter][0] != 0:
                
                #Make every other element to off first
                while(True):
                    try:
                        configuration[nameCounter][1][currentConfiguration][1][outerCounter][innerCounter][1] = 0
                    except:
                        break
                    else:
                        innerCounter += 1
                
                #Make the active element on
                configuration[nameCounter][1][currentConfiguration][1][outerCounter][configuration[nameCounter][1][currentConfiguration][1][outerCounter][0] + 1][1] = 1
            
        except:
            break
        outerCounter += 1    


def change_matchColumn(counter, add):
    
    index = 0
    
    try:
        configuration[nameCounter][currentConfiguration][counter + add][configuration[nameCounter][currentConfiguration][counter][0] + 1] == None
    except:
        while(True):
            try:
                configuration[nameCounter][currentConfiguration][counter + add][configuration[nameCounter][currentConfiguration][counter][0] - index] == None
            except:
                index += 1
            else:
                configuration[nameCounter][currentConfiguration][counter + add][0] = configuration[nameCounter][currentConfiguration][counter][0] - (index + 1)
                break
    else:
        configuration[nameCounter][currentConfiguration][counter + add][0] = configuration[nameCounter][currentConfiguration][counter][0]
    configuration[nameCounter][currentConfiguration][counter][0] = 0
        
def change(direction):

    #0: left, 1: right, 2: up, 3: down
    
    counter = 0
    
    while(True):
        try:
            #Find the active element
            if configuration[nameCounter][currentConfiguration][counter][0] != 0:
                
                #Move Left
                if direction == 0:
                    
                    if configuration[nameCounter][currentConfiguration][counter][0] == 1:
                        configuration[nameCounter][currentConfiguration][counter][0] = 1
                    else:
                        configuration[nameCounter][currentConfiguration][counter][0] = configuration[nameCounter][currentConfiguration][counter][0] - 1
                        
                #Move Right
                elif direction == 1:
                    try:
                        #Difficult to understand because 2 represents the second element, but in pure index 2 means the first element.
                        #Everytime we try to use the element number as index, we need to + 1
                        configuration[nameCounter][currentConfiguration][counter][configuration[nameCounter][currentConfiguration][counter][0] + 2] == None 
                    except:
                        break
                    configuration[nameCounter][currentConfiguration][counter][0] = configuration[nameCounter][currentConfiguration][counter][0] + 1
                
                #Move Down
                elif direction == 3:
                    
                    #Try if I can get LOWER
                    try:
                        configuration[nameCounter][currentConfiguration][counter + 1][0] = 1
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
            
#Draw text
def matrix_text(test):

    outerCounter = 0
    innerCounter = 2
    
    while (True):
        try:
            if outerCounter == len(test)-1:
                break
            
            outString = test[outerCounter][1]
            
            spaces = ""
            for x in range(15-len(outString)):
              spaces = spaces + " "
              
            outString = outString + spaces

            #Iterate over every field of one menu row
            while(True):
                try:
                    #If field is active, turn it green
                    if test[outerCounter][0] == innerCounter - 1:
                        outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 102], 8) + ANSI(0) + ANSI(97) + " "
                    else:
                        #If field is ON, turn it red
                        if test[outerCounter][innerCounter][1] == 1:
                            outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 41], 8) + ANSI(0) + ANSI(97) + " "
                        #If field is OFF, remove all colors
                        else:
                            outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 0], 8) + ANSI(0) + ANSI(97) + " "
                    
                    innerCounter += 1
                except:
                    innerCounter = 2
                    break

            #Complete string and print it
            if outerCounter != 0:
                outString = "\n" + outString
            print (outString)
            outerCounter += 1
        except:
            break;
 
def display(inputContent):
    content = [" " + inputContent[0], inputContent[1]]
    
    #Indent variable
    spaces = ""
    for x in range((windowWidth // 2 - 2)-len(inputContent[0])):
      spaces = spaces + " "

    print (content[0] + spaces + content[1] + ANSI(0) + ANSI(configuration[0][0]))

def oneSide(inputContent):

    #Pass into new list because we don't want to alter the original
    content = " " + inputContent + " "

    print (ANSI(configuration[0][0]) + ANSI(configuration[0][1]) + content + ANSI(0) + ANSI(configuration[0][0]))
 
def twoSide(inputContent):

    #Pass into new list because we don't want to alter the original
    content = [" " + inputContent[0], inputContent[1] + " "]

    spaces = ""
    for x in range(windowWidth-len(content[1])-len(content[0])):
        spaces = spaces + " "

    print (ANSI(configuration[0][0]) + ANSI(configuration[0][1]) + content[0] + spaces + content[1] + ANSI(0) + ANSI(configuration[0][0]))

def spacing():
    print("")
    
def seperator():

    lineString = ""
    for x in range(windowWidth):
        lineString = lineString + "_"

    print(ANSI(int(configuration[0][1])-10) + lineString + ANSI(0) + ANSI(configuration[0][0]))

def menu(inputContent):
    #Pass into new list because we don't want to alter the original
    content = [inputContent[0], inputContent[1]]

    #Correct "abbreviation"
    if len(content[0]) > 2:
        content[0] == "xx"
    elif len(content[0]) == 1:
        content[0] = content[0] + " "

    #Form string and print it
    content[0] = ANSI(configuration[0][0])+ ANSI(configuration[0][1]) + " " + content[0] + " "
    content[1] = ANSI(0)+ ANSI(configuration[0][0]) + " " + content[1]
    print(content[0] + content[1] + ANSI(0) + ANSI(configuration[0][0]))

def menuDisplay(inputContent):

    #Pass into new list because we don't want to alter the original
    content = [inputContent[0], inputContent[1], inputContent[2]]
    
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

global configuration
configuration = ReadFileRecursive.captureArray("configurationRecursive.b3d")

print (configuration[0])
input()

def testWindow():

    window("window_configuration")

    character = getch()
    if character == "e":
        return
    elif character == "d":
        change(1)
    elif character == "a":
        change(0)
    elif character == "s":
        change(3)
    elif character == "w":
        change(2)
    elif character == "q":
        accept()
    testWindow()
    
#testWindow()

#COLORS
#Text-Color         configuration[0][0]
#Background-Color   configuration[0][1]
#OK                 configuration[0][2]
#Fail               configuration[0][3]
#Alert              configuration[0][4]
