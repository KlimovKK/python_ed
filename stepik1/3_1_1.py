"""
Напишите функцию f(x), которая возвращает значение следующей функции,
определённой на всей числовой прямой:
1-(x+2)^2, при x <= -2
- x/2, при -2 < x <= 2
(x-2)^2+1, при 2 < x
"""


def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - (x / 2)
    else:
        return (x - 2) ** 2 + 1
