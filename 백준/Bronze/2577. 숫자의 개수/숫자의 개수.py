A=int(input())
B=int(input())
C=int(input())

result=str(A*B*C)
arr=[0]*10
for char in result:
    arr[int(char)]+=1
for i in range(10):
    print(arr[i])