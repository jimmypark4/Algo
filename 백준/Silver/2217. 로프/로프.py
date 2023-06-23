N = int(input())
arr= list(int(input()) for _ in range(N))
arr.sort(key= lambda x:-x)

answer= 0
for i in range(len(arr)):
    temp = (i+1) * arr[i]
    answer = max(answer,temp)

print(answer)
