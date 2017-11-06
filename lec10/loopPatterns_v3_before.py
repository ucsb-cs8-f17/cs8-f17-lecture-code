import pytest
#Accumulator loop pattern

def factorial(N):
    ''' returns the factorial of the input N defined as
        1 if N<=0
        1*2*3*...*N if N>0
    '''
    result = 0 # Initialize result
    for i in range(N): # Counter loop
        result = result * i # update result
    return result

# Which of the following tests will fail when
# the above code is executed? -> E: all the above
#A
def test_factorial_0():
    assert(factorial(-1)==1)
#B
def test_factorial_1():
    assert(factorial(0)==1)
#C        
def test_factorial_2():
    assert(factorial(1)==1)       
#D
def test_factorial_3():
    assert(factorial(3)==6)

def test_factorial_4():
    assert(factorial(4)==24)
#E All of the above


def acronym(inputString):
    ''' returns the acronym of a given input string
        e.g.
        acronym('random access memory') is RAM
        acronym('central processing unit) is CPU
    '''
    return "stub"

#Write code to test acronym()

def test_acronym_0():
    assert(acronym('random')=='R')

def test_acronym_1():
    assert(acronym('random access')=='RA')
      
def test_acronym_2():
    assert(acronym('random access memory')=='RAM')
















