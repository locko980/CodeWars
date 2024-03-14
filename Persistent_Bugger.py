# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

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