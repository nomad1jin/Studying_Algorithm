from collections import deque

def solution(maps):
    answer = 0    
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    distance = [[0] * col for _ in range(row)]
    
    q = deque([(0, 0)])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    ### 시작!
    visited[0][0] = True
    distance[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions: 
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                    
        
    # 다 끝나면 뭐 반복문하던지 해서 못 가면 -1 해야됨
    if visited[row-1][col-1] == False:
        return -1      
    
    
    return distance[row-1][col-1]