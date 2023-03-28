#Input 함수 최적화
import sys
input = sys.stdin.readline
#입력
n = int(input())
# arr = [list(map(int,input().rstrip())) for _ in range(n)]
arr = [list(( map(lambda x:x+1,map(int,input().split())))) for _ in range(n)]
answer = [0,0,0]

"""
분할 정복 방식 알고리즘
전체 반복문을 돌며 만약 색이 같지 않으면 4조각내어 함수 다시 실행
최종적으로 만복문을 통과한다면 색이 같으므로 color값 추가
answer에 저장된 값을 마지막으로 출력하면 정답.
"""

def divide_and_conquer(x, y, size):
    color = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                new_size = size // 3
                divide_and_conquer(x, y, new_size)
                divide_and_conquer(x, y + new_size, new_size)
                divide_and_conquer(x, y + 2*new_size, new_size)

                divide_and_conquer(x + new_size, y, new_size)
                divide_and_conquer(x + new_size, y+ new_size, new_size)
                divide_and_conquer(x + new_size, y + 2*new_size, new_size)

                divide_and_conquer(x + 2*new_size, y , new_size)
                divide_and_conquer(x + 2*new_size, y + new_size, new_size)
                divide_and_conquer(x + 2*new_size, y + 2*new_size, new_size)

                return
    answer[color] += 1


# Start the divide and conquer algorithm from the top left corner of the entire ay
divide_and_conquer(0, 0, n)

# Print the answer
print(*answer,sep=" ",end="")
