#1932 정수 삼각형
# 깊이 우선 탐색으로 풀어야하나..
# dp로 풀어야하나..
#dp 로간다.
# 전에 왔을 때 자리의 최대수를 놓고
# 내가 오른쪽위에 왼쪽위를 받을 때 최대인걸 선택해서 업데이트
# 근데 맨 왼쪽이나 끝에는 그냥 본인 머리 위에 거를 선택하는 구문을 추가
#해서 맨 밑바닥에 있는 것중에서 최고 큰거를 팝!

import sys
input = sys.stdin.readline
n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
# print(*arr,sep="\n")
dp = [[-1 for j in range(i)] for i in range(1,n+1)]
dp[0][0]=arr[0][0]

for i in range(n):
    for j in range(i+1):
        if dp[i][j] == -1:
            if i==1:
                dp[1][0]=dp[0][0] + arr[1][0]
                dp[1][1]=dp[0][0] + arr[1][1]
                continue
            if j==0: #왼쪽끝
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif j==i: # 오른쪽 끝
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else: # 중간
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + arr[i][j]
# print(*dp,sep="\n")
# print(*dp[n-1])
print(max(dp[n-1]))
