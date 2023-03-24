from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(height):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > height:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] > height:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
    return count

max_height = max(map(max, arr))
max_count = 0

for h in range(max_height + 1):
    max_count = max(max_count, bfs(h))

print(max_count)
