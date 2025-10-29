#3으로 나눈 나머지 값을 합침 -> 합친 값을 3으로 나눴을 때 나머지 0->
#그대로 최대 인원
#but 나머지 0 아니면 가장 큰 인원의 바로 다음을 합친 값 3나눴을 때
#나머지 0 되는지 확인

#나중에
s = 0
cou = 0
tmp = 0; tmp2 = 0
N = int(input())
M = list(map(int, input().split()))
kn1 = []; kn2 = []; kn3 = []

if sum(M) % 3 == 0:
    print(sum(M))
else:
    M.sort(reverse=True)
    for i in range(len(M)-1, -1, -1):
        if M[i] % 3 == 0:
            del M[i]
    for j in range(len(M)):
        if M[i] == 1:
            #1 2개 찾기
            for k in range(1, len(M)):
                if M[k] % 3 == 1:
                    cou += 1
                    kn1.append(k)
                if cou == 2:
                    break
            if len(kn1) != 1:
                tmp = M[j] + M[kn1[0]] + M[kn1[1]] 
            # 2 1개 찾기
            for k in range(1, len(M)):
                if M[k] % 3 == 2:
                    cou += 1
                    kn2.append(k)
                if cou == 1:
                    break
            if len(kn2) != 0:
                tmp2 =  M[j] + M[kn2[0]]

            if tmp > tmp2:
                s += tmp
                M[j] = 0; M[kn1[0]] = 0; M[kn1[1]] = 0
                M.sort(reverse=True)
                kn1.clear(); kn2.clear()
            elif tmp < tmp2:
                s += tmp2
                M[j] = 0; M[kn2[0]] = 0
                M.sort(reverse=True)
                kn1.clear(); kn2.clear()

        elif M[j] == 2:
            for k in range(1, len(M)):
                if M[k] % 3 == 1:
                    cou += 1
                    kn1.append(k)
                if cou == 1:
                    break
            M[j] = 0; M[kn3[0]] = 0
            M.sort(reverse=True)
            kn3.clear
    print(M)
    print(s)
