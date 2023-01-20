from itertools import combinations
# dwarfs =[]
# for __ in range(9):
#     dwarfs.append(int(input()))
dwarfs=[int(input()) for __ in range(9)]
for i in combinations(dwarfs,7):
    if sum(i) == 100:
        for height in sorted(i):
            print(height)
        break