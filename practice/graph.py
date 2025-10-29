#그래프 제작
def graph(n):
    dic={}
    for j in range(n-1):
        a, b = input().split()
        if a in dic.keys():
            dic[a].append(b)
        else:
            dic[a] = []
            dic[a].append(b)
        if b in dic.keys():
            dic[b].append(a)
        else:
            dic[b] = []
            dic[b].append(a)
    return dic





    





