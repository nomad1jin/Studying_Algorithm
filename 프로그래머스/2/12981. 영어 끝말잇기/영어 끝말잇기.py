def solution(n, words):
    answer = []
    # 가장 먼저 탈락하는 사람의 번호, 
    # 그 사람이 자신의 몇 번째 차례에 탈락하는지 = 반복 회차
    
    s = set()
    s.add(words[0])
    
    for i in range(1, len(words)):
        
        if words[i-1][-1] != words[i][0]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
            
        elif words[i] in s:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
            
        s.add(words[i])
    
    if len(answer) == 0:
        answer = [0,0]
    
    return answer