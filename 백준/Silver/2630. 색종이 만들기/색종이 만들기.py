import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]

def divide_and_conquer(x, y, size):
    color = arr[x][y]

    # Check if all the elements in the square are of the same color
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                # If not, divide the square into four smaller squares and recursively check each one
                new_size = size // 2
                divide_and_conquer(x, y, new_size)
                divide_and_conquer(x, y + new_size, new_size)
                divide_and_conquer(x + new_size, y, new_size)
                divide_and_conquer(x + new_size, y + new_size, new_size)
                return

    # If all the elements in the square are of the same color, update the answer array
    answer[color] += 1

# Start the divide and conquer algorithm from the top left corner of the entire array
divide_and_conquer(0, 0, n)

# Print the answer
print(answer[0])
print(answer[1])
