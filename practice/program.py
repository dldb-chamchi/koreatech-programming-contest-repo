#3
# li = []
# tmp = 0


# n = int(input())

# for i in range(n):
#     num = int(input())
#     li.append(num)

# li.sort()

# while True:
#     for x in range(1, n):
#         if li[x-1] == li[x]:
#             tmp +=1
            


#1



#12345  5-4+3-2+1
#123456 6-5+4-3+2-1
#310 = 0-1+3
#21 = 1-2


#12345    len = 5  1=>0 2=>1 3=>2 4=>3 5=>4
'''
if len(n_list) % 2 == 0: #짝수
    for i in range(len(n_list)-1, 0, -2): #if 123456 -> 6 4 2 #0이 포함안됨
        re = re + (n_list[i])

    for x in range(len(n_list)-2, -1, -2): #if 123456 -> 5 3 1 #-1이 포함안됨
        re1 = re1 + (-n_list[x])

    print(re+re1)

else: #홀수
    for y in range(len(n_list)-1, -1, -2): #if 12345 -> 5 3 1
        re2 = re2 + n_list[y] #
    print(re2)
    for z in range(len(n_list)-2, 0, -2): # 4 2
        re3 = re3 + (-n_list[z])
    print(re3)
'''


from pprint import pprint

string = input()
M, N = map(int, input().split())   #M세로, N가로

#str 분리 후 li(좌표평면) 만들기
li = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    tmp = input()
    for j in range(N):
        li[i][j] = tmp[j]




#중복제거, 정렬


tmpLi=[]
for i in string:
    tmpLi.append(i)
tmpSet=set(tmpLi)
tmpLi=list(tmpSet)

spe=[]
for j in string:
    for i in range(len(tmpLi)):
        if tmpLi[i]==j:
            if j in spe:
                continue
            else:
                spe.append(tmpLi[i])



X = [[] for x in range(len(string))]
Y = [[] for x in range(len(string))]
for k in range(len(string)):
    for i in range(M):
        for j in range(N):
            if li[j][i] == string[k]:
                X[k].append(i)
                Y[k].append(j)



print(X, Y)
    


        
