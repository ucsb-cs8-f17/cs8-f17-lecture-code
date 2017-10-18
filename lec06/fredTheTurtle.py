import turtle

import drawSquare
import random

colors = ["blue","purple","green","pink",
          "magenta","cyan"]


def drawRandomSquare(t):
    theColor = random.choice(colors)
    print("We chose",theColor)
    t.color(theColor)
    sizeOfSquare=random.randint(50,100)
    drawSquare.square(fred,sizeOfSquare)

if __name__=="__main__":
    fred = turtle.Turtle("turtle")
    fred.speed(0)
    for i in range(10):
        fred.up()
        fred.goto(random.randint(-100,100),
                  random.randint(-100,100))
        fred.down()
        drawRandomSquare(fred)
