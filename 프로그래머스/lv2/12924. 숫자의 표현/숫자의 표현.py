def solution(n):
    answer = 0
    for i in range(n,0,-1):
        num = 0
        for j in range(i,0,-1):
            num += j
            if num > n:
                break
            elif num == n:
                answer += 1;break
            elif num < n:
                pass
            
    return answer
