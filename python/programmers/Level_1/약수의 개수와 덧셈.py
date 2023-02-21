# 나의 풀이
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count = len([i for i in range(1, num+1) if num % i == 0])
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

# 배운 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
## 제곱수를 제외한 모든 정수들의 약수의 개수는 무조건 짝수 개수이고, 제곱수만 홀수 개수이다