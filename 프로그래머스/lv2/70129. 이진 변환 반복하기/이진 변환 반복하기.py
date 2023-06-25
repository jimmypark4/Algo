def solution(s):
    times = 0
    count = 0
    
    def binary_trans(s,count):
        #0은 제거하고 1은 남기고 
        value = ""
        for c in s:
            if c =="0":
                count += 1
            elif c =="1":
                value += "1"
                
        c = len(value)
        bi_num = ""
        
        while c > 0:
            if c%2 == 1:
                bi_num+="1"
            else:
                bi_num+="0"
            
            c = int(c/2)
        
        bi_num=bi_num[::-1]
        return bi_num,count
    
    while s != "1":
        times +=1
        s,count = binary_trans(s,count)
    
    answer = [times,count]
    return answer