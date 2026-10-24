def solution(n):
    answer = 0
    base = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        base += str(mod)
    
    
    return int(base, 3)