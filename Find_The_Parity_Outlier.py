def find_outlier(integers):
    even = 0
    odds = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            number_even = integers[i]
            even += 1
        else: 
            number_odds = integers[i]
            odds += 1
    if odds < even:
        return number_odds
    else:
        return number_even
            
print(find_outlier([2, 4, 6, 8, 10, 3]))