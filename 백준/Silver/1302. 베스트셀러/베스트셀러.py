import sys
input = sys.stdin.readline
d ={}
for _ in range(int(input())):
    key = input()
    if key in d:
        d[key] +=1
    else:
        d[key] = 1
dict2= dict(sorted(d.items()))
dict3 = sorted(dict2.items(),key=lambda x:x[1],reverse=True)
print(dict3[0][0])