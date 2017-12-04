### Input is a sequence, output is a sequence

def oddLengthString(alist):
  ''' input is a list of strings
  returns a list that has all the strings with odd length
  '''
  result = []
  for item in alist:
    ### Find the right element to append to the list
    if len(item)%2 !=0:
      result.append(item)
  return result

def test_oddLengthString_0():
  assert(oddLengthString(['ox'])==[])
  
def test_oddLengthString_1():
  assert(oddLengthString(['ox','dog'])==['dog'])

def test_oddLengthString_2():
  assert(oddLengthString(['ox','dog', 'cat'])==['dog', 'cat'])

def indexOfOddLengthString(alist):
  ''' input is a list of strings
  returns a list that has all the strings with odd length
  '''
  result = []
  for index in range(len(alist)): # [0, 1, 2]
    ### Find the right element to append to the list
    if len(alist[index])%2 !=0:
      result.append(index)
  return result

# A: Know how to change the code
# B: Don't know how to change the code to get the right

def test_indexOfOddLengthString_0():
  assert(indexOfOddLengthString(['ox'])==[])
  
def test_indexOfOddLengthString_1():
  assert(indexOfOddLengthString(['ox','dog'])==[1])

def test_indexOfOddLengthString_2():
  assert(indexOfOddLengthString(['ox','dog', 'cat'])==[1,2])
