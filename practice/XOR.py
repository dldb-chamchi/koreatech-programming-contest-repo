#XOR은 즐거워?

result= []
T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input(). split()))
    M = int(input())
    for m in range(M):
        S, I, J = map(int, input(). split())
        if S==1:
            A[I] ^= J
        elif S==2:
            tmp = A[I]
            for k in range(I+1, J+1):
                tmp ^= A[k]
            result.append(tmp)

print(*result, sep='\n')