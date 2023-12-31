"""
Упражнение 40. Громкость звука
Уровни громкости различных источников:
Отбойный молоток 130 дБ
Газовая газонокосилка 106 дБ
Будильник 70 дБ
Тихая комната 40 дБ
Создайте программу, в которой пользователь будет вводить уровень
шума в децибелах. Если введенное им значение будет в точности совпа-
дать с одним из значений в приведенной таблице, необходимо вывести,
чему соответствует указанный уровень громкости. Если значение попа-
дет между уровнями в таблице, нужно сообщить, между какими именно.
Также программа должна выдавать корректные сообщения, в случае если
введенное пользователем значение окажется ниже минимального или
больше максимального.
"""

nois_level = float(input('Введите уровень шума (дБ): '))

if nois_level > 130:
    print('Уровень шума выше, чем у отбойного молотка')
elif 106 < nois_level <= 130:
    if nois_level == 130:
        print('Уровень шума соответствует отбойному молотку')
    else:
        print('Уровень шума ниже, чем у отбойного молотка, '
              'но выше, чем у газовой газонокосилки')
elif 70 < nois_level <= 106:
    if nois_level == 106:
        print('Уровень шума соответствует газовой газонокосилке')
    else:
        print('Уровень шума ниже, чем у газовой газонокосилки, '
              'но выше, чем у будильника')
elif 40 <= nois_level <= 70:
    if nois_level == 70:
        print('Уровень шума соответствует будильнику')
    elif nois_level == 40:
        print('Уровень шума соответствует тихой комнате')
    else:
        print('Уровень шума ниже, чем у будильника, '
              'но выше, чем в тихой комнате')
else:
    print('Уровень шума ниже, чем в тихой комнате')
