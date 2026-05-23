def solution(people, limit):
    boat = 0    
    people.sort()

    i = 0
    j = len(people) - 1
    while i <= j:
        # 제일 가벼운 애 + 제일 무거운애가 한계보다 작으면 좀 덜 가벼운애로
        if people[i] + people[j] <= limit:
            i += 1
            
        # 리밋보다 크면. 덜 무거운 애로
        j -= 1
        boat += 1
    
    return boat