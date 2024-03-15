def is_valid_walk(walk):    
    n = walk.count('n')
    s = walk.count('s')
    w = walk.count('w')
    e = walk.count('e')
    
    if len(walk) == 1:
        return False
    elif len(walk) > 10 or len(walk) < 10:
        return False
    elif n > s or w > e or s > n or e > w:
        return False
    else:
        return True

