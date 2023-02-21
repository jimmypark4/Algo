#1149 RGB거리 
#dp 문제
# 빨강 초록 파랑 인경우를 고려
# 과거 고른 것중에서 작은거, 그리고 이번에 고른 색깔 지정
# 각각 고른 것중에서 최소인거 마지막에 출력
#세가지 경우를 병렬적으로 진행하는 느낌
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0] #지금 0번 고르고 그전에는 1번 2번중 최소
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1] #지금 1번 고르고 그전에는 0번 2번중 최소 
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2] #지금 2번 고르고 그전에는 0번 1번중 최소 
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2])) #지금껏 고른 것들 중에서 최소 출력