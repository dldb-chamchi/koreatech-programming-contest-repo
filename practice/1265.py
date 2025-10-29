

#틀림
from pprint import pprint

f = []
b = []
num = 0 #죽인 벌레 수

#보드판 크기
M, N = map(int, input().split())

#보드판 생성
board = [[0 for _ in range(M)] for _ in range(N)]

#파이어뱃 위치 저장 및 보드에 입력
for _ in range(int(input())):
    xf, xy = map(int, input().split())
    f.append([xf, xy])
    board[xf][xy] = 'F'


#빌딩 위치 저장 및 보드에 입력
for _ in range(int(input())):
    xb, yb = map(int, input().split())
    b.append([xb, yb])
    board[xb][yb] = 'B'

#파이어뱃
#가로 
for i in range(len(f)):
    x = f[i][1]
    y = f[i][0]
    
    #왼쪽
    for j in range(x+1, M):
        if board[y][j] == "B" or board[y][j] == 'F':
            break
        #중복처리
        elif board[y][j] == 'x':
            pass
        else:
            board[y][j] = 'x'
            

    #오른쪽
    for k in range(x-1, -1, -1):
        if board[y][k] == 'B' or board[y][k] == 'F':
            break
        elif board[y][k] == 'x':
            pass
        else:
            board[y][k] = 'x'
            


#세로
for i in range(len(f)):
    x = f[i][1]
    y = f[i][0]

    #아래  
    for j in range(y+1, N):
        if board[j][x] == 'B' or board[j][x] == 'F':
            break
        elif board[j][x] == 'x':
            pass
        else:
            board[j][x] = 'x'
            

    #위
    for k in range(y-1, -1, -1):
        if board[k][x] == 'B' or board[k][x] == 'F':
            break
        elif board[k][x] == 'x':
            pass
        else:
            board[k][x] = 'x'
            
            
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            num += 1

print(num)


    
