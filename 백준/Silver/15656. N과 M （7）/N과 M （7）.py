import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_arr = list(map(int,input().split()))
input_arr.sort()
arr = []
visited = [0] * n
def dfs():
    if len(arr) == m:
        print(*arr,sep=' ')
        return
    for i in range(0,n):
        arr.append(input_arr[i])
        dfs()
        arr.pop()

dfs()

