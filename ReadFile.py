#always import
import os

def captureArray(passedContent):

    #Temporary variables until passed to top array
    tempContents = []
    tempContentsString = ""

    rowStart = False

    for i in range(len(passedContent)):

        if rowStart == False and (passedContent[i] != " " and passedContent[i] != "\n"):
            rowStart = True

        #Process row if it has ended
        if passedContent[i] == "\n" and (passedContent[i-1] == "," or passedContent[i-1] == "]"):

            tempInnerContents = []
            tempInnerContentsString = ""
            tempInnerLevelCounter = 0
            
            for a in range(len(tempContentsString)):

                if tempContentsString[a] == "," and tempInnerLevelCounter == 0:
                    if tempContentsString[a-1] != "]":
                        if tempInnerContentsString[0] == " ":
                            tempInnerContentsString = tempInnerContentsString[1:]
                        tempInnerContents.append(tempInnerContentsString)
                    tempInnerContentsString = ""
                elif tempContentsString[a] == "]" and tempInnerLevelCounter == 1:
                    
                    tempInnerLevelCounter -= 1
                    tempInnerInnerContents = []
                    tempInnerInnerContentsString = ""
                    
                    for b in range(len(tempInnerContentsString)):
                        if tempInnerContentsString[b] == ",":
                            if tempInnerInnerContentsString[0] == " ":
                                    tempInnerInnerContentsString = tempInnerInnerContentsString[1:]
                            tempInnerInnerContents.append(tempInnerInnerContentsString)
                            tempInnerInnerContentsString = ""
                        else:
                            tempInnerInnerContentsString += tempInnerContentsString[b]
                            if b == len(tempInnerContentsString)-1:
                                if tempInnerInnerContentsString[0] == " ":
                                    tempInnerInnerContentsString = tempInnerInnerContentsString[1:]
                                tempInnerInnerContents.append(tempInnerInnerContentsString)

                    tempInnerContents.append(tempInnerInnerContents)
                    
                elif tempContentsString[a] == "[":
                    tempInnerLevelCounter += 1
                else:
                    tempInnerContentsString += tempContentsString[a]

            tempContents.append(tempInnerContents)

            #Reset variables
            tempInnerContents = []
            tempInnerContentsString = ""
            tempContentsString = ""
            rowStart = False

        if rowStart == True:
            tempContentsString += passedContent[i]

    return tempContents

def captureText(passedContent):

    #Temporary variables until passed to top array
    tempContents = []
    tempContentsString = ""
    
    for i in range(len(passedContent)):
        #If there is a seperator (","), split the string and append it to the array
        if passedContent[i] == ",":
            tempContents.append(tempContentsString)
            tempContentsString = ""
        else:
            #Delete the space after a seperator (","), eg. "Test, ABC" -> "Test,ABC"
            if passedContent[i-1] != ",":
                tempContentsString += passedContent[i]
            #Append to array if line is finished
            if i == len(passedContent)-1:
                tempContents.append(tempContentsString)
    return tempContents

def configuration(filename):

    #Counters
    levelCounter = 0
    mainCounter = 0

    #Color
    colors = []
    tempStringColors = ""

    #Hierarchy from top array to bottom
    windows = [] #Array of all window configurations
    singleWindow = ["", []] #Array of a single window configuration
    singleWindowOneEntry = ["", ""] #Array of one single structure

    content = open(filename).read() #Read given file

    for fileIndex in range(len(content)):

        if content[fileIndex] == "{":
            levelCounter += 1
            if levelCounter == 1:
                mainCounter += 1
                if mainCounter == 1:
                    windows.append(colors) 
            continue
            
        if content[fileIndex] == "}":
            levelCounter -= 1
            if levelCounter == 1:
                windows.append([singleWindow[0], singleWindow[1]])
                singleWindow = ["", []]
            continue
        
        if levelCounter == 1 and mainCounter >= 2 and content[fileIndex] != " " and content[fileIndex] != "\n" and content[fileIndex] != ",":
            singleWindow[0] += content[fileIndex]

        #Capture Colors
        if mainCounter == 1 and levelCounter == 1:
            if content[fileIndex] != " " and content[fileIndex] != "\n":
                
                if content[fileIndex] != ",":
                    tempStringColors += content[fileIndex]
                else:
                    colors.append(tempStringColors)
                    tempStringColors = ""

        #Capture configuration window
        if mainCounter >= 2 and levelCounter == 2 and content[fileIndex] != " " and content[fileIndex] != "\n":
              
            #If line has ended (With separator ","), process it. PROBLEM IF LAST LINE, THERE IS NO ","
            if content[fileIndex] == ",":
                #print ("Last: " + content[fileIndex-1])
                
                #Temporary variables until passed to top array
                tempContents = []
                tempContentsString = ""
                
                #Dependent on which type is wanted, format the string differently
                if singleWindowOneEntry[0] == "Two-Side" or singleWindowOneEntry[0] == "One-Side" or singleWindowOneEntry[0] == "Display" or singleWindowOneEntry[0] == "Menu" or singleWindowOneEntry[0] == "Menu-Display":
                    tempContents = captureText(singleWindowOneEntry[1])        
                if singleWindowOneEntry[0] == "Configuration":
                    tempContents = captureArray(singleWindowOneEntry[1])

                #Add another dimension to array only if necessary
                if tempContents == []:
                    singleWindow[1].append(singleWindowOneEntry[0])
                else:
                    singleWindow[1].append([singleWindowOneEntry[0], tempContents])

                #Reset variables to use in next line
                singleWindowOneEntry[0] = ""
                singleWindowOneEntry[1] = ""

            else:
                singleWindowOneEntry[0] += content[fileIndex]
                
        if mainCounter >= 2 and levelCounter >= 3:
            singleWindowOneEntry[1] += content[fileIndex]

    return windows
