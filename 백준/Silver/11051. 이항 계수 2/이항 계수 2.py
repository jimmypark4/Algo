#11051 이항계수
#b(n,0)=b(n,n)=1
#b(n,r)=b(n-1,r-1)+b(n-1,r)
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)
N,K = map(int,input().split())
cache=[[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    cache[i][0]=1
    cache[i][i]=1
def b(n,r):
    if cache[n][r] == 0:
        cache[n][r]=b(n - 1, r - 1) + b(n - 1, r)
    return cache[n][r]

result = b(N,K)%10007
print(result)