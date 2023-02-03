#15686 치킨배달
#완전탐색 문제같음.
from itertools import combinations
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
map= [input().split() for __ in range(N)]
houses=[]
chickens=[]
#치킨집과 가정집 주소 매핑
for j in range(0,N):
    for c in range(0,N):
        if map[j][c]=="1":
            houses.append([j,c])
        elif map[j][c] == "2":
            chickens.append([j,c])
        else:
            pass
#치킨 집마다 치킨거리 구하기
city_chicken_distance=99999
chickens_list=list(combinations(chickens,M))
for choosed_chickens in chickens_list:
    houses_distance = [9999] * len(houses)
    index = 0
    for j1,c1 in houses:
        for j2,c2 in choosed_chickens:
            distance=abs(j1-j2)+abs(c1-c2)
            houses_distance[index]=min(distance,houses_distance[index])
        index+=1

    city_chicken_distance=min(sum(houses_distance),city_chicken_distance)
print(city_chicken_distance)
