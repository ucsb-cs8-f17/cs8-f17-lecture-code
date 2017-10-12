# Learning goals
#* Modules and how to use them
#* Design functions that are READABLE,
# REUSABLE, and DRY (Don't repeat yourself)!

# Modules
# Group of  functions
# import name_module
# name_module.name_function

import turtle

jane= turtle.Turtle()
jane.shape("turtle")
jane.color("red")

def drawRectangle(width, height):
    ''' Draw a rectangle at the current location of turtle "jane",
        of width 'width' and height 'height'
    '''
    jane.begin_fill()
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.left(90)
    jane.end_fill()

# More reusable : Paramaters
def jumpTo(x,y):
    jane.up()
    jane.goto(x,y)
    jane.down()
    
def drawThreeRectangles(width, height, space):
    jane.color("red")
    drawRectangle(width,height)
    jumpTo(jane.xcor()+width+space, jane.ycor())

    drawRectangle(width,height)
    jumpTo(jane.xcor()+width+space, jane.ycor())
    
    drawRectangle(width,height)
    jumpTo(jane.xcor()+width+space, jane.ycor())


def drawNRectangles(width, height, space, N):
    jane.color("red")
    colors = ["red", "blue", "green"]
    for i in range(N):
        jane.color(colors[i%3])
        drawRectangle(width,height)
        jumpTo(jane.xcor()+width+space, jane.ycor())



# Use functions to make your code more readable 

jane.up()
jane.goto(-200, 0)
jane.down()
jane.speed(0)
drawNRectangles(10, 200, 50, 5)


