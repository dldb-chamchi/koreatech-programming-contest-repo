def calcul(x):
    test2, test5, test10 = 0, 0, 0
    tmp = 1
    while tmp<=x:
        tmp = tmp*2
        test2 += 1
    tmp = 1
    while tmp<=x:
        tmp = tmp*5
        test5 += 1
    tmp = 1
    while tmp<=x:
        tmp = tmp*10
        test10 += 1
    
    if test2>test5:
        if test5>test10:
            return test5
        else:
            return test10
    else:
        if test2>test10:
            return test2
        else:
            return test10

    
output = []
for i in range(int(input())):
    output.append(calcul(int(input()))-1)

print(*output, sep="\n")