# 나의 풀이
def solution(hp):
    general_ant = hp//5
    hp -= general_ant*5

    sodier_ant = hp//3
    hp -= sodier_ant*3

    work_ant = hp
    return general_ant + sodier_ant + work_ant

# 배운 풀이
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)