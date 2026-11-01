def solution(word):
    answer = 0
    word_list = []
    words = "AEIOU"
    
    def dictionary(w, cnt):
        
        if cnt == 5:
            return
        
        for i in range(len(words)):
            word_list.append(w + words[i])
            dictionary(w + words[i], cnt + 1)
    
    dictionary("", 0)
    
    return word_list.index(word) + 1