from collections import deque

T = int(input())
for _ in range(T):
    stack = deque() # (skill, idx)
    N = int(input())
    skill = list(map(int, input().split()))
    ans = [-1]*N

    stack.append((skill[0], 0))
    for i in range(1, N):
        top, tIdx = stack.pop()
        if skill[i] > top:      # 자기가 크면
            # 안에 있는 애들을 모두 빼고
            if len(stack) > 0:
                print(len(stack))
                while stack:
                    t, tI = stack.pop()
                    # 나온애에 답 기록하기
                    ans[tI] = skill[i]
            ans[tIdx] = skill[i]

            # 자신을 넣기
            stack.append((skill[i], i))
            
        elif skill[i] < top:    # 자기가 작으면
            # 답 기록하기
            ans[i] = top
            # 원래 가장 컸던 애를 넣기
            stack.append((top, tIdx))
        else:                   # 동일하면
            # 일단 다 넣고 보류하기 (더 큰 애를 만나기전까지)
            stack.append((top, tIdx))
            stack.append((skill[i], i))

    print(*ans)
    
    