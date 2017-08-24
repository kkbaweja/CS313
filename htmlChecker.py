#  File: htmlChecker.py
#  Description: A program that checks tags in html code to ensure that they match up 
#  Student's Name: Keerat Baweja        
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 51320

#  Date Created: 10/07/2016
#  Date Last Modified: 10/07/2016

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty (self):
        return self.items == []
    def size (self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

def getTag(file):
    isTag = False
    char = file.read(1)
    tag = ""
    while char != "":
        if (char == ">" and isTag) or (char == " " and isTag):
            isTag = False
            return tag
        if isTag:
            tag = tag + char
        if char == "<":
            isTag = True
        char = file.read(1)
    return("Done")
    
def main():
    inputfile = open('htmlfile.txt', 'r')

    # Create list of tags
    tagList = []
    VALIDTAGS = []
    EXCEPTIONS = ["meta", "hr", "br", "link", "input", "img"]
    foundTag = getTag(inputfile)
    while foundTag != "Done":
        tagList.append(foundTag)
        foundTag = getTag(inputfile)

    print(tagList, "\n")

    # Check tags
    tagStack = Stack()
    for element in tagList:
        # Check if tag is an exception 
        if element in EXCEPTIONS:
            print("Tag", element, "does not need to match: stack is still", tagStack)
            if element not in VALIDTAGS:
                VALIDTAGS.append(element)
            continue
        # Check if ending tag
        if element[0] == "/":
            if element[1:] == tagStack.peek():
                tagStack.pop()
                print("Tag", element, "matches top of stack: stack is now", tagStack, "\n")
            else:
                print("Mismatch error: Tag is", element, "but the top of the stack is", tagStack.peek(), "\n")
                return()
        # Check if starting tag 
        else:
            if element not in VALIDTAGS:
                VALIDTAGS.append(element)
                print("New tag", element, "found and added to list of valid tags")
            tagStack.push(element)
            print("Tag", element, "pushed: stack is now", tagStack, "\n")

    # Print Output
    if tagStack.items == []:
        print("Processing complete. No mismatches found.")
    else:
        print("Processing complete. Unmatched tages remain on stack:", tagStack)


    VALIDTAGS.sort()
    EXCEPTIONS.sort()
    print("\n\nThese are the valid tags:\n", VALIDTAGS)
    print("These are the exceptions:\n", EXCEPTIONS)
        
    inputfile.close()

main()
