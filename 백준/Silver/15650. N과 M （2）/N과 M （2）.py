import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def dfs(start, depth):
    if depth == m:
        print(*arr)
        return

    for i in range(start, n+1):
        arr.append(i)
        dfs(i+1, depth+1)
        arr.pop()

dfs(1, 0)
