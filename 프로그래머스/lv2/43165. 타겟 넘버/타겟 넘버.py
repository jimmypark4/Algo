# dfs bfs 문제 
# bfs 혹은 dfs를 이용하여 탐색한 값을 저장하는 배열을 만든뒤
# 해당값이 존재하는 경우를 세서 출력함
def solution(numbers, target):
    arr = [0]                   #노드들을 저장할 배열 덧셈이므로 0 으로 생성
    for i in numbers:           #들어온 숫자를 다 돌아야 하므로 반복문 설정
        temp = []               #각 숫자별로 연산하므로 temp 생성
        for j in arr:           
            temp.append(j+i)    #더하거나 뺴거나 이므로 temp에 추가
            temp.append(j-i)
        arr = temp              #기존에 있었던 노드들을 지우고 
                                #새로 들어온 i를 기준으로 빼고 더하고 한 새로운 배열로 업데이트.
    answer = arr.count(target)  # target 값의 개수를 센다.
    return answer