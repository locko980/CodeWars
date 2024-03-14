def collinearity(x1, y1, x2, y2):
    if x1 == 0 and x2 == 0 or y1 == 0 and y2 == 0: 
        return True
    
    if x1 == 0 or y1 == 0:
        return False
    
    elif x2 / x1 == y2 / y1:
        return True
    
    else: 
        return False


collinearity(0,0,-588, -577)
collinearity(0,0, -300, -187)
