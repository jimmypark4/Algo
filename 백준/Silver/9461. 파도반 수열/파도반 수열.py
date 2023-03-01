#9461 파도반 수열
#f(n) = f(n-1)+f(n-5)
T = int(input())
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1

dp[3] = 2
dp[4] = 2

dp[5] = 3


for i in range(6,100):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(T):
    N = int(input())
    print(dp[N-1])