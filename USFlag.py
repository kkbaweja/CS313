
#  File: USFlag.py
#  Description: A program that draws the american flag 
#  Student's Name: Keerat Baweja 
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 9/12/2016
#  Date Last Modified: 9/16/2016

import math 
import turtle
ttl = turtle.Turtle()

# Method to draw rectangle
def drawRectangle(self, width, height, startx, starty):
    self.penup()
    self.goto(startx, starty)
    self.pendown()
    self.forward(width)
    self.left(90)
    self.forward(height)
    self.left(90)
    self.forward(width)
    self.left(90)
    self.forward(height)
    self.penup()

# Method to draw starts
def drawWhiteStar(self, radius, startx, starty):
    self.penup()
    self.goto(startx, starty)
    counter = 0
    self.pendown()
    while counter < 5:
        self.right(144)
        self.forward(radius*(3/4))
        self.left(72)
        self.forward(radius*(3/4))
        counter += 1
    self.penup()

def main():
    ttl.speed(20)
    # Establish the height and width of the flag 
    height = int(input("Please enter vertical height (hoist) of the flag in pixels: "))
    width = 1.9*height
    
    # Print out correct screen size
    screen = turtle.Screen()
    screen.setup(width + 200, height + 200)

    # Draw flag rectangle 
    drawRectangle(ttl, width, height, -width/2, -height/2)

    # Draw stripes 
    ttl.fillcolor("red")
    counter = -height
    while counter <= height:
        ttl.home()
        ttl.begin_fill()
        drawRectangle(ttl, width, height/13, -width/2, counter/2)
        ttl.end_fill()
        counter += 4*(height/13)

    # Draw canton
    ttl.fillcolor("blue")
    ttl.begin_fill()
    cantonWidth = width*(2/5)
    cantonHeight = height*(7/13)
    drawRectangle(ttl, cantonHeight, cantonWidth, -width/2, height/2)
    ttl.end_fill()

    # Draw stars
    ttl.fillcolor("white")
    y = height/2 - (cantonHeight/10)*(3/4)
    ycounter = 0
    ttl.home()
    for ycounter in range(9):
        # draw six stars for all even rows 
        if ycounter % 2 == 0:
            x = -(width/2) + (cantonWidth)*(3/24)
            for xcounter in range(6):
                ttl.begin_fill()
                drawWhiteStar(ttl, ((height/13)*(4/5))/2, x, y)
                x += (cantonWidth/12)*2
                ttl.end_fill()
        # draw five stars of all odd rows
        else:
            x = -(width/2) + (cantonWidth)*(5/24)
            for xcounter in range(5):
                ttl.begin_fill()
                drawWhiteStar(ttl, ((height/13)*(4/5))/2, x, y)
                x += (cantonWidth/12)*2
                ttl.end_fill()
        y -= cantonHeight/10
        ycounter += 1
    
main()
