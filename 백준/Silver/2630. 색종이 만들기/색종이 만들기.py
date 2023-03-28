import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
checked = [[False] * n for _ in range(n)]
answer = [0,0]
#큰거에서 시작해서 작은거로 쪼개기
# 1/4 등분
def func(x,y,n):
    color = arr[x][y]
    if n == 1 and not checked[x][y]:
        checked[x][y] = True
        answer[color] += 1
        return
    for i in range(x,x+n):
        for j in range(y,y+n):
            if checked[i][j]:
                continue
            if arr[i][j] != color:
                func(x,         y         ,int(n/2))
                func(x+int(n/2),y         ,int(n/2))
                func(x,         y+int(n/2),int(n/2))
                func(x+int(n/2),y+int(n/2),int(n/2))
    if not checked[x][y]:
        answer[color] += 1
    for i in range(x, x + n):
        for j in range(y, y + n):
            checked[i][j] = True

    return


func(0,0,n)
print(*answer,sep="\n")