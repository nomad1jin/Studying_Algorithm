from collections import deque

def bfs(board, r, c):
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    q = deque()
    count = 0
    q.append((r, c, count))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while q:
        
        x, y, count = q.popleft()
        visited[x][y] = True
        
        for i in range(4):
            
            nx = x
            ny = y
           
            # 미끄러지기~~~~
            # D를 만나면 break 좌표 갱신
            while 0 <= nx+dx[i] < len(board) and 0 <= ny+dy[i] < len(board[0]):
                
                # 다음 좌표와 D랑 비교
                if board[dx[i] + nx][dy[i] + ny] == 'D':
                    break
                    
                nx += dx[i]
                ny += dy[i]
                    
                
            # 순회하다가 G면 바로 멈추는 것 XX
            # 멈춘 지점이 G여야 하므로, while 밖에서 실행
            if board[nx][ny] == 'G':
                return count + 1
            
            # G이 아니라면 큐에 추가해서 반복
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))
                # D를 만날때만 count하게되면..음.. 게임판 범위를 벗어날때 카운트가 안돼
                
                    
        
    return -1


def solution(board):
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'R':
                return bfs(board, r, c)
