"""
Упражнение 24. Единицы времени
Создайте программу, в которой пользователь сможет ввести временной
промежуток в виде количества дней, часов, минут и секунд и узнать общее
количество секунд, составляющее введенный отрезок.
"""

days = int(input('Количество дней: '))
hours = int(input('Количество часов: '))
minutes = int(input('Количество минут: '))
seconds = int(input('Количество секунд: '))

seconds += minutes * 60 + hours * 3600 + days * 86400
print(f'Временной промежуток составляет {seconds} секунд')