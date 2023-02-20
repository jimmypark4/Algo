#1463 1로 만들기
# 3으로 나누어 떨어지면 3으로 나누기
# 2로 나누어 떨어지면 2로 나누기
# 1을 뺴기
#이런 거는 그래프로 모든 경우에 따른 가지를 3씩 해서 풀어나가야 하더라
x=int(input())
dp=[0 for _ in range(x+1)]

for i in range(2,x+1):
    if i==2 or i==3:
        dp[i]=1
    elif dp[i]==0:
        dp[i] = dp[i-1]+1
        if i%2 == 0 :
            dp[i] = min(dp[i] , dp[int(i/2)]+1)

        if i%3 == 0 :
            dp[i]=min(dp[i], dp[int(i/3)]+1)
print(dp[x])
