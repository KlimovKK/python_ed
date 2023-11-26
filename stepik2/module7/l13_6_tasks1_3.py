#  Середина отрезка
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


#  Площадь и длина
from math import pi


# объявление функции
def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)


#  Корни уравнения
from math import sqrt


# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    root_1 = (- b - sqrt(d)) / (2 * a)
    root_2 = (- b + sqrt(d)) / (2 * a)
    return min(root_1, root_2), max(root_1, root_2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
