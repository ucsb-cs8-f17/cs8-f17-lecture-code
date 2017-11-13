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
  return "42"
  

  
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
  return "42"

def test_minOfTwoLists_0():
  assert([1, 3, 5], [20, 7, 2.5])==pytest.approx([1,3,2.5]))

def test_minOfTwoLists_1():
  assert([1, 30, 5], [20, 7, 2.5])==pytest.approx([1,7,2.5]))



  
