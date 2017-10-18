import turtle

import drawSquare
import random
import sys

colors = ["black"]

def drawRandomSquare(t):
    theColor = random.choice(colors)
    print("We chose",theColor)
    t.color(theColor)
    sizeOfSquare=random.randint(50,100)
    drawSquare.square(fred,sizeOfSquare)

if __name__=="__main__":
    colors += sys.argv[1:]
    fred = turtle.Turtle("turtle")
    fred.speed(0)
    for i in range(10):
        fred.up()
        fred.goto(random.randint(-100,100),
                  random.randint(-100,100))
        fred.down()
        drawRandomSquare(fred)
    x = input("press return")
