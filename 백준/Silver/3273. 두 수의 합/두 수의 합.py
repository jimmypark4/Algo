import itertools
import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))

X = int(input())
ans = 0
left, right = 0, n - 1
while left < right:
    result = arr[left] + arr[right]
    if result == X:
        ans += 1
        left += 1
    elif result > X:
        right -= 1
    else:
        left += 1
print(ans)
