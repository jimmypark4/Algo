K, N = map(int, input().split())
arr = list(int(input()) for _ in range(K))
arr.sort()
# print(arr)

def cnt_lens(length,arr):
    total = 0
    for a in arr:
        total += int(a//length)
    return total
def binary_search(arr,N):
    st,en = 1 , max(arr)
    while st < en:
        mid = int((st+en+1)/2)
        a = cnt_lens(mid,arr)
        if a < N: #타겟보다 a가 작은 경우, 더 작게 length 감소
            en = mid -1
        elif a >= N:#length 늘려보기
            st = mid #여기까지가 N최대 이므로 그냥 st= mid로 진행!

    return st #끝났으면은 st을 반환 mid하니까 오류뜸. #st가 마지막N 이 만족한 곳이기 떄문인거같음
print(
binary_search(arr,N)
)
