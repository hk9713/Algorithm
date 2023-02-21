# 나의 풀이
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer

# 배운 풀이
def sumMatrix(A,B):
    return [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
## zip()
## 여러 개의 iterable자료형이 개수가 동일할 때, 
## 각각의 요소를 순서대로 묶어서 요소 개수만큼 새로운 iterable 자료형을 생성한다.