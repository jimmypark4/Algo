import sys
input = sys.stdin.readline

n , m = map(int , input().split())
s = list(map(int,input().split()))

global ans
ans = 0

def dfs(index,_sum):
    global ans
    if index == n:
        if _sum == m:
            ans += 1
        return
    dfs(index+1, _sum + 0)
    dfs(index+1, _sum + s[index])

dfs(0,0)
if m == 0:
    ans -= 1
print(ans)

