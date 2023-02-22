#15649 N과 M (1)
import itertools
N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
for x in itertools.permutations(arr, M):
    for i in range(M):
        print(x[i],end=" ")
    print()