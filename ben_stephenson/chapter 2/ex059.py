"""
Упражнение 59. Следующий день
Разработайте программу, принимающую на вход дату и выводящую на
экран дату, следующую за ней. Например, если пользователь введет дату,
соответствующую 18 ноября 2019 года, на экран должен быть выведен
следующий день, то есть 19 ноября 2019 года. Если входная дата будет
представлять 30 ноября, то на выходе мы должны получить 1 декабря.
И наконец, если ввести последний день года – 31 декабря 2019-го, пользо-
ватель должен увидеть на экране дату 1 января 2020-го. Дату пользователь
должен вводить в три этапа: год, месяц и день. Убедитесь, что ваша про-
грамма корректно обрабатывает високосные годы.
"""

print('Введите дату')
year = int(input('год: '))
month = input('месяц: ').lower()
day = int(input('день: '))

#  Определяем високосный год
if year % 400 == 0:
    year_type = 1
elif year % 100 == 0:
    year_type = 0
elif year % 4 == 0:
    year_type = 1
else:
    year_type = 0

#  Последний день месяца
if day == 31 and month == 'декабрь':
    year += 1
    day = 1
    month = 'январь'
elif day == 31 and month == 'январь':
    day = 1
    month = 'февраль'
elif day == 28 + year_type and month == 'февраль':
    day = 1
    month = 'март'
elif day == 31 and month == 'март':
    day = 1
    month = 'апрель'
elif day == 30 and month == 'апрель':
    day = 1
    month = 'май'
elif day == 31 and month == 'май':
    day = 1
    month = 'июнь'
elif day == 30 and month == 'июнь':
    day = 1
    month = 'июль'
elif day == 31 and month == 'июль':
    day = 1
    month = 'август'
elif day == 31 and month == 'август':
    day = 1
    month = 'сентябрь'
elif day == 30 and month == 'сентябрь':
    day = 1
    month = 'октябрь'
elif day == 31 and month == 'октябрь':
    day = 1
    month = 'ноябрь'
elif day == 30 and month == 'ноябрь':
    day = 1
    month = 'декабрь'
else:
    day += 1

print(f'Следующий день {day}-e число, месяц {month}, {year} год')
