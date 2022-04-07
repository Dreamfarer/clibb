#always import
import os

content = open("configuration.b3d").read()
data = [""]

levelCounter = 0
mainCounter = 0

colors = []
temporary = ""
temp2 = ["", ""]
inhalt = []

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
                temporary += content[x]
            else:
                colors.append(temporary)
                temporary = ""

    #Capture configuration window
    if mainCounter == 3 and levelCounter == 2:
        if content[x] != " " and content[x] != "\n":
            
            if content[x] == ",":
                inhalt.append(temp2[0])
                inhalt.append(temp2[1])

                testus = [temp2[0], temp2[1]]
                
                temp2[0] = ""
                temp2[1] = ""

                if testus[0] == "Two-Side":
                    array = [""]
                    counter = 0
                    for i in range(len(temp2[1]))
                        if 




                #print (testus[1])


                
            else:
                temp2[0] += content[x]
            
    if mainCounter == 3 and levelCounter == 3:
        temp2[1] += content[x]


#print (inhalt)
input()
