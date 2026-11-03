def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x: x[0])

    for book in book_time:
        for i in range(len(book)):
            h, m = map(int, book[i].split(":"))
            minute = h * 60 + m
            book[i] = minute
    
    rooms = []
    
    for book in book_time:
        start = book[0]
        end = book[1]
        used = False
        
        # 첫 시작은 반복문 실행 못 함
        for i in range(len(rooms)):
            if rooms[i] <= start:
                used = True
                rooms[i] = end + 10
                break
        
        if used == False:
            rooms.append(end + 10)
            
    return len(rooms)