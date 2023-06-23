import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key= lambda x: [x[1],x[0],x[1]-x[0]])
cnt = 1
if n == 1:
    print(cnt)
    exit()

m = arr[0]
for a in arr[1:]:
    if m[1] > a[0]:
        continue
    elif m[1] <= a[0]:
        m = a
        cnt += 1
print(cnt)
