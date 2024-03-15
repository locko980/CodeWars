def is_isogram(string):
    string = string.lower()  
    for i in range(len(string)):
        letter = string[i]
        for j in range(i + 1, len(string)):
            if letter == string[j]:
                return False
    return True
