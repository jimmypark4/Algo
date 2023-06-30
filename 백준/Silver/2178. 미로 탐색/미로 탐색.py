from collections import deque
dx = [ 1, 0,-1,0]
dy = [0,1, 0, -1]
#입출력
n, m = map(int,input().split())
paper = list( list(input()) for _ in range(n))
visited = list( [-1]*m for _ in range(n) )
stack = deque()
stack.append((0,0))
visited[0][0] = 0
while stack:
    x,y = stack.popleft() #pop이 아니라 앞에서 꺼내는게 중요!
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx <0 or ny <0 or nx >= n or ny >= m: continue
        if paper[nx][ny] == "0" or visited[nx][ny] >= 0: continue
        visited[nx][ny] = visited[x][y] + 1
        stack.append((nx,ny))

print(visited[n-1][m-1]+1)
"""
4 6
101111
101010
101011
111011
"""
#15