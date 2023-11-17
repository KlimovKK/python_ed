#  Таблица-1
COL = 3

n = int(input())

for i in range(n):
    for j in range(COL):
        print(n, end=' ')
    print()


#  Таблица-2
COL = 5

n = int(input())

for i in range(1, n + 1):
    for j in range(COL):
        print(i, end=' ')
    print()


#  Таблица-3
NUM = 9

n = int(input())

for i in range(1, n + 1):
    for j in range(1, NUM + 1):
        print(f'{i} + {j} = {i + j}')
    print()


#  Звездный треугольник
n = int(input())

for i in range(1, n + 1):
    if i <= n // 2 + 1:
        for j in range(i):
            print('*', end='')
    else:
        for j in range(n + 1, i, - 1):
            print('*', end='')
    print()


#  Численный треугольник 1
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()
