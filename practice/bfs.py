# 그래프 탐색 (BFS)
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque()

    # 시작노드 큐에 담기
    queue.append(start)
    
    # 방문 노드와 연결된 모든 노드들을 담고 하나씩 방문
    while queue:
        i = 0
        l = len(visited)
        tmp = list(queue)
        now = queue.popleft()

        while i>l:
            if visited[i] in tmp:
                i -=1
                tmp.remove(visited[i])
            else:
                i += 1
        
        # 아직 방문하지 않았다면 방문 마크 후 인접 노드들 큐에 넣기
        if now not in visited:
            visited.append(now)
            queue.extend(graph[now])

    return ' '.join(visited)

graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(bfs(graph, 'A'))