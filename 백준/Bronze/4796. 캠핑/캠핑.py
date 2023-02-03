
cnt=1
results=[]
while 1:
    l,p,v = map(int,input().split())
    if l ==0:
        break
    results.append( (v//p)*l + min(l,(v%p)))
for result in results:
    print(f"Case {cnt}: {result}")
    cnt+=1
