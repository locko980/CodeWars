def alphabet_position(text):
    NUM = 31
    result = ''
    
    for i in text:
        if i == "." or i==" ":
            continue
        result += f'{(ord(i) & NUM)}' + " "
    
    return result
        
