def solution(message, spoiler_ranges):
    answer = 0
    
    # 단어 내 일부 문자만 스포일러 -> 그 단어 스포일러
    # 스포방지 구간이 아닌 평문에서 등장하면 -> 중요 단어
    # 만약 중복되지 않으면 -> 중요 단어
    # 스포방지 구간에 띄어쓰기로 있으면 각각 다른 단어
    # 마지막 경우가 이해안됨
  
    words = message.split(" ")
    
    
    spoiler_words = set()
    normal_words = set()
    start = 0
    
    # 반복문을 너무 어렵게 생각하지말자
    # 단어의 시작과 끝
    for w in words:
        end = start + len(w) - 1
        is_spoiler = False
        
        for spoiler in spoiler_ranges:
            s = spoiler[0]
            e = spoiler[1]
            
            # 가장 중요했던 포인트
            # 두 구간을 한번에 비교해서 하나라도 (한 단어라도 spoiler면 True, break)
            if start <= e and end >= s:
                is_spoiler = True
                break
                
        if is_spoiler:
            spoiler_words.add(w)
        else:
            normal_words.add(w)
        
        start = end + 2
            
    # 차집합으로 스포방지 구간이 아닌 평문에서 등장한걸 빼야 중요 단어임.
    # set면 원소의 수를 세야 하므로 len()
    answer = len(spoiler_words - normal_words)
    
    return answer