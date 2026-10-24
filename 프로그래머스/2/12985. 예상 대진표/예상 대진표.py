def solution(n,a,b):
    answer = 0

    # 몫과 나머지 더하기?
    # 같아지는 지점에서는 둘다 1임
    while a != b:
        a = (a // 2 + a % 2)
        b = (b // 2 + b % 2)
        answer += 1    

    return answer