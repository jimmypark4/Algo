lists = list(input())
answer = 0
stack = []
temp = 1
for index , c in enumerate(lists):
    # print(index,c,stack)
    if c =="(":
        temp *= 2
        stack.append(c)

    elif c == "[":
        temp *= 3
        stack.append(c)

    elif c == ")":
        if not stack or stack[-1] != "(":
            print(0)
            exit()

        if lists[index-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()

    elif c == "]":
        if not stack or stack[-1] != "[":
            print(0)
            exit()

        if lists[index-1] =='[':
            answer += temp
        temp //= 3
        stack.pop()


print(0) if stack else print(answer)