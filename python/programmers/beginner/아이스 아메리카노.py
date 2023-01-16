# 나의 풀이
def solution(money):
    max_num = money//5500
    change = money - (max_num*5500)
    return [max_num, change]

# 배운 풀이
def solution(money):
    return divmod(money, 5500)