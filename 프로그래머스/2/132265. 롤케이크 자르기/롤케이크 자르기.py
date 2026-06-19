def solution(topping):
    answer = 0
    
    old = set()
    young = {}
    
    for t in topping:
        if t in young:
            young[t] += 1
        else :
            young[t] = 1 

    for s in topping:            
        old.add(s)
        young[s] -= 1
        
        if s in young:
            if young[s] == 0:
                del young[s]
        
        if len(old) == len(young):
            answer += 1
    
    return answer