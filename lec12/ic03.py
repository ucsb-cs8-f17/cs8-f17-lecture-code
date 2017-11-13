def hasNoX_2(s):
    if type(s)!=str:
       return False
    for c in s:
        if c!='x' or c!='X':
           return True
    return False

def result_hasNoX_2():                      
  print('hasNoX_2("Fox")', hasNoX_2("Fox"))
  #A. True  B.False  C. None  D. Error E. Something else
  print('hasNoX_2("Xie")', hasNoX_2("Xie"))
  #A. True  B.False  C. None  D. Error E. Something else
  print('hasNoX_2("Axe")', hasNoX_2("Axe"))
  #A. True  B.False  C. None  D. Error E. Something else
  print('hasNoX_2("Pat")', hasNoX_2("Pat"))
  #A. True  B.False  C. None  D. Error E. Something else
  print('hasNoX_2(12345)',hasNoX_2(12345))
  

def hasNoX_3(s):
    if type(s)!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return False
        return True

def result_hasNoX_3():
  print('hasNoX_3("Fox")', hasNoX_3("Fox"))
  print('hasNoX_3("Xie")', hasNoX_3("Xie"))
  print('hasNoX_3("Axe")', hasNoX_3("Axe"))
  print('hasNoX_3("Pat")', hasNoX_3("Pat"))
  print('hasNoX_3(12345)',hasNoX_3(12345))

def hasNoX_4(s):
    if type(s)!=str:
       return False
    for c in s:
        if c!='x' and c!='X':
           return True
        else:
           return False

def result_hasNoX_4():
  print('hasNoX_4("Fox")', hasNoX_4("Fox"))
  print('hasNoX_4("Xie")', hasNoX_4("Xie"))
  print('hasNoX_4("Axe")', hasNoX_4("Axe"))
  print('hasNoX_4("Pat")', hasNoX_4("Pat"))
  print('hasNoX_4(12345)', hasNoX_4(12345))

def hasNoX_5(s):
    if s!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return False
    return True


def result_hasNoX_5():
  print('hasNoX_5("Fox")', hasNoX_5("Fox"))
  print('hasNoX_5("Xie")', hasNoX_5("Xie"))
  print('hasNoX_5("Axe")', hasNoX_5("Axe"))
  print('hasNoX_5("Pat")', hasNoX_5("Pat"))
  print('hasNoX_5(12345)', hasNoX_5(12345))

def hasNoX_6(s):
    if type(s)!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return True
    return False


def result_hasNoX_6():
  print('hasNoX_6("Fox")', hasNoX_6("Fox"))
  print('hasNoX_6("Xie")', hasNoX_6("Xie"))
  print('hasNoX_6("Axe")', hasNoX_6("Axe"))
  print('hasNoX_6("Pat")', hasNoX_6("Pat"))
  print('hasNoX_6(12345)', hasNoX_6(12345)) 
print("Q6")
result_hasNoX_6()
