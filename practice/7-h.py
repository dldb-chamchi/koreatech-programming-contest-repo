#세계 여행

t = int(input())

able = [] #가능한 도시
fule = [] #연료량
fab = [] #진짜 가능한 도시들

#케이스 t만큼 
while t>0:
    c = int(input()) #도시 갯수
    a = list(map(int, input(). split())) #주유량
    b = list(map(int, input(). split())) #소비량

    #가능한 도시 갯수 탐색
    for i in range(c):
        if a[i] - b[i] >=0:
            able.append(i) #가능한 도시 인덱스 값 넣기
            fule.append(a[i] - b[i])#가능한 도시 연료량 계산
        l = len(able)
        
    if l ==0:
        print(-1)
        t=0
        break
    try:
        for i in range(len(able)):
            next = a[able[i] + 1] #가능한 도시의 바로옆 도시 인덱스 
            fule[i] = fule[i] + a[next] - b[next] #연료량 계산
            if fule[i] >=0: #연료량 양수
                i -= 1
            if next >= len(a): #
                next = 0
            if next <= a[able[i]]:
                print("A") #처음으로 돌아옴
                fab.append(able[i])
                i += 1
            elif fule[i] <0: #가능한 도시 없음
                print(-1)
                print('b')
                t = 0
                break
    except:
        pass    

    
    t-=1

print(fab)
for z in range(len(fab)):
    print(fab[i])
            