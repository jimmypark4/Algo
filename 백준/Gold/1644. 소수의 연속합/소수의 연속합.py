'''
소수의 연속합
1. 에라이토소테넷 의 채
2. 투포인터
'''

answer = 0
n = int(input())
if n == 1:
    print(0)
    exit()
a = [False,False] + [True]*(n-1)
primes=[]

#에라토스테네스의 채
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
#투포인터
s,e = 0,0
total = primes[0]
while True:
    # if s > e:
    #     s,e = e,s
    #     total = sum(primes[s:e])

    if total == n:
        answer += 1

    if total < n:
        e += 1
        if e >= len(primes):
            break
        total += primes[e]
    elif total >= n:
        total -= primes[s]
        s += 1
        if s >= len(primes):
            break



print(answer)