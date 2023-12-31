"""
Упражнение 18. Объем цилиндра
Объем цилиндра может быть рассчитан путем умножения площади круга,
лежащего в его основе, на высоту. Напишите программу, в которой поль-
зователь будет задавать радиус цилиндра и его высоту, а в ответ получать
его объем, округленный до одного знака после запятой.
"""
from math import pi

h = float(input('Высота цилиндра (см): '))
r = float(input('Радиус цилиндра (см): '))

print(f'Объем цилиндра равен {(r ** 2) * pi * h: <.1f} куб. см')
