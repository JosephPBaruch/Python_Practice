'''
    Joseph Baruch
    CS 212
    Turtle Module : Assignmnet 2
    Due: 9/11/2023
'''

import turtle as t
from math import cos
from math import pi

# --- Turtle Instances ---
starT = t.Turtle()

houseT = t.Turtle()

donutT = t.Turtle()

cylinderT = t.Turtle()

quadT = t.Turtle()

# ---- Function Definitions ------

def house(size, turt, x, y):
    turt.width(5)
    turt.speed(15)
    turt.pencolor("white")
    turt.setpos(x-15, y-15)
    turt.pencolor("blue")
    turt.left(90)
    turt.forward(size)
    turt.right(45)
    turt.forward(size * cos(45 * (pi/180))) # cosine uses radians as default
    turt.right(90)
    turt.forward(size * cos(45 * (pi/180))) # cosine uses radians as default
    turt.right(45)
    turt.forward(size)
    turt.right(90)
    turt.forward(size)
''' house
    - This function draws a donut by essentially drawing a 
      circle by moving toward the enter every angle change. 
    - The inputs are the instance of turtle used (houseT), 
      And its coordinates relative to (0,0) used to move
      The turtle to its starting position to draw. It also
      an input for the size of the walls of the house (also
      used for the calculation of the roof walls). 
'''

def star(turt, x, y):
    turt.width(5)
    turt.speed(15)
    turt.pencolor("white")
    turt.setpos(x, y)
    turt.pencolor("green")
    for i in range(0,9):
        turt.right(110)
        turt.forward(30)
        turt.left(70)
        turt.forward(30)
''' star
    - This function draws a star by using a for loop to 
      draw the points of the star while linking them together.
    - The inputs are the instance of turtle used (starT), 
      And its coordinates relative to (0,0) used to move
      The turtle to its starting position to draw.
'''

def donut(turt, x, y):
    turt.speed(15)
    turt.pencolor("white")
    turt.setpos(x, y)
    turt.pencolor("red")
    turt.width(20)
    for i in range(0, 180):
        turt.right(1)
        turt.forward(2)
        turt.right(91)
        turt.forward(60)
        turt.left(179)
        turt.forward(60)
        turt.right(89)
    turt.width(5)
''' donut
    - This function draws a donut by essentially drawing a 
      circle by moving toward the enter every angle change. 
    - The inputs are the instance of turtle used (donutT), 
      And its coordinates relative to (0,0) used to move
      The turtle to its starting position to draw.
'''

def cylinder(tur, x, y):
    tur.pencolor("white")
    tur.setpos(x, y)
    tur.pencolor("orange")
    tur.width(5)
    tur.speed(15)
    for i in range(0, 90):
        tur.right(1)
        tur.forward(1)
    tur.right(90)
    for i in range(0, 90):
        tur.right(1)
        tur.forward(1)
    tur.left(135)
    tur.forward(60)
    tur.left(45)
    for i in range(0, 90):
        tur.left(1)
        tur.forward(1)
    tur.left(45)
    tur.forward(60)
''' cylinder
    - This function draws a 3D cylinder in orange. 
      It uses quarder circles to make ovals and straight
      line. 
    - The inputs are the instance of turtle used (cylinderT), 
      And its coordinates relative to (0,0) used to move
      The turtle to its starting position to draw.
'''
        
def quad(turt):
    turt.width(5)
    turt.speed(15)
    for i in range(0, 4):
        turt.right(90)
        turt.forward(1000)
        turt.backward(1000)    
''' quad
    - This function draws the lines seperating 
      the four different quadrants of the turtle
      drawing window. 
    - The input is the instance of turtle used (quadT).

'''

# ----- Calling the Functions --------
        
star(starT, -200, 200)      
    
house(100, houseT, 200, 125)

donut(donutT, 250, -125)

cylinder(cylinderT, -250, -125)

quad(quadT)