N = int(input())
cols = [-1] * N
count = 0
# 대각선 체크
def promising(row, col):
    for i in range(row):
        if cols[i] == col or abs(cols[i] - col) == row - i:
            return False
    return True
# 백트래킹 함수
def backtrack(row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if promising(row, col):
            cols[row] = col
            backtrack(row + 1)
            cols[row] = -1
# 백트래킹 실행
backtrack(0)
print(count)
