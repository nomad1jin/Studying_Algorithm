def solution(n, arr1, arr2):
    
    # 십진수를 이진수로
    map1 = []
    map2 = []
    arr = []
    
    for a1 in arr1:
        binary = format(a1, 'b')
        binary = '0' * (n - len(binary)) + binary
        map1.append(binary)
        
    for a2 in arr2:
        binary = format(a2, 'b')
        binary = '0' * (n - len(binary)) + binary
        map2.append(binary)
        
    for i in range(n):
        temp = ''
        
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                temp += "#"
                
            else:
                temp += " "
                
        arr.append(temp)
    
    
    return arr