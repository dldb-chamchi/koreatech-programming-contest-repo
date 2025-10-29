#넌 얼마나 빠르게 왔었니?
 
n = int(input()) #학생 수
ni = list(map(int, input().split())) #학생 순서
q = int(input()) #궁금한 학생 수
qi = list(map(int, input().split())) #궁금한 학생

#유용
dic = {}
for i in range(n):
    if ni[i] not in dic.keys():
        dic[ni[i]]=[i+1]
    else:
        dic[ni[i]].append(i+1)
for i in range(q):
    if qi[i] in dic.keys():
        print(*dic[qi[i]])
    else:
        print(-1)
print(dic)