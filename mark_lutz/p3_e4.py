L = []
X = 5
Y = int(input())
for i in range(Y):
    L.append(2 ** i)
print(L)
if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 **X))
else:
    print(X, 'not found')
