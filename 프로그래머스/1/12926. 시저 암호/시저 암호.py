def solution(s, n):
    answer = ''
    
    # ord('A') => 65
    # ord('a') => 97
    # ord('z') => 122?
    
    for ch in s:
        
        if ch == ' ':
            answer += ch
            
        elif ord(ch) <= 90:
            ch = (ord(ch) - ord('A') + n) % 26 + ord('A')
            ch = chr(ch)
            answer += ch
            
        else :
            ch = (ord(ch) - ord('a') + n) % 26 + ord('a')
            ch = chr(ch)
            answer += ch
    
    
    return answer

