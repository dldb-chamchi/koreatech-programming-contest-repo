def main():
    t = int(input())
    x = []
    y = []

    for i in range(t):
        yTmp, xTmp = input().split()
        x.append(xTmp)
        y.append(yTmp)

    for i in range(t):
        exsit = []
        Try = 0
        for j in range(len(y[i])-len(x[i])+1):
            if y[i][j:j+len(x[i])] == x[i]:
                exsit.append(j+1)
                Try += 1
        if Try == 0:
            print(0)
        else:
            print(Try, '\n', *exsit, sep='')

main()