def solution(babbling):
    answer = 0
    
    speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        used = ''
        
        
        while len(bab) > 0:
            found = False
            
            for i in range(len(speak)):
                if bab.startswith(speak[i]):
                    
                    if speak[i] != used:
                        found = True    # 발음할 수 있는 거 찾음                   
                        used = speak[i]  # 발음했으면 연속 안 되게 사용함에 넣기
                        bab = bab[len(speak[i]):]  
                        break   # 발음 찾았으므로 for문 종료
                    
                        
            if not found:
                break
                
        if len(bab) == 0:
            answer += 1
    
    return answer