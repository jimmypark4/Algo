N , K = map(int,input().split())
arr = list( list(map(int,input().split())) for _ in range(N))
arr.sort(key= lambda x : [x[1],x[0]])

ex = arr[0]
answer = 1
cnt = 0
for i in range(1,len(arr)):
    ex = arr[i-1]
    if ex[0] != arr[i][0] or ex[1] != arr[i][1]:#학년이나 성별이 다른 경우
        cnt = 1
        answer += 1

    elif ex == arr[i]:#학년이나 성별이 같고 방이 안찬경우
        if cnt < K:
            cnt += 1
        else:
            cnt = 1
            answer += 1
print(answer)