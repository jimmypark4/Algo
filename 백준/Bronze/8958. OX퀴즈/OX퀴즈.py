#8958 OX퀴즈

n = int(input())

for _ in range(n):
    str = input().strip()
    ans = 0
    cnt = 0
    for c in str:
        if c == "O":
            cnt += 1
            ans += cnt
        elif c =="X":
            cnt = 0
    print(ans)