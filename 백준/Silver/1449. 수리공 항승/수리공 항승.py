n , l = map(int,input().split())
loc=list(map(int,input().split()))
loc.sort()
result = 1
tape = loc[0]
for i in loc:
    if (i < tape+l):
        pass
    else:
        tape = i
        result += 1
print(result)