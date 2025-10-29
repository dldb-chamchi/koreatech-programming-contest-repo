"""from collections import deque

def find_farthest_node(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    farthest_node = None
    max_distance = 0

    while queue:
        node, distance = queue.popleft()
        visited.add(node)

        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance

# 그래프 예시
graph = {
    1: [2, 3,6,7,8],
    2: [1, 4, 5],
    3: [1,9,10],
    4: [2,14,15],
    5: [2,11,12,13],
    6: [1],
    7: [1],
    8: [1],
    9: [3],
    10: [3],
    11: [5],
    12: [5],
    13: [5],
    14: [4],
    15: [4]
}

start_node = 1
farthest_node, max_distance = find_farthest_node(graph, start_node)

print(f"가장 먼 노드: {farthest_node}, 길이: {max_distance}")
"""
from collections import deque

def find_farthest_node(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    farthest_node = None
    max_distance = 0

    while queue:
        node, distance = queue.popleft()
        visited.add(node)

        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        for neighbor in graph[node]:
            print(queue)
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance

# 그래프 예시
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

queue = None
start_node = 1
farthest_node, max_distance = find_farthest_node(graph, start_node)


print(f"길이: {max_distance}")

