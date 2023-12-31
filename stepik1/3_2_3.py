"""
Напишите программу, которая считывает строку с числом n,
которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x(i), по одному числу в каждой строке.
Итого будет n+1 строк.

При считывании числа x(i) программа должна на отдельной строке
вывести значение f(x(i)). Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только
от переданного аргумента x. Для того, чтобы уложиться в ограничение по времени,
нужно избежать повторного вычисления значений.
"""

n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])
