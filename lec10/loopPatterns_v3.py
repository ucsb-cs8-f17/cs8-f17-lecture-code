import pytest
#Accumulator loop pattern

def factorial(N):
    ''' returns the factorial of the input N defined as
        1 if N<=0
        1*2*3*...*N if N>0
    '''
    result = 1 # Initialize result
    for i in range(1, N+1): # Counter loop
        result = result * i # update result
    return result

# Which of the following tests will fail when
# the above code is executed?
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
    #Convert input string into a list of words (ll)
    ll = inputString.split()
    
    # initialize result to be an empty string
    result = str() #same as result = ''
    # for each word in ll:
        #     Get the first letter of word
        ##        firstLetter = word[0]  
        ##        # Convert the letter into upper case
        ##        firstLetter= firstLetter.upper()
        ##        #   Concatenate the letter to result and store it in result
        ##        result = result+firstLetter
    # return result
    for word in ll:
        result = result +  word[0].upper()
    
    return result

#Write code to test acronym()

def test_acronym_0():
    assert(acronym('random')=='R')

def test_acronym_1():
    assert(acronym('random access')=='RA')
      
def test_acronym_2():
    assert(acronym('random access memory')=='RAM')
















