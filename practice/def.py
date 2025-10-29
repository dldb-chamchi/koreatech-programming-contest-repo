a=3

def test():
    global a
    return 4


b = test()
print(b)