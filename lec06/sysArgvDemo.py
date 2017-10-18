# Try to add two numbers
# But this might not do what we want..

import sys

# Everything that isn't function def or import
# goes inside name == main block

if __name__=="__main__":

    # sys.argv is the argument vector
    # the "vector" of things on the command line
    print("sys.argv=",sys.argv)

    print("Here they are one line at a time:")
    for thing in sys.argv:
        print(thing)

    print("Here they are with numbers")
    for i in range(len(sys.argv)):
        print("i=",i," sys.argv[i]=",sys.argv[i])
