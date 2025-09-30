
from collections import deque


for _ in range(int(input())):
    l, n = map(int, input().split())
    loc = map(int, input().split())
    dir = []

    for d in input():
        if (d=='L'):
            dir.append(-1)
        else:
            dir.append(1)

    cur = [-1]*l
    for i in range(n):
        cur[loc[i]] = i
    
    cnt = 0
    while(cnt < n):
        move = [False]*n
        for i in range(l):
            if (move[i]):
                continue

            flag = False
            self = cur[i].popleft()    
            next = i + dir[self]
            next2 = i + 2*dir[self]
            if (0<=next<n):
                if (cur[next] != -1): #가려는곳에 누가 있으면
                    if (dir[self] != dir[cur[next]]): # 방향도 다르면 방향변경
                        dir[self] *= -1
                        move[self] = True
                        dir[cur[next]] *= -1
                        move[cur[next]] = True
                        continue
                    else:
                        flag = True
                # else:
                #     cur[next] = self #움직이기
                #     move[self] = True
            else:
                cnt += 1 #탈출
            if (0<=next2<n):
                if (cur[next2] != -1):
                    if (dir[self] != dir[cur[next]]): # 방향도 다르면 방향변경
                        dir[self] *= -1
                        dir[cur[next2]] *= 1
                        continue
            cur[i] = -1
            
            
