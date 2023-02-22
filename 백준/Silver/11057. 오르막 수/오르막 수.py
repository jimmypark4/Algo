#11057 오르막수
# 10007로 나누는거 보니 수가 졸라크고
# n에 의해 각기 규칙이 있어보이니
# DP로 해봅시다.

N = int(input())

dp = [[0 for i in range(10)] for i in range(N)]
for i in range(1):
    for j in range(10):
            dp[i][j] = 1

for i in range(1,N):
    for j in range(0,10):
       dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # for k in range(j,10):
        #     dp[i][j] += dp[i-1][k]
# print(*dp,sep="\n")

print(sum(dp[N-1])%10007)