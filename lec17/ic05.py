def count_ae(s):
  ''' Input sequence (string) return an int, number of occurrences of
  'a' and 'e' in s
  '''
  if type(s)!=str:
    return 0

##  finalCount = 0
##  for item in s:
##    if item =='a' or item =='e':
##      finalCount = finalCount +1
##  return finalCount
  return s.count('a') + s.count('e')

def test_count_ae_0():
  assert(count_ae(-42)==0)

def test_count_ae_1():
  assert(count_ae("Santa")==2)  

def test_count_ae_2():
  assert(count_ae("Santa Ynez")==3)  

