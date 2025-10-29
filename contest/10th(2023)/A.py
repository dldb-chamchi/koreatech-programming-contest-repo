Arabia = [1000, 900, 500, 400, 100, 90, 50, 40]

def calcul(li):
    global Arabia
    result = 0

    for j in range(len(li)):
        tmp = []
        for i in Arabia:
            if li[j]<40:
                break
            else:
                li[j] -= (li[j]//i) * i
        result += li[j]//10
    
    return result
    
output = []
for _ in range(int(input())):
    B = int(input())
    li = list(map(int, input(). split()))
    output.append(calcul(li))

print(*output, sep="\n")

'''
{1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL"}
'''