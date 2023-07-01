"""
적록색약 : BFS문제
1. arr에서 각각 R,G,B에 대해 BFS진행 => answer_1
2. rgarr에서 RG,B에 대해 BFS진행 => answer_2
print(answer_1,answer_2)
"""

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = list(list(input())for _ in range(n))
rgarr = list( [0]*n for _ in range(n))
# print(*arr,sep='\n')
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R":
            arr[i][j] = 1
            rgarr[i][j] = 1
        elif arr[i][j] == "G":
            arr[i][j] = 2
            rgarr[i][j] = 1

        elif arr[i][j] == "B":
            arr[i][j] = 3
            rgarr[i][j] = 0

r_answer = 0
g_answer = 0
b_answer = 0
rg_answer = 0
q = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            r_answer += 1
            q = deque()
            q.append((i,j))
            while q:
                y,x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
                    if arr[ny][nx] != 1: continue
                    arr[ny][nx] = -1
                    q.append((ny,nx))
        elif arr[i][j] == 2:
            g_answer += 1
            q = deque()
            q.append((i,j))
            while q:
                y,x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
                    if arr[ny][nx] != 2: continue
                    arr[ny][nx] = -1
                    q.append((ny,nx))
        elif arr[i][j] == 3:
            b_answer += 1
            q = deque()
            q.append((i,j))
            while q:
                y,x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
                    if arr[ny][nx] != 3: continue
                    arr[ny][nx] = -1
                    q.append((ny,nx))
        if rgarr[i][j] == 1:
            rg_answer += 1
            q = deque()
            q.append((i,j))
            while q:
                y,x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
                    if rgarr[ny][nx] != 1: continue
                    rgarr[ny][nx] = -1
                    q.append((ny,nx))
answer1 = r_answer+g_answer+b_answer
answer2 = rg_answer+b_answer
print(answer1,answer2,sep=" ")

