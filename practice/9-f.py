n = int(input())
li = []
ltmp = 0
stmp = 0
num = 0

li = list(map(int, input().split()))

for i in range(n-1):
    if li[i] == li[i+1]:
        num +=1
    elif ltmp >= 1:
        if li[i] < li[i+1]:
            num +=1
        else:
            ltmp = 0
    elif stmp >= 1:
        if li[i] > li[i+1]:
            num += 1
        else:
            stmp = 0 
    if li[i] < li[i+1]:
        ltmp += 1
    if li[i] > li[i+1]:
        stmp +=1
print(num)