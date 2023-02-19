# 나의 풀이
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) != 0 :
        return sorted(answer)
    else:
        return [-1]

# 배운 풀이
def solution(arr, divisor): 
    return sorted([n for n in arr if n % divisor == 0]) or [-1]