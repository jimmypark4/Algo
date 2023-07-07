def solution(sizes):
    max1,max2 = 0,0
    for x,y in sizes:
        # print(x,y)
        a = max(x,y)
        b = min(x,y)
        max1 = max(a,max1)
        max2 = max(b,max2)
    answer = max1 * max2
    return answer