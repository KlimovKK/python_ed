num = int(input())
print(num)
print(num + 1)
print(num + 2)

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(first_num + second_num + third_num)

a = int(input())
V = a * a * a
S = 6 * a * a
print('Объем =', V)
print('Площадь полной поверхности =', S)

a = int(input())
b = int(input())
func = 3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41
print(func)

num = int(input())
print(f'Следующее за числом {num} число: {num + 1}')
print(f'Для числа {num} предыдущее число: {num - 1}')

monitor_price = int(input())
sys_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())
total = (monitor_price + sys_unit_price + keyboard_price + mouse_price) * 3
print(total)

num1 = int(input())
num2 = int(input())
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')

a1, d, n = int(input()), int(input()), int(input())
an = a1 + d * (n - 1)
print(an)

num = int(input())
print(num, 2 * num, 3 * num, 4 * num, 5 * num, sep='---')
