# Calculate the factorial of N
def fac(n):
             ''' returns n*(n-1)*(n-2)...*1, n>1
                          1, n <=1
             '''
             if n <=1:
                          return 1
             return n * fac(n-1)

def facIterative(n):
             result = 1
             for i in range(2, n+1):
                          result = result * i
             return result
