import sys

N, M, K = map(int, sys.stdin.readline().split())
notebook = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    stickers.append(sticker)

def rotate_sticker(sticker):
    R = len(sticker)
    C = len(sticker[0])
    rotated_sticker = [[0] * R for _ in range(C)]
    for i in range(R):
        for j in range(C):
            rotated_sticker[j][R-i-1] = sticker[i][j]
    return rotated_sticker

def is_valid_position(x, y, sticker, notebook):
    R = len(sticker)
    C = len(sticker[0])
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
    return True

def attach_sticker(x, y, sticker, notebook):
    R = len(sticker)
    C = len(sticker[0])
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1

def count_filled_cells(notebook):
    count = 0
    for row in notebook:
        count += sum(row)
    return count

for sticker in stickers:
    for _ in range(4):
        R = len(sticker)
        C = len(sticker[0])
        for i in range(N - R + 1):
            for j in range(M - C + 1):
                if is_valid_position(i, j, sticker, notebook):
                    attach_sticker(i, j, sticker, notebook)
                    break
            else:
                continue
            break
        else:
            sticker = rotate_sticker(sticker)
            continue
        break

filled_cells = count_filled_cells(notebook)
print(filled_cells)
