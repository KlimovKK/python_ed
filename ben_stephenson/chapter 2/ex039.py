"""
Упражнение 39. Сколько дней в месяце?
Количество дней в месяце варьируется от 28 до 31. Очередная ваша про-
грамма должна запрашивать у пользователя название месяца и отобра-
жать количество дней в нем. Поскольку годы мы не учитываем, для фев-
раля можно вывести сообщение о том, что этот месяц может состоять как
из 28, так и из 29 дней, чтобы учесть фактор високосного года.
"""

month = input('Название месяца: ').lower()

if month == 'февраль':
    day_in_month = '28 или 29'
elif month == 'апрель' or 'июнь' or 'сентябрь' or 'ноябрь':
    day_in_month = 30
else:
    day_in_month = 31

print(f'В этом месяце {day_in_month} дней')
