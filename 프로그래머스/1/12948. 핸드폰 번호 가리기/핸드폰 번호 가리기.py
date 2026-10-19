def solution(phone_number):
    answer = ''
    
    end = len(phone_number) - 4
   
    for i in range(0, end):
        answer += '*'
    
    answer = answer + phone_number[-4:]
    return answer