def pprint():
    print("===========")
    for t in text:
        print(*t)

def real_print():
    for t in text:
        for i in t:
            if i != "!!!!!!!!!!!!!!!!!!!!!!!!!!":
                print(i, end=" ")
        print()

# T = int(input())
# for _ in range(T):

N = int(input())
text = []
for __ in range(N):
    text.append(input().split(' '))

print("=============")

one = 0     # //을 찾으면 1
star = 0    # /*을 찾으면 1, */을 찾으면 0
for i in range(N):
    for j in range(len(text[i])):
        if text[i][j] == '//':      # 그 라인 출력 안하기
            if j == 0:
                one = 1
            break
        elif text[i][j] == '/*':    #
            star = 1
        elif text[i][j] == '*/':
            star = 0
        elif star == 0:
            print(text[i][j], end=" ")

    if one == 0:
        print()
    
    one = 0



# pprint()
# real_print()