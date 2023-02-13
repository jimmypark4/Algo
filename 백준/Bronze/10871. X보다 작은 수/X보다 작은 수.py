#10871
N,X=map(int,input().split())
A=list(map(int,input().split()))
result=[i for i in A if i<X]
for i in result:
    print(i,end=" ")