import turtle

print("HI")
def square(side):      
    regularShape(side,4)

def pentagon(side):      
    regularShape(side,5)

def regularShape(side,n):      
    for i in range(n):
        t.forward(side)     
        t.right(360/n)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    for s in range(10,20,1):
         square(s)
    

        

