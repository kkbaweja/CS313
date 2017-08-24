#  File: Circular.py
#  Description: A program that plays Hot Potato with circular lists

#  Student's Name: Keerat Baweja        
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 10/20/2016
#  Date Last Modified: 10/20/2016

# class tht defines a Node 
class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return(self.data)
    
    def getNext(self):
        return(self.next)
    
    def setData(self, newData):
        self.data = newData
        
    def setNext(self, newNext):
        self.next = newNext

# class that defines a Circular List
class CircularList():
    # Create a circular list 
    def __init__(self):
        sentinel = Node(None) 
        self.head = sentinel
        sentinel.setNext(self.head)

    # Check and see if there is only one node in the list 
    def onlyOneNode(self):
        temp = self.head.getNext()
        return (self.head.getNext() == temp) and (temp.getNext() == self.head)
        
    # Check to see if the list in empty 
    def isEmpty(self):
        return self.head.getNext() == None  
    
    # Add an item to the list 
    def add(self, item):
        temp = Node(item)
        if self.head.getNext == None:
            temp = Node(item)
            self.head.setnext(temp)
            temp.setNext(self.head)
        else:
            current = self.head.getNext()
            previous = self.head
            while current != self.head:
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(self.head)
        
    # Remove an item from a list 
    def remove(self, current, previous):
        previous.setNext(current.getNext())

    # Print a list 
    def __str__(self):
        current = self.head.getNext()
        counter = 0
        if self.isEmpty():
            print("List is Empty")
        while current != self.head:
            if current.getData() == None:
                current = current.getNext()
                continue
            print(current.getData(), "  ", end = "")
            counter += 1
            if counter == 10:
                print(end = "\n    ")
                counter = 0
            current = current.getNext()
        return("")
            
    # Method that plays the game of Hot Potato 
    def hit(self, hitNumber):
        current = self.head.getNext()
        previous = self.head
        counter0 = 1
        while not self.onlyOneNode():
            counter = 1
            while counter < hitNumber:
                previous = current 
                current = current.getNext()
                if current == self.head:
                    continue
                counter += 1
            print("Iteration number:", counter0)
            print("The person eliminated is:", current.getData())
            self.remove(current, previous)
            current = previous.getNext()
            if current.getData() == None:
                current = current.getNext()
            print("The people remaining are:", "\n", "  ", self)
            print("")
            counter0 += 1

def main():
    # Read in data from file 
    inputfile = open('HotPotatoData.txt', 'r')
    for line in inputfile:
        input = line.split()
        numPeople = int(input[0])
        hitNumber = int(input[1])
        
        # Create circular list of players
        counter = 0
        newList = CircularList()
        while counter < numPeople:
            name = inputfile.readline()
            name = name.replace("\n","")
            newList.add(name)
            counter += 1
        print("Number of people playing Hot Potato:", numPeople)
        print("Number of moves in each round:", hitNumber)
        print("People playing Hot Potato:\n   ", newList, "\n")

        # Play game of hot potato 
        newList.hit(hitNumber)
        print("The sole survivor is:", newList, "\n\n")

main()
