#15651
n, m = map(int, input().split())
s = []
def dfs():
    #길이가 되면 지금까지 모은거 프린트 하고 리턴!
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    #1부터 n 까지 돌면서
    #넣고 재귀호출 넣고 재귀호출 
    for i in range(1, n + 1):
        s.append(i)
        dfs() #m되서 끝나면 그전에꺼 팝하고 다시 2부터 시작!
        s.pop()
dfs()