#15650 N과 M(2)
# 오름차순으로 출력하는 것이므로
#BFS or DFS일 것같다.
#오름차순 모든 경우의 수 출력 => BFS

#편법
from itertools import combinations
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
for combi in combinations(arr,M):
    print(*combi,sep=" ")