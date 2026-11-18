T = int(input())

for t in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = [0]

    for num in nums:
        heap.append(num)
        child = len(heap) - 1

        while child > 1:
            parent = child // 2

            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
            else:
                break

    child = n
    answer = 0

    while child > 1:
        child = child // 2
        answer += heap[child]

    print(f"#{t} {answer}")