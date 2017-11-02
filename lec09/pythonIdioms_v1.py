# English to python
##############################################
# Basic loop patterns

# Generate a list of N numbers in sequence
# N = 5, [1, 2, 3, 4, 5]

def generateSequence(N):
    ''' Input: N number of terms in the sequence
        Output: return a news list [1, N]
    '''
    ll = list()
    for j in range(N):
        ll.append(j)

    return ll

# Print each element in a list
# Example of Iteration loop pattern
def printElements(ll):
    ''' Input: list (ll)
        Output: each element printed to screen

    Iterate through the elements of the list
       print each element

    OR

    for each element e in ll
       print e
    '''
    for e in ll:
        print(e)


# Print the powers of 2 of elements of a list
def printPowersOfTwo(ll):
    ''' Input: list (ll): [1, 2, 4]
    Output: 1 4 16

    Iterate through the elements of the list
    print 2** element

    OR

    for each element e in ll
    print 2**e
    '''

    for e in ll:
        print(2**e)


# Print every other elememt of a list
# Example of a counter loop pattern 
    ''' Input: list (ll): [1, 2, 4, 5, 10, 15]
        Output: 1 4 10 

    for i in [0, 2, 4, ....len(ll)-1]
        print the element of ll at index i
      
    '''    
def printEveryOther(ll):
    for index in range(0, len(ll), 2 ): # [ 0, 2, 4]
        print(ll[index])

# Print all elements of a list two at a time
# This example uses the Counter loop pattern,
# essentially the loop variable i is used to count up
def printTwoAtATime(ll):

    ''' Input: list (ll): [1, 2, 4, 5, 10, 15]
        Output: 1  2
                4  5
                10 15
        for i in [0, 2, 4, ....len(ll)-1]
            print element and index i and element at index i+1
      
    '''
    for i in range(0, len(ll), 2):
        print(ll[i], ll[i+1])
        
#############################
# Searching a list
# Check if a keyword exists in the list

def findElement(ll, key):
    ''' Inputs (1): list (ll)     [1, 2, 4, 5, 10, 15]
               (2): keyword (key) 10 

        Output: Return True if keyword exists, False otherwise
        
        for each element e in ll
           if e is equal to key, then return True
           else return False
        
    # Is there a  bug in the above algorithm?
    A. Yes-> Yes there is a bug because it would incorrectly
       return False if the list was the same as above and the
       key value was anything other than 1, need to put the return False
       outside the for loop
    B. No

    '''
    for e in ll:
        if e==key:
            return True
    return False





