from collections import deque
dx = [+1, 0, 0,-1]
dy = [ 0,+1,-1, 0]
m , n  = map(int,input().split())
arr = list( list(map(int,input().split())) for _ in range(n))
# print(*arr)

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
# print(q,nomato,tomato)
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
    # print(*arr,q,sep='\n')

print(-1) if nomato != 0 else print(answer)
