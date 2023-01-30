#11051 이항계수
#b(n,0)=b(n,n)=1
#b(n,r)=b(n-1,r-1)+b(n-1,r)
#bottom up 방식
N,K = map(int,input().split())
cache=[[0]*(N+1) for _ in range(N+1)]
#N*N의 이차원 배열을 생성함
for i in range(N+1):
    cache[i][0] = 1
    cache[i][i] = 1
    for j in range(N+1):
        if cache[i][j] ==0:
            cache[i][j]=cache[i-1][j-1]+cache[i-1][j]
   # print(cache[i])
def b(n,r):
    return cache[n][r]

result = b(N,K)%10007
print(result)