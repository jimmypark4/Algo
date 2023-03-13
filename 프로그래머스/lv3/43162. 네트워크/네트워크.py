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