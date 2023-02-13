import sys
input=sys.stdin.readline

n=int(input())
stack=[]
ans=[]
arr=[int(input()) for i in range(n)]
i,index=0,1
cando = True
while i<n:
    if stack == []:
        stack.append(index)
        index+=1
        ans.append("+")
        # print(arr[i],index,stack)

    while arr[i] != stack[-1]:
        if arr[i] < stack[-1]:
            cando=False
            break
        stack.append(index)
        ans.append("+")
        index+=1
        # print(arr[i],index,stack)
    stack.pop()
    ans.append("-")
    # print(arr[i], index, stack)
    i+=1
if cando:
    for i in ans:
        print(i)
else:
    print("NO")
#ex1 순서도
# 43687521
#
# 1
# 12
# 123
# 1234
# 123
# 12
# 125
# 1256
# 125
# 1257
# 12
# 1
# x