N = int(input())
arr = [int(input()) for _ in range(N)]
for _ in range(N):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
print(*arr,sep='\n')