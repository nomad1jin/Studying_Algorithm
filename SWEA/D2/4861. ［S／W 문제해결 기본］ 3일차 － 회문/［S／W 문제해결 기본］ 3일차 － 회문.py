T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(input())

    answer = ""

    # 가로 검사
    for row in arr:
        for i in range(N - M + 1):
            s = row[i:i + M]

            if s == s[::-1]:
                answer = s

    # 세로 검사
    for col in range(N):
        string = ""

        for row in range(N):
            string += arr[row][col]

        for i in range(N - M + 1):
            s = string[i:i + M]

            if s == s[::-1]:
                answer = s

    print(f"#{t} {answer}")