# NEW



n = int(input())    #돌멩이의 개수
js = list(input())  #종욱이의 돌멩이
ms = list(input())  #머신의 돌멩이
Try = 0             #false 횟수

#리스트에서 "O" 제거하기
js_notO=list(filter(lambda r:r!='O', js))
ms_notO=list(filter(lambda r:r!='O', ms))

#좌표 구하기
jX = list(filter(lambda x: js[x]=="G" or js[x]=="F", range(n)))
mX = list(filter(lambda x: ms[x]=="G" or ms[x]=="F", range(n)))
tmp = len(jX)

#G는 왼쪽(-1)으로만 이동, F는 오른쪽(+1)으로만 이동
if js_notO != ms_notO:
    Try += 1
else:
    for i in range(tmp):
        if js_notO[i]=="G" and mX[i] > jX[i]:
            Try += 1
            break
        elif js_notO[i]=="F" and mX[i] < jX[i]:
            Try += 1
            break

if Try != 0:
    print("false")
else:
    print("true")

'''
GGOO#나
OOGG#점술기계
==false
OOFF#나
FFOO#점술기계
==false
'''