# # 1018 체스판 다시 칠하기
# # 알고리즘:브루트 포스 알고리즘
# # 생각 경우의 수가 크지 않을 것으로 예상 하나씩 다해보기
# # 1. 맨 왼쪽의 칸이 흰색인 경우
# # 2. 맨 왼쪾의 칸이 검은색인 경우
# # 2가지 경우에 대해 고쳐야하는 칸은 true false로 만들기.
# # 그후에 2가지 경우에 대해 최소값을 구한 뒤 출력
# # 구현 해보기
n,m     = map(int, input().split())
board =[input() for _ in range(n)]
ans= 100
def check(x, y, bw):
    cnt=0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2:
                if  board[y+i][x+j] == bw:
                    cnt +=  1
            elif  board[y+i][x+j] != bw:
                    cnt +=  1
    return cnt
for i in range(0,m-7):
    for j in range(0,n-7):
        ans = min (ans, min(check(i,j,"B"),check(i,j,"W") ) )
print(ans)

