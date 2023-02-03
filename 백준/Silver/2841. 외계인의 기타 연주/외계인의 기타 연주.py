import sys
input = sys.stdin.readline
N,P = map(int , input().split())
lines=[ [] for _ in range(7)]
count = 0
arrays=[list(map(int,input().split())) for _ in range(N)]
for line ,plat in arrays:
    while len(lines[line]) > 0 and lines[line][-1] > plat:  # 새 플랫이 더 낮을 떄 => 손가락 뗌
        lines[line].pop()  # 떼기
        count += 1
    if len(lines[line]) == 0 or lines[line][-1] < plat:
        lines[line].append(plat)  # 누르기
        count += 1
print(count)