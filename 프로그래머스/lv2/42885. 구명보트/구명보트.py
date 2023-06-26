from collections import deque

def solution(people, limit):
    people.sort()
    dq = deque(people)
    boat = 0
    answer = 0    
    while len(dq) > 0:
        if boat == 0:
            answer += 1
            boat += dq.popleft()
        else:
            p = dq.pop()
            if boat + p > limit:
                answer += 1
            elif boat + p <= limit:
                boat = 0 
    return answer