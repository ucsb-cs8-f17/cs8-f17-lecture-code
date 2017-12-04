def sumList(lst):
  '''return the sum of all the elements of the list'''
  if len(lst) ==0:
    return 0
  # [ 1, 4, 5, 6]
  sumOfRestOfList = sumList(lst[1:])
  return lst[0] + sumOfRestOfList

def sumIter(lst):
  result=0
  for item in lst:
    result+=item

  return result

def minList(lst):
  if len(lst)==1:
    return lst[0]

  m= minList(lst[1:])
  if m < lst[0]:
    return m
  else:
    return lst[0]
  


  
