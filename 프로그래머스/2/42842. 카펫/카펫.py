import math

def solution(brown, yellow):

    # 갈갈갈갈갈갈갈갈
    # 갈         갈
    # 갈         갈
    # 갈         갈
    # 갈         갈
    # 갈갈갈갈갈갈갈갈
    # brown + yellow가 return 곱하기임
    # 가로 - 2, 세로 - 2 = yellow의 가로, 세로
    
    arr = []
    sum = brown + yellow
    
    for i in range(1, sum):
        
        # i가 세로, 나눈게 가로
        if sum % i == 0:
            # i=3, width = 16가정, 8, 6
            width = sum // i
            height = i
            
            # 14 * 1 != 24
            # 6 * 4 == 24
            if (width-2) * (height-2) == yellow:
                if len(arr) == 0:
                    arr.append(width)
                    arr.append(height)

    return arr