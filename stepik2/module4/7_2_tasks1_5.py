#  Последовательность чисел 1
m, n = int(input()), int(input())

for i in range(m, n + 1):
    print(i)


#  Последовательность чисел 2
m, n = int(input()), int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)


#  Последовательность чисел 3
m, n = int(input()), int(input())

for i in range(m - 1 + m % 2, n - 1, -2):
    print(i)


#  Последовательность чисел 4
m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
        print(i)


#  Таблица умножения
START = 1
END = 10
n = int(input())

for i in range(START, END + 1):
    res = n * i
    print(f'{n} x {i} = {res}')
