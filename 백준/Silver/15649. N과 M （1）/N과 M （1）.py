#15649 N과 M (1)

#1. 야매 풀이법
# 그저 itertools import 한 다음
# permutations(arr,M) 돌리면 튜플로 경우의 수 다 나온거 출력
# import itertools
# N, M = map(int, input().split())
# arr = [i for i in range(1,N+1)]
# for x in itertools.permutations(arr, M):
#     for i in range(M):
#         print(x[i],end=" ")
#     print()
#

# 2. 정석 풀이법 백트레킹
# dfs의 구현 방식 중 하나
# 백트레킹
N, M = map(int, input().split()) # 1~N 까지 정수중 #M가지 선택
s = []
def dfs():
    if len(s) == M: #M 가지 선택 완료 하면 
        print(' '.join(map(str, s))) #" ".join(map(str, s)) 로 출력
        return

    for i in range(1, N + 1): #N+1 까지 다 탐색 할때까지
        if i not in s: #s안에 없으면
            s.append(i) #추가
            dfs() #재귀 다시 돌리고오
            s.pop() #있던거 스택에서 팝 젤뒤에꺼

dfs() #재귀 시작