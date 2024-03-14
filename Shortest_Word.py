def find_short(s):
    words = s.split()
    l = words[0]
    for i in range(len(words)):
        aux = len(words[i])
        if len(l) > aux:
            l = words[i]
    return len(l) 
