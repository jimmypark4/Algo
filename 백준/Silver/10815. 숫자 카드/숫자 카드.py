n = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
cards = set(map(int, input().split()))  # 상근이가 가지고 있는 숫자 카드
m = int(input())  # 찾아야 할 숫자의 개수
numbers = list(map(int, input().split()))  # 찾아야 할 숫자

# set을 이용하여 찾고자 하는 숫자가 상근이가 가지고 있는 숫자 카드에 있는지 확인
for number in numbers:
    if number in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
