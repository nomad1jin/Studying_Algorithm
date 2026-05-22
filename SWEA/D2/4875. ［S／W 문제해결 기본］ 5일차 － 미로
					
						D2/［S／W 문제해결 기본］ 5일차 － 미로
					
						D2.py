T = int(input())

def miro(r, c, n, visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    if arr[r][c] == 3:
        return True
    visited[r][c] = True
    
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if not visited[nx][ny] and arr[nx][ny] != 1:
                if miro(nx, ny, n, visited):
                    return True
      
    return False

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    start_r, start_c = 0, 0
    
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 2:
                start_r = r
                start_c = c
    
    result = miro(start_r, start_c, n, visited)
    
    print(f"#{tc} {1 if result else 0}")