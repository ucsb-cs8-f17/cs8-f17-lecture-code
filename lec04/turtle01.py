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

def drawSquare(width):
    ''' Draw a square at the current location of turtle "jane",
        of size 'width'
    '''
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    jane.left(90)

# More reusable : Paramaters


