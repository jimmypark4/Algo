import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_arr = list(map(int,input().split()))
input_arr.sort()
arr = []
visited = [0] * n
def dfs(k):
    if len(arr) == m:
        print(*arr,sep=' ')
    for i in range(k,n):
        if input_arr[i] not in arr:
            arr.append(input_arr[i])
            dfs(i+1)
            arr.pop()

dfs(0)

