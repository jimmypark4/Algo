#2225 합분해
#다이나믹 프로그래밍

#f(n,k) = f(0,k-1) + f(1,k-1) + f(2,k-1) + f(3,k-1) --- + f(n,k-1) + f
#f(n,k) = f(n-1,k) + f(n,k-1)

mod = 1000000000 #나눗셈을 위한 고정수
N,K =map(int,input().split() ) #N,K 받기

arr = [[0 for col in range(K+1)] for row in range(N+1)] #2차원 행렬 생성 행은 N 열은 K 
arr[0][0]=1 #초기화를 위한 1
# 가로로 한줄씩 돌아가면서 점화식 진행
for n in range(N + 1): 
    for k in range(1,K + 1):
        arr[n][k] = arr[n-1][k]+ arr[n][k-1]#f(n,k) = f(n-1,k) + f(n,k-1)

# print(*arr,sep="\n") # 배열 출력 확인
print(arr[N][K] % mod) # 결과값나누어 출력

