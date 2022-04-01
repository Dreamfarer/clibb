import os

def ANSI(code):
    return "\33[{code}m".format(code=code)

windowWidth = 50

#Word string is always: ["Word", font-color, background-color]

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
    
    return ANSI(word[1]) + ANSI(word[2]) + spaceB + word[0] + spaceE  + ANSI(0) + ANSI(97)
    

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
                    if test[outerCounter][innerCounter][1] == 1:
                        outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 41], 8) + ANSI(0) + ANSI(97) + " "
                    else:
                        outString = outString + center([str(test[outerCounter][innerCounter][0]), 97, 0], 8) + ANSI(0) + ANSI(97) + " "
                    
                    innerCounter += 1
                except:
                    innerCounter = 2
                    break

            #Complete string and print it   
            print (outString)
            outerCounter += 1
        except:
            break;
    

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

    print(ANSI(0) + ANSI(31) + lineString + ANSI(40) + ANSI(97))

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
