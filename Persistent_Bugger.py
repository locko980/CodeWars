def persistence(n):
    cont = 0
    n = str(n)
    
    while len(n) != 1:
        new_n = 1
        for i in range(len(n)):
            new_n = new_n * int(n[i])
        n = str(new_n)
        cont += 1
    return cont
    
persistence(39)