def quad(arr, answer, x, y, size):
    
    first = arr[x][y]
    is_same = True
    half = 0

    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != first:
                # 하나라도 다르면 분할할듯
                is_same = False
                break
        if not is_same:
            break
        
    if is_same:
        answer[first] += 1
                
    else:
        half = size // 2    
        
        # row / 2로 쪼개
        # 시작 좌표만 다 설정하고
        # 이중 포문, size 2씩 하면 됨
        quad(arr, answer, x, y, half)
        quad(arr, answer, x, y + half, half)
        quad(arr, answer, x + half, y, half)
        quad(arr, answer, x + half, y + half, half)
            

def solution(arr):
    answer = [0, 0]
    row = len(arr)
     
    quad(arr, answer, 0, 0, row)
    
    return answer