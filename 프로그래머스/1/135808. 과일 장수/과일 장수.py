def solution(k, m, score):
    answer = 0

    score = sorted(score)
    
    boxes = len(score) // m 
    total_sum = 0
    
    for i in range(boxes):
        
        sum = 0
        Min = score.pop()
        
        # 어떻게 큰 것부터 꺼내지?
        for j in range(m-1):            
            Min = min(Min, score.pop())
            
        sum += Min * m
        total_sum += sum 
    
    return total_sum