# sentence1 = input('whrite here the sentence that u want to: ')
# sentence1 = input('second sentence: ')


s1 = "--++--"
s2 = "++--++"
result = ""

print(len(s1), len(s2))

if len(s1) < len(s2):
    small = len(s1)
else:
    small = len(s2)

for i in range(small):
    if s1[i] == '+' and s2[i] == '+' :
        result += '+'
    elif s1[i] == '+' and s2[i] == '-' or s1[i] == '-' and s2[i] == '+':
        result += '0'
    elif s1[i] == '-' and s2[i] == '-':
        result += '-'

print(result)