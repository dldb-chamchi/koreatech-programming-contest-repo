#값을 3개씩 어케 묶어야 할까


from pprint import pprint
#체스처럼
adr = []
board = []
re = []
m = 0

N = int(input())
for i in range(N):
    #map 쓰면 뜨어쓰기 없어도 각각 원소로 저장 가능ㄴ
    board.append(list(map(int, input()))) 

#가장 큰 수
for i in range(N):
    for j in range(N):
        if board[i][j] >= m:
            m = board[i][j]

for i in range(N):
    for j in range(N):
        if board[i][j] == m:
            adr.append([i, j])
        


print(adr)


#세로 아래
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x+1
        if x != N:  
            re.append(board[x][y])
            print(x,y)
        #리스트의 끝에 도달
        else:
            re.append(board[0][y])
            print(0, y)
            x = 0

'''
#세로 위
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x-1
        if x != 0:  
            re.append(board[x][y])
        #리스트의 끝에 도달
        else:
            re.append(board[x][y])
            x = N

#가로 양수
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        y = y+1
        if y != N:  
            re.append(board[x][y])
        #리스트의 끝에 도달
        else:
            re.append(board[x][0])
            y = 0

#가로 음수
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        y = y-1
        if y != 0:  
            re.append(board[x][y])
        #리스트의 끝에 도달
        else:
            re.append(board[x][y])
            y = N



#대각선 왼위
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x-1
        y = y-1
        if (y != 0) and (x!=0):
            re.append(board[x][y])
        elif x == 0:
            re.appned(board[x][y])
            x = N
        elif y == 0:
            re.append(board[x][y])
            y = N
        else:
            re.append(board[x][y])
            x = N; y=N

            

#대각선 왼아 
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x+1
        y = y-1
        if (y != 0) and (x!=N):
            re.append(board[x][y])
        elif x == N:
            re.appned(board[0][y])
            x = 0
        elif y == 0:
            re.append(board[x][y])
            y = N
        else:
            re.append(board[x][y])
            x = 0; y=N


#대각선 오위   
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x-1
        y = y+1
        if (y !=N) and (x!=0):
            re.append(board[x][y])
        elif x == 0:
            re.appned(board[0][y])
            x = N
        elif y == N:
            re.append(board[x][y])
            y = 0
        else:
            re.append(board[x][y])
            x = N; y=0
'''
'''
#대각선 오아
for i in range(len(adr)):
    #가장 큰 값의 좌표
    x = adr[i][0] #세로
    y = adr[i][1] #가로
    for _ in range(N-1):
        x = x+1
        y = y+1
        if (y !=N) and (x!=N):
            re.append(board[x][y])
        elif x == N:
            re.appned(board[0][y])
            x = N
        elif y == N:
            re.append(board[x][y])
            y = N
        else:
            re.append(board[x][y])
            x = N; y= N
'''





print(re)









'''
print(board)
print(x, y)
'''