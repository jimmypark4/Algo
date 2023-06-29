from collections import deque
dx = [ 0, 0,+1,-1]
dy = [+1,-1, 0, 0]
#입출력
n, m = map(int,input().split())
paper = list( list(map(int,input().split())) for _ in range(n))
visited = list( [0]*m for _ in range(n) )

cnt = 0
max_size = 0
dq = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 0 or visited[i][j] == 1:
            continue
        cnt += 1
        dq.append((i,j))
        visited[i][j] = 1
        temp_size = 0

        while dq:
            temp_size += 1
            x,y = dq.pop()
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y

                if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
                if paper[nx][ny] == 0 or visited[nx][ny]:continue
                visited[nx][ny] = 1
                dq.append((nx, ny))


        # print(nx,ny,cnt,temp_size)
        max_size = max(temp_size,max_size)

print(cnt)
print(max_size)
"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""