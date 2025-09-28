# 반례: 2 6 3 4 4 2 7

T = int(input())
for _ in range(T):
    N = int(input())
    skill = list(map(int, input().split()))
    ans = ['a']*N
    MAX = max(skill)

    idx = skill.index(min(skill))
    cnt = 0
    #-2인 애가 하나라도 잇으면 안됨
    # while any(ans[i] == 'a' for i in range(N)):
    while cnt < N:
        start, sIdx = skill[idx], idx
        if start == MAX:
            ans[sIdx] = -1
            cnt += 1
            idx += 1
            if idx >= N:
                idx = 0
            continue
        
        while True:
            idx += 1

            if idx >= N:
                idx = 0

            if skill[sIdx] < skill[idx]:
                # 가장 큰 값을 찾음
                break
            elif skill[sIdx] >= skill[idx]:
                # ans[sIdx]와 값이 같음. 아래에서 삽입
                continue
        
        # 지금 idx는 1마주친 값
        if idx > sIdx:
            for i in range(sIdx, idx):
                if ans[i] != 'a':    break
                ans[i] = skill[idx]
                cnt += 1
        else:
            for i in range(sIdx, N):
                if ans[i] != 'a':    break
                ans[i] = skill[idx]
                cnt += 1
            for i in range(0, idx):
                if ans[i] != 'a':    break
                ans[i] = skill[idx]
                cnt += 1
    

    print(*ans)
    
    