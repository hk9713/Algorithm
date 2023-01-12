# 나의 풀이
def solution(array):
    arr = sorted(array)
    index = len(array)//2
    return arr[index]

# 배운 풀이
def solution(array):
    array.sort()
    return array[int(len(array)/2)]