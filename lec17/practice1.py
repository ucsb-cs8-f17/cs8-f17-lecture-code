## Accumulator pattern
### input - sequence (list, string) Output -> single number (or value)
import pytest
def sumList(alist):

  result = 0
  for item in alist:
    result = item +result

  return result



def test_sumList_0():
  assert(sumList([1, 1, 2]) == 4)

def sumEven(alist):

  result = 0
  for item in alist:
    if item%2 ==0:
      result = item +result
    
  return result


def test_sumEvenList_0():
  assert(sumEven([1, 1, 2]) == 2)

def test_sumEvenList_1():
  assert(sumEven([1, 4, 1, 2]) == 6)


def minList(alist):
  if len(alist) == 0:
    return False
  
  minElem = alist[0]
  for item in alist:
    if item < minElem:
      minElem = item
    
  return minElem

def test_minList_0():
  assert(minList([]) == False)

def test_minList_1():
  assert(minList([1]) == 1)

def test_minList_2():
  assert(minList([1, -1]) == -1)
  
# Which line of code is incorrect
# A. minElem = 0
# B. Something else
