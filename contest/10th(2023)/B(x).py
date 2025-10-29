result = []
for t in range(int(input())):
    flip = 0
    a, b, c = map(int, input().split())
    a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
    aL, bL, cL = len(a), len(b), len(c)
    maxL = max(aL, bL, cL)
    if aL != maxL:
        a = "0"*(maxL-aL) + a
    if bL != maxL:
        b = "0"*(maxL-bL) + b
    if cL != maxL:
        c = "0"*(maxL-cL) + c
    
    for i in range(maxL):
        if c[i] == '1':
            if a[i] == '0' and b[i] == '0':
                flip += 1
        else:
            if a[i] == '1':
                flip += 1
            if b[i] == '1':
                flip += 1
    result.append(flip)

print(*result, sep="\n")
    