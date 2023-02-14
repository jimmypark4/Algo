#1158 요세푸스
from collections import deque
N,K =map(int,input().split())
ans=[]
circle = [i for i in range(1,N+1)]
dq = deque(circle)
while len(dq) != 0:
    dq.rotate(-(K-1))
    ans.append(dq.popleft())
print("<"+", ".join(str(i) for i in ans)+">")

