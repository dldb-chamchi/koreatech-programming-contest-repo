memo = {}

def fun(n):
    global memo
    if n in memo:
        return memo[n]
    elif (n==1) or (n==2) or (n==3):
        memo[n] = n
        return memo[n]
    else:
        memo[n] = fun(n-1)+fun(n-2)+fun(n-3)
        return memo[n]

t = int(input())
num = [int(input()) for i in range(t)]
for i in range(t):
    print(fun(num[i])%1000000007)