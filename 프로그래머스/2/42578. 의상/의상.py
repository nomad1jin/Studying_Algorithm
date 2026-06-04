def solution(clothes):

    type = {}
    
    for clothe in clothes:
        if clothe[1] in type:
            type[clothe[1]] += 1
        else :
            type[clothe[1]] = 1
        
    mul = 1
    for t in type:
        mul *= (type[t] + 1)
    
    return mul-1