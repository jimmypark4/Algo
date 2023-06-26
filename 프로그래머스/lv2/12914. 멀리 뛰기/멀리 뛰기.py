def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    if n > 2:
        for i in range(3,2000+1):
            dp[i] = dp[i-2] + dp[i-1]
    return dp[n]%1234567