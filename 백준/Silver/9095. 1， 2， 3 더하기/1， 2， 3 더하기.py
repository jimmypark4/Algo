#9095 1,2,3 더하기
T =int(input())
arr = [int(input()) for _ in range(T)]
max_number = max(arr)
# print(max_number)
dp= [0] * (max_number + 1)

if max_number > 0:
    dp[1] = 1
if max_number > 1:
    dp[2] = 2
if max_number > 2:
    dp[3] = 4
for i in range(4, max_number+1):
   for j in range(1,3+1):
       dp[i] += dp[i-j]
       
for j in arr:
    print(dp[j])
# print(*dp,sep=" ")