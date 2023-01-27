# 나의 풀이
def solution(order):
    order = str(order)
    return order.count('3')+order.count('6')+order.count('9')

# 배운 풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))