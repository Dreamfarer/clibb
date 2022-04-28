def captureArray_Recursion(counter, content):

    tempArray = []
    captureString = ""
    
    while True:

        #Only record the desired chracters. We will neglect e.g. "{" or "}"
        if not content[counter] == "\n" and not content[counter] == "\t" and not content[counter] == "{" and not content[counter] == "}":
            captureString += content[counter]

        #If there is a comma (",") we need to seperate the recorded characters
        if content[counter] == ",":
            captureString = captureString.strip()
            if not captureString[0:-1] == "":
                tempArray.append(captureString[0:-1])
            captureString = ""

        #Increment the counter which counts through every character of the file
        counter += 1

        #Open up a new recursion loop because we are digging deeper
        if content[counter] == "{":
            receive = captureArray_Recursion(counter, content)
            counter = receive[0]
            tempArray.append(receive[1])

        #Close recursion loop because there is nothing left at this level. Return the current counter and the built up array
        elif content[counter] == "}":

            captureString = captureString.strip()

            #If there is only one element, do not put it into an array
            if len(tempArray) == 0:
                return [counter, captureString]
            else:
                if not captureString == "":
                    tempArray.append(captureString)
                return [counter, tempArray]
    
def captureArray(filename):
    content = open(filename).read() #Read given file
    array = captureArray_Recursion(0, content)[1] #capture array

    return array
    
print (captureArray("configurationRecursive.b3d"))

x = input()
