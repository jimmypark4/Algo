#11053 가장 긴 증가하는 부분 수열

# 수열의 길이와 같은 dp테이블을 만들어서
# n번쨰 원소보다 작은 개수를 저장하는 테이블을 만듭니다.
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N


for i in range(N):
    for j in range(i):
        #전있던 것들 중에서 내가 젤 큰거 취하고
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # 거기에 1 더하기.
    dp[i] +=1
print(max(dp))