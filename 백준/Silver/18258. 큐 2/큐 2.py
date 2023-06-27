from collections import deque
import sys
input = sys.stdin.readline
N  = int(input())
commands = list(input() for _ in range(N))
dq = deque()
# print(commands)
for cmd in commands:
    if cmd[1] == "u":
        value = int(cmd[4:-1])
        # print(value)
        dq.append(value)


    elif cmd[0] == "p":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.popleft())

    elif cmd[0] == "s":
        print(len(dq))

    elif cmd[0] == "e":
        print("1") if len(dq) == 0 else print('0')

    elif cmd[0] == "f":
        if len(dq) == 0:
            print("-1")
        else:
            c = dq.popleft()
            print(c)
            dq.appendleft(c)

    elif cmd[0] == "b":
        if len(dq) == 0:
            print("-1")
        else:
            c = dq.pop()
            print(c)
            dq.append(c)
# print(dq)
    # print(cmd,dq)