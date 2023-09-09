import turtle as turt
from math import cos
from math import pi

lt = turt.Turtle()

lt.speed(15)

def house(size, turt, x, y):
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

def star(size, turt, x, y):
    turt.pencolor("white")
    turt.setpos(x, y)
    turt.pencolor("green")
    for i in range(0,9):
        turt.right(110)
        turt.forward(size)
        turt.left(70)
        turt.forward(size)
        
def fullCircle(size, turt, x, y):
    turt.pencolor("white")
    turt.setpos(x, y)
    turt.pencolor("blue")
    for i in range(0, 360):
        turt.right(1)
        turt.forward(size)
        turt.right(89)
        turt.forward(150)
        turt.left(179)
        turt.forward(150)
        
# star(30, lt, -200, 200)      
    
 # house(100, lt, 200, 125)

fullCircle(2, lt, 30, 30)