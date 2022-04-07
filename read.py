#always import
import os

content = open("configuration.b3d").read()

levelCounter = 0
mainCounter = 0

colors = []

#Top array containing all data
windowContents = []

#Inner string that holds type and content for one line until it gets formated and eventually passed to the top array
windowContentsOneLine = ["", ""] 

tempStringColors = ""

for x in range(len(content)):

    if content[x] == "{":
        levelCounter += 1

        if levelCounter == 1:
            mainCounter += 1
            #print(mainCounter)
        continue
        
    if content[x] == "}":
        levelCounter -= 1
        continue

    #Capture Colors
    if mainCounter == 1 and levelCounter == 1:
        if content[x] != " " and content[x] != "\n":
            
            if content[x] != ",":
                tempStringColors += content[x]
            else:
                colors.append(tempStringColors)
                tempStringColors = ""

    #Capture configuration window
    if mainCounter == 3 and levelCounter == 2:
        if content[x] != " " and content[x] != "\n":
            
            #Line does always end with ",". Proceed to format and store this line 
            if content[x] == ",":
                
                
                #Temporary variables until passed to top array
                tempContents = [""]
                tempContentsString = ""
                
                #Dependent on which type is wanted, format the string differently
                if windowContentsOneLine[0] == "Two-Side" or windowContentsOneLine[0] == "One-Side" or windowContentsOneLine[0] == "Display" or windowContentsOneLine[0] == "Menu" or windowContentsOneLine[0] == "Menu-Display":
                    for i in range(len(windowContentsOneLine[1]))
                        if windowContentsOneLine[1][i] == ",":
                            tempContents.append(tempContentsString)
                            tempContentsString = ""
                        else:
                            tempContentsString += windowContentsOneLine[1][i]
                            
                if windowContentsOneLine[0] == "Configuration":
                    print("Not Ready! LOL")
                
                if tempContents == [""]:
                    windowContents.append(windowContentsOneLine[0])
                else:
                    windowContents.append([windowContentsOneLine[0], tempContents])
                
                windowContentsOneLine[0] = ""
                windowContentsOneLine[1] = ""

            else:
                windowContentsOneLine[0] += content[x]
            
    if mainCounter == 3 and levelCounter >= 3:
        windowContentsOneLine[1] += content[x]


#print (windowContents)
input()
