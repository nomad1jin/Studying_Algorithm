from collections import deque

def solution(s):
    
    answer = 0
       
    for i in range(len(s)):
        d = deque(s)
        d.rotate(-i)
        temp = deque()
        
        for j in d:
            
            if len(temp) == 0:
                temp.append(j)
            else :
                if (j=='}' and temp[-1] == '{') or (j==']' and temp[-1] == '[') or (j==')' and temp[-1] == '(') :
                    temp.pop()
                else :
                    temp.append(j)
                    
        if len(temp) == 0:
            answer += 1
        
    return answer