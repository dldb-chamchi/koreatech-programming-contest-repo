sp = []
score = 0
N, M, K = map(int, input().split())



for i in range(M):
    sp.append(list(map(int, input().split())))

sp.sort(reverse=True)

for i in range(len(sp)):
    if K >= sp[i][1]:
        K -= sp[i][1]
        score += sp[i][0]*sp[i][1]
    else:
        score += sp[i][0]*K
        break
    if K == 0:
        break

print(score)

