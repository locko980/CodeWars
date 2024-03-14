def find_missing_letter(chars):
    for i in range(len(chars)):
        chars[i] = ord(chars[i])
        
        if i > 0:
            if chars[i] - chars[i - 1] > 1:
                return chr(chars[i-1] + 1)

