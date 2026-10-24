def solution(msg):
    answer = []
    
    string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {num : idx for idx, num in enumerate(string, start=1)}
    prev = next = 0

    while next < len(msg):
        next += 1
        if next == len(msg):
            answer.append(dic[msg[prev:next]])
            break
            
        if msg[prev : next + 1] not in dic:
            # 단어 없으면 사전에 추가
            dic[msg[prev : next + 1]] = len(dic) + 1
            # 있는 이번 단어 출력
            # 출력했으면 다음 단어할 수 있게 이동
            answer.append(dic[msg[prev:next]])
            prev = next
                
    
    return answer

