
board = []
ans = []

for _ in range(int(input())):
    for _ in range(9):
        board.append(list(input().split()))
    while True:
        s = list(input().split())
        ans.append(s)
        if s[0] == 'G':
            if: #진짜로 결이면 
                break
        if s in ans:
            pass #점수 -1
        
        if board 