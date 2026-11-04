def solution(data, col, row_begin, row_end):
    answer = 0
    
    for r in range(0, (len(data)-1)):
        for i in range(r+1, len(data)):
            # 내림차순 부등호 잘 생각하자
            if data[r][col-1] > data[i][col-1]:
                data[r], data[i] = data[i], data[r]
            elif data[r][col-1] == data[i][col-1]:
                if data[r][0] < data[i][0]:
                    data[r], data[i] = data[i], data[r]
        
    for i in range(row_begin, row_end + 1):
        s = 0
        
        for c in range(len(data[0])):
            s += (data[i-1][c] % i)
        
        answer = answer ^ s
    
    
    return answer