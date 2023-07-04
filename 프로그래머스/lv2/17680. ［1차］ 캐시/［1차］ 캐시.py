from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    answer = 0    
    q = deque()
    for city in cities:
        city = city.upper()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        
        elif city not in q:
            answer += 5
            if len(q) < cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
                
    return answer