from collections import deque
def solution(s):
    answer = []
    s = s[1:-1]
    b = s.split(",")
    # print(b)
#     if len(b) == 1:
#         answer.append(eval(b[0]).pop());return answer
    
    dic = dict()
    for c in b:
        temp = ""
        for d in c:
            if d == "{" or  d == "}": continue
            temp += d
        temp = int(temp)
        if temp in dic:
            dic[temp] += 1
        else:
            dic[temp] = 1
    sort_dic = sorted(dic.items() , key=lambda x:-x[1])
    for key,value in sort_dic:
        answer.append(key)
    return answer