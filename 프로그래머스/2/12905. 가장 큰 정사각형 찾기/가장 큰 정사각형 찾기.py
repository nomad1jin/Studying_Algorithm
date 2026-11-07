from collections import deque

def solution(board):
    
    answer = 0
    row = len(board)
    col = len(board[0])
    dp = [[0] * col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            if board[r][c] == 0:
                continue
            else:
                dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                answer = max(answer, dp[r][c])
    
    return answer * answer