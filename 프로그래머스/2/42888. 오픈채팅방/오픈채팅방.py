class Name:
    def __init__(self):
        self.name = {}
        # name 딕셔너리, id는 키로 넣기
        
    def change(self, id, name):
        self.name[id] = name
    
    ## 재입장할때 이름 바뀌는데... id는 그대로네
    # 아래 함수는 호출전에는 안바뀌자나
    
    def enter(self, id):
        return f"{self.name[id]}님이 들어왔습니다."   
        
    def leave(self, id):
        return f"{self.name[id]}님이 나갔습니다."
    

def solution(record):
    answer = []
    member = Name()
    
    for r in record:
        line = r.split()
        msg = line[0]
        id = line[1]
        
        ### 어려웠던 부분. 그냥 출력만 하는것이 아니라
        ### enter에서도 이름을 기록해야하는 것
        if msg == "Enter" or msg == "Change":
            name = line[2]
            member.change(id, name)
            
    for r in record:
        line = r.split()
        msg = line[0]
        id = line[1]
        
        if msg == "Enter":
            answer.append(member.enter(id))
        
        if msg == "Leave":
            answer.append(member.leave(id))
   
    return answer