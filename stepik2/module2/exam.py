print('*' * 17)
space = ' ' * 15
print('*', '*', sep=space)
print('*', '*', sep=space)
print('*' * 17)

a, b = int(input()), int(input())
square_of_sum = (a + b) ** 2
sum_of_squares = a ** 2 + b ** 2
print(f'Квадрат суммы {a} и {b} равен {square_of_sum}')
print(f'Сумма квадратов {a} и {b} равна {sum_of_squares}')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a ** b + c ** d)

n = int(input())
res = n + (n * 10 + n) + (n * 100 + (n * 10 + n))
print(res)
