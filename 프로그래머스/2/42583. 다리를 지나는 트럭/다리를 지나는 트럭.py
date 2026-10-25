from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0] * bridge_length)
    truck = deque(truck_weights)
    # 다음거가 올라올 수 있나 없나 확인을 2중 반복문으로 해도 되는걸까 => X => 덱 2개 사용
    
    while truck or sum(q) > 0:
        
        # 다음 거 무게 검사 전에 트럭 내려감
        q.popleft()
        
        # truck[0]같은 거 쓸때는. 전부 다 빈걸 생각해야돼
        # []인 경우에는 index out or range가 나기 때문에
        # if truck을 추가함
        if truck and sum(q) + truck[0] <= weight:
            t = truck.popleft()
            q.append(t)
            
        else:
            q.append(0)

        answer += 1
    
    return answer