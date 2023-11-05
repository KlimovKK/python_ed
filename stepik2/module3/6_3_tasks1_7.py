#  Евклидово расстояние
from math import sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

res = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(res)


#  Площадь и длина
from math import pi

R = float(input())

S = pi * R ** 2
C = 2 * pi * R
print(S, C, sep='\n')


#  Средние значения
from math import sqrt

a, b = float(input()), float(input())

arith_mean = (a + b) / 2
geo_mean = sqrt(a * b)
harm_mean = 2 * a * b / (a + b)
RMS = sqrt((a ** 2 + b ** 2) / 2)
print(arith_mean, geo_mean, harm_mean, RMS, sep='\n')


#  Тригонометрическое выражение
from math import radians, sin, cos, tan

x = radians(float(input()))

res = sin(x) + cos(x) + tan(x) ** 2
print(res)


#  Пол и потолок
from math import ceil, floor

x = float(input())

res = ceil(x) + floor(x)
print(res)


#  Квадратное уравнение
from math import sqrt

a, b, c = float(input()), float(input()), float(input())

D = b ** 2 - 4 * a * c
if D < 0:
    print('Нет корней')
elif D == 0:
    root = - b / (2 * a)
    print(root)
else:
    root_1 = (- b - sqrt(D)) / (2 * a)
    root_2 = (- b + sqrt(D)) / (2 * a)
    print(min(root_1, root_2))
    print(max(root_1, root_2))


#  Правильный многоугольник
from math import tan, pi

n = int(input())
a = float(input())

S = (n * a ** 2) / (4 * tan(pi / n))
print(S)
