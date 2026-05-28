def solution(k, tangerine):
    # 귤을 크기별로 분류해서, 서로 다른 종류의 수를 최소화
    # k는 한 상자에 담으려는 개수, 결과는 종류의 최솟값
    # 귤이 가장 많은 크기 순으로 
    
    answer = 0
    dict = {}
    tangerine.sort()
    
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else :
            dict[t] = 1
    
    sum = 0
    sorted_dict = sorted(dict.items(), key = lambda item:item[1], reverse=True)
    for d in sorted_dict:
        if sum >= k:
            return answer
        
        sum += d[1]
        answer += 1
       
    return answer