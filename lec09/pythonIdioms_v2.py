# Accumulator Pattern : Very important!!!
# Accumulate (add to, pile on , build on) "something" in every iteration of a loop

def sumElement(ll):
    ''' Input: list (ll)     [1, 2, 4]
        Output: Return sum of the elements of the list (7)
        Algorithm:
        initialize sum to 0       
        for each element e in ll
            add e to sum  ; sum = sum + e 
    '''
    total = 0
    for e in ll:
        total = total +e

    return total

def avgElement(ll):
    ''' Input: list (ll) e.g.    [1, 2, 4]
        Output: Return average (7/3)
        Algorithm
        1. Calculate the sum
        initialize total to 0
        for each element e in ll:
            set total to current total + e
        2. Return sum/(number of elements in the list)   

    '''
    total = 0
    for e in ll:
        total = total +e
    if len(ll) ==0:
        return 0
    return total/len(ll)

def prodElement(ll):
    ''' Input: list (ll)     [1, 2, 4]
        Output: Product of the elements of ll: 8
      
    '''
    prod = 1
    for e in ll:
        prod = prod*e
    return prod
    
def factorial(N):
    ''' Input: N
        Output: N < 1 , 1
                N* (N-1)* (N-2)....*1

        e.g. N=5, return   5*4*3*2*1
        fact = 1
        Iteration #                fact  
        1                           1
        2                           1*2
        3                           1*2*3     

    '''
    fact = 1
    for i in range(N):
        fact = fact*i
    return fact
    





    










        















