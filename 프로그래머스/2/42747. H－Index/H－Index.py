def solution(citations):
    answer = []
    
    for h in range(len(citations) + 1):
        up = 0
        
        for num in citations:
            if num >= h:
                up += 1
                
            if up >= h:
                answer.append(h)
    answer.sort()            
   
    return answer[-1]