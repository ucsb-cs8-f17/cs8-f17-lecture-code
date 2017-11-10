def getFields(filename):
    ''' Input is a filename
        return a list [[months], [days], [names]]
    '''
    try:
        f = open(filename)
    except:
        print('Input file does not exist')
        return
    line= f.readline()
    line= f.readline()
    months  =[]
    days = []
    names =[]
    while line.startswith('#'):
        line = f.readline()
    
    while line:
        lst=line.strip().split(',')
        month =lst[0]
        day=lst[1]
        name= lst[2]
        months.append(month)
        days.append(day)
        names.append(name)
        print(month, day, name)
        line = f.readline()

    f.close()
    return [months, days,names]


def writeStripped(filename):
    ''' Input is a filename
        return a list [[months], [days], [names]]

    '''
    try:
        f = open(filename)
    except:
        print('Input file does not exist')
        return
    g = open('outputFile','w')
    line= f.readline()
    line= f.readline()
    months  =[]
    days = []
    names =[]
    # Skip over all lines that start with a # sign
    while line.startswith('#'):
        line = f.readline()
    
    while line:
        g.write(line)
        line = f.readline()

    f.close()
    return 

writeStripped('songs.txt')
