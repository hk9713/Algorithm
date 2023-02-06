# 나의 풀이
def solution(keyinput, board):
    x = (board[0]-1)/2
    y = (board[1]-1)/2
    answer = [0,0]
    for k in keyinput:
        if k=="up":
            if answer[1] < y:
                answer[1] += 1
        elif k=="down": 
            if answer[1] > -y:
                answer[1] -= 1
        elif k=="left":
            if answer[0] > -x:
                answer[0] -= 1
        elif k=="right":
            if answer[0] < x:
                answer[0] += 1
    return answer

# 배운 풀이
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy
    return [x,y]