#1389번 케빈 베이컨의 6단계
#그래프
#인접행
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
relations=[[] for _ in range(N)]
for _ in range(M):
    i,j=map(lambda x:x-1,   map(int, input().split())   )
    relations[i].append(j)
    relations[j].append(i)


def bfs(start,goal):
    check = [False]*N
    check[start] =True
    dq=deque()
    dq.append((start,0))
    while dq:
        now,d=dq.popleft()
        if now ==goal:
            return d

        nd =d+1
        for nxt in relations[now]:
            if not check[nxt]:
                check[nxt] =True
                dq.append((nxt,nd))

def get_kevin(start):
    tot=0
    for i in range(N):
        if i!=start:
            tot += bfs(start,i)
    return tot
result=9999999999
for i in range(N):
    kevin_d=get_kevin(i)
    if result > kevin_d:
        ans = i+1
        result = kevin_d
print(ans)
