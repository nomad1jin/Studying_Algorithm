def solution(n):
    answer = ''
    
    num = ['4', '1', '2']
    
    # n==3이라면 n=1, mod=0
    # 1, 2, 0
    # 이러면 마지막 자리수는 1 2 4 반복 활용가능한데.. 
    # 3의 배수일때마다 몫이 올라가서 규칙에 어긋나보여.. 몫 - 1
    

    while n > 0:
        
        n, mod = divmod(n, 3)

        answer = num[mod] + answer
        
        if mod == 0:
            n -= 1
    
    return answer