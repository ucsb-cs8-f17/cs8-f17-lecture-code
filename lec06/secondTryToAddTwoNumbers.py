# Try to add two numbers
# But this might not do what we want..

import sys

if __name__=="__main__":
    print("Please enter a number")
    num1AsString = input("First number: ")

    try:
        num1 = int(num1AsString)
    except:
        print("Ooops, that's not a number")
        sys.exit()

    print("Please enter another number")
    num2AsString = input("Second number: ")

    try:
        num2 = int(num2AsString)
    except:
        print("Ooops, that's not a number")
        sys.exit()

    print("You entered:")
    print("first number=",num1)
    print("second number=",num2)
    
    print("the sum is: ")
    print(num1 + num2)
