"""
Упражнение 22. Площадь треугольника (снова)
В предыдущем упражнении мы вычисляли площадь треугольника при из-
вестных длинах его основания и высоты. Но можно рассчитать площадь
и на основании длин всех трех сторон треугольника. Пусть s1, s2 и s3 – дли-
ны сторон, а s = (s1 + s2 + s3)/2. Тогда площадь треугольника может быть
вычислена по следующей формуле: area = sqrt(sx(s-s1)x(s-s2)x(s-s3)
Разработайте программу, которая будет принимать на вход длины всех
трех сторон треугольника и выводить его площадь.
"""

print('Введите длины сторон треугольника')
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2  # Полупериметр
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('Площадь треугольника равна', round(area, 2))
