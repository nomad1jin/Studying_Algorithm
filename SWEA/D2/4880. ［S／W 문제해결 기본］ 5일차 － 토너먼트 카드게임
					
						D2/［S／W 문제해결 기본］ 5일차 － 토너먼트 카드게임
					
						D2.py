T = int(input())

def tournament(start, end):
    if start == end:
        return start
    first_g = tournament(start, (start+end)//2)
    second_g = tournament((start+end)//2 + 1, end)
    return rcp(first_g, second_g)

def rcp(first, second):
    n = abs(arr[first] - arr[second])
    if n == 0:
        return first
    elif n == 1:
        if arr[first] > arr[second]:
            return first
        else :
            return second
    elif n == 2:
        if arr[first] < arr[second]:
            return first
        else :
            return second

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    # 여기 토너먼트 범위에 n을 그대로 넣으면 범위 에러가 난다.
    print(f"#{test_case} {tournament(0, n-1) + 1}")
