def solution(number):
    ans = 0
    
    if number < 0:
        return 0
    
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            ans += i
        else:
            if i % 3 == 0:
                ans += i
            elif i % 5 == 0:
                ans += i
    return ans

