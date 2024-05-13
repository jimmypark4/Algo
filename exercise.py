# input two numbers a and b, print all numbers between a and b
a,b = input().split()
a = int(a)
b = int(b)


if a > b:
    a,b = b,a
print(b-a-1)
for i in range(a+1,b):
    print(i,end=" ")