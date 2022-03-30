import os

def ANSI(code):
    return "\33[{code}m".format(code=code)

windowWidth = 50

#Clear console
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

#Draw normal text
def normal(left = None, right = None):
    left[0] = " " + left[0]

    if right == None:
        print (ANSI(left[1])+ ANSI(left[2]) + left[0] + ANSI(0) + ANSI(97))
    else:
        right[0] = right[0] + " "
        spaces = ""
        for x in range(windowWidth-len(right[0])-len(left[0])):
          spaces = spaces + " "
        print (ANSI(left[1])+ ANSI(left[2]) + left[0] + spaces + right[0] + ANSI(0) + ANSI(97))

#Draw a line across whole width
def line(mode):

    lineString = ""
    for x in range(windowWidth):
        lineString = lineString + "_"

    if mode == 0:
        print(ANSI(0) + ANSI(31) + lineString + ANSI(40) + ANSI(97))
    elif mode == 1:
        print(ANSI(0) + ANSI(31) + "\n" + lineString + ANSI(40) + ANSI(97))
    elif mode == 2:
        print(ANSI(0) + ANSI(31) + lineString + "\n" + ANSI(40) + ANSI(97))

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
