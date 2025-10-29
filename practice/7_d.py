

#Top down -> 재귀함수 쓰는 것 but 지금 문제는 재귀함수쓰면 런타임에러남
'''
def fibo(N):    
    if N <=0:
        return 0
    elif 1<= N <=3:
        return N
    else:
        if dp[N] != 0:
            pass
        else:
            dp[N] = fibo(N-1) + fibo(N-2) + fibo(N-3)
        return dp[N]


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)
    if N>=2:
        dp[0] = 1 
        dp[1] = 2
        dp[2] = 3


    ans.append(fibo(N)%1000000007)

for i in range(T):
    print(ans[i])
'''


#메모리 제한 초과 
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0]* (N+1)
    if N >3:
        dp[0] = 1
        dp[1] = 2
        dp[2] = 3
        for i in range(3, N, 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[N-1]%1000000007)
            
    else:
        print(N)
    

