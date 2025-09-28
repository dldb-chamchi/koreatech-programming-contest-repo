# for _ in range(int(input())):
    
#     N = int(input())
#     dp = [0]*(N+1)
#     soilder = list(map(int, input().split()))
#     dp[0] = soilder[0]

#     flag = True
#     for i in range(1, N):
#         # dp[i] = max(dp[i-1]*soilder[i], soilder[i], dp[i-1])
#         # dp[i] = max(dp[i-1]*soilder[i], soilder[i])
#         if flag:
#             if dp[i-1]*soilder[i] < soilder[i]:
#                 flag = True
#                 dp[i] = soilder[i]
#             else:
#                 dp[i] = dp[i-1]*soilder[i]
#         else:
#             dp[i] = soilder[i]
#             flag = False

#     print(dp)
#     print(max(dp))
    
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0]*(N+1)
    soilder = list(map(int, input().split()))
    dp[0] = (soilder[0], 1)     # (최대, 자기가 포함되면 1)

    for i in range(1, N):
        
        if dp[i-1][1] == 1:
            if dp[i-1][0] * soilder[i] > soilder[i]:
                dp[i] = (dp[i-1][0] * soilder[i], 1)
            elif dp[i-1][0] * soilder[i] <= soilder[i]:
                dp[i] = (soilder[i], 1)
        
        elif dp[i-1][1] == 0:
            if dp[i-1][0] > soilder[i]:
                dp[i] = (dp[i-1][0], 0)
            elif dp[i-1][0] <= soilder[i]:
                dp[i] = (soilder[i], 1)

    print(dp)
    