"""
Упражнение 4. Площадь садового участка
Создайте программу, запрашивающую у пользователя длину и ширину
садового участка в футах. Выведите на экран площадь участка в акрах.
"""

length = float(input('Введите длину садового участка в футах: '))
width = float(input('Введите ширину садового участка в футах: '))
square = length * width
acreage = square / 43560      # Переводим в акры
print('Площадь садового участка %.3f акров' % acreage)
