M ,N= map(int,input().split())

bol = [False,False] + [True] * (N-1)
answer = 0
primes = set()
#에레머시기의 채
for i in range(N+1):
    if bol[i] == True:
        primes.add(i)
        for j in range(i*2,N+1 ,i):
            bol[j] = False
for i in range(M,N+1):
    if i in primes:
        print(i)



