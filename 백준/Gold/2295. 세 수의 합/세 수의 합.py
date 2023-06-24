N = int(input())
arr = list(int(input()) for _ in range(N))
arr.sort()
# print(arr)


two = set()
for i in range(N):
    for j in range(N):
       two.add(arr[i] + arr[j])

for z in range(N-1,-1,-1):
    for k in range(N):
        a = arr[z] - arr[k]
        if a in two:
            print(a + arr[k])
            exit()
