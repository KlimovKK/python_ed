"""
Упражнение 79. Наибольший общий делитель
Наибольший общий делитель двух положительных чисел представляет
собой наибольшее число, на которое без остатка делятся оба числа. Су-
ществует несколько алгоритмов, позволяющих определить наибольший
общий делитель двух чисел, включая следующий.
Инициализируйте переменную d меньшим из чисел n и m
Пока n или m не делятся на d без остатка, выполнять
Уменьшить d на единицу
Выведите на экран d, это и есть наибольший общий делитель для n и m
Напишите программу, запрашивающую у пользователя два положи-
тельных целых числа и выводящую для них наибольший общий делитель.
"""

n = int(input('Введите первое положительное целое число: '))
m = int(input('Введите второе положительное целое число: '))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d -= 1

print(f'Наибольший общий делитель для чисел {n} и {m} равен {d}')
