def solution(s):
    s = s.lower()
    answer= ""
    flag = True # 대문자 만들어야 하는 플래그
    for ch in s:
        if ch >= "a" and ch <= "z" and flag == True:
            ch = ch.upper()
            flag = False
        
        
        flag = False
        
        if ch == " ":
            flag = True
            
        answer+=ch

    return answer