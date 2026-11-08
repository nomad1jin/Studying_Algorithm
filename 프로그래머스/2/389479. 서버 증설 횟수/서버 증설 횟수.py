def solution(players, m, k):
    result = [0] * len(players)            # 증설 횟수
    made_server = [0] * len(players)      # 증설된 서버의 수
    
    # k 시간동안 증설된 서버 시간 운영 코드 작성 어렵
    # 17~18 시간대 13명, 4, 3 이해안됨
    # n*m <= < (n+1)*m 때문에 n=4대 
    
    
    # i = len(player)
    
    # while i > 0:
    for j in range(len(players)):
        n = 0
        
        if players[j] < m:
            continue
              
        else:
            # 이용자에 따라 필요한 서버 수 n
            n = players[j] // m
            
            # made_server에 서버 수와 n 체크
            if made_server[j] < n:
                add = n - made_server[j]
                for i in range(j, min(len(players), j+k)):
                    made_server[i] += add
                    result[j] = add
        
    print(result)
    
    return sum(result)