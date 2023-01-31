#10844 쉬운계단수
#n자리수와 마지막 자리수 d로 나눔
#f(n,d)= f(n,d-1) +f(n,d+1) (단 ,d=(0,9))
n=int(input()) # N >= 1 and N <=100 인 자연수
steps=[[0]*10 for _ in range(n+1)]#모두 0으로 초기화된  n x 10배열 생성
for i in range(1,10):# n=1 인 인접수 계산
    steps[1][i] = 1 #마지막 자리가 0일떄를 제외하고 모두 1이다.
for i in range(1,n+1): # n=1~n까지 모든 일의 자리수를 돌며 계산함.
    for j in range(0,10):
        if steps[i][j] == 0: #bottom up 방식으로 진행
            if j==0: #0과 9는 각각 1 과 9밖에 진행을 못함.
                steps[i][j] = steps[i-1][j+1]
            elif j==9:
                steps[i][j] = steps[i-1][j-1]
            else: #나머지는 두 경우다 진행.
                steps[i][j] = steps[i-1][j+1] + steps[i-1][j-1]
result=0
for i in range(0,10):
    result += steps[n][i]
print(f"{result%1000000000}")






