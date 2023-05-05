import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_arr = list(map(int,input().split()))
input_arr.sort()
arr = []

def dfs(start):
    if len(arr) == m:
        print(*arr,sep=' ')
        return

    for i in range(0,n):
        if input_arr[i] not in arr:
            arr.append(input_arr[i])
            dfs(start+1)
            arr.pop()
dfs(0)