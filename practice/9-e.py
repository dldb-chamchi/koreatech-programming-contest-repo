# 사격수 9-e

import collections

def mFun(x, y, I, J):
    if x[I] != x[J]:
        return (y[J]-y[I])/(x[J]-x[I])
    else:
        if y[I] == y[J]:
            return 'eq'
        else:
            return 'inf'
            
n = int(input())
xList, yList = [], []
result = []

for i in range(n):
    tmpX, tmpY = map(int, input().split())
    xList.append(tmpX)
    yList.append(tmpY)
    
for i in range(n):
    #기울기 m
    mList = [mFun(xList, yList, i, j) for j in range(n) if i!=j]
    mstC = collections.Counter(mList).most_common(1)[0]
    if mstC[0] == 'eq':
        result.append(mstC[1])
    else:
        result.append(mstC[1]+mList.count('eq'))

print(max(result)+1)