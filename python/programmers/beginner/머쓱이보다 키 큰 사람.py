# 나의 풀이
def solution(array, height):
    answer = 0
    array.sort(reverse=True)
    for i in array:
        if i > height:
            answer += 1
        else:
            break
    return answer

# 배운 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)