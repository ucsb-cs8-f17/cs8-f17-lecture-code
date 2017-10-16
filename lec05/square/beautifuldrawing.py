# my beautiful drawing

import turtle
import drawSquare

from drawSquare import square

fred = turtle.Turtle("turtle")
fred.color("green")

fred.up()
fred.goto(100,100)
fred.down()
square(fred,50)

sheila = turtle.Turtle("turtle")
sheila.color("blue")
sheila.up()
sheila.goto(-100,-100)
sheila.down()
drawSquare.pentagon(sheila,50)
