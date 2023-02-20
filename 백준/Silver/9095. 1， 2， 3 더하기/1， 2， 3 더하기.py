#9095 1,2,3 더하기
#dp 문제
# 1+ (~~~)
# 2+ (~~~) 
# 3+ (~~~) 를 구하는 문제 입니다. 
#그래서 반복문을 세번 돌면 dp값이 채워집니다.
#최대인 값을 구한뒤 그값까지 dp테이블을 채운뒤 arr에 있는 값들을 리턴해줌.

T =int(input())
arr = [int(input()) for _ in range(T)]
max_number = max(arr)
# print(max_number)
dp= [0] * (max_number + 1)
#초기값들 설정
if max_number > 0:
    dp[1] = 1
if max_number > 1:
    dp[2] = 2
if max_number > 2:
    dp[3] = 4

for i in range(4, max_number+1):
    # 1을 더하면서 시작할때, 
    # 2를 더하면서 시작할때 
    # 3을 더하면서 시작할 때를 나누어 더함
   for j in range(1,3+1):
       dp[i] += dp[i-j]
# 리스트들에 있는 각각의 값들을 출력!
for j in arr:
    print(dp[j])
# print(*dp,sep=" ")