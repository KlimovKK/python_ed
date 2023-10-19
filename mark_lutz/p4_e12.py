"""
Вычисление факториалов. И напоследок классика компьютерных наук (но оттого не менее иллюстративная).
При обсуждении перестановок в главе 20 мы использовали понятие факториалов: N!, вычисляемое как N*(N-1)*(N-2)*...1.
Например, 6! равно 6*5*4*3*2*1, или 720. Напишите и хронометрируйте четыре функции, каждая из которых
для вызова fact(N) возвращает N!. Реализуйте эти четыре функции
(1) как рекурсивный обратный отсчет согласно главе 19;
(2) применяя вызов функции reduce согласно главе 19;
(3) с помощью простого цикла с подсчетом согласно главе 13;
(4) используя библиотечный инструмент math.factorial согласно главе 20.
Для измерения времени выполнения каждой функции применяйте модуль timeit из главы 21. Какие выводы вы смогли сделать
из полученных результатов?
"""
from functools import reduce
from math import factorial


def fact0(N):
    if N == 1:
        return N
    else:
        return N * fact0(N - 1)


def fact1(N):
    return N if N == 1 else N * fact1(N - 1)


def fact2(N):
    return reduce((lambda x, y: x * y), range(1, N + 1))


def fact3(N):
    res = 1
    for i in range(1, N + 1): res *= i
    return res


def fact4(N):
    return factorial(N)


if __name__ == '__main__':
    num = 8
    print(fact0(num))
    print(fact1(num))
    print(fact2(num))
    print(fact3(num))
    print(fact4(num))
