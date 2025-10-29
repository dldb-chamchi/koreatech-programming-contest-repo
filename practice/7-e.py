#노드의 길이
"""
#그래프 제작
def graph(n):
    dic={}
    for j in range(n-1):
        a, b = input().split()
        if a in dic.keys():
            dic[a].append(b)
        else:
            dic[a] = []
            dic[a].append(b)
        if b in dic.keys():
            dic[b].append(a)
        else:
            dic[b] = []
            dic[b].append(a)
        
    return dic

#하위 노드 개수 탐색
num = 0
visit = []

def fun(key):
    global num, visit
    
    if key not in visit:
        num += 1
        visit.append(key)
        
        for j in dic[key]:
            fun(str(j))
    
    return num

for i in range(int(input())):
    n = int(input())
    dic = graph(n)
    li = [(i+1, len(dic[str(i+1)])) for i in range(n)] #튜플
    print(li)

    nodeNum = {}    #최상의 노드가 key일 때 최대길이 value
    tmp = {}
    for i in range(1, n):
        tmp[str(i)] = fun(str(i))
        nodeNum[i] = max(tmp.values())
        visit = []
        num = 0
#모든 노드 탐색 -> 전체 노드 갯수 나옴...(n값)
print(nodeNum)"""

from collections import deque

def graph(n):
    dic={}
    for j in range(n-1):
        a, b = input().split()
        if a in dic.keys():
            dic[a].append(b)
        else:
            dic[a] = []
            dic[a].append(b)
        if b in dic.keys():
            dic[b].append(a)
        else:
            dic[b] = []
            dic[b].append(a)
        
    return dic

def find_farthest_node(start):
    global dic

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

        for neighbor in dic[str(node)]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return max_distance, farthest_node

# 그래프 예시

for i in range(int(input())):
    n = int(input())
    dic = graph(n)

    nodeNum = {}    #최상의 노드가 key일 때 최대길이 value
    max_distance = {}
    farthest_node = {}
    for i in range(1, n): 
        max_distance[i], farthest_node[i]  = find_farthest_node(i)

    print(max(max_distance), max_distance, farthest_node)