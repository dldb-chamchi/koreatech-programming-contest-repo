
num = 0
even = 0
j = 0
i = 0

n = int(input())
li = list(input().split() for i in range(n))

'''
while True:
    if i == n-1:                
        if li[j][i+1] == '1':
            num += 1
            i += 1
            print("오른 가로")
        if li[j][i+1] == '0':
            if j == n-1:
                if li[j+1][i] == '1':
                    j += 1
                    num += 1
                    print("세로 밑")
                if li[j+1][i] == '0':
                    if li[j][i-1] == '1':
                        i += 1
                        num +=1
                        print("왼쪽 가로")
                    if li[j][i-1] == '0':
                        print(-1)
                        break
            else:
                if li[j+1][i] == '1':
                    j += 1
                    num += 1
                    print("세로 밑")
                if li[j+1][i] == '0':
                    if li[j][i-1] == '1':
                        i += 1
                        num +=1
                        print("왼쪽 가로")
                    if li[j][i-1] == '0':
                        print(-1)
                        break
    else:                
        if li[j][i+1] == '1':
            num += 1
            i += 1
            print("오른 가로")
        if li[j][i+1] == '0':
            if li[j+1][i] == '1':
                if j == n-1:
                j += 1
                num += 1
                print("세로 밑")
            if li[j+1][i] == '0':
                if li[j][i-1] == '1':
                    i += 1
                    num +=1
                    print("왼쪽 가로")
                if li[j][i-1] == '0':
                    print(-1)
                    break

    if num % 2 == 0:
        even += 2
        
    if i == n-1 and j == n-1:
        break
    print(i, j)

print(num + even)
'''