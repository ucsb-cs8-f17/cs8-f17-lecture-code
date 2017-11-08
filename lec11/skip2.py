def skip(f):
  line = f.readline()
  line = f.readline()
  while line.startswith('#' ): 
    line = f.readline()
  return line
