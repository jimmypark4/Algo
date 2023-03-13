# 기본적인 dfs
# 방문하지 않은 노드를 방문한 경우 dfs를 돌리고
# 한번 dfs를 끝낼 때마다 answer 값을 올려줍니다.
def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(now):
        for i in range(n):
            if now == i:
                continue
            elif computers[now][i] == 1 and visited[i] == False:
                visited[i] = True
                dfs(i)
                
    for i in range(n):
        if visited[i] == False: 
            dfs(i)
            answer += 1
        
    return answer