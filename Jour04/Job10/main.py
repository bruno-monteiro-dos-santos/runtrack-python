L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
long = len(L)

#produit des valeurs de [25, 91]
p = 1
for i in range (0, long) :
     if 25 <= L[i] <= 91 :
          p = p*L[i]
print ("produit des valeurs comprises entre 25 et 91 : ", p)