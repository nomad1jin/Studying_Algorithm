def solution(s):

    # 탑과 지금 넣는게 같으면 빼기
    stack = []
    stack.append(s[0])
    i = 1
    
    while i < len(s):
        if stack and stack[-1] == s[i]:
            stack.pop()
            answer = 1

        else :
            stack.append(s[i])
            
        i += 1
    
    if stack:
        answer = 0
        
    return answer