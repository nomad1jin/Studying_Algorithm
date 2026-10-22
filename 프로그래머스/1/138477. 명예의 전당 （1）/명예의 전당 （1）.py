def solution(k, score):
    
    answer = [] # 발표 점수 출력이 정답
    arr = []    # 명예의 전당
    day = 0
    announce = 100000
    
    for s in score:
        day += 1
        
        if day <= k:
            arr.append(s)
            announce = min(s, announce)
            answer.append(announce)
            
        else:
            arr.sort()      # 오름차순
            
            if s > arr[0]:          # 기존 명예의 전당 가장 큰 값보다 이번 값이 크면..
                n = arr.pop(0)
                arr.append(s)          
                answer.append(min(arr))      
            else:
                answer.append(arr[0])
                
            
    
    return answer