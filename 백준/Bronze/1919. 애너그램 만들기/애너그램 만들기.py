str1= input()
str2= input()

str1 = sorted(str1)
str2 = sorted(str2)
dict1 = dict()
for i in range(ord('a'),ord('z')+1):
    dict1[chr(i)] = 0

for c in str1:
    dict1[c] += 1
for c in str2:
    dict1[c] -= 1
answer = 0
for i in dict1.values():
    answer += abs(i)
print(answer)