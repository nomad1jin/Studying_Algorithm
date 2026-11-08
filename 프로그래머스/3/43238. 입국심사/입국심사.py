def solution(n, times):
    answer = 0
    
    # 그냥 배열의 인덱스가 아니라 여기선 기준이 시간임
    # 따라서 1부터 시작하며, 최대 걸릴 수 있는 시간으로 설정
    start = 1
    end = max(times) * n
    
    while start <= end:
        
        # 첫 시작 mid = 30 
        mid = (start + end) // 2
        spend = 0
        
        for t in times:
            spend += mid // t
            
        # n명을 심사하기에 충분한 시간.. 줄이자
        if spend >= n:
            answer = mid
            end = mid - 1
        
        # n명 심사할수 없어. 시간을 늘려야함
        else:
            start = mid + 1
        
    
    return answer