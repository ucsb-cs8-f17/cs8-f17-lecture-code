# Try to add two numbers
# But this might not do what we want..

import sys

# Everything that isn't function def or import
# goes inside name == main block

def convertToFloat(s):
    try:
        result = float(s)
        return result
    except:
        print("Sorry, ",s," can't be converted to a number")
        sys.exit()
        
if __name__=="__main__":

    if len(sys.argv)!=3:
        print("I need two numbers")
        sys.exit()
    num1 = convertToFloat(sys.argv[1])
    num2 = convertToFloat(sys.argv[2])
    print("product = ", num1 * num2)
    
