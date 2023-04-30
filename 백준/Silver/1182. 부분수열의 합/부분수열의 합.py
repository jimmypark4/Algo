import sys
input = sys.stdin.readline

N , S = map(int, input().split())
arr = list(map(int,input().split()))
cnt = 0
ans = []

def dfs(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt +=1
        

    for i in range(start, N):
        ans.append(arr[i])
        dfs(i+1)
        ans.pop()


dfs(0)
print(cnt)