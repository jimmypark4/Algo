#2293 동전 1
n,k = map(int, input().split() )
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1
# print(n, k, coins)
#코인의 경우의수를 생각해서
#코인보다 지금 k가 적으면 더하고 아니면 걍 넘기기
for coin in coins:
    for i in range(coin,k+1):
        if i-coin>=0:
            dp[i] += dp[i-coin]
print(dp[k])