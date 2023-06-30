from collections import deque
n,k =map(int,input().split())
arr = [-1] * (200001)
q = deque()
q.append(n)
arr[n] = 0
while(q):
    x = q.popleft()
    nxs = [x-1,x+1,2*x]
    for nx in nxs:
        if nx < 0 or nx >= 200000: continue
        if arr[nx] != -1: continue
        arr[nx] = arr[x] + 1
        q.append(nx)
print(arr[k])
