"""
영역구하기 : BFS
1. 전체를 1로 선언 , 직사각형 마킹된 부분은 0으로 초기화
2. bfs 돌면서 1이면 visited처리하면서, 크기 세고 정답 넣기



"""
dx = [0,0,-1,+1]
dy = [1,-1,0,0]
import sys
from collections import deque

input = sys.stdin.readline
n,m,k = map(int,input().split())
sqrs = list( list(map(int, input().split())) for _ in range(k))
arr = list([1]*m for _ in range(n))
# print(*arr,sep='\n')
# print()
for x1,y1,x2,y2 in sqrs:
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 0

# print(*arr,sep='\n')

cnt = 0
arr_size = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            q = deque()
            q.append((i,j))
            temp = 1
            arr[i][j] = -1
            while q:
                y,x = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
                    if arr[ny][nx] != 1 : continue
                    arr[ny][nx] = -1
                    q.append((ny,nx))
                    temp += 1

            # print(temp)
            arr_size.append(temp)

# print()
# print(*arr,sep='\n')
arr_size.sort()
print(cnt)
print(*arr_size,sep=" ")

