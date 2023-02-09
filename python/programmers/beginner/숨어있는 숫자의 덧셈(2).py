# 나의 풀이
import re
def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    return sum(map(int,numbers))

# 배운 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())