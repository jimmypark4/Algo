import sys
input = sys.stdin.readline
N = int(input())
freq = [0] * 2000001
for _ in range(N):
    num = int(input())
    num += 1000000
    freq[num] += 1
for number ,frequency in enumerate(freq):
    if frequency != 0:
        for _ in range(frequency):
            print(number-1000000,sep='\n')