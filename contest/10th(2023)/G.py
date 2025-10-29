result = []

for _ in range(int(input())):
    li = [input() for i in range(8)]
    Bstr="BBBBBBBB"

    if Bstr in li:
        result.append("B")
    else:
        result.append("R")

print(*result, sep="\n")

