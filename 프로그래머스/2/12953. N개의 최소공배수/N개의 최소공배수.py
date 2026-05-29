def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return -1

def solution(arr):
    # 입력 arr 모든 수와의 최소공배수
    # 최소공배수 = 두 수의 곱 / 최대공약수
    answer = 1
     
    # 2, 6, 24, 168
    for a in arr:
        answer = answer * a // gcd(answer, a)
  
    return answer