"""
토마토 : BFS 문제
1. 배열을 돌면서 토마토가 없는 nomato을 세고, 토마토가 있으면 큐에 해당 위치를 넣음
2. 큐에 있는 위치들을 하나씩 popleft()하면서 상하좌우로 움직이며 노마토가 있는 지 체크
3. 노마토 이면 nomato 카운트를 하나 지우고, 해당 칸을 토마토로 채우고 큐에 해당 위치를 넣음
4. 만약 노마토가 0이 되거나, 큐가 비어있게 되면 반복을 종료 후, 결과 출력!
"""
from collections import deque
dx = [+1, 0, 0,-1]
dy = [ 0,+1,-1, 0]
m , n  = map(int,input().split())
arr = list( list(map(int,input().split())) for _ in range(n))

q =deque()
wall = 0
nomato = 0
tomato = 0
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            wall += 1
        elif arr[i][j] == 0:
            nomato += 1
        else:
            tomato += 1
            q.append((i,j))
if nomato == 0: print(0);exit()

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        if arr[nx][ny] == -1 or arr[nx][ny] >= 1: continue
        nomato -= 1
        arr[nx][ny] = arr[x][y] + 1
        if nomato == 0:
            answer = arr[nx][ny] -1
            break
        q.append((nx,ny))
    

print(-1) if nomato != 0 else print(answer)
