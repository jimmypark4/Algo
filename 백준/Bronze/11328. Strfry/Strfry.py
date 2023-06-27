N = int(input())
arr = list(input().split() for _ in range(N))

for a in arr:
    str1 = sorted(a[0])
    str2 = sorted(a[1])
    print("Possible"if str1==str2 else "Impossible")
