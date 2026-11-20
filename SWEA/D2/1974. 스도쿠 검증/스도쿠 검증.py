T = int(input())

for t in range(1, T + 1):
    arr = []
    result = 1

    for _ in range(9):
        arr.append(list(map(int, input().split())))


    for r in range(9):
        sudoku = set()
        for c in range(9):
            sudoku.add(arr[r][c])
        if len(sudoku) != 9:
            result = 0
            break

    for c in range(9):
        sudoku = set()
        for r in range(9):
            sudoku.add(arr[r][c])
        if len(sudoku) != 9:
            result = 0
            break

    def thirdthird(x, y):
        sudoku = set()

        for r in range(x, x + 3):
            for c in range(y, y + 3):
                sudoku.add(arr[r][c])

        if len(sudoku) != 9:
            return 0

        return 1

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            if thirdthird(r, c) == 0:
                result = 0
                break

    print(f"#{t} {result}")