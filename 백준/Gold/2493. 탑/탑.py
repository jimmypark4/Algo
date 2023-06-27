from collections import deque
import sys
import copy
input = sys.stdin.readline
N = int(input())
towers = list(map(int,input().split()))
answer = deque()
stack = []
for index ,value in enumerate(towers):
    while stack:
        if stack[-1][1] > towers[index]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack: 
        answer.append(0)
    stack.append([index,value])  # 인덱스, 값

print(*answer)
