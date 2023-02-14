import sys
input =sys.stdin.readline
K=int(input())
account=[]
for i in range(K):
    num=int(input())
    if num:
        account.append(num)
    else:
        account.pop()
print(sum(account))