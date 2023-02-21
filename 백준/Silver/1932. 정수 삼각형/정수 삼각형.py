#1932 정수 삼각형
# 하나씩 해보기엔 졸라 크기 때문에
#dp로 갑니다.

import sys
input = sys.stdin.readline
n = int(input())
#직각 삼각형 모양으로 값을 받아주고 dp테이블도 동일하게 만들어 줍니다.
arr =[list(map(int,input().split())) for _ in range(n)]
# print(*arr,sep="\n")
dp = [[-1 for j in range(i)] for i in range(1,n+1)]
#초기값 설정
dp[0][0]=arr[0][0]

for i in range(n):
    for j in range(i+1):
        if dp[i][j] == -1:
            # if i==1:
            #     dp[1][0]=dp[0][0] + arr[1][0]
            #     dp[1][1]=dp[0][0] + arr[1][1]
            #     continue
            if j==0: #왼쪽끝
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif j==i: # 오른쪽 끝
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else: # 중간
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + arr[i][j]
# print(*dp,sep="\n")
# print(*dp[n-1])
print(max(dp[n-1]))
