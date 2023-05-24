import sys
input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]
cards.sort()

max_card = cards[0]
max_count = 1

current_card = cards[0]
current_count = 1

for i in range(1, N):
    if cards[i] == current_card:
        current_count += 1
    else:
        if current_count > max_count:
            max_card = current_card
            max_count = current_count
        current_card = cards[i]
        current_count = 1

# 마지막 카드들의 개수를 확인
if current_count > max_count:
    max_card = current_card
    max_count = current_count

print(max_card)
