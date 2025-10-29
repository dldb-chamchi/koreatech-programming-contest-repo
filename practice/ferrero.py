


#페레로쉐


'''
from pprint import pprint

string = input()
M, N = map(int, input().split())   #M세로, N가로

#str 분리 후 li(좌표평면) 만들기
li = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    tmp = input()
    for j in range(N):
        li[i][j] = tmp[j]'''

"""
X = [[] for x in range(len(string))]
Y = [[] for x in range(len(string))]
for k in range(len(string)):
    for i in range(M):
        for j in range(N):
            if li[j][i] == string[k]:
                X[k].append(i)
                Y[k].append(j)"""

#중복제거, 정렬





'''
for i in range(len(Y)-1):
    for z in range(len(Y[i])):

        
        if Y[i][z] + 1 == Y[i+1][z]:
            Y[i][z] = 100
        if Y[i][z] - 1 == Y[i-1][z]:
            Y[i][z] = 100

        

print(li)
print(X, Y)

'''
from copy import copy

N = int(input())

li = [["x" for i in range(N)] for i in range(N)]
for i in range(N):
    A = input()
    for j in range(N):
        li[i][j]=A[j]

#최댓값 탐색
tmpli = []
XMax=[]
for i in range(N):
    tmpli=copy(li[i])
    for j in range(N):
        MaxNum = max(li[i])
        try:
            XMax.append(tmpli.index(MaxNum, j, N))
        except:
            break
    XMax.append(-1)

for i in range(len(XMax)-1, -1, -1):
    try:
        if XMax[i]==XMax[i-1] and XMax[i]!=-1:
            del XMax[i]
    except:
        break

Try=N
YMax=[0 for x in range(len(XMax))]
for i in range(len(XMax)-1, -1, -1):
    if XMax[i]==-1:
        del XMax[i], YMax[i]
        Try-=1
    else:
        YMax[i]=Try

tmpli = []
for i in range(len(XMax)):
    tmpli.append(li[YMax[i]][XMax[i]])

Max=[]
for i in range(len(XMax)):
    if li[YMax[i]][XMax[i]]==max(tmpli):
        Max.append((XMax[i], YMax[i]))


#최댓값을 기준으로 가로세로대각의 수 구하고 결과 비교하기
result = []
for i in range(len(Max)):
    tmpli = ['' for k in range(4)]
    for j in range(N):
        tmpli[0] += str(li[Max[i][1]][Max[i][0]-j]) #가로
        tmpli[1] += str(li[Max[i][1]-j][Max[i][0]]) #세로
        tmpli[2] += str(li[Max[i][1]-j][Max[i][0]-j]) #대각1
        try:
            tmpli[3] += str(li[Max[i][1]+j][Max[i][0]-j])
        except:
            tmpli[3] += str(li[j-1][Max[i][0]-j])
            print(li[j-1][Max[i][0]-j])
    print(tmpli)
    for j in range(4):
        try:
            if int(tmpli[j][:0:-1])>int(tmpli[j][1:]):
                tmpli[j] = int(tmpli[j][0] + tmpli[j][:0:-1])
            else:
                tmpli[j] = int(tmpli[j])
        except:
            tmpli[j] = int(tmpli[j])
    result.append(max(tmpli))

print(max(result))