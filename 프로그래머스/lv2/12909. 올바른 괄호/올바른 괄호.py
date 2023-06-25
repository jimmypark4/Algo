def solution(s):
    answer = False
    state = 0
    for ch in s:
        if ch == "(" :
            state += 1
        elif ch == ")" and state > 0:
            state -= 1
        elif ch == ")" and state == 0:
            state = -999999
            answer = False
    
    if state == 0:
        answer = True
            
        
    return answer