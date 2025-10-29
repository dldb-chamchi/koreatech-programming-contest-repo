#외주왕
"""
result = []

for i in range(int(input())):
    a, b, c = map(int, input().split())
    d = list(map(int, input().split()))
    num = 0

    if b==c:
        result.append(b)
    else:
        d.sort()
        for j in range(b):
            d.pop()
        for z in range(len(d)):
            if a - d[z] < 0:
                break
            else:
                a = a - d[z]
                num += 1
        result.append(num+b)

print(*result , sep= '\n')
"""
"""
def calcul():
    A, B, C = map(int, input(). split())
    D = list(map(int, input(). split()))
    tmp, idx = 0, 0
    num = 0 #마무리할 수 있는 외주 개수

    #외주 개수 자르기
    for i in range(len(D)):
        tmp += D[i]
        if tmp >= A:
            idx = i+B   #외주의 최대? 개수(인덱스)
            break
    
    tmpli = D[:idx+1]
    for i in range(B):
        DMax = tmpli.index(max(tmpli))
        del tmpli[DMax]
        num += 1
    
    for i in range(len(tmpli)):
        A -= tmpli[i]
        if A<0:
            break
        num += 1

    return num

result = []
for _ in range(int(input())):
    result.append(calcul())
print(*result, sep="\n")
"""

result = []
for _ in range(int(input())):
    A, B, C = map(int, input(). split())
    D = list(map(int, input(). split()))
    tmp = A
    num = 0 #외주 횟수
    Try = 0 #B보다 외주 횟수가 많으면 안됨
    Max = 0
    M = []

    if B==C:
        result.append(B)
    else:
        for i in range(len(D)):
            tmp -= D[i]

            if D[i]>=Max:
                Max = D[i]
                M.append(Max)

            if tmp <= 0 and Try<B and len(M)!=0:
                if max(M)==M[-1]:
                    Max = 0
                    TMP = M.pop()
                    tmp += TMP
                    Try += 1
                else:
                    Max = 0
                    TMP = max(M)
                    tmp += TMP
                    Try += 1
            
            if tmp>=0:
                num += 1
            
            if tmp == 0:
                break
        
        result.append(num)

print(*result, sep="\n")