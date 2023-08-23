"""
Упражнение 19. Свободное падение
Напишите программу для расчета скорости объекта во время его сопри-
косновения с землей. Пользователь должен задать высоту в метрах, с ко-
торой объект будет отпущен. Поскольку объекту не будет придаваться
ускорение, примем его начальную скорость за 0 м/с. Предположим, что
ускорение свободного падения равно 9,8 м/с2.
"""
from math import sqrt
acceleration = 9.8
height = float(input('Введите высоту (м): '))
speed = sqrt(2 * acceleration * height)
print(f'Скорость при соприкосновеннии с поверхностью равна {speed: <.3f} м/с')