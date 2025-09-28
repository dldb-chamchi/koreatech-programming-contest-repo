T = int(input())
for _ in range(T):
    N = int(input())
    skill = list(map(int, input().split()))
    ans = [-2]*N
    MAX = max(skill)

    answer = []
    
    for i in range(N):
        for j in range(N):
            if skill[i] < skill[j]:
                answer.append(skill[j])
    
    

            

    

    print(*ans)
    
    