from collections import deque
N,M = map(int,input().split())
numbers_1 = deque(list(map(int,input().split())))
numbers_2 = deque(list(map(int,input().split())))
ans = []

for i in range(N+M):
    if len(numbers_2) != 0 and len(numbers_1) != 0:
        if numbers_1[0] < numbers_2[0]:
            ans.append(numbers_1.popleft())
        else:
            ans.append(numbers_2.popleft())
    elif len(numbers_1) == 0:
        ans.append(numbers_2.popleft())
    elif len(numbers_2) == 0:
        ans.append(numbers_1.popleft())
print(*ans,sep=' ')

