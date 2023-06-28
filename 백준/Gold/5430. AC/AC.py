from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    flag = False
    cmd = list(input())
    n = int(input())
    arr = deque((eval(input())))
    di = True

    for c in cmd:
        if c == 'R':
            di = not di
        elif c == 'D':
            if len(arr) == 0:
                print("error")
                flag = True
                break
            if di == True:
                arr.popleft()
            elif di == False:
                arr.pop()


    if len(arr) != 0:
        print('[',end='')
        if di:
            arr = list(arr)
            print(*arr,sep=',',end='')
        else:
            reversed_list = list(arr)
            a = list(reversed(reversed_list))
            print(*a,sep=',',end='')
        print(']')
    elif flag == False:
        print('[]')
