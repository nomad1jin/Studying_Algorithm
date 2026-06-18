from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    
    while q:
        max_n = max(q)
        pop_n = q.popleft()
        location -= 1  # 하나 꺼냈으니 위치 - 1
        
        if pop_n < max_n:
            q.append(pop_n) # 튜플
            
            # 만약 꺼내기 전 문서가 인덱스 0이라면 -1이 됨. 
            # 추가되었으니 이제 마지막 인덱스가 됨
            if location < 0:
                location = len(q) - 1
            
        else :
            # 없으면 프로세스 실행
            answer += 1
            if location < 0:
                return answer
    
    return answer