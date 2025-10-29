from collections import deque

def solution(n, edge):
    graph = dict()
    visited = [0] * (n+1)
    
    for i in range(1, n+1): # 빈 딕셔너리 생성 {노드 번호: [연결노드]}
        graph[i] = []
    
    for i in edge:  # 딕셔너리 키 - 값 할당
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    return bfs(graph, n, visited)

def bfs(graph, n, visited):
    queue = deque([1])  # 큐에 시작 노드 1 삽입
    visited[1] = 1
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
    
    return visited.count(max(visited))