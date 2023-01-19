# 나의 풀이
def solution(emergency):
    order_em = sorted(emergency)
    order_em.reverse()
    return [order_em.index(i)+1 for i in emergency]

# 배운 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(i) + 1 for i in emergency]