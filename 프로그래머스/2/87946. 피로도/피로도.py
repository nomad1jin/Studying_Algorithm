answer = 0

def solution(k, dungeons):
    global answer
    count = 0
    visited = [False] * len(dungeons)

    dfs(k, count, visited, dungeons)
    
    return answer 

def dfs(k, count, visited, dungeons):
    global answer
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        if visited[i] == False and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], count+1, visited, dungeons)
            visited[i] = False
