def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n+1)]

    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
        
    for cut_a, cut_b in wires:
        # 1부터 방문 시작
        visited = [False] * (n+1)
        stack = [1]
        count = 0
        
        while stack:        
            
            node = stack.pop()
        
            if not visited[node]:
                visited[node] = True
                count += 1
                next_node = graph[node]

                for next_node in graph[node]:
                    
                    if (node == cut_a and next_node == cut_b) or (node == cut_b and next_node == cut_a):
                        continue
                    
                    if not visited[next_node]:
                        stack.append(next_node)
        
        answer = min(answer, abs(count - (n - count)))
        
    return answer