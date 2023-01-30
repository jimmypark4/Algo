#2748 피보나치 수 2
# # 캐쉬를 사용하지 않은 경우
# # 이런식으로 사용하면 f가 기하급수적으로 호출되므로
# # 효율적인 컴퓨터가 되지 못한다.
# def f(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#
#     return f(n-1) + f(n-2)
# print(f(int(input())))

#그래서 이런식으로 캐쉬를 만들어서 -1 을 통해 구분함
cache = [-1]*91
cache[0]=0
cache[1]=1

def f(n):
    if cache[n] == -1:#계산한 적이 없으면 계산을 하고 아니면 계산하지 않음
        cache[n]= f(n-1) + f(n-2)
    return cache[n]
print(f(int(input())))
