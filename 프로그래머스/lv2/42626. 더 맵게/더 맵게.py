"""
    1. 스코빌을 힙으로 만듬
    2. 음식 두 개 일 때 까지 진행
        가장 작은 값 꺼내기
        두번째로 작은 값 꺼내기
        둘을 섞어서 넣기
        카운트 ++

"""
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >= 2:
        a = heapq.heappop(scoville)
        if a < K:
            b =  heapq.heappop(scoville)
            c= a + (2*b)
            heapq.heappush(scoville,c)
            cnt += 1
        elif a >= K:
            heapq.heappush(scoville,a)
            break
    if heapq.heappop(scoville) < K:
        cnt = -1



    return cnt