def solution(bandage, health, attacks):
    
    current_health = health
    count = 0
    
    # 시간을 어떻게 카운트함? 초기 체력으로 했으나 틀림 => 마지막 공격 시간
    # 예제 보면 마지막 공격 언급함!
    for t in range(0, attacks[-1][0] + 1):
   
        count += 1
        attacked = False   
        
        for attack in attacks:
            if attack[0] == t:
                current_health -= attack[1]
                count = 0
                attacked = True
                
                # 맞고 나서 현재 체력을 계산해야 return -1 반환 가능.
                if current_health <= 0:
                    return -1
                
                break
              
        
        # 안 맞은 경우 회복 
        if attacked == False:

            current_health = min(health, current_health + bandage[1])

            if count == bandage[0]:
                current_health = min(current_health + bandage[2], health)
                count = 0

        print(current_health)
    return current_health