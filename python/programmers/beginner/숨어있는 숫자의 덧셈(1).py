# 나의 풀이
import re
def solution(my_string):
    return sum(map(int, (list(re.sub('[^0-9]','', my_string)))))

# 배운 풀이
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())