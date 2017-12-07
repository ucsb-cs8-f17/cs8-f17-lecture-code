import turtle
t = turtle.Turtle()
t.speed(0)
t.width(5)
t.color("red")
import random

def drawTree(trunkLen, level):
             if level ==0:
                          t.forward(trunkLen)
                          return
             t.forward(trunkLen)
             x = t.xcor()
             y = t.ycor()
             h = t.heading()
             t.left(45+random.randint(-10,10))

             drawTree(trunkLen*random.randint(5,8)/10, level-1)
             t.up()
             t.goto(x,y)
             t.seth(h)
             t.down()
             t.right(45+random.randint(-10,10))
             drawTree(trunkLen*random.randint(5,8)/10, level-1)

def koch(level, L):
             if level ==0:
                          t.forward(L)
                          return
             koch(level-1, L/3)
             t.left(60)
             koch(level-1, L/3)
             t.right(120)
             koch(level-1, L/3)
             t.left(60)
             koch(level-1, L/3)


             
koch(3, 400)            
             

#t.left(90)          
#drawTree(100, 6)

