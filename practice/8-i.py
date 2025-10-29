#original
def main(y, x):
    tmp = 0 #찾은 문자열 수
    end = len(y) - len(x)

    if len(x)==1:
        output=[]
        Try=0
        for i in range(len(y)):
            if y[i]==x:
                output.append(i+1)
                Try+=1
        return Try, output
    else:
        if len(x)==x.count(x[0]) and len(y[:end])==y.count(x[0], 0, end):
            Try = end-len(x)+1
            output = [x+1 for x in range(Try)]
            for i in range(end-len(x)+1, len(y)-len(x)+1):
                if y[i:i+len(x)]==x:
                    Try+=1
                    output.append(i+1)
            return Try, output    
        else:
            string = list(filter(lambda t:y[t]==x[0], range(len(y)))) #x[0]의 위치 탐색
            output = []
            for i in range(len(string)):
                if string[i]>len(x)+string[i]:
                    break
                
                if y[string[i]:string[i]+len(x)]==x:
                    tmp+=1
                    output.append(string[i]+1)
            
            return len(output), output
            
result=[]
for i in range(int(input())):
    result.append(main(*input().split()))

for i in range(len(result)):
    print(result[i][0])
    if len(result[i][1])!=0:
        print(*result[i][1])


'''입력예시
4
banana ana
qwerty asdf
aaaaa aaa
aaabaaaabaaaabaaaaba aaa
'''

'''출력예시
2
2 4
0
3
1 2 3
7
1 5 6 10 11 15 16
'''
