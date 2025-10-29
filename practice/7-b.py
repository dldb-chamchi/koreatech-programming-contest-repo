from itertools import combinations, product
from collections import Counter

test = int(input()) #테스트케이스
output = []

for t in range(test):
    card = list(list(input().split()) for i in range(9)) #카드 정보

    #합의 경우 찾기
    fiTmp = [list() for i in range(3)]
    colTmp = [list() for i in range(3)]
    backTmp = [list() for i in range(3)]
    for i in range(9):
        if card[i][0] == 'T': #삼각형
            fiTmp[0].append(i)
        if card[i][0] == 'S': #사각형
            fiTmp[1].append(i)
        if card[i][0] == 'C': #원
            fiTmp[2].append(i)
        if card[i][1] == 'B': #파랑
            colTmp[0].append(i)
        if card[i][1] == 'R': #빨강
            colTmp[1].append(i)
        if card[i][1] == 'Y': #노랑
            colTmp[2].append(i)
        if card[i][2] == 'B': #검은색
            backTmp[0].append(i)
        if card[i][2] == 'W': #흰색
            backTmp[1].append(i)
        if card[i][2] == 'G': #회색
            backTmp[2].append(i)
    figure = [list(combinations(fiTmp[i], 3)) for i in range(3)]
    figure.append(list(product(fiTmp[0], fiTmp[1], fiTmp[2])))
    color = [list(combinations(colTmp[i], 3)) for i in range(3)]
    color.append(list(product(colTmp[0], colTmp[1], colTmp[2])))
    background = [list(combinations(backTmp[i], 3)) for i in range(3)]
    background.append(list(product(backTmp[0], backTmp[1], backTmp[2])))

    figure=sum(figure, [])
    color=sum(color, [])
    background=sum(background, [])

    tmp = figure+color+background
    for i in range(len(tmp)):
        tmp[i] = tuple(sorted(tmp[i]))

    result=[i for i, j in Counter(tmp).items() if j==3]

    score = [0, 0]
    stop = True
    while stop:
        for i in range(2):
            tmp = list(input().split())
            if tmp[0] == "G":
                if len(result) == 0:
                    score[i] += 3
                    stop = False
                    break
                else:
                    if score[i] > 0:
                        score[i] -= 1
            elif tmp[0] == 'T':
                continue
            else:
                tmp = (int(tmp[1])-1, int(tmp[2])-1, int(tmp[3])-1)
                tmp = tuple(sorted(tmp))
                if tmp in result:
                    del result[result.index(tmp)]
                    score[i] += 1
                else:
                    if score[i] > 0:
                        score[i] -= 1

    output.append(tuple(score))
for i in range(test):
    print(*output[i])