"""
Упражнение 49. Китайский гороскоп
Китайский гороскоп делит время на 12-летние циклы, и каждому году
соответствует конкретное животное. Один из таких циклов приведен
в табл. 2.11. После окончания одного цикла начинается другой, то есть
2012 год снова символизирует дракона.
Таблица 2.11. Китайский гороскоп
Год Животное Год Животное
2000 Дракон 2006 Собака
2001 Змея 2007 Свинья
2002 Лошадь 2008 Крыса
2003 Коза 2009 Бык
2004 Обезьяна 2010 Тигр
2005 Петух 2011 Кролик
Напишите программу, которая будет запрашивать у пользователя год
рождения и выводить ассоциированное с ним название животного по
китайскому гороскопу. При этом программа не должна ограничиваться
только годами из приведенной таблицы, а должна корректно обрабаты-
вать все годы нашей эры.
"""

year = int(input('Введите год рождения: '))

if year == 2000 or (2000 - year) % 12 == 0:
    chin_horo = 'Дракон'
elif year == 2001 or (2001 - year) % 12 == 0:
    chin_horo = 'Змея'
elif year == 2002 or (2002 - year) % 12 == 0:
    chin_horo = 'Лошадь'
elif year == 2003 or (2003 - year) % 12 == 0:
    chin_horo = 'Коза'
elif year == 2004 or (2004 - year) % 12 == 0:
    chin_horo = 'Обезьяна'
elif year == 2005 or (2005 - year) % 12 == 0:
    chin_horo = 'Петух'
elif year == 2006 or (2006 - year) % 12 == 0:
    chin_horo = 'Собака'
elif year == 2007 or (2007 - year) % 12 == 0:
    chin_horo = 'Свинья'
elif year == 2008 or (2008 - year) % 12 == 0:
    chin_horo = 'Крыса'
elif year == 2009 or (2009 - year) % 12 == 0:
    chin_horo = 'Бык'
elif year == 2010 or (2010 - year) % 12 == 0:
    chin_horo = 'Тигр'
elif year == 2001 or (2001 - year) % 12 == 0:
    chin_horo = 'Кролик'
else:
    chin_horo = ''

if chin_horo == '':
    print('Введите год нашей эры')
else:
    print(f'{year}-й год ассоциирован с животным {chin_horo}')