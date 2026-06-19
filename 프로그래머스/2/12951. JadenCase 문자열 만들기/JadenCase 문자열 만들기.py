def solution(s):
    answer = []
    
    string = list(map(str, s.split(" ")))
    
    for st in string:
        sentence = ''
            
        for i in range(len(st)):
            
            if i == 0:
                if st[i].isalpha():
                    sentence = st[i].upper()
                else :
                    sentence = st[i]
                    
            else :
                if st[i].isupper():
                    sentence += st[i].lower()
                else :
                    sentence += st[i].lower()
        
        # print(sentence)
        answer.append(sentence)  
    
    return " ".join(answer)