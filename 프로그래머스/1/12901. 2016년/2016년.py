def solution(a, b):
    answer = ''
    
    # 나머지 0을 고려해서, 0~6으로 구성해야됨
    week = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    # {3:"MON", 4:"TUE", 5:"WED", 6:"THU", 0:"FRI", 1:"SAT", 2:"SUN"}
    
    # 날짜 초기화를 어캐하지
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = 0
    
    for i in range(1, a):
        
        day += month.get(i)
    
    day += b
    # 달이 달라지면 나눗셈 숫자가 요일이아니네..
    # 진짜 중요한 점: 7%7 = 나머지가 0이라서. 요일에 0을 둬야함
    answer = week.get(day % 7)
    
    return answer