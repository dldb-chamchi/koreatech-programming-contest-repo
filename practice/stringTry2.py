def main(y, x):
    if len(x)!=1:
        string = list(filter(lambda t:y[t]==x[0], range(len(y)))) #x[0]의 위치 탐색
        output = []
        
        for i in range(len(string)):
            if string[i]>len(x)+string[i]:
                break
            
            if y[string[i]:string[i]+len(x)]==x:
                output.append(string[i]+1)
        
        return len(output), output
    else:
        output=[]
        for i in range(len(y)):
            if y[i]==x:
                output.append(i+1)
        return len(output), output
            
result=[]
for i in range(int(input())):
    result.append(main(*input().split()))

for i in range(len(result)):
    print(result[i][0])
    if len(result[i][1])!=0:
        print(*result[i][1])

    
'''입력예시
3
banana ana
qwerty asdf
aaaaa aaa
'''

'''출력예시
2
2 4
0
3
1 2 3
'''