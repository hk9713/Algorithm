# 나의 풀이
def solution(numbers, k):
    index = (k-1)*2
    while (index > len(numbers)):
        index -= len(numbers)
    return numbers[index]

# 배운 풀이
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]