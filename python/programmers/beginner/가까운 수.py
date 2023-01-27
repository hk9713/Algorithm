# 나의 풀이
def solution(array, n):
    answer = max(array)
    for i in array:
        if abs(n-i) < abs(n-answer):
            answer = i
        elif abs(n-i) == abs(n-answer):
            answer = min(i, answer)
    return answer

# 배운 풀이
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer

## 리스트 정렬 기준을 여러개 세우고 싶을 떄는 튜플 형식으로 lambda식을 세워주면 된다
## sort( key = lambda x: (x[0], x[1], x[2]) )  