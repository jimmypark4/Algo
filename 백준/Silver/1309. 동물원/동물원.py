N = int(input())
dp = [ i+1 for i in range(2)] 
for _ in range(1,N):
  dp[0] , dp[1] = dp[0] + dp[1] , 2 * dp[0] + dp[1]
print(sum(dp)%9901)