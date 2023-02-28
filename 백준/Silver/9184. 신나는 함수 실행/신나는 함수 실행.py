#9148 신나는 함수 재귀
global dp
dp =[[[0 for _ in range(102)] for _ in range(102)] for _ in range(102)]
def w(a,b,c):
    aa = a + 50
    bb = b + 50
    cc = c + 50

    if dp[aa][bb][cc] == 0:
        if a <= 0 or b <= 0 or c <= 0:
            dp[aa][bb][cc] = 1
            return dp[aa][bb][cc]
        elif a > 20 or b > 20 or c > 20:
            dp[aa][bb][cc] = w(20,20,20)
            return dp[aa][bb][cc]
        elif a<b and b<c:
            dp[aa][bb][cc] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dp[aa][bb][cc]
        else:
            dp[aa][bb][cc] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dp[aa][bb][cc]
    else: return dp[aa][bb][cc]
while(1):
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        exit(0)
    print(f"w{a,b,c} =",sep=" ",end=" ")
    print(w(a,b,c))