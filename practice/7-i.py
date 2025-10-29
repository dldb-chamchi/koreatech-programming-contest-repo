def main(li):
    if ("R" in li) and ("L" in li):
        Rindex = li.index("R")
        Lindex = li.index("L")
    elif "R" in li:
        Rindex = li.index("R")
        Lindex = 
    elif "L" in li:
        Lindex = li.index("L")
    else:
        return li

    
    if Rindex < Lindex:
        if (len(li[Rindex:Lindex])+1)%2 == 1:
            for i in range(Rindex, (Rindex+Lindex)//2):
                li[i] = "R"
            for i in range((Rindex+Lindex)//2+1, Lindex):
                li[i] = "L"
        else:
            for i in range(Rindex, (Rindex+Lindex)//2+1):
                li[i] = "R"
            for i in range((Rindex+Lindex)//2+1, Lindex):
                li[i] = "L"
    else:
        for i in range(Lindex):
            li[i] = "L"
        for i in range(Rindex, len(li)):
            li[i] = "R"
    
    return ''.join(map(str, li))

T = int(input())
answer = []
for i in range(T):
    answer.append(main(list(input())))

print(*answer, sep="\n")