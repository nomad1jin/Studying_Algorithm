def solution(land):
    answer = 0
    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0][:]
    
    for r in range(1, len(land)):
        for c in range(0, len(land[0])):
            # dp[1][0] = max(max(dp[0][1], dp[0][2]), dp[0][3])
            dp[r][c] = land[r][c] + max(dp[r-1][(c+1)%4], dp[r-1][(c+2)%4], dp[r-1][(c+3)%4])
       
    return max(dp[-1])