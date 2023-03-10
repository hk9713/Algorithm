# 나의 풀이
def solution(chicken):
    answer = 0
    while chicken >= 10:
        service = chicken // 10
        coupon = chicken % 10 
        answer += service
        chicken = service + coupon
    return answer

# 배운 풀이
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer