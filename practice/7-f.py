from math import ceil
from math import floor

#순이익
t = int(input())
nlist = [0 for i in range(t)]
li = [0 for i in range(t)]

for i in range(t):
    p, k = map(int, input().split())
    n = ceil(ceil(p*((3*k)/(k+9)))/3)*3
    li[i] 
    nlist[i] = n
print(nlist)



