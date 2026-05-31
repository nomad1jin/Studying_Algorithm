def solution(want, number, discount):
    answer = 0
    dic = {}
    count = {}
    
    for w, n in zip(want, number):
        dic[w] = n
    
    for i in range(len(discount) - 9):
        dic2 = {}
        
        for j in range(i, i+10):
            if discount[j] in dic2:
                dic2[discount[j]] += 1
            else :
                # 전부터 생각못하는 포인트:
                # 딕셔너리에 없는 거면 1을 해줘야함 (등록)
                dic2[discount[j]] = 1
                
        if dic == dic2:
            answer += 1
            
    return answer