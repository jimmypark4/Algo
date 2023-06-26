def solution(n):
    ans = 0
    b_n = bin(n)[2:]
    ans = b_n.count("1")
    return ans