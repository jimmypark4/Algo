N = int(input())
if N == 1:
    exit()

bol = [False,False] + [True] * (N-1)
primes = []
#에레머시기의 채
for i in range(N+1):
    if bol[i] == True:
        primes.append(i)
        for j in range(i*2,N+1 ,i):
            bol[j] = False

answer = []
#만약 소수에 의해 나누어지면 그값 저장
#다시 그 소수로 나눠보고 안되면 다음거
i = 0
while N != 1:
    prime = primes[i]
    if N % prime == 0:
        answer.append(prime)
        N /= prime
    else:
        i += 1


print(*answer,sep='\n')




