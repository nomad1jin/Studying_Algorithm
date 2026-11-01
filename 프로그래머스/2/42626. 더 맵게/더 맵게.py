import heapq

def solution(scoville, K):
    answer = 0
    
    # 음식 섞으면 없어진다, 새로운 음식 반환
    heapq.heapify(scoville)

    
    while scoville[0] < K:
        
        if len(scoville) < 2:
            return -1

        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_food = food1 + (food2 * 2)
        heapq.heappush(scoville, new_food)
        answer += 1

    
    return answer