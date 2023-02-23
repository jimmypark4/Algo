N = int(input())
dp = [0] * 2
dp[0] = 1
dp[1] = 2

for _ in range(1,N):
  dp[0] , dp[1] = dp[0] + dp[1] , 2 * dp[0] + dp[1]


print(sum(dp)%9901)