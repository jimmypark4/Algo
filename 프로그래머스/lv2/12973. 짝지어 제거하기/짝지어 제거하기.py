def solution(s):
    answer = 1
    arr = []
    for i in s:
        if len(arr) == 0:
            arr.append(i)
            continue
            
        if arr[-1] == i:
            arr.pop()
        elif arr[-1] !=i:
            arr.append(i)
            
    if len(arr) != 0:
        answer = 0
        
    return answer