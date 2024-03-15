
def likes(names):
    result = ''
    
    if len(names) == 1:
        return names[0] + ' likes this'
    
    elif len(names) == 2:
        return names[0] + ' and' + names[1] + ' like this'
    
    elif len(names) == 3:
        return  names[0] + ', ' + names[1] + ' and' + names[2] + ' like this'
    
    elif len(names) > 3:
        return names[0] + ', ' + names[1] + ' and ' + f'{len(names) - 2}' + ' others likes this'



