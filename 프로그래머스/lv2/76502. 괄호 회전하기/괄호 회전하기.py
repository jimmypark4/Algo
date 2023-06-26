"""
    1. 한칸씩 돌려가면서 검사
    2. 맞으면 1 더하기
"""
import copy
from collections import deque
def solution(s):
    answer = 0
    a = deque(s)
    for i in range(len(s)):
        a.rotate(-1)
        b = copy.deepcopy(a)
        stack = []
        flag = True
        
        while len(b):
            c = b.popleft()
            # print(c,stack)
            if len(stack) == 0:
                if c == ']' or c == ')' or c == '}':
                    flag = False
                    break
                elif c == '{' or c == '[' or c == '(':
                    stack.append(c)
            else:
                if (c == ']' and stack[-1] == "[") or (c == '}' and stack[-1] == "{") or (c == ')' and stack[-1] == "("):
                        stack.pop()
                elif c == '{' or c== '[' or c== '(':
                    stack.append(c)
                    
        
        # print(*a,flag)
        if flag == True and len(stack) == 0:
            answer += 1
            

    
    return answer