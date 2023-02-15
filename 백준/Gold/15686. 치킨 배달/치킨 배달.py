#15686 치킨배달
#완전탐색 문제같음.
from itertools import combinations
import sys
input = sys.stdin.readline #입력 시간 빠르게하는 구문

#1. N,M입력
N,M = map(int, input().split()) #입력


#2.지도 입력
map= [input().split() for __ in range(N)]


#3.치킨집과 가정집 주소 매핑
houses=[]  #집의 주소를 저장하는 리스트
chickens=[]#치킨집의 주소를 저장하는 리스트
#x,y축을 돌며 0,1,2 중 1이면 집의 주소를 넣고 2이면 치킨집의 주소로 넣습니다.
for j in range(0,N):
    for c in range(0,N):
        if map[j][c]=="1":
            houses.append([j,c])
        elif map[j][c] == "2":
            chickens.append([j,c])
        else:
            pass


#집과 치킨집들의 좌표가 리스트안에 리스트로 들어감.
# print("house list" + houses)
# print("chicken list"+ chickens)


#4.치킨집이 남겨지는 조합들 만들기
chickens_list=list(combinations(chickens,M)) # combinations( 치킨집 , 고르는 개수)
# print(chickens_list)


#5.각 조합에 대해 "도시의 치킨 거리" 계산
city_chicken_distance=999999  #최소인 도시 치킨거리를 위한 변수 선언
for choosed_chickens in chickens_list:

    houses_distance = [9999] * len(houses) #각 집마다 치킨거리를 구하기 위한 리스트 생성
    index = 0 #집 검색용 인덱스

    #5.a 각 집에 대해 치킨거리 계산
    #각 집에 대해 모든 치킨집들의 치킨거리를 연산 후 그 중 최소값을 해당 집의 치킨거리로 초기화.
    for j1,c1 in houses:
        for j2,c2 in choosed_chickens:
            distance=abs(j1-j2)+abs(c1-c2) #치킨거리 연산
            houses_distance[index] = min(distance,houses_distance[index])
        index+=1

    #각 조합의 도시의 치킨거리 중 최소값 찾기
    city_chicken_distance=min(sum(houses_distance),city_chicken_distance)


#6. 결과값 출력
print(city_chicken_distance)