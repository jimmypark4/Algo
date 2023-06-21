def solution(sequence, k):
    answer = []
    s,e =0,0
    total = sequence[0]
    while True:
        if total == k:
            answer.append([s,e])
            
        if s > e:
            s,e =e,s
            total = sum(sequence[s:e+1])
        
        
        if total < k:
            e += 1
            if e >= len(sequence):
                break
            total += sequence[e]
        
        elif total >= k:            
            total -= sequence[s]
            s += 1
            if s >= len(sequence):
                break
        
    answer.sort(key = lambda x : (x[1]-x[0],x[0]))
    return answer[0]