def new_sighting_0(kinds, counts, sighting):
  '''(list of str, list of int, str) -> NoneType
  Add new sighting to parallel lists kinds and counts.
  ''' 
  if sighting not in kinds:
    kinds.append(sighting)
    counts.append(0)
  ind = kinds.index(sighting)  
  counts[ind] = counts[ind] + 1

def test_new_sighting_0():
  kinds = ['falcon','hawk','sparrow','woodpecker']
  counts = [5, 8, 2, 1]
  new_sighting(kinds, counts, 'sparrow')
  if counts[2]!=3:
    assert(False)
    
def new_sighting_1(bird_dict, sighting):
  '''(dict, str) -> NoneType
  Add new sighting to a dictionary of birds and their counts
  '''
  return
