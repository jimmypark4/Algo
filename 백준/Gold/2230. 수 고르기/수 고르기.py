n , m = map(int,input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()

answer = 2000000000+1
st = 0
en = 0
diff = 0
while True:
    diff = arr[en] - arr[st]
    if diff < m:
        en += 1
        if en >= len(arr):
            break
    elif diff > m:
        st += 1
        answer = min(answer,diff)
    if diff == m:
        answer = m
        break

print(answer)