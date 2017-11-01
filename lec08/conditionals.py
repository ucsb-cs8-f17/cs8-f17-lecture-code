def checkTypeAndValue(x):
           return(type(x)==int) and (x < 0 )


def isOdd(x):
           return(type(x)==int) and ((x %2) != 0 )

def printIfOdd(x):

             if(type(x)==int) and ((x %2) != 0 ):
                          print('x is an int and it is odd')
             else:
                          print('x is even')


def printUptoX(x):
             for i in range(1,x+1,2):
                          print(i)

def printChar(x):
             for i in range(len(x)):
                          print(x[i])
def printChar_2(x):
             for i in x:
                 print(i)

def printOddElements(x):
             for i in x:
                 if(i%2 ==1):
                    print(i)

                          
