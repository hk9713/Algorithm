# 2292 - 벌집
# 육각형으로 이루어진 벌집이 있다.
# 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다.
# 출력 - 숫자 N이 주어졌을 때, 중앙 1에서 N번 방까지 지나가는 방의 최소 개수

N = int(input())

room = 1
cnt =  1

while N > room:
    room += 6*cnt
    cnt += 1

print(cnt)


'''
실패한 코드 - 시간초과
N = int(input())

room = 1
temp = [1]

while True:
    if N in temp:
        break
    else:
        room += 1
        r = temp[-1]
        temp = [r+1+i for i in range(6*(room-1))]

print(room)
'''
