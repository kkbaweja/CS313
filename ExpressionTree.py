#  File: ExpressionTree.py
#  Description: A program creates a tree and traverses it to evaluate a function
#  Student's Name: Keerat Baweja        
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 12/1/2016
#  Date Last Modified: 12/1/2016

# Class that defines binary tree
class BinaryTree(object):
    def __init__(self,initVal):
        self.data = initVal
        self.left = None
        self.right = None
        self.parent = None

    def insertLeft(self,newNode):
        t = BinaryTree(newNode)
        if self.left == None:
            self.left = t
        else:
            t.left = self.left
            self.left = t
        t.parent = self

    def insertRight(self,newNode):
        t = BinaryTree(newNode)
        if self.right == None:
            self.right = t
        else:
            t.right = self.right
            self.right = t
        t.parent = self
            
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data

    def createTree(self, expression):
        current = self
        operators = ["+", "-", "*", "/"]
        for element in expression:
            if element == ")":
                current = current.parent
            elif element == "(":
                current.insertLeft(0)
                current = current.getLeftChild()
            elif element in operators:
                current.setRootVal(element)
                current.insertRight(0)
                current = current.getRightChild()
            else:
                current.setRootVal(element)
                current = current.parent

    def preOrder(self, root):
        current = root
        print(current.getRootVal(), end = " ")
        if current.getLeftChild() != None:
            current.getLeftChild().preOrder(current.getLeftChild())
        if current.getRightChild() != None:
            current.getRightChild().preOrder(current.getRightChild())

    def postOrder(self, root):
        current = root
        if current.getLeftChild() != None:
            current.getLeftChild().postOrder(current.getLeftChild())
        if current.getRightChild() != None:
            current.getRightChild().postOrder(current.getRightChild())
        print(current.getRootVal(), end = " ")

    def evaluate(self, root):
        current = root
        operators = ["+", "-", "*", "/"]
        while current.getLeftChild() != None and current.getRightChild() != None: 
            if current.getLeftChild() != None:
                current.getLeftChild().evaluate(current.getLeftChild())
                  
            if current.getRootVal() in operators and current.getLeftChild().getRootVal() not in operators and current.getRightChild().getRootVal() not in operators:
                operator = current.getRootVal()
                if operator == "+":
                    current.setRootVal(float(current.getLeftChild().getRootVal()) + float(current.getRightChild().getRootVal()))
                    current.left = None
                    current.right = None
                if operator == "-":
                    current.setRootVal(float(current.getLeftChild().getRootVal()) - float(current.getRightChild().getRootVal()))
                    current.left = None
                    current.right = None
                if operator == "*":
                    current.setRootVal(float(current.getLeftChild().getRootVal()) * float(current.getRightChild().getRootVal()))
                    current.left = None
                    current.right = None
                if operator == "/":
                    current.setRootVal(float(current.getLeftChild().getRootVal()) / float(current.getRightChild().getRootVal()))
                    current.left = None
                    current.right = None
                  
            if current.getRightChild() != None:
                current.getRightChild().evaluate(current.getRightChild())
        
def main():
    inputfile = open('treedata.txt', 'r')
    for line in inputfile:
        print("Infix Expression: ", line)
        line = line.split()

        myTree = BinaryTree(0)
        myTree.createTree(line)
        myTree.evaluate(myTree)
        print("     Value:", myTree.getRootVal())
        myTree.createTree(line)
        print("     Prefix Expression:  ", end = "")
        myTree.preOrder(myTree)
        print("")
        print("     Postfix Expression:  ", end = "")
        myTree.postOrder(myTree)
        print("\n")
        
    inputfile.close()
    
main()
