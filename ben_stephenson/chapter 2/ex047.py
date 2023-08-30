"""
Упражнение 47. Определение времени года
Год делится на четыре сезона: зима, весна, лето и осень. Хотя даты смены
сезонов каждый год могут меняться из-за особенностей календаря, мы
в данном упражнении примем допущения, перечисленные в табл. 2.9.
Таблица 2.9. Даты смены сезонов
Сезон Первый день
Весна 20 марта
Лето 21 июня
Осень 22 сентября
Зима 21 декабря
Разработайте программу, запрашивающую у пользователя день и ме-
сяц – сначала месяц в текстовом варианте, затем номер дня. На выходе
программа должна выдать название сезона, которому принадлежит вы-
бранная дата.
"""

month = input('Введите месяц: ').lower()
day = int(input('и день месяца: '))

if (month == 'март' and day >= 20) or month == 'апрель' or month == 'май' or (month == 'июнь' and day < 21):
    season = 'Весна'
elif (month == 'июнь' and day >= 21) or month == 'июль' or month == 'август' or (month == 'сентябрь' and day < 22):
    season = 'Лето'
elif (month == 'сентябрь' and day >= 22) or month == 'октябрь' or month == 'ноябрь' or (month == 'декабрь' and day < 21):
    season = 'Осень'
else:
    season = 'Зима'

print(month, day, 'это', season)
