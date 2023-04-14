L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def MinList(L):
    minimum = L[0]
    for x in L:
     if x < minimum :
      minimum = x
    return minimum
def MaxList(L):
    maximum = L[0]
    for x in L:
     if x > maximum :
      maximum = x
    return maximum
print("L'élément minimum est:", MinList(L))
print("L'élément le plus grand est :", MaxList(L))








