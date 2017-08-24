#  File: Queens.py
#  Description: A program that solves the Eight Queens Problem 

#  Student's Name: Keerat Baweja        
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 11/10/2016
#  Date Last Modified: 11/10/2016

# Class that holds the value for location of queen 
class Queen():
    def __init__(self,row,col):
        self.row = row
        self.col = col
        
class QueensProblem():
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = []
        self.queens = []
        self.solution = 1
        for i in range(0, self.boardSize):
            temp = []
            for j in range (0, self.boardSize):
                temp.append("*")
            self.board.append(temp)
            
    def __str__(self):
        for i in range(0, self.boardSize):
            for j in range(0, self.boardSize):
                print(self.board[i][j], "", end = "")
            print("")
        return("")
    
    # Adds queen to a location in the board 
    def addQueen(self, row, col):
        queen = Queen(row, col)
        self.queens.append(queen)

        self.board[row].insert(col,"Q")
        self.board[row].pop(col+1)

    # Removes from a location in a board 
    def removeQueen(self):
        queen = self.queens.pop()
        self.board[queen.row].insert(queen.col,"*")
        self.board[queen.row].pop(queen.col + 1)
    
    # Checks that a space in valid 
    def isValidPlace(self, row, col):
        valid = True
        for queen in self.queens:
            if queen.row == row or queen.col == col:
                valid = False
            if abs(queen.row - row) == abs(queen.col-col):
                valid = False
        return(valid)

    # Solves the either queens problem 
    def solve(self, n):
        correct = False
        position = self.boardSize - n
        
        # Checks base case 
        for i in range(self.boardSize):
            if position == self.boardSize - 1:
                if self.isValidPlace(i,position):
                    self.addQueen(i, position)
                    print("Solution #" + str(self.solution))
                    print(self)
                    self.solution += 1
                    self.removeQueen()
            else:
                if self.isValidPlace(i,position):
                    self.addQueen(i, position)
                    correect = self.solve(n-1)

        if correct == False:
            if position == 0:
                return(False)
            else:
                self.removeQueen()
                return(False)

def main():
    # Prompt the user for valid input 
    boardSize = int(input("Enter the size of the square board: "))
    while boardSize < 4:
        print("Invalid input.")
        boardSize = int(input("Enter the size of the square board: "))

    # Create new instance of problem
    myBoard = QueensProblem(boardSize)
    myBoard.solve(boardSize)

main()
