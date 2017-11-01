# counting by something other than an int

def myList():
    lst=[]
    i = 0.0
    while i < 1.0:
        lst.append(i)
        i = i + 0.1

    return lst

if __name__ == "__main__":
    myList= myList()
    for myvar in myList:
        print(myvar)
