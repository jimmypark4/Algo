lasers = list(input())
stack = []
answer = 0
for index in range(len(lasers)-1):
    c = lasers[index]
    if  c =='(' and lasers[index+1] ==')':#레이저 인 경우
        answer += len(stack)
    elif c == '(' and lasers[index+1] == '(': #쇠막대기 여는 경우
        stack.append(c)
        answer += 1
    elif c == ')' and lasers[index-1] ==')':
        stack.pop()
    elif c == ')' and lasers[index-1] == '(':
        pass
print(answer)