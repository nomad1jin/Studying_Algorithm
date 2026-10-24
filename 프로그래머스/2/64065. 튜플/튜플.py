def solution(s):
    answer = []
    
    # 집합 원소 하나짜리부터 나열
    # 새로운 거 있으면 append()
    
    # {{2}, {2, 1}} 이런식으로 꺼내짐 => 제거
    string = s[2:-2].split("},{")
    string.sort(key = len)
    
    for i in string:
        for num in i.split(","):
            num = int(num)
            if num not in answer:
                answer.append(num)
    
    return answer