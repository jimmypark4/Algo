from math import ceil

N=int(input())
result=str(N)
arr=[0]*10
for char in result:
    arr[int(char)]+=1
arr[6]=ceil((arr[6]+arr[9])/2)
arr[9]=0
print(max(arr))