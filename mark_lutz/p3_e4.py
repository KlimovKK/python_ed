L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i in L:
    if 2 ** X == i:
        print((2 ** X), 'was found at', L.index(i))
        break
else:
    print(X, 'not found')
