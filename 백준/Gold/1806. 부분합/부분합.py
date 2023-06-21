N,S = map(int,input().split())
arr = list(map(int,input().split()))

s,e,answer = 0,0,0
total = arr[0]
while True:
    if s>e:
        s,e = e,s
        total = sum(arr[s:e+1])

    if total < S:
        e += 1
        if e >= len(arr):
            break
        total += arr[e]


    elif total >= S:
        temp = e - s + 1
        answer = temp if answer == 0 else min(answer, temp)

        total -= arr[s]
        s += 1

        if s >= len(arr):
            break

print(answer)