step = int(input())
stairs = [int(input()) for _ in range(step)]

dp = [0] * step

dp[0] = stairs[0]
if step > 1:
    dp[1] = stairs[0] + stairs[1]
if step > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, step):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])
