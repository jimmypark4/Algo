n = int(input())

a = set()
for i in range(n):
    name , action = input().split()
    if name not in a and action == "enter":
        a.add(name)
    elif name in a and action == "leave":
        a.remove(name)
a = list(a)
a.sort(reverse=True)
print(*a,sep="\n")