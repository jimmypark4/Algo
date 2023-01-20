import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M = map(int,input().split())# 정점과 간선의 개수
adj = [ [0] * N  for _ in range(N)]
for __ in range(M):
    a,b=map(lambda x:x-1,map(int,input().split()))
    adj[a][b]=1
    adj[b][a]=1
# for row in adj:
#     print(row)
ans = 0
check = [False]*N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not check[nxt]:
            check[nxt] = True
            dfs(nxt)
for i in range(N):
    if not check[i]:
        check[i]=True
        ans+=1
        dfs(i)
print(ans)