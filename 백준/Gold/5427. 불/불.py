"""
불 : bfs
1. 불이 이동하는 지도를 만듬 벽은 -1 불은 1부터 1씩 증가
2. 상근이가 이동하는 bfs 실시, 이동시, 불 == 상근이시간이면 못움직임.
"""
"""
1
2 2
.@
..

ans : 1
"""
"""
1
5 6
*#.##
#...#
#...#
#...#
#.@.#
#####
"""
dx = [0,0,1,-1]
dy = [1,-1,0,0]

from collections import deque
t = int(input())

for _ in range(t):
    m,n = map(int,input().split())
    o = list(list(input()) for _ in range(n))
    q = deque()
    p = deque()

    fire = list([0]*m for _ in range(n))
    arr = list([0]*m for _ in range(n))
    for i in range(n):
        for j in range(m):
            if o[i][j] == "#":
                fire[i][j] = -1
                arr[i][j] = -1

            elif o[i][j] == "*":
                fire[i][j] = 1
                q.append((i,j))
            elif o[i][j] == "@":
                arr[i][j] = 1
                p.append((i,j))

    while q:
        y,x = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx <0 or ny<0 or nx >=m or ny >= n: continue
            if fire[ny][nx] == -1: continue
            if fire[ny][nx] >= 1: continue
            fire[ny][nx] = fire[y][x] + 1
            q.append((ny,nx))

    flag = False
    while p:
        if flag: break
        y,x = p.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                print(arr[y][x])
                flag = True
                break
            if arr[ny][nx] == -1: continue
            if arr[ny][nx] >= 1: continue
            if fire[ny][nx] > 0 and fire[ny][nx] <= (arr[y][x]+1): continue
            arr[ny][nx] = arr[y][x] + 1
            p.append((ny, nx))


    if not flag:
        print("IMPOSSIBLE")
