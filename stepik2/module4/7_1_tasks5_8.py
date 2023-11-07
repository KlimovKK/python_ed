#  Повторяй за мной 2
text = input()

for i in range(10):
    print(i, text)


#  Квадрат числа
n = int(input())

for i in range(n + 1):
    print(f'Квадрат числа {i} равен {i ** 2}')


#  Звездный треугольник
n = int(input())

for i in range(n):
    print('*' * (n - i))


#  Популяция
m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    pop = m * (1 + p / 100) ** i
    print(i + 1, pop)
