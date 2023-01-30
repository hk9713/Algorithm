# 나의 풀이
def solution(numbers):
    answer = []
    eng = { "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }  
    temp = ''
    for c in numbers:
        temp += c
        if temp in eng:
            answer.append(eng[temp])
            temp = ''
    return int(''.join(map(str,answer)))

# 배운 풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)