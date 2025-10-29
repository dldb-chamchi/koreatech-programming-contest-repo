#2번
import collections

n, m = map(int, input().split())
li = []


for i in range(m):
    li += map(int, input().split())
    
winner = []
loser = []
wd = {}
ld = {}
sc = []
t = 0

try:
    for i in range(0, len(li), 4):
        if li[i] == li[i+3] and li[i+1] == li[i+2]:
            t +=1
except:
    pass 

for i in range(0, len(li), 2): #짝수 (이기는)
    winner.append(li[i])

for x in range(1, len(li), 2): #홀수 (지는)
    loser.append(li[x])

for x in range(1, n+1, 1):  #이기는 사람 숫자 세기
    wd[x] = winner.count(x)
    ld[x] = loser.count(x)

#순위 예측


for i in wd.keys():
    if t<1:
        if wd[i] >= 1:
            print(ld[i], m+1-wd[i])
        if wd[i] == 0:
            print(m+1, m+1)
    elif t>=1:
        print(-1)
        break














