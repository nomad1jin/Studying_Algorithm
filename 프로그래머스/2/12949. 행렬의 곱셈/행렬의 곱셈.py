def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(answer)
    
    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                answer[r][c] += arr1[r][k] * arr2[k][c]
    
    return answer