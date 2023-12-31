"""
Упражнение 62. Играем в рулетку
На игровой рулетке в казино 38 выемок для шарика: 18 красных, столько
же черных и две зеленые, пронумерованные 0 и 00 соответственно. Крас-
ные числа на рулетке: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34
и 36. Остальные номера в диапазоне положительных чисел до 36 – черные.
Игрок может сделать самые разные ставки. Мы в данном упражнении
будем рассматривать лишь следующие виды ставок:
 одно число (от одного до 36, а также 0 или 00);
 красное или черное;
 четное или нечетное (заметьте, что номера 0 и 00 не являются ни
четными, ни нечетными);
 от 1 до 18 против от 19 до 36.
Напишите программу, имитирующую игру на рулетке при помощи ге-
нератора случайных чисел в Python. После запуска рулетки выведите на
экран выпавший номер и все сыгравшие ставки. Например, при выпаде-
нии номера 13 на экране должна появиться следующая последователь-
ность строк:
Выпавший номер: 13…
Выигравшая ставка: 13
Выигравшая ставка: черное
Выигравшая ставка: нечетное
Выигравшая ставка: от 1 до 18
Если на рулетке выпал номер 0, вывод должен быть следующим:
Выпавший номер: 0…
Выигравшая ставка: 0
Для номера 00 сообщения будут иметь следующий вид:
Выпавший номер: 00…
Выигравшая ставка: 00
"""

from random import randint

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

num = randint(0, 37)
if num == 37:
    print('Выпавший номер: 00...')
else:
    print(f'Выпавший номер: {num}...')

#  Выигрыш для одного числа
if num == 37:
    print('Выигравшая ставка: 00')
else:
    print('Выигравшая ставка:', num)

#  Выигрыш по цветам
#  Достали нагромождения условий, поэтому использую список
if num in red:
    print('Выигравшая ставка: красное')
elif num == 0 or num == 37:
    pass
else:
    print('Выигравшая ставка: черное')

#  Чет/нечет
if 1 <= num <= 36:
    if num % 2 == 0:
        print('Выигравшая ставка: четное')
    else:
        print('Выигравшая ставка: нечетное')

# Первая или вторая половина
if 1 <= num <= 18:
    print('Выигравшая ставка: от 1 до 18')
elif 19 <= num <= 36:
    print('Выигравшая ставка: от 19 до 36')
