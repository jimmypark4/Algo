from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,0,0,+1,-1]
dy = [+1,-1,0,0,0,0]
dz = [0,0,+1,-1,0,0]

m,n,h=map(int,input().split())
arr = list(list(list(map(int,input().split())) for _ in range(n))for _ in range(h))
# print(*arr,sep="\n")
nomato = 0
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
          if arr[i][j][k] == 0: nomato += 1
          elif arr[i][j][k] == 1: q.append((i,j,k))
if nomato == 0: print(0);exit()

#bfs
while q:
    z,y,x = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if nz < 0 or ny < 0 or nx < 0 or nz >=h or ny >= n or nx >= m: continue
        if arr[nz][ny][nx] == -1: continue
        if arr[nz][ny][nx] >= 1 and arr[nz][ny][nx] <= arr[z][y][x]+1: continue
        nomato -= 1
        arr[nz][ny][nx] = arr[z][y][x] + 1
        q.append((nz,ny,nx))
        if nomato == 0: print(arr[z][y][x]);exit()
print(-1)



