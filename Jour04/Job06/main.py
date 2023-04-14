#swap function
def swap_positions (list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

#driver function

list = ['white','red', 'blue', 'green', 'black']
pos1, pos2 = 1, 5

print (swap_positions(list, pos1-1, pos2-1))


    