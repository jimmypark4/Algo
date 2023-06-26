from collections import deque
def solution(elements):
    answer = set()
    dq = deque(elements)
    arr = [0] * len(elements)
    for i in range(len(elements)):
        dq.rotate()
        for j in range(len(elements)):
            arr[j] += dq[j]
            answer.add(arr[j])
    return len(answer)