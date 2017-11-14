import pytest

def maskedPassword(pw):
  '''
  takes one parameter `pw` and returns a string consisting
  of the first three characters contained in the variable `pw`
  followed by 'x's instead of the remaining characters in `pw`.
  The length of the returned value should be the same as the length
  of the parameter passed in. If the length of `pw` is less than 3
  return `pw` without any modification (YOU MAY ASSUME `pw` is of
  type `str`)
  '''
  if len(pw)<=3:
    return pw
  result1 = pw[0:3] # Trying to get the first three letters
  result2 = ''
  for i in range((len(pw)-3)):
    result2= result2.lower()
    result2 = result2 +'x'# Trying to generate N 'x's
  
  return result1+result2

def test_maskedPassword_0():
  assert(maskedPassword("hello") =="helxx" )

def test_maskedPassword_1():
  assert(maskedPassword("hi") == "hi" )

def test_maskedPassword_2():
  assert(maskedPassword("password123") == "pasxxxxxxxx")

def test_maskedPassword_3():
  assert(maskedPassword("hie") == "hie" )

  
def isValidPassword(pw):
  '''
  takes a parameter `pw` and returns True if the variable `pw`
  is of type `str` and is a valid **password**, according to
  the following rules: it must consist of at least 8 characters,
  include one of the special characters `*` or `#` and terminate
  with a numeric digit (`0`-`9`)
  '''
  return True

def minOfTwoLists(alist, blist):
  '''
  takes two lists as parameters: `alist` and `blist`.
  The functions returns a new list where each element in
  the new list is the minimum of the corresponding elements
  in `alist` and `blist`. The function should raise a `ValueError`
  exception with an appropriate message, if either `alist` or `blist`
  is not a list or if either of them contains anything
  other than numbers (either int or float) or if they are not of
  the same length
  '''
  if type(alist)!=list:
    raise ValueError("first parameter is not a list")

  if type(blist)!=list:
    raise ValueError("second parameter is not a list")
  if len(alist)!=len(blist):
    raise ValueError("length of lists are not equal")

  result=[]
  
  for i in range(len(alist)):
    if not (type(alist[i])==int or type(alist[i])==float):   #alist[i] is not a number
      raise ValueError("alist has a non-numeric element)
    if alist[i]<blist[i]:
      result.append(alist[i])
    else:
      result.append(blist[i])
    #blah blah blah
    
  return result

def test_minOfTwoLists_0():
  assert(minOfTwoLists([1, 3, 5], [20, 7, 2.5])==pytest.approx([1,3,2.5]))

def test_minOfTwoLists_1():
  assert(minOfTwoLists([1, 30, 5], [20, 7, 2.5])==pytest.approx([1,7,2.5]))



  
