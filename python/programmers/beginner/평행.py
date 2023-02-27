# 나의 풀이
def solution(dots):
    a,b,c,d = sorted(dots,key=lambda x:x[0])
    if ((a[1]-b[1]) / (a[0]-b[0])) == ((c[1]-d[1]) / (c[0]-d[0])):
        return 1
    elif ((a[1]-c[1]) / (a[0]-c[0])) == ((b[1]-d[1]) / (b[0]-d[0])):
        return 1
    elif ((a[1]-d[1]) / (a[0]-d[0])) == ((b[1]-c[1]) / (b[0]-c[0])):
        return 1
    else:
        return 0