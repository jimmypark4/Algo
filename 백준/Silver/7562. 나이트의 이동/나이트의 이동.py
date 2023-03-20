from collections import deque
n = int(input())

dx = [-2,-1,+1,+2,+2,+1,-1,-2]
dy = [+1,+2,+2,+1,-1,-2,-2,-1]

def bfs(dq,rx,ry):
   visited = {(-1,-1)}
   while dq:
       x ,y ,count = dq.popleft()
       if x==rx and y==ry:
           return count

       if (x,y) not in visited:
           visited.add((x,y))
           for i in range(8):
               nx = x + dx[i]
               ny = y + dy[i]
               if nx == rx and ny == ry: # 답인 경우
                   count += 1
                   return count
               if nx < 0 or ny < 0 or nx > l-1 or ny > l-1: #경계바깥으로 나감
                   pass
               else: #그 외 움직인 경우
                   dq.append((nx,ny,count+1))
   count = 0
   return count

for _ in range(n):
    l = int(input())
    sx,sy = map(int,input().split())
    rx,ry = map(int,input().split())

    dq = deque()
    dq.append((sx,sy,0))

    answer = bfs(dq,rx,ry)

    print(answer)
