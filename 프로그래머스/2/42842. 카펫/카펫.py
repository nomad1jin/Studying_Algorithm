import math

def solution(brown, yellow):

    sum = brown + yellow
    arr = []
    
    # 곱해지는 약수 세트 
    # sum = 12, width = 2, height = 6
    for i in range(1, sum+1):
        if sum % i == 0:
            width = sum // i
            height = i
            
        if (width - 2) * (height - 2) == yellow:
            arr.append(width)
            arr.append(height)
            return arr
    
    