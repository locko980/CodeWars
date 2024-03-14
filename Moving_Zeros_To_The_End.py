def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            aux = lst[i]
            lst.remove(lst[i])
            lst.append(aux)
    return lst
