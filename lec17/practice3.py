def combineNames(alist, blist):

  result  =[]
  for index in range(len(alist)):
    result.append(alist[index] + ' '+ blist[index])

 
  return result


def test_combineNames_0():
  assert(combineNames(['Joe'],['Smith'])==['Joe Smith'])

def test_combineNames_1():
  assert(combineNames(['Joe', 'Bruce'],['Smith', 'Lee'])==['Joe Smith', 'Bruce Lee'])
