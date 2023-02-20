# 나의 풀이
def solution(phone_number):
    hide = ["*" for n in range( len(phone_number)-4 )]
    for num in phone_number[-4:]:
        hide.append(num)
    return ''.join(hide)

# 배운 풀이
def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]