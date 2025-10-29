def kmp(all_string, pattern):
    #  kmp_table, 접미사와 접두사 찾기
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        #nknn의 경우 k를 탐색할 때 뒤에서 찾을 수 없어서 뒤로 빽함
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
            
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    
    print(table)

    #kmp
    result = []
    i = 0 #지금까지 같았던 값들
    for j in range(len(all_string)):
        print(i, j)
        while i > 0 and pattern[i] != all_string[j]:
            print("B")
            i = table[i-1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                #print(i, len(pattern))
                result.append(j - i + 2)
                i = table[i-1]
    
    return result

print(kmp("nnnnknn", "nknn")) #O
print(kmp("nnnnknnknn", "nknn")) #O
#print(kmp("advawdjwasc", "abccab")) #X
#print(kmp("advawdjwasc", "abccabab")) #O

"""
res=[]

for i in range(int(input())):
    A, B = input().split()
    res.append(kmp(A, B))

for i in range(0, len(res)):
    print(len(res[i]))
    if len(res[i])!=0:
        print(*res[i])
"""