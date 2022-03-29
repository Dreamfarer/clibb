import os
import requests

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style(code):
        return "\33[{code}m".format(code=code)
  
    def color(code):
        return "\33[{code}m".format(code=code)

#Printer
def printer(text, backgroundColor, textColor):
    print(ANSI.background(backgroundColor) + ANSI.color(textColor) + text + ANSI.background(40) + ANSI.color(97))

#Clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

#main-main_oneside
def main_oneside(left):
    left[0] = " " + left[0]
    print (ANSI.background(left[1])+ ANSI.color(left[2]) + left[0])

#main-main_twoside
def main_twoside(left, right):
    right[0] = right[0] + " "
    left[0] = " " + left[0]

    #Calculate Spaces
    spaces = ""
    for x in range(50-len(right[0])-len(left[0])):
      spaces = spaces + " "
    print (ANSI.background(left[1])+ ANSI.color(left[2]) + left[0] + spaces + right[0])

#main-line
def main_line(mode):

    if mode == 0:    
        printer("__________________________________________________", 40, 31)
    elif mode == 1:
        print("")
        printer("__________________________________________________", 40, 31)
    elif mode == 2:
        printer("__________________________________________________", 40, 31)
        print("")

#main-list
def main_list(abbreviation, detail, status):

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
    for x in range(23-lengthAbbrevation-lengthDetail):
      spaces = spaces + " "

    #Form strings
    abbreviation = ANSI.background(41)+ ANSI.color(97) + " " + abbreviation + " "
    detail = ANSI.background(40)+ ANSI.color(97) + " " + detail + spaces
    
    print(abbreviation + detail + status)
