#10844 쉬운 계단수
# dp

mod = 1000000000

dp = [[0 for _ in range(10)] for _ in range(101)]

for k in range(0,9+1):
    dp[1][k] = 1

for n in range(2,100+1):
    for k in range(10):
        if k == 0:
            dp[n][k] = dp[n-1][k+1]
        elif k== 9:
            dp[n][k] = dp[n-1][k-1]
        else:
            dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]


N = int(input())

print(sum(dp[N][1:]) % mod)