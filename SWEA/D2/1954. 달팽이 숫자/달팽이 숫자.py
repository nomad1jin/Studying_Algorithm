T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    r, c = 0, 0
    d = 0

    for j in range(1, N*N + 1):
        arr[r][c] = j

        nx = r + dx[d]
        ny = c + dy[d]

        # 범위 벗어나거나. 이미 숫자가 있다면(방문) 못가므로 방향 전환
        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] != 0:
            d = (d + 1) % 4
            nx = r + dx[d]
            ny = c + dy[d]
        r, c = nx, ny

    print(f"#{t}")
    for row in arr:
        print(*row)