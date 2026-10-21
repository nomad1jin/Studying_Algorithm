def solution(nums):
    answer = 0
    
    mon = {}
    for num in nums:
        if num not in mon:
            mon[num] = 1
        else:
            mon[num] += 1
        
        answer = min(len(nums)//2, len(mon))
    
    return answer