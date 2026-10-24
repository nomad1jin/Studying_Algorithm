def solution(a, b, n):
    answer = 0
    
    while n >= a:
        take = n - (n % a)
        get = n // a * b
        answer += get
        
        now = n - take + get
        n = now
    
    return answer