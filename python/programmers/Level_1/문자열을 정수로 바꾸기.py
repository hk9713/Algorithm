# 나의 풀이
def solution(s):
    return int(s)

# 배운 풀이
def strToInt(str):
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        elif number == '+':
            continue
        else:
            result += int(number) * (10 ** idx)
    return result