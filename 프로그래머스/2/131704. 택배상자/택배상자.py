from collections import deque

def solution(order):
    answer = 0
    
    # 시간 초과 -> pop말고 popleft deque()사용
    priority = deque(sorted(order))
    sub_container = []
    
    for o in order:
        
        # priority가 비었는지 꼭 확인하기, 안 그럼 에러
        # while에서 pop()을 계속 하기 때문에 if에서도 확인해야함
        
        while priority and priority[0] < o:
            sub_container.append(priority.popleft())
        
        if priority and o == priority[0]:
            priority.popleft()
            answer += 1
            
        elif sub_container and sub_container[-1] == o:
            sub_container.pop()
            answer += 1
            
        else:
            break        
    
    return answer