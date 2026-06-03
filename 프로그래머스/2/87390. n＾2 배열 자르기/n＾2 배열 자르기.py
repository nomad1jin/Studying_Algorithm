def solution(n, left, right):
    
    answer = []

    for i in range(left, right + 1):
        r = i // n
        c = i % n
        answer.append(max(r+1, c+1))
            
    return answer