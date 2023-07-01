"""
불 : BFS
1. 불이 다 번진 지도를 만든다.
2. 지훈이가 가장자리로 가거나 큐가 빌때까지 이동한다.
    이 때, 벽(-1) 이거나 본인의 움직임보다 크거나 같은 곳은 가지 못한다.
"""
dx = [1,0,0,-1]
dy = [0,1,-1,0]
from collections import deque
import copy
n,m = map(int,input().split())
arr = list(list(input()) for _ in range(n))
arr2 = list([-1]*m for _ in range(n))
q= deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == "#":
            arr[i][j] = -1
        elif arr[i][j] == ".":
            arr[i][j] = 0
            arr2[i][j] = 0
        elif arr[i][j] == "J":
            arr[i][j] = 0
            arr2[i][j] = 1
            J =(i,j)
        elif arr[i][j] == "F":
            arr[i][j] = 1
            q.append((i,j))
while(q):
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue #넘어가면 패스
        if arr[nx][ny] == -1 or arr[nx][ny] >= 1: continue #방문했거나 벽이면 패스
        arr[nx][ny] = arr[x][y] + 1
        q.append((nx,ny))

q2= deque()
q2.append(J)
# print(*arr, sep='\n')
# print()
# print(*arr2, sep='\n')
while(q2):
    x,y = q2.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:#넘어가면 통과한겨
            print(arr2[x][y])
            # print(*arr,sep='\n')
            # print()
            # print(*arr2,sep='\n')
            exit()
        if arr[nx][ny] == -1 or arr2[nx][ny] >= 1: continue
        if arr[nx][ny] > 0 and arr[nx][ny] <= (arr2[x][y]+1): continue
        arr2[nx][ny] = arr2[x][y] + 1
        q2.append((nx, ny))

print("IMPOSSIBLE")
"""
5 5
##F##
#J.##
#..##
.....
#####

5 4
####
#...
#.##
#.J#
####

7 7
#######
#J###F#
#.....#
#.#.#.#
#.#.#.#
F.#.#.#
##F.#.#
"""