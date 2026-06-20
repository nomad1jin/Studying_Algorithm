from collections import deque

def solution(cacheSize, cities):
    # 가장 오랫동안 참조되지 않은 페이지를 찾아서 없애주는 작업
    answer = 0
    q = deque(maxlen = cacheSize)
 
    
    for city in cities:
        
        # Test Case 5 "NewYork", "newyork"
        city = city.lower()
        
        # cache hit
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        
        # cache miss
        else :
            answer += 5
            q.append(city)
           
    
    return answer