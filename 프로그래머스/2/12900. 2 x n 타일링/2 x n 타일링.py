def solution(n):
    answer = 0
    
    # 왜 IndexError? 리스트 크기 지정
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    if n < 3:
        answer = dp[n]
    
    else:
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
            answer = dp[i]
    
    return answer