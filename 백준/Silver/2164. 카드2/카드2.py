from collections import deque
q = deque(i for i in range(int(input()),0,-1))  #큐 생성
while len(q) > 1:
    q.pop()
    q.rotate()
print(q.pop())