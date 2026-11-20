from collections import deque

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    queue = deque(arr)

    for j in range(M):
        queue.append(queue.popleft())

    print(f"#{t} {queue[0]}")