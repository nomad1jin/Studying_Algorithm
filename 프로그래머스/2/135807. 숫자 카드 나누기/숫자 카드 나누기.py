from math import gcd

def calculate(arrayA, arrayB):
    
    num = arrayA[0]
 
    for a in arrayA:
        num = gcd(num, a)
    
    for b in arrayB:
        if b % num == 0:
            return 0

    return num        

def solution(arrayA, arrayB):
    answer = 0
    dic = {}
    
    answer = max(calculate(arrayA, arrayB), calculate(arrayB, arrayA))
    
    return answer