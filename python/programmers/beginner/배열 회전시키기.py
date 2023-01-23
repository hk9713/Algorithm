# 나의 풀이
def solution(numbers, direction):
    if direction == 'left':
        first = numbers[0]
        numbers.remove(first)
        numbers.append(first)
    else:
        last = numbers[-1]
        numbers.remove(last)
        numbers.insert(0,last)
    return numbers

# 배운 풀이
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

''' 
deque(데크): 앞, 뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거할 수 있다
deque.rotate(num) : 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽)
'''