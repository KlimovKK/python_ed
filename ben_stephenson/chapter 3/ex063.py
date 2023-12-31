"""
Упражнение 63. Среднее значение
В данном упражнении вы должны написать программу для подсчета
среднего значения всех введенных пользователем чисел. Индикатором
окончания ввода будет служить ноль. При этом программа должна выда-
вать соответствующее сообщение об ошибке, если первым же введенным
пользователем значением будет ноль.
"""

num = float(input('Введите число (0 для окончания ввода): '))

if num != 0:
    num_sum = 0
    qty = 0
    while num != 0:
        num_sum += num
        qty += 1
        num = float(input('Введите число (0 для окончания ввода): '))
    print('Среднее значение введенных чисел равно', num_sum / qty)
else:
    print('Первое число должно быть отличным от нуля')
