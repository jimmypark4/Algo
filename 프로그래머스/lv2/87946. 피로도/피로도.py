from itertools import permutations
def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    s = list(i for i  in range(l))
    arr = permutations(s,l)
    for turns in arr:
        # print(turns)
        piro = k
        temp = 0
        for index in turns:
            min_p , cun_p = dungeons[index][0] ,dungeons[index][1]
            if min_p <= piro and piro - cun_p >0:
                piro -= cun_p
                temp += 1
        answer = max(answer,temp)
        
    return answer