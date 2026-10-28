def solution(storey):
    answer = 0
    
    while storey > 0:
        
        a = storey % 10
        next_digit = (storey // 10) % 10
        
        # 작은수면 뺴고 크면 더한다
        # 5 같은 경우는 다음 자리까지 고민해야된다
        
        
        if a < 5:
            answer += a
   
        elif a > 5 or (a == 5 and next_digit >= 5):
            answer += (10 - a)
            # 95를 생각해보자
            storey += (10 - a)
        
        else :
            # a == 5 and next_digit < 5라면..
            # 35
            answer += (10 - a)
                            
        storey //= 10
            
    
    return answer