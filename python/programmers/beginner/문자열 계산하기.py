# 나의 풀이
def solution(my_string):
    return eval(my_string)

# 배운 풀이
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))