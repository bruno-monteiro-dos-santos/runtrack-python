chaine="abcdefghijklmnopqrstuvwxyz" * 10
n=1
i=0
stop = False
while i < len(chaine):
    for j in range(n):
        if j < len(chaine):
            print(chaine[i],end=' ')
            i+=1
        else:
            stop = True
            break
    print()
    n += 1
