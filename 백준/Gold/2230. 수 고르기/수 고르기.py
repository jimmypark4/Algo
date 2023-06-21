"""
투 포인터 문제:
st 와 en의 index를 두개를 생성한다.
정렬된 배열의 인덱스를 기준으로 동작.
arr[en] - arr[st] 의 차이가 m보다 작으면 en을 증가
                     차이가 m보다 크거나 같으면 st를 증가시킨다.
st가 고정일 때, 특정 en을 계속 증가시켜도 m을 넘은 이후에는  비교의 의미가 없다.
따라서 m보다 크거나 같으면 st를 증가시킴.

탈출 조건은 en이 끝까지 도달했을 경우, 혹은 차이 m을 만족하는 경우이다.
st의 탈출 조건은 없다.
 st와 en이 같아지면 en이 무조건 먼저 증가 하기 때문이다.
"""

n , m = map(int,input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()

answer = 2000000000+1
st = 0
en = 0
diff = 0
while True:
    diff = arr[en] - arr[st]
    if diff < m:
        en += 1
        if en >= len(arr):
            break
    elif diff > m:
        st += 1
        answer = min(answer,diff)
    if diff == m:
        answer = m
        break

print(answer)