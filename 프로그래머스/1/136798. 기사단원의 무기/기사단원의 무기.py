def prime(num):
    
    # 숫자별 약수 개수를 저장
    count = [0] * (num+1)
    
    for i in range(1, num+1):   
        for j in range(i, num+1, i):
            count[j] += 1       # 약수면 개수 증가, 누적
                 
    return count
            
    

def solution(number, limit, power):
    answer = 0
    arr = []
    prime_count = prime(number)    # 구해두고 꺼내쓰자
    
    #1 ~ number
    for num in range(1, number+1):
        
        #num 의 약수 개수 구하기
        if prime_count[num] > limit:
            arr.append(power)
        else:            
            arr.append(prime_count[num])
            
    answer = sum(arr)
        
    
    return answer