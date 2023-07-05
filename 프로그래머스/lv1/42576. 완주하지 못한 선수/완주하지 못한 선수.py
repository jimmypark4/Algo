from collections import Counter
def solution(participant, completion):
    answer = ""
    counter = Counter(participant)
    comple  = Counter(completion)
    counter.subtract(comple)
    for key,values in counter.items():
        if values >= 1:
            answer += key
    return answer