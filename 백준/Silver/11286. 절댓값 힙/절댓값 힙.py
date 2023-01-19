import sys
import heapq as h
pq=[]
input = sys.stdin.readline
for __ in range(int(input())):
    x = int(input())
    if x:
        h.heappush(pq,(abs(x),x))
    else:
        print(h.heappop(pq)[1] if pq else 0)