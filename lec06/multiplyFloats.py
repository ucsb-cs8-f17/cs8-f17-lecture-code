# Try to add two numbers
# But this might not do what we want..

import sys

def getFloat(prompt):
    # print out the prompt, a message to the user
    # get back some input 
    result = input(prompt)
    # try to convert to a number
    try:
        number = float(result)
        return number
    except:
        print("Sorry, ", result, " isn't a number")
        sys.exit()

# Everything that isn't function def or import
# goes inside name == main block

if __name__=="__main__":

    num1 = getFloat("First Number:")
    num2 = getFloat("Second Number:")        
    print("the product is: ",num1 * num2)
