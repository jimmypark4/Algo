n,m,v = map(int,input().split())
arr = list([] for _ in range(n+1))
vis = [False] * (n+1)
vis2 = [False] * (n+1)

# print(arr)
for _ in range(m):
    a,b = map(lambda x:x,map(int,input().split()))
    arr[a].append(b)
    arr[b].append(a)
for a in arr:
    a.sort()
# print(arr)

def dfs(v):
    s = []
    s.append(v)
    while s:
        cur = s.pop()
        if vis[cur]:continue
        vis[cur] = True
        print(cur,end=" ")
        for i in range(len(arr[cur])):
            nxt = arr[cur][len(arr[cur])-1-i]
            if vis[nxt]: continue
            s.append(nxt)

def dfs2(cur):
    vis[cur] = True
    print(cur,end=" ")
    for nxt in arr[cur]:
        if vis[nxt] : continue
        dfs2(nxt)



from collections import deque


def dfs(v):
    s = []
    s.append(v)
    while s:
        cur = s.pop()
        if vis[cur]:continue
        vis[cur] = True
        print(cur,end=" ")
        for i in range(len(arr[cur])):
            nxt = arr[cur][len(arr[cur])-1-i]
            if vis[nxt]: continue
            s.append(nxt)
def bfs():
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if vis2[cur] : continue
        vis2[cur] = True
        print(cur,end=" ")
        for nxt in arr[cur]:
            if vis2[nxt]: continue
            q.append(nxt)

dfs(v)
print()
bfs()
